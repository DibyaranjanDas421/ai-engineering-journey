class Product:
    total_created_product = 0

    def __init__(self, name, price):
        Product.track_product()
        self.name = name
        self.price = price

    @classmethod
    def track_product(cls):
        cls.total_created_product += 1

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        return final_price


l1 = Product("HP", 45000)
l2 = Product("Dell", 50000)

discounted_price = Product.calc_discount(l1.price, 10)

print("Discounted price:", discounted_price)
print("Total products:", Product.total_created_product)