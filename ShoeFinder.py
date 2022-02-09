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

    def createMap(self):
        # Create Map containing all the scraped information
        # Easiest for Pandas to read and handle
        # Sorting will be done by Pandas
        self.allContent = {
                    "Name":self.shoeNames,
                    "Price":[int(float(price.replace("$", ""))) for price in self.shoePrices],
                    "Link":self.shoeLinks
        }

    def createDataFrame(self):
        # Creating Panda data frame
        frame = pd.DataFrame(self.allContent)
        # Sort based on price
        sortedFrame = frame.sort_values(by=['Price'])
        # Convert to HTML script
        results = sortedFrame.to_html()

        with open('results.html', 'w') as html:
            html.write(self.htmlHeader() + "\n")

        # TOD!!! Open this html file in separate tab
        # ^^^ Temporary Fix, look up how to move html table to another html file
        with open('results.html', 'a') as html:
            # Write will overwrite anything currently in file, cannot add anything to
            # results.html because it will be erased
            html.write("<body>")
            html.write(results)
            html.write("</body>")

    # Sequentially Scraping all websites
    def scrapeWebsites(self):
        google = Google(self.searchCap)
        
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

        shop = google.search_bot
        shop.findSearchbar()
        sleep(1)
        shop.searchTerm(self.searchItem)
        sleep(1)
        shop.pageScrape()
        self.__extendArrays(shop.names, shop.prices, shop.links)
        shop.quitSearch()

        self.createMap()

    def __extendArrays(self, shoe_names, shoe_prices, shoe_links):
        self.shoeNames.extend(shoe_names)
        self.shoePrices.extend([price.replace("+", "").replace(",", "") for price in shoe_prices])
        self.shoeLinks.extend(shoe_links)

    def showArrays(self):
        print(self.shoeNames)
        print(self.shoePrices)
        print(self.shoeLinks)

    # Add Style Sheet to HTML file
    def htmlHeader(self):
        header = "<link rel=\"stylesheet\" href=\"styles.css\">"
        return header

    def main(self):
        pass
