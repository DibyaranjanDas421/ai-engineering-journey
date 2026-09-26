f = open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt","r")

data = f.read()

print(f"content inside file is = {data}")
print(type(data))


data1=f.readline()

print(f"line by line data {data1}")

f.close()