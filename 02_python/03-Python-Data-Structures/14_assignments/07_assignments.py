str=input("Enter a string to check space:")




count=0
for i in str:
    if(i==' '):
        count +=1


print(f"Entered string has {count} space")