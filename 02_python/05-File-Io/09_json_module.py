import json

#if the json data is in a String
#1- json to python object(dict)
data = '''
{
    "name": "Dibyaranjan Das",
    "isTeacher": true,
    "address": {
        "city": "Delhi",
        "country":null
    }
}
'''

print(type(data))

py_obj=json.loads(data)

print(py_obj,type(py_obj))

#2 python object to json

data1={
     "name": "Dibyaranjan Das",
    "isTeaacher": True,
    "adderss": {
        "city": "Delhi",
        "country": "India"
    }
}

print(type(data1))

json_data=json.dumps(data1)

print(type(data1),data1)


#2 if json data is in file format
#1- json to python object
with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\data.json","r") as f:
 data_file=json.load(f)
 print(type(data_file),data_file)

#2 python to json object
with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\data.json","w") as f:
 json.dump(data1,f,indent=4)

