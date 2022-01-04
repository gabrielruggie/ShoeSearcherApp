# Web app tester methods
from SearchBot import WebScrapper
import time

PATH = "/Users/gabrielruggie/Desktop/chromedriver"

def testFlightClub():

    # Test 1: Find Search Bar Successfully
    web = "https://www.flightclub.com/"
    tag = "input"
    # Instantiate selenium search bot
    # Find search bar and give input for search
    bot = WebScrapper(PATH, web, tag)
    bot.findSearchbar("TAG NAME")
    bot.searchTerm("nike")
    # Test 2: Scrape Successfully
    page_of_shoes = "sc-10ono97-0"
    shoe_name_class = "sc-10kqv19-0"
    shoe_price_class = "whkzwq-5"
    bot.pageScrape(page_of_shoes, shoe_name_class, shoe_price_class)

    # Test 3: Build Object Successfully
    bot.build()
    print(bot.content)
    # Quit bot
    time.sleep(5)
    bot.quitSearch()

def testEbay():

    # Test 1: Find Search Bar Successfully
    web = "https://www.footlocker.com/"
    search_xpath = "/html/body/div[1]/div[1]/header/nav[2]/div[3]/div/div/form/div[2]/div[1]/input"
    page_of_shoes = "Page-body"
    shoe_name_class = "ProductName-primary"
    shoe_price_class = "ProductPrice"

    bot = WebScrapper(PATH, web, search_xpath, page_of_shoes, shoe_name_class, shoe_price_class)
    bot.findSearchbar()
    bot.searchTerm("Jordan 1")

    bot.closePopUp("/html/body/div[31]/div[1]/div[2]/button")
    #Test 2: Scrape Successfully

    bot.pageScrape()

    time.sleep(5)
    bot.quitSearch()
# testFlightClub()
testEbay()
