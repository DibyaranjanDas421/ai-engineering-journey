def calculator(a,b,operation):
    if(operation=='+'):
        return a+b
    elif(operation=='-'):
        return a-b
    elif(operation=='/'):
        return a/b
    elif(operation=='*'):
        return a*b
    else:
        return 0


print(calculator(3,4,'+'))    
print(calculator(3,4,'*'))  
print(calculator(3,4,'a'))                    


