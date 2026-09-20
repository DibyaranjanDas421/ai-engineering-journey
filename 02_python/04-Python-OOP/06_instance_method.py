class Laptop:
    storage_type="ssd"


    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage


    def get_info(self):
        print(f"laptop has {self.ram} and {self.storage} and {self.storage_type}")  # can access class variables also





l1=Laptop("8GB","128GB")
l2=Laptop("16GB","256GB")

l1.get_info()

l2.get_info()


