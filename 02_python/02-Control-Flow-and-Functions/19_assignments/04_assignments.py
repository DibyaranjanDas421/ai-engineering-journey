'''Q4. Write a function to return the count the number of digits in a number, n .
'''


def count_digit(num):

    count=0

    while(num>0):
        count +=1
        num=num//10
        
    return count



num=int(input("Enter a number:"))
print(count_digit(num))

