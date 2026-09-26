try:
 data=int(input("enter a number!"))
 res=10/data
except ZeroDivisionError:
    print(f"Divide byy zero is not allowed!")
except ValueError:
    print(f"Invalid input")
else:
    print(f"ans={res}")  
finally:
    print("end of the python program!")           