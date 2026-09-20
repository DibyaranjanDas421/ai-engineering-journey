from collections.abc import AsyncGenerator
class Student:
    college="Bput"


    def __init__(self,name,gpa):
        self.gpa=gpa
        self.name=name


stud1=Student("Rahul",9.0)

# print(Student.name)  # here we will get an error Student class  dose not have any attribute name(name belongs to object level like stud)

print(Student.college) # but the college attribute is belongs to class Student

