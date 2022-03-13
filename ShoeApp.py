from ShoeFinder import Finder
from browser import Results

# Creates the Shoe Searcher User Interface. Allows 3 Options
# 1. View the last search's results
# 2. Start new search
# 3. Quit
class ShoeSearcherUI:

    # Instantiates Result object and Finder Object
    def __init__(self):
        self.finder = Finder()
        self.results = Results("results.html")

    # Runs the Shoe Finder class based on user input
    def run_finder(self):
        shoe = input("Enter a shoe to search: ")
        capacity = int(input("How many results would you like to see?: "))

        # Passes user input to search
        self.finder.setSearchItem(shoe)
        self.finder.setSearchCapacity(capacity)
        self.finder.scrapeWebsites()
        self.finder.createDataFrame()

        # Opens results in browser using Results object
        self.results.showResults()

    # Opens Menu
    def open_menu(self):
        with open("StarterMenu.txt", 'r') as file:
            content = file.read()
            print(content)

    # Opens the Shoe Searcher App Interface.
    # Ongoing loop until the user quits execution
    def open_application(self):
        stream = True

        while stream:
            self.open_menu()
            user = input("Enter: ")
            # If the user decides to quit
            if user == '3':
                print("Logging Off...")
                stream = False
            # If the user decides to view the last search's results
            elif user == '1':
                self.results.showResults()

            # If the user decides to start a new search
            elif user == '2':
                self.run_finder()

            # If there was invalid input, restart loop 
            else:
                print("Please select from the options below")
