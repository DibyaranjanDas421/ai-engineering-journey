'''Q5. Write a function to return the sum of digits of a number, n .
'''


def sum_digit(num):

    sum=0

    while(num>0):
        sum +=(num%10)
        num=num//10
        
    return sum



num=int(input("Enter a number:"))
print(sum_digit(num))