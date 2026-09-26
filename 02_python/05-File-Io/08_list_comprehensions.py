list=[i*i for i in range(6)]
print(list)

odd_list=[i*i for i in range(6) if i%2!=0]

print(odd_list)

negative_list=[-2,-4,3,5,2,-1]

new_list=[0 if i<0  else i for i in negative_list]

print(new_list)


words=["hello","Dibya"]

words=[val.upper() for val in words]

print(words)