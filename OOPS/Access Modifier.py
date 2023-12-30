# Various object-oriented languages like C++, Java, Python control access modifications which are used to restrict access to the variables and methods of the class. Most programming languages has three forms of access modifiers, which are Public, Protected and Private in a class.
# Python uses ‘_’ symbol to determine the access control for a specific data member or a member function of a class. Access specifiers in Python have an important role to play in securing data from unauthorized access and in preventing it from being exploited.
# A Class in Python has three types of access modifiers:

# Public Access Modifier
# Protected Access Modifier
# Private Access Modifier

# PUBLIC ACCESS MODIFIER

# class Geek:
#   def __init__(self,name,age):
#     self.Geekname=name
#     self.Geekage=age

#   # public member function
#   def displayAge(self):
#     # accessing public data member
#     print("Age:",self.  Geekage)

# # creating object of the class
# obj=Geek("Ya3h",18)

# # accessing public data member
# print("Name:",obj.Geekname)

# obj.displayAge()

# Protected Access Modifier

# class Student:
#   _name=None
#   _roll=None
#   _branch=None

#   def __init__(self,name,roll,branch):
#     self._name=name
#     self._roll=roll
#     self._branch=branch
#   def _displayRollAndBranch(self):
#     print("Roll:",self._roll)
#     print("Branch:",self._branch)

# class Geek(Student):
#   def __init__(self,name,roll,branch):
#     Student.__init__(self,name,roll,branch)

#   def displayDetails(self):
#     print("Name:",self._name)
#     self._displayRollAndBranch()

# obj=Geek("YaSh",2737,"CS")
# obj.displayDetails()

# Private Access Modifier


class Geek:
  __name = None
  __roll = None
  __branch = None

  def __init__(self, name, roll, branch):

    self.__name = name
    self.__roll = roll
    self.__branch = branch

  def __displaydetails(self):

    print("Name:", self.__name)
    print("Roll:", self.__roll)
    print("Branch:", self.__branch)

  def accessPrivateFunction(self):
    self.__displaydetails()


obj = Geek("Yash", 2763, "CS")

obj.accessPrivateFunction()
