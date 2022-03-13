from SearchBot import WebScrapper
from WebObjects import FlightClub
from WebObjects import Nike
from WebObjects import Google
from time import sleep
import pandas as pd

# Shoe Finder Class that instantiates of Web Scaper to search 3 websites and scrape
# its data. Stores collected data in 1 hash table and converts said hash table to
# html file using Pandas
class Finder:

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

    # Create Map containing all the scraped information
    # Easiest for Pandas to read and handle
    # Sorting will be done by Pandas
    def createMap(self):
        # Fix prices so they can be successfully converted to integers
        self.fixPrices()

        self.allContent = {
                    "Name":self.shoeNames,
                    "Price":[int(price) for price in self.shoePrices],
                    "Link":self.shoeLinks
        }

    # Removes period from nums in order to convert to integers
    # Time Complexity: O(N)
    def fixPrices(self):
        fixedPrices = []
        # Iterates through all the prices in self.shoePrices
        for price in self.shoePrices:
            temp = []
            nums = list(price)

            if '.' in nums:
                index = nums.index('.')
                temp = nums[0:index]
            else:
                # If there was no period then set temp to the entire number
                temp = nums
            # Create new string of price
            newPrice = ''.join(temp)
            # Edge case, if there was no price in the first place aka, empty string!
            if len(newPrice) == 0:
                newPrice = ''.join((newPrice, '0'))
            # Add in price to new list immediately to not lose order of self.shoePrices
            fixedPrices.append(newPrice)

        # Reset self.shoePrices to fixed prices list
        self.shoePrices = fixedPrices

    # Creates the html file that will contain all the information collected from
    # WebScrapper
    def createDataFrame(self):
        # Creating Panda data frame
        frame = pd.DataFrame(self.allContent)
        # Sort based on price
        sortedFrame = frame.sort_values(by=['Price'])
        # Convert to HTML script
        results = sortedFrame.to_html()
        # Path to results.html
        path = "results.html"

        # Open cleared file to add header
        with open(path, 'w') as html:
            html.write(self.htmlHeader() + "\n")

        # TOD!!! Open this html file in separate tab
        # ^^^ Temporary Fix, look up how to move html table to another html file
        with open(path, 'a') as html:
            # Write will overwrite anything currently in file, cannot add anything to
            # results.html because it will be erased
            html.write("<body>")
            html.write(results)
            html.write("</body>")

    # Sequentially Scraping all websites
    # Every time this method is called, we clear all the previous data
    def scrapeWebsites(self):
        google = Google(self.searchCap)
        flightclub = FlightClub(self.searchCap)
        nike = Nike(self.searchCap)
        # Clear this instance's data every time we run a new search
        self.clearData()

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

        # Scrape FlightClub
        FC_bot = flightclub.search_bot
        FC_bot.findSearchbar()
        sleep(1)
        FC_bot.searchTerm(self.searchItem)
        sleep(1)
        FC_bot.pageScrape()
        self.__extendArrays(FC_bot.names, FC_bot.prices, FC_bot.links)
        FC_bot.quitSearch()

        # Scrape Google
        shop = google.search_bot
        shop.findSearchbar()
        sleep(1)
        shop.searchTerm(self.searchItem)
        sleep(1)
        shop.pageScrape()
        self.__extendArrays(shop.names, shop.prices, shop.links)
        shop.quitSearch()

        self.createMap()

    # Create arrays of names, prices, and links
    # Removes, pluses, commas and dollar signs from prices
    def __extendArrays(self, shoe_names, shoe_prices, shoe_links):
        self.shoeNames.extend(shoe_names)
        self.shoePrices.extend([price.replace("+", "").replace(",", "").replace("$", "") for price in shoe_prices])
        self.shoeLinks.extend(shoe_links)

    # Prints arrays to console for testing purposes
    def showArrays(self):
        print(self.shoeNames)
        print(self.shoePrices)
        print(self.shoeLinks)

    # Add Style Sheet to HTML file
    def htmlHeader(self):
        header = "<link rel=\"stylesheet\" href=\"styles.css\">"
        return header

    # Clears data to prevent html being overloaded and past results being shown
    # in a new search
    def clearData(self):
        # Clears all arrays
        self.shoeNames.clear()
        self.shoePrices.clear()
        self.shoeLinks.clear()

        # Clears html file
        path = "results.html"
        with open(path, 'r+') as html:
            html.truncate(0)
