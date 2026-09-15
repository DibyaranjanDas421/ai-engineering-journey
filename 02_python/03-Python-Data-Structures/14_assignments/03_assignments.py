

def input_data(list):
 for i in range(1,4):
    data=int(input(f"Enter {i} data to list {list} :"))
    list.append(data)


list1=[]
list2=[]

result=[]
input_data(list1)
input_data(list2)



result=list1+list2
result.sort()

print(result)





