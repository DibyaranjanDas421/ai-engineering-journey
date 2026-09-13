age=int(input("Enter your age:"))


if (age<13) and (age>0):
  print("you are a child!")
elif (age>=13) and (age<=18):
    print("you are a teenager!")
elif age>18 and (age>0):
    print("you are a adult!")  
else:
    print("Invalid age")      


username=input("Enter username:")
password=input("Enter password:")


if(username=="admin" and password=="pass"):
    print("logged in")
elif(username != 'admin'):
    print("username is invalid!")
else:
    print("Invalid password!")     


n= int(input("enter num: "))

if (n%5==0):
    print("multiple of 5")
else:
    print("not multiple of 5")    