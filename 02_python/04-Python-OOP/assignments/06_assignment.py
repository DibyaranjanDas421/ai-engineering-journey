from abc import ABC, abstractmethod
class Employee(ABC):



    @abstractmethod
    def calculate_salary(self):
        pass


class  Intern(Employee):

        def calculate_salary(self):
         return 1000


class  FullTimeEmployee(Employee):

        def calculate_salary(self):
         return 3000


class  ContractEmployee(Employee):

        def calculate_salary(self):
         return 2000