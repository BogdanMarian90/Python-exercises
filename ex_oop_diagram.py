# Diagram 1
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Creature(ABC):
    pass

    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def __init__(self, age, weight):
        self.age = age
        self.wieght = weight

    def eat(self):
        print(f"I am an eating {self.__class__.__name__}")


class WildAnimal(Animal):
    def __init__(self, age, weight, location):
        super().__init__(age, weight)
        self._location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value


class DomesticAnimal(Animal):
    def __init__(self, age, weight, owner, location):
        super().__init__(age, weight)
        self.owner = owner
        self._location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value


class JungleAnimal(WildAnimal):
    def __init__(self, age, weight):
        super().__init__(age, weight, "Jungle")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception("Unable to modify location")


class ForestAnimal(WildAnimal):
    def __init__(self, age, weight):
        super().__init__(age, weight, "Forest")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception("Unable to modify location")


class Pet(DomesticAnimal):
    def __init__(self, age, weight, owner, name):
        super().__init__(age, weight, owner, "House Yard")
        self.name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception("Unable to modify location")


p1 = Person("Bogdan", 22)
dog = Pet(10, 15, "Bogdan", "Rex")
wolf = ForestAnimal(10, 25)
bird = JungleAnimal(10, 3)
cow = DomesticAnimal(5, 250, "Bogdan", "House Yard")

# wolf.location = "House"
list = [dog, wolf, bird, cow]
for animal in list:
    animal.eat()
    # print(animal.age)
    # print(animal.wieght)

print(dog.owner, dog.age, dog.name, dog.wieght, dog.location)



# Diagram 2

from abc import ABC


class Vehicle(ABC):
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    def start_engine(self):
        print("You start the engine!")

    def stop_engine(self):
        print("Your engine is stopped!")

    @property
    def set_color(self):
        return self._color

    @set_color.setter
    def set_color(self, value):
        raise Exception("Unable to change car color")


class Car(Vehicle):
    def __init__(self, brand, color, model, max_speed):
        super().__init__(brand, color)
        self._model = model
        self._max_speed = max_speed

    def accelearte(self):
        print(f"Your car is accelerate vrummm vrumm!!!")


class ElectricCar(Car):
    def __init__(self, brand, color, model, max_speed, battery_capacity):
        super().__init__(brand, color, model, max_speed)
        self._battery_capacity = battery_capacity

    def charge_batery(self, value):
        if value < 0:
            raise Exception("Negative charging!")

        if value < self._battery_capacity:
            print(f"You need to charge up to {self._battery_capacity - value}")

        if value > self._battery_capacity:
            raise Exception(f"Unable to charge more than {self._battery_capacity}")

        if value == self._battery_capacity:
            print("Finish charging!")


c1 = Car("Dacia", "Red", "Logan", 180)
c1.start_engine()
c1.accelearte()
print(c1.set_color)
# c1.set_color = "Black"

ec1 = ElectricCar("Volovo", "Black", "XC90", 300, 50000)
ec1.start_engine()
ec1.accelearte()
ec1.stop_engine()
ec1.charge_batery(20000)
ec1.charge_batery(50000)
print(ec1.set_color)
# ec1.set_color = "Red"


# Diagram 3
class Employee:
    def __init__(self, id, name, salary):
        self._id = id
        self._name = name
        self._salary = float(salary)

    def get_details(self):
        print(f"I am {self._name}, I have {self._id}, my salary is {self._salary}")

    def calculate_pay(self):
        return self._salary * 12


class Manager(Employee):
    def __init__(self, id, name, salary, team):
        super().__init__(id, name, salary)
        self._team = team

    def assign_task(self):
        print("We have to do something!")

    def get_team(self):
        return self._team


class Developer(Employee):
    def __init__(self, id, name, salary, programming_languages):
        super().__init__(id, name, salary)
        self._programming_languages = programming_languages

    def __repr__(self):
        return (f"\nId :{self._id}, "
                f"Name: {self._name}, "
                f"Salary: {self._salary}, "
                f"Prog_lang: {self._programming_languages}\n")

    def write_code(self):
        print("You write the code!")

    def get_languages(self):
        return self._programming_languages


dev1 = Developer(15, "Bogdan", 3000.500, ["Python", "Java", "C++"])
print(dev1.get_languages())
dev1.write_code()
dev2 = Developer(16, "Ion", 3000.500, ["JS", "Java", "PHP"])
dev3 = Developer(17, "Maria", 3000.500, ["Html", "Css", "C++"])

print("*" * 40)

dev_team = [dev1, dev2, dev3]
print(dev_team)
print("*" * 40)

manager = Manager(1, "Alex", 8000, dev_team)

for dev in manager.get_team():
    print(dev.get_languages())
manager.assign_task()
