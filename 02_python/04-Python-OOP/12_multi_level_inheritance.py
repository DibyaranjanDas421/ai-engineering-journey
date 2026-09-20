class Employee:
    start_tiime="9am"
    end_time="6pm"


class Staff(Employee):

    def __init__(self,role):
        self.role=role



class AccountStaff(Staff):

    def __init__(self,role,salary):
        super().__init__(role)
        self.salary=salary


a1=AccountStaff("SDE",60000)


print(f"start time {a1.start_tiime} ,end time {a1.end_time} ,role {a1.role} ,salary {a1.salary}")

