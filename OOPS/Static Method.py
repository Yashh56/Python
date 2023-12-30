# Static Method


class Maths():

  @staticmethod
  def addNum(num1, num2):
    return num1 + num2


if __name__ == "__main__":
  res = Maths.addNum(10, 10)
  print("The Result is", res)


class Person():

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @staticmethod
  def isAdult(age):
    return age > 18


if __name__ == "__main__":
  res = Person.isAdult(17)
  print('Is person adult:', res)

  res = Person.isAdult(22)
  print('\nIs Person adult:', res)
