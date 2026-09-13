import math
def is_prime(num):
    for i in range(2,math.floor(math.sqrt(num))):
        return True

    return False        



num=int(input("Enter a number to chec prime or not:"))

print(is_prime(num))

