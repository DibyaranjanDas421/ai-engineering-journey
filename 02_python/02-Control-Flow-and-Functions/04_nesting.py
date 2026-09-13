username=input("Enter username:")
password=input("Enter password:")



if(username=='admin' and password=='pass'):
    print("logged in!")
else:
    if(username!='admin'):
        print("Invalid username!")
    else:
        print("Invalid password!")
               