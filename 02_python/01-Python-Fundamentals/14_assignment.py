''' Write a program that asks the user for their name and age, then prints a
sentence like:
Q1
Hello Shradha, you are 21 years old! '''

name=input("Enter your name :")
age=int(int(input("Enter your age :")))

print("Hello",name,"you are",age,"years old!")


''' Take two numbers as input from the user and print their
.
Q2 sum, difference,
product, and quotient '''

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

sum=num1+num2
diffarence=num1-num2
product=num1*num2
quotient=num1/num2

print("sum is :",sum,"diffarence is :",diffarence,"product is :",product,"quotient is :",quotient)


'''Q3 Ask the user to enter two integers and one float. Convert them all to floats
and print their average.
'''

int1=float(input("Enter first integer:"))
int2=float(input("Enter second integer:"))
float1=float(input("Enter first integer:"))

avg=(int1+int2+float1)/3

print("avg is:",avg)


''' Q4. The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types. '''


str1=input("Enter s string:")
print("integer is",int(str1),"float is",float(str1),"string is",str1)



'''Q6. Write a program to swap values of two numbers entered by the user.
'''

number1=int(input("Enter first number:"))
number2=int(input("Enter second  number:"))

tmp=number1
number1=number2
number2=tmp

print("First number",number1,"Second number",number2)


'''Ask the user for a temperature in Celsius (string input). Convert it to ,
then calculate and print temperature in Fahrenheit.
Q7 float
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +'''


temp=input("Enter temprature in celsius :")

fahrenheit_temp=(float(temp)*(9/5)+32)

print("FahrenheitTemp is :",fahrenheit_temp)



'''Q8. Take the radius (r) as user input and print the area.
Use the formula: Area = π * r (value of π = 3.14)'''

radius=float(input("Enter radious :"))

print("Area =",(3.141*radius**2))


'''Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
compute simple interest:
Q9 float
SI = (P ∗ R ∗ T)/100'''

principal=int(input("Enter principal:"))
rate=int(input("Enter rate :"))
time=int(input("Enter time :"))
print("SI =",(principal*rate*time)/100)




'''Q10. Take a decimal number as input (like 45.78 ) and output its:
• integer part - 45
• fractional part - .78'''


a=45.78

print("Integer part -",int(a))
print("fractional part-",a-int(a))