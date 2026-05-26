"""class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Balaji", 20)
s1.display()"""
"""class Calculator: #  calculator
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

c = Calculator()

c.add(10, 5)
c.subtract(10, 5)"""
"""class BankAccount: #Bank Account Management
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.show_balance()"""
"""class Animal: #inheritance
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()"""
"""class Bird:  #polymorphism
    def sound(self):
        print("Bird chirps")

class Cat:
    def sound(self):
        print("Cat meows")

b = Bird()
c = Cat()

b.sound()
c.sound()"""
"""class Employee: #Encapsulation
    def __init__(self):
        self.__salary = 50000

    def show_salary(self):
        print("Salary:", self.__salary)

e = Employee()
e.show_salary()"""
"""class Car:
    def __init__(self, brand):     #constructor
        self.brand = brand

    def show(self):
        print("Car Brand:", self.brand)

c1 = Car("Toyota")
c1.show()"""
"""class Mobile:
    def __init__(self, name, price):     #Multiple objects
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "-", self.price)

m1 = Mobile("Samsung", 20000)
m2 = Mobile("iPhone", 80000)

m1.display()
m2.display()"""
"""from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):

    def start(self):
        print("Car starts with key")
class Bike(Vehicle):

    def start(self):
        print("Bike starts with button")
c = Car()
b = Bike()

c.start()
b.start()"""
class Rectangle:
    def __init__(self, length, width): # Area of rectangle
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

r = Rectangle(10, 5)
r.area()