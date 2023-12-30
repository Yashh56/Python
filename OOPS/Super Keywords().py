class Employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id


class Programmer(Employee):
  def __init__(self,name,id,lang):
    self.name=name
    super().__init__(name,id)
    self.lang=lang

yash=Employee("Yash Saini","596")
zoro=Programmer("Zoro","07","Python")
print(yash.name)
print(zoro.lang)