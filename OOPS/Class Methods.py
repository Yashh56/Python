# class Employee:
#   company="Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   def changeCompany(cls, newCompany):
#     cls.company=newCompany

# e1=Employee()
# e1.name="Yash"
# e1.show()
# e1.name="Zoro"
# e1.changeCompany("Strawhats")
# e1.show()

from datetime import date


class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def fromBirthYear(cls, name, year):
    return cls(name, date.today().year - year)

  @staticmethod
  def isAdult(age):
    return age > 18


person1 = Person('Yash', 23)
person2 = Person.fromBirthYear('Yash', 2000)

print(person1.age)
print(person2.age)
print(Person.isAdult(21))
