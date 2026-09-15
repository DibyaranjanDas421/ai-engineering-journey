'''Q1. Ask the user for a string and check whether it is a palindrome or not.
'''


def check_palindrome(str):
    start=0
    end=len(str)-1
    while(start<end):
        if(str[start]==str[end]):
            start +=1
            end  -=1
        else:
            return False
    return True            
     
str=input("Enter s string to check palindrome or not:")

print(check_palindrome(str))



