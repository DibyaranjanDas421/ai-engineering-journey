info={
    "name":"Dibya",
    "gpa":7.9,
    "subject":["Math","CS"],
    3.14:"PI"
}


keys=info.keys()
print(keys,type(keys))
print(list(keys))

values=info.values()
print(values,type(values))
print(list(values))


items=info.items()
print(items,type(items))
print(list(items))


#get vs key
# print(info["gpa2"])
print(info.get("gpa2"))

print("End of code")  # not executed