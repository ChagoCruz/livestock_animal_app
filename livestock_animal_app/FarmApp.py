class FarmApp:
    def __init__(self):
        self.__livestockList = []

    def add_livestock(self, animal):
        self.__livestockList.append(animal)

    def get_livestock(self):
        return self.__livestockList 

    def get_total_price(self):
        price = 0
        for i in self.__livestockList:
            price += int(i.get_price())
            #price += temp_price
        return price

