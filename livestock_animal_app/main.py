from LiveStock import Alpaca
from LiveStock import Camel   
from LiveStock import Donkey
import FarmApp

def main():
    farm = FarmApp.FarmApp()
    animal1 = Alpaca(5, 600)
    animal2 = Camel(5, 3)
    animal3 = Donkey(6, 'Miniature')

    farm.add_livestock(animal1)
    farm.add_livestock(animal2)
    farm.add_livestock(animal3)

    animals = farm.get_livestock()
    print('List of Animals Sold')
    print('====================\n')

    for animal in animals:
        print(animal.get_animal_type(), '\t$', animal.get_price())
    print('\nTotal sales \t$', farm.get_total_price(), '\n')

    animal4 = Donkey(2, 'American Mammoth Jack')
    animal5 = Donkey(7, 'Burro')
    animal6 = Alpaca(2, 250)

    farm.add_livestock(animal4)
    farm.add_livestock(animal5)
    farm.add_livestock(animal6)

    for animal in animals:
        print(animal.get_animal_type(), '\t$', animal.get_price())
    print('\nTotal sales \t$', farm.get_total_price(), '\n')


main()
