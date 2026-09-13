
'''Design a program to continuously input a number from user & print if it is
positive or negative until the user enters “Quit”'''




while True:
    user_input=input("Enter a number or Quit: ")
    if user_input=="Quit":
        break
    num=int(user_input)

    if(num>0):
        print("positive")
    elif(num<0):
        print("negative")
    else:
        print("Zero")


