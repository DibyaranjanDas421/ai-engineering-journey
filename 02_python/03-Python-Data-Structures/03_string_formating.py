#by using format function
a=5
b=10
sum=a+b
print("sum is {}".format(sum))
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a,b,sum))
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based formating

print("values of vars {a} & {b}".format(a=5,b=10))

#by using f-strings

b=10
c=15
print(f"sum of {a} & {b} is {a+b}")