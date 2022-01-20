from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

# Seach Bot class that uses selenium to create a search bot.
# The goal of the search bot is to searcha specific term in a search bar and
# retrieve web page links
class WebScrapper:

    # Creating instance variables that are unique to each search bot created
    def __init__ (self, path, url, xpath, res_page, nameID, priceID):
        self.path = path            # Path of chrome driver on this computer
        self.url = url              # website url
        self.xpath = xpath          # XPATH of search bar
        self.res_page = res_page    # result page class id
        self.nameID = nameID        # xpath of name of shoe
        self.priceID = priceID      # xpath of price of shoe
        self.capacity = None        # Total amount of shoes to be scraped
        self.linkedProduct = False  # If the product card is, itself the link

        # Initialized selenium driver
        self.chrome = None
        # Doesn't work for some reason
        # Maybe try making the window size 0 or adjusting the window size
        # self.setOptions()
        self.driver = webdriver.Chrome(self.path, options=self.chrome)
        self.driver.get(self.url)   # Open URL

        self.searchBar = None       # search bar of particular website
        self.prices = []            # scraped prices
        self.names = []             # scraped product names
        self.links = []             # scraped product links

        self.content = {}           # object that contains all characteristics

    # Find the search bar a given website
    # RETURNS search bar html id used to search up items on website given
    def findSearchbar(self):
        # Locate Search Bar on website
        WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, self.xpath)))

        self.searchBar = self.driver.find_element(By.XPATH, self.xpath)

    # Searches a term on given website
    # INPUT s_term is the search term
    def searchTerm(self, s_term):
        # search term should be a string
        if isinstance(s_term, str):
            self.searchBar.send_keys(s_term)
        else:
            raise ValueError("Search term must be of type string")
            self.driver.quit()

        self.searchBar.send_keys(Keys.RETURN)

    # Scrapes 1 page of given website
    def findResultsPage(self):
        try:
            # wait for search results to be fetched
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.res_page))
            )
        except Exception as e:
            print(e)
            self.driver.quit()

        try:
            webpage = self.driver.find_elements(By.CLASS_NAME, self.res_page)
            # Creates list of a tags found on current web page
            # results = webpage.find_elements(By.TAG_NAME, "a")
            # Think about lowering time to 10
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.nameID)))
        except Exception as e:
            print(e)
            self.quitSearch()
            return

        # WebDriverWait(self.driver, 20).until(
        # EC.presence_of_element_located((By.XPATH, self.priceID)))
        return webpage
    # Scrapes 1 page of given website
    def pageScrape(self):
        # Trigger if capacity for lists has been reached
        cap = False

        results = self.findResultsPage()

        if results == None:
            raise ValueError

        if type(self.capacity) == int:
            cap = True
        # Iterate through all items with product card class
        for result in results:
            thing = result
            # Checking if link isn't already in product card
            if not self.linkedProduct:
                thing = result.find_element(By.TAG_NAME, "a")

            link = thing.get_attribute("href")
            # Possibly use tag name here instead if other websites allow
            name = result.find_element(By.CLASS_NAME, self.nameID)
            # Probably gonna need to keep as class name
            price = result.find_element(By.CLASS_NAME, self.priceID)
            # Only fill arrays to capacity
            if len(self.links) < self.capacity:
                self.names.append(name.text)
                self.prices.append(price.text)
                self.links.append(link)
                self.build(name.text, price.text, link)
            else:
                break

    # Clicks a button to retrieve data blocked by pop up window
    # INPUT btn, button xpath to be pressed
    def clickBtn(self, btn):
        # Waits for a button to appear and then clicks it
        try:
            sb = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, btn))
            )
            sb.click()
        except Exception as e:
            print(e)
            self.quitSearch()

    # Optional method that sets capacity to amount of shoes scraped
    # INPUT num, number to set capacity to.
    def setCapacity(self, num):
        self.capacity = num

    # Allows Silent Background execution
    # Creates a virtual invisible display
    # Must be set before self.driver is created
    def setOptions(self):
        self.chrome = Options()
        self.chrome.add_argument("--headless")

    # Since Flight club makes the link embedded in the product card, set this to
    # True to avoid NoSuchElementException
    def isLinkedProduct(self):
        self.linkedProduct = True

    # Builds the dictionary that stores all the information of each shoe
    def build(self, name, price, link):
        self.content[name] = {'price':price, 'link':link}

    # Quit Driver
    def quitSearch(self):
        self.driver.quit()
