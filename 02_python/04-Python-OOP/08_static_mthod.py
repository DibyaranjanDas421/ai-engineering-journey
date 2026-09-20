class Laptop:
    storage_type="ssd"


    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage

    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"laptop has discounted price={final_price}")\



l1=Laptop("16GB","512GB")
l1.calc_discount(40000,10)                