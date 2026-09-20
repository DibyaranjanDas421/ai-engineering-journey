class Laptop:
    storage_type="ssd"


    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage



    @classmethod
    def get_storage(cls):
        print(f"storage type={cls.storage_type}")
        # print(f"storage type={cls.ram}")  # class methos can't access instance variable



l1=Laptop("16GB","128GB")

Laptop.get_storage()

l1.get_storage()

