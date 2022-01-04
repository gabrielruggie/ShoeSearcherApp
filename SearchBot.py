from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
        self.res_page = res_page
        self.nameID = nameID
        self.priceID = priceID
        # Initialized selenium driver
        self.driver = webdriver.Chrome(self.path)
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
        self.searchBar = self.driver.find_element(By.XPATH, self.xpath)

    # Searches a term on given website
    # INPUT s_term is the search term
    def searchTerm(self, s_term):
        # Search term must be of type string
        if isinstance(s_term, str):
            self.searchBar.send_keys(s_term)
        else:
            raise ValueError("Search term must be of type string")
            self.driver.quit()

        self.searchBar.send_keys(Keys.RETURN)

    # Scrapes 1 page of given website
    # INPUT pageId is the current class of the found web page
    # INPUT nameId is the class name of each shoe name found on web page
    # INPUT priceId is the class name of each shoe price found on web page
    def pageScrape(self):
        try:
            # wait for search results to be fetched
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.res_page))
            )
        except Exception as e:
            print(e)
            self.driver.quit()

        webpage = self.driver.find_element(By.CLASS_NAME, self.res_page)
        # Creates list of a tags found on current web page
        results = webpage.find_elements(By.TAG_NAME, "a")

        for r in results:
            link = r.get_attribute("href")
            # Possibly use tag name here instead if other websites allow
            name = r.find_element(By.CLASS_NAME, self.nameID)
            # Probably gonna need to keep as class name
            price = r.find_element(By.CLASS_NAME, self.priceID)

            self.names.append(name.text)
            self.prices.append(price.text)
            self.links.append(link)

    def closePopUp(self, btn):
        sb = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, btn))
        )
        sb.click()

    # Builds the dictionary that stores all the information of each shoe
    def build(self):
        try:
            for i in range(len(self.names)):
                self.content[self.names[i]] = {"price:":self.prices[i],
                "link:":self.links[i]}
        except Exception:
            pass

    def quitSearch(self):
        self.driver.quit()
