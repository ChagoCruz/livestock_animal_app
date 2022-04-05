class Livestock:
    def __init__(self, age):
        self.__age = age
        self.__type = type
    
    def get_age(self):
        return self.__age

    def get_animal_type(self):
        return self.__type 

    def get_price(self):
        return 0 

class Alpaca(Livestock):
    def __init__(self, age, weight):
        self.__age = age
        self.__weight = weight
        self.__type = 'Alpaca'

    def get_animal_type(self):
        return self.__type

    def get_price(self):
        if self.__age <= 3:
            return 10000 
        elif self.__age > 3 and self.__weight <= 300:
            return 8000 
        elif self.__weight > 300:
            return 100000


class Camel(Livestock):
    def __init__(self, age, numberOfHumps):
        self.__age = age
        self.__numberOfHumps = numberOfHumps
        self.__type = 'Camel' 
    
    def get_animal_type(self):
        return self.__type

    def get_price(self):
        if self.__age <= 3:
            return 50000
        elif self.__age > 3 and self.__numberOfHumps == 2:
            return 150000 
        elif self.__age > 3 and self.__numberOfHumps == 3:
            return 200000 

class Donkey(Livestock):
    def __init__(self, age, breed):
        self.__age = age   
        self.__breed = breed 
        self.__type = 'Donkey'

    def get_animal_type(self):
        return self.__type

    def get_price(self):
        if self.__age <= 3:
            return 20000
        elif self.__age > 3 and self.__breed == 'Miniature':
            return 100000
        elif self.__age > 3 and self.__breed == 'Burro':
            return 120000 
        elif self.__age > 3 and self.__breed == 'American Mammoth Jack':
            return 180000
