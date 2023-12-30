#CLASS

# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.


class person:
  name = "Yash"
  Occ = "Software Developer"
  networth = 65000

  def info(self):
    print(f"{self.name} is a {self.Occ}")


a = person()
b = person()
a.name = "Zoro"
a.Occ = "Swordsman"
# print(a.name)    This is the object  object is the instance of the class used to access the properites of the class.
b.name = "Shanks"
b.Occ = "Yonko"
print(b.Occ)
a.info()
b.info()


class Myclass:
  x = 5


p1 = Myclass()
print(p1.x)

# CONSTRUCTORS

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created


class Dog:

  # class attribute
  attr1 = "mammal"

  # Instance attribute
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"my name is {self.name}")


# Driver code
# object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()


class GFG:

  def __init__(somename, name, company):
    somename.name = name
    somename.company = company

  def show(somename):
    print(f"Hello My name is {somename.name} and I work in {somename.company}")


obj = GFG("Yash", "GeeksForGeeks")
obj.show()

# DECORATORS


def greet(fx):

  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")

  return mfx


@greet
def hello():
  print("Hello World")


def add(a, b):
  print(a + b)


hello()
greet(add)(1, 2)

# GETTERS AND SETTERS


class Myclass:

  def __init__(self, value):
    self._value = value

  def show(self):
    print(f"Value is {self._value}")

  @property
  def ten_value(self):
    return 10 * self._value

  @ten_value.setter
  def ten_value(self, new_value):
    self._value = new_value / 10


obj = Myclass(10)
obj.ten_value = 100
print(obj.ten_value)
obj.show()

# Inheritance in python


class Employee:

  def __init__(self, name, id):
    self.name = name
    self.id = id

  def showdetails(self):
    print(f"The name of Employee:{self.id} is {self.name}")


class programmer(Employee):

  def showLanguage(self):
    print("The default language is python")


e1 = Employee("Zoro", 1)
e2 = programmer("Yash", "47")
e1.showdetails()
e2.showLanguage()
