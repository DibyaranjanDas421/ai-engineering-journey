class Teacher:
    
    def __init__(self,salary):
        self.salary=salary


class Student:
       def __init__(self,gpa):
        self.gpa=gpa




class TA(Teacher,Student):

    def __init__(self,name,salary,gpa):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name=name

ta1=TA("Dibya",60000,8.9)    

print(f"name {ta1.name},salry{ta1.salary},gpa{ta1.gpa}")



