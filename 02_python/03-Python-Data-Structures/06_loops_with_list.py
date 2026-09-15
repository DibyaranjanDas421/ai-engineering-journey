list=[1,2,3,10,11,17]

for i in list:
    print(i)

# give me the idx of a number
idx=0
num=10

for i in list:
    if(i==num):
        print(f"number found at idx={idx}")
        break
    else:
        idx +=1