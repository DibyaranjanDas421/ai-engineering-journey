list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8]
list3 = [1, 2, 3]
list4 = [3, 4]

s1=set(list1)
s2=set(list2)

s3=set(list3)
s4=set(list4)


print(f"common elements between list1 and 2{s1.intersection(s2)}")
print(f"common elements between list3 and 4{s3.intersection(s4)}")