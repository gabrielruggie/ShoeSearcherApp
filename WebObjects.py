from SearchBot import WebScrapper

class FlightClub:

    def __init__(self, capacity):
        self.__PATH = "/Users/gabrielruggie/Desktop/chromedriver"
        self.__URL = "https://www.flightclub.com/"
        self.__searchbar_xpath = "/html/body/div[1]/div/div[1]/div/nav/div[1]/div/span/input"
        self.__results = "sc-1wc5x2x-0"
        self.__shoeName = "sc-10kqv19-0"
        self.__shoePrice = "whkzwq-5"

        self.capacity = capacity

        self.search_bot = WebScrapper(self.__PATH, self.__URL,
        self.__searchbar_xpath, self.__results, self.__shoeName, self.__shoePrice)

        self.search_bot.setCapacity(self.capacity)
        self.search_bot.isLinkedProduct()


class Nike:

    def __init__(self, capacity):
        self.__PATH = "/Users/gabrielruggie/Desktop/chromedriver"
        self.__URL = "https://www.nike.com/"
        self.__searchbar_xpath = "/html/body/div[1]/div[3]/header/div/div[1]/div[2]/div/div/div[1]/div/div/input"
        self.__results = "product-card"
        self.__shoeName = "product-card__title"
        self.__shoePrice = "product-price"

        self.search_bot = WebScrapper(self.__PATH, self.__URL,
        self.__searchbar_xpath, self.__results, self.__shoeName, self.__shoePrice)

        self.search_bot.setCapacity(capacity)


class Google:

    def __init__(self, capacity):
        self.__PATH = "/Users/gabrielruggie/Desktop/chromedriver"
        self.__URL = "https://shopping.google.com/?sa=X&ved=2ahUKEwj3-qXR4Lz1AhVsS28EHfRUByUQtukFegQIABAS"
        self.__searchbar_xpath = "/html/body/c-wiz[1]/div/div/c-wiz/form/div[2]/div[1]/input"
        self.__results = "sh-dgr__grid-result"
        self.__shoeName = "Xjkr3b"
        self.__shoePrice = "a8Pemb"

        self.search_bot = WebScrapper(self.__PATH, self.__URL,
        self.__searchbar_xpath, self.__results, self.__shoeName, self.__shoePrice)

        self.search_bot.setCapacity(capacity)
