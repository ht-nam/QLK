class Date:
    def __init__(self, day=0, month=0, year=0):
        self.__day = day
        self.__month = month
        self.__year = year

    def setDate(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def setday(self, day):
        self.__day = day

    def getDay(self):
        return self.__day

    def setMonth(self, month):
        self.__month = month

    def getMonth(self):
        return self.__month

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__day, self.__month, self.__year)
