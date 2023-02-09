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
        print("What do you want to know about? (Chose one of these)\n'S' if Sun\n'M' if Moon\n'E' if Earth")

#Star is an abstract class here
#class Star---<composition>Universe
class Star:
    def __init__(self):
        pass

    def locetion(self):
        return "gtnvum e tiezerqum u.size.size_ taracqov"

    def shining(self):

#class Moon--|inheritance>Star
class Moon(Star):
    def __init__(self, now):
        self.now = now

    def shining(self):
           
        if 6 <= self.nowh <= 11:
            return "Aravot e"
        elif 12 <= self.now <= 17:
            return "aravot e"
        elif 18 <= self.now <= 21:
            return "lusiny kamac kamac erevum e"
        else:
            return "gisher e, lusiny gexecik erevum e"

#class Sun--|inheritance>Star
class Sun(Star):
    def __init__(self, now):
        self.now = now

    def shining(self):
           
        if 6 <= self.nowh <= 11:
            return "Arevy cagum e ev sksum e lusavorel"

        elif 12 <= self.now <= 17:
            return "The sun is lighting amboxj paycarutyamb"
        elif 18 <= self.now <= 21:
            return "Arevy arden mayr e mtnum"
        else:
            return "gisher e"

#class Planet---<composition>Universe
class Planet:
    def __init__(self, galaxy, name, age, size):
        self.galaxy = galaxy
        self.name = name
        self.age = age
        self.size = size

#class Earth--|inheritance>Planet
class Earth(Planet):
    def __init__(self, galaxy, name, age, size, continent, ocean):
        super().__init__(galaxy, name, age, size)
        self.continent = continent
        self.ocean = ocean

    def galaxy_name(self):
        return self.galaxy

    def planet_name(self):
        return self.name

    def age(self):
        return self.age

    def size(self):
        return self.size

    def description(self):
        print(f'        Galaxy name: {galaxy_name()}')
        print(f'        Planet name: {planet_name()}')
        print(f'        Age: {age()}')
        print(f'        Size: {size}')
        print(f'Earth is divided into {continent} continents, and {ocean} oceans')


#class Oxygen---<composition>Earth
class Oxygen:
    def __init__(self):

#class Continent---<composition>Earth
class Continent:
    def __init__(self, continent, country):
        self.cont = continent
        self.country = country

#class Ocean---<composition>Earth
class Ocean:
    def __init__(self, name)
    

#class Inanimate---<composition>Earth
class Inanimate:

#class Building--|inheritance>Inanimate
class Building(Inanimate):

#class Animate---<composition>Earth
class Animate:
    def __init__(self, breath):
        self.breath = breath
    
    def awake(self, now):

#class Person--|inheritance>Animate
class Person(Animate):

#class Animal--|inheritance>Animate
class Animal(Animate):




# oxygen u carery assosiation kap unin

# constructor for initialization
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# instance method
	def emp_data(self):
		print('Name of Employee : ', self.name)
		print('Age of Employee : ', self.age)


class Data:
	def __init__(self, address, salary, emp_obj):
		self.address = address
		self.salary = salary

		# creating object of Employee class
		self.emp_obj = emp_obj

	# instance method
	def display(self):

		# calling Employee class emp_data()
		# method
		self.emp_obj.emp_data()
		print('Address of Employee : ', self.address)
		print('Salary of Employee : ', self.salary)

# creating Employee class object
emp = Employee('Ronil', 20)

# passing obj. of Emp. class during creation
# of Data class object
data = Data('Indore', 25000, emp)

# call Data class instance method
data.display()
