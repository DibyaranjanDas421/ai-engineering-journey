import json


cities = {
    "Delhi": 32900000,
    "Mumbai": 21600000,
    "Bengaluru": 14000000
}

with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\assignments\cities.json","w+") as f:
    json.dump(cities,f,indent=4)
    f.seek(0)       

    print(f.read())


new_city=input("Enter new city:")  
new_population=input("Enter new population:") 

cities.update({new_city:new_population})

print(cities)


with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\assignments\cities.json","w+") as f:
    json.dump(cities,f,indent=4)





