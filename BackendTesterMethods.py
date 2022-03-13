# Web app tester methods
from SearchBot import WebScrapper
from ShoeFinder import Finder
from browser import Results
from ShoeApp import ShoeSearcherUI
import time

PATH = "/Users/gabrielruggie/Desktop/chromedriver"

def testFlightClub():

    # Test 1: Find Search Bar Successfully
    web = "https://www.flightclub.com/"
    search_xpath = "/html/body/div[1]/div/div[1]/div/nav/div[1]/div/span/input"
    page = "sc-1wc5x2x-0"
    name_path = "sc-10kqv19-0"
    price_path = "whkzwq-5"
    # Instantiate selenium search bot
    # Find search bar and give input for search
    bot = WebScrapper(PATH, web, search_xpath, page, name_path, price_path)
    bot.setCapacity(10)
    bot.isLinkedProduct()
    bot.findSearchbar()
    bot.searchTerm("Jordan 1")
    time.sleep(1)
    # Test 2: Scrape Successfully
    try:
        bot.pageScrape()
    except ValueError as e:
        print(f'Items not found: {e}')


    # Test 3: Build Object Successfully
    print(bot.content)
    # Quit bot
    time.sleep(5)
    bot.quitSearch()

def testFootLocker():

    # Test 1: Find Search Bar Successfully
    web = "https://www.footlocker.com/"
    search_xpath = "/html/body/div[1]/div[1]/header/nav[2]/div[3]/div/div/form/div[2]/div[1]/input"
    page = "SearchResults"
    name_path = "ProductName-primary"
    price_path = "ProductPrice"

    bot = WebScrapper(PATH, web, search_xpath, page, name_path, price_path)
    bot.findSearchbar()
    bot.searchTerm("jordan 1")

    bot.clickBtn("/html/body/div[31]/div[1]/div[2]/button")

    #Test 2: Scrape Successfully
    bot.setCapacity(50)
    bot.pageScrape()

    print(bot.links)
    print(len(bot.links))
    print(bot.names)
    print(len(bot.names))
    print(bot.prices)
    print(len(bot.prices))
    # print(bot.content)

    time.sleep(5)
    bot.quitSearch()

def testGoogle():

    web = "https://shopping.google.com/?sa=X&ved=2ahUKEwj3-qXR4Lz1AhVsS28EHfRUByUQtukFegQIABAS"
    search_xpath = "/html/body/c-wiz[1]/div/div/c-wiz/form/div[2]/div[1]/input"
    page = "sh-dgr__grid-result"
    name_path = "Xjkr3b"
    price_path = "a8Pemb"

    bot = WebScrapper(PATH, web, search_xpath, page, name_path, price_path)
    bot.setCapacity(11)
    # button = "/html/body/div[12]/div[3]/div/div/div/div[2]/form/div[3]/div[3]/button"
    # time.sleep(1)
    # bot.clickBtn(button)
    bot.findSearchbar()
    bot.searchTerm("Jordan 1")

    time.sleep(1)
    bot.pageScrape()

    print(bot.links)
    print(len(bot.links))
    print(bot.names)
    print(len(bot.names))
    print(bot.prices)
    print(len(bot.prices))
    print(bot.content)

    time.sleep(5)
    bot.quitSearch()

def testNike():
    web = "https://www.nike.com/"
    search_xpath = "/html/body/div[1]/div[3]/header/div/div[1]/div[2]/div/div/div[1]/div/div/input"
    page = "product-card"
    name_path = "product-card__title"
    price_path = "product-price"

    bot = WebScrapper(PATH, web, search_xpath, page, name_path, price_path)
    bot.setCapacity(11)
    # button = "/html/body/div/div/header[1]/header/div[3]/button"
    # bot.clickBtn(button)
    bot.findSearchbar()
    bot.searchTerm("Jordan 1")

    time.sleep(1)
    bot.pageScrape()

    print(bot.links)
    print(len(bot.links))
    print(bot.names)
    print(len(bot.names))
    print(bot.prices)
    print(len(bot.prices))
    print(bot.content)

def testRunner():
    # If you get Flight club to work, then it will work in runner
    # Doesn't work for virtual. Research
    walker = Runner()
    walker.setSearchItem("Jordan")
    # Neccessary
    walker.setSearchCapacity(10)
    walker.scrapeWebsites()
    # Not Neccessary
    walker.showArrays()
    # Not Neccessary
    print(walker.allContent)

    walker.createDataFrame()

    rpage = Results('results.html')
    rpage.showResults()


# testRunner()

def testApp():

    walker = ShoeSearcherUI()
    walker.open_application()

testApp()
