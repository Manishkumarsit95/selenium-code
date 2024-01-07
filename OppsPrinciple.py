# Classes are user defined blueprint or prototype
# operation in a calculator Sum,Multiplication,addition,Constant
# Class Having Methods, Class variable,Instance variable,Constructor ete
# objects for your classes
class Calculators:
    num = 100

    def getdata(self):
        print("I am now executing as method in class")


obj = Calculators()
obj.getdata()
print(obj.num)

#___________ Constructor________________

class Calculator:
    num = 100 # Class variable and we can create multiple object
    #efault Construtor

    def __init__(self): # Construtor
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class ")


obj = Calculator() # syntax to create object in python
obj.getdata()
print(obj.num)

obj1 = Calculator() # syntax to create object in python
obj1.getdata()
print(obj.num)
print("------------------------------------------------")

class Calculator:

    num = 100 # Class variable and we can create multiple object
#default Construtor

    def __init__(self, a, b):  # Construtor decleare the para meter
        self.FirstNumber = a
        self.SecondNumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class ")

    def Summation(self):
        return self.FirstNumber + self.SecondNumber + Calculator.num #(Self.Num is also fine  .. Self is global and universal)


obj = Calculator(2,3) # syntax to create object in python
obj.getdata()
print(obj.num)
print(obj.Summation())


obj1 = Calculator(4, 5) # syntax to create object in python
obj1.getdata()
print(obj.num)
print(obj1.Summation())


