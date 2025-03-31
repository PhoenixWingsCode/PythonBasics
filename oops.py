class Student: #class name starts with capital
    name = "hiral"#class attribute
    collegeName = "ABC"
    def __init__(self, name, marks): #self is an alias
        self.name = name #here name is the variable
        self.marks = marks#obj attribute > class attribute
        print(self)
        print("Adding new constructor")

    @staticmethod
    def college():#decorator
        print("college")

    def welcome(self):
        print("welcome student", self.name)

s1 = Student("nirali",97)#Parenthesis are used to call the constructor 
print(s1)
print(s1.name, s1.marks)
s1.welcome()
s1.college()

print("Abstraction")
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started....")
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)
car1.start()

class Account:
    def __init__(self, num, password):
        self.num = num
        self.__password = password#this is a private attribute

    def write(self):
        print(self.__password)

account = Account(12345,"abcde")
print(account.num)
account.write()