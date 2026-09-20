class Student:
    def __init__(self,name,age,cgpa):  #parameterized (only one constructor should be their)
        self.age=age
        self.name=name
        self.cgpa=cgpa
    

    def get_cgpa(self):
        return self.cgpa


    def __init__(self):
        print("Constructor...................")   #default parameter the last one will be treated as a constructor 



stud1=Student("Rahul",27,9.0)
stud2=Student("Dibya",24,8.0)




print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}")
