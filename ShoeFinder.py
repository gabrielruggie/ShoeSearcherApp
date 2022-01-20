from SearchBot import WebScrapper
from WebObjects import FlightClub
from WebObjects import Nike
from WebObjects import Google
from time import sleep
import pandas as pd

class Runner:

    def __init__(self):
        # All links, names and prices from all websites
        self.shoeNames = []
        self.shoePrices = []
        self.shoeLinks = []
        self.searchItem = None
        self.searchCap = 0
        self.allContent = []

        # Look up how to automate closing browsers when finished

    # Takes search input from JS file and runs it through WebScrapper
    # Handle in app.py
    def setSearchItem(self, item):
        # Checking if data from JS is valid
        if type(item) != str:
            raise ValueError('Failed to convert to string')

        self.searchItem = item

    # Takes capacity input from JS file and runs it through WebScrapper
    # Handle in app.py
    def setSearchCapacity(self, cap):
        # May need to change from data type to int
        if type(cap) != int:
            raise ValueError('Failed to convert to int')

        self.searchCap = cap

    def sortContent(self):
        content = {}
        sorted_items = []

        for i in range(len(self.shoeNames)):
            # Must convert to float because some prices are formed like $84.00
            # Convert to float than int to bypass this error
            content[self.shoeNames[i]] = {'price':int(float(self.shoePrices[i].replace("$", ""))),
            'link':self.shoeLinks[i]}
        # Lambda function used to sort list based on the price as an int
        sorted_items = sorted(content.items(), key=lambda x: x[1]['price'])

        self.allContent = {item[0]:item[1] for item in sorted_items}

    # Sequentially Scraping all websites
    def scrapeWebsites(self):
        google = Google(self.searchCap)
        '''
        flightclub = FlightClub(self.searchCap)
        nike = Nike(self.searchCap)

        # Scrape Nike
        # Set capacity through parameter
        nike_bot = nike.search_bot
        nike_bot.findSearchbar()
        sleep(1)
        nike_bot.searchTerm(self.searchItem)
        sleep(1)
        nike_bot.pageScrape()
        self.__extendArrays(nike_bot.names, nike_bot.prices, nike_bot.links)
        nike_bot.quitSearch()

        FC_bot = flightclub.search_bot
        FC_bot.findSearchbar()
        sleep(1)
        FC_bot.searchTerm(self.searchItem)
        sleep(1)
        FC_bot.pageScrape()
        self.__extendArrays(FC_bot.names, FC_bot.prices, FC_bot.links)
        FC_bot.quitSearch()
        '''
        shop = google.search_bot
        shop.findSearchbar()
        sleep(1)
        shop.searchTerm(self.searchItem)
        sleep(1)
        shop.pageScrape()
        self.__extendArrays(shop.names, shop.prices, shop.links)
        shop.quitSearch()

        self.sortContent()

    def createDataFrame(self):
        data = pd.DataFrame()
    
    def __extendArrays(self, shoe_names, shoe_prices, shoe_links):
        self.shoeNames.extend(shoe_names)
        self.shoePrices.extend(shoe_prices)
        self.shoeLinks.extend(shoe_links)

    def showArrays(self):
        print(self.shoeNames)
        print(self.shoePrices)
        print(self.shoeLinks)

    def main(self):
        pass
