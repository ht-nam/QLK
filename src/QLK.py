from src.Date import Date


class QLK:
    def __init__(self, name="", quantity=0, price=0, date=Date()):
        self.__name = name
        self.__quantity = int(quantity)
        self.__price = int(price)
        self.__expiryDate = date

    def setInfo(self, name, quantity, price, date):
        self.__name = name
        self.__quantity = int(quantity)
        self.__price = int(price)
        self.__expiryDate = date

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setQuantity(self, quantity):
        self.__quantity = int(quantity)

    def getQuantity(self):
        return self.__quantity

    def setPrice(self, price):
        self.__price = int(price)

    def getPrice(self):
        return self.__price

    def setExpDate(self, day, month, year):
        self.__expiryDate = Date(int(day), int(month), int(year))

    def getExpDate(self):
        return self.__expiryDate

    def getTotalPrice(self):
        return self.__price * self.__quantity

    def __str__(self):
        return "{:^25}{:^10}{:^10}{:^15}{:^15}".format(
            self.__name,
            str(self.__price),
            str(self.__quantity),
            str(self.getTotalPrice()),
            self.__expiryDate.__str__(),
        )
