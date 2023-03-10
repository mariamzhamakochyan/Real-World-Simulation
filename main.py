import os
import time
import datetime

now = datetime.datetime.now()
localtime = time.asctime( time.localtime(time.time()))


class Universe:

    def __init__(self):
        print(localtime)
        print("Welcome to the Universe!\n")

    def size(self):
        size_ = 93
        return f'While the spatial size of the entire universe is unknown. The diameter of the observable universe is currently about {size_}  billion light years.'
    
    def matter(self):
        matter1 = "normal matter"
        matter2 = "dark matter"
        matter3 = "dark energy"
        return f'The Universe is thought to consist of three types of substance: {matter1}, {matter2} and {matter3}\n'

    def start(self):
        print(u.size())
        input()
        print(u.matter())
        input("Press enter to continue")
        # print("What do you want to know about? (Chose one of these)\n'S' if Sun\n'M' if Moon\n'E' if Earth")

#Star: abstract class
#class Star---<composition>Universe
class Star:
    def __init__(self, name):
        self.name = name

#class Moon--|inheritance>Star
class Moon(Star):
    def __init__(self, name, distance):
        super().__init__(name)
        self.distance = distance
    
    def get_distance(self):
        return self.distance

#class Sun--|inheritance>Star
class Sun(Star):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
    def get_size(self):
        return self.size

#class Planet---<composition>Universe
class Planet:
    def __init__(self, galaxy, name, age, surface_area):
        self.galaxy = galaxy
        self.name = name
        self.age = age
        self.surface_area = surface_area

#class Earth--|inheritance>Planet
class Earth(Planet):
    def __init__(self, galaxy, name, age, surface_area, continent, ocean):
        super().__init__(galaxy, name, age, surface_area)
        self.continent = continent
        self.ocean = ocean

    def galaxy_name(self):
        return self.galaxy

    def planet_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_surface_area(self):
        return self.surface_area

    def description(self):
        print(f'        Galaxy name: {e.galaxy_name()}')
        print(f'        Planet name: {e.planet_name()}')
        print(f'        Age: {e.get_age()}')
        print(f'        Surface area: {e.get_surface_area()}')
        print(f'Earth is divided into {self.continent} continents, and {self.ocean} oceans')

#class Oxygen---<composition>Earth
class Oxygen:
    def __init__(self, oxygen_lvl):
        self.oxygen_lvl = oxygen_lvl
    
    def increase(self, amount):
        self.oxygen_level += amount
    
    def decrease(self, amount):
        self.oxygen_level -= amount


#class Continent---<composition>Earth
class Continent:
    def __init__(self, continent, area, population):
        self.name = name
        self.area = area
        self.population = population

    def get_name(self):
        return self.continent

    def get_size(area):
        return self.area
    
    def get_population(self):
        return self.popultion

#class Ocean---<composition>Earth
class Ocean:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
    
    def get_name(self):
        return self.name

    def get_depth(self):
        return self.depth

#class Inanimate---<composition>Earth
class Inanimate:
    def __init__(self, name):
        self.name = name

#class Ground--|inheritance>Inanimate
class Ground(Inanimate):
    def __init__(self, name, hardness):
        super().__init__(name)
        self.hardness = hardness
    
    def get_hardness(self):
        return self.hardness
    
#class Building--|inheritance>Inanimate
class Building(Inanimate):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
    
    def get_height(self):
        return self.height
    
#class Nature--|inheritance>Inanimate
class Nature(Inanimate):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

#class Water--|inheritance>Inanimate
class Water(Nature):
    def __init__(self, name, type, temperature):
        super().__init__(name, type)
        self.temperature = temperature
    
    def get_temperature(self):
        return self.temperature
    
    def set_temperature(self, temperature):
        self.temperature = temperature

#class Animate---<composition>Earth
class Animate:
    def __init__(self, name):
        self.name = name

#class Person--|inheritance>Animate
class Person(Animate):
    def __init__(self, name, age, gender):
        super().__init__(name)
        self.age = age
        self.gender = gender

    def get_age(self):
        return self.age
    
    def get_gender(self, gender):
        self.gender = gender

#class Animal--|inheritance>Animate
class Animal(Animate):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    
    def get_species(self):
        return self.species


# make Car, Truck, Motorcycle, Boat, and Airplane. Inherit from the Vehicle class
