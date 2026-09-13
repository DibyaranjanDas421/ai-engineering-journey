'''Write a program that takes as input. Using conditional statements,
calculate the based on these rules:
Q1 salary
final tax rate
• If salary < 30,000 → 5%
• If salary is 30,000–70,000 → 15%
• If salary > 70,000 → 25%
'''
def tax(salary):
    if(salary<30000):
        return (0.5*30000)
    elif(salary>=30000 and salary<70000):
        return(0.15*salary)
    else:
        return(0.25*salary)
    return 0;       

salary=int(input("Enter your salary :"))

print(tax(salary))



