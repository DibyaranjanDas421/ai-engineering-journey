tup=(1,2,3,4,5,6,7,8,9,10)

odd_list=[]
even_list=[]



for i in tup:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)    



odd_tup=tuple(odd_list)
even_tup=tuple(even_list)


print(odd_tup)
print(even_tup)
