class Student:

  def set_name(self,name):
    self.__name=name

  def set_roll_no(self,roll_no):
    self.__roll_no=roll_no

  def set_marks(self,marks):
    self.__marks=marks

  def get_name(self):
    return self.__name

  def get_roll_no(self):
    return self.__roll_no

  def get_marks(self):
    return self.__marks




student1 = Student()

student1.set_name("Dibya")
student1.set_roll_no(101)
student1.set_marks(90)

print(student1.get_name())
print(student1.get_roll_no())
print(student1.get_marks())