'''Q3. Write a function that prints the digits of a number, n .
For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.'''


def digit(num):

    while(num>0):

        print(num%10)
        num=num//10



num=int(input("Enter a number:"))

digit(num)




