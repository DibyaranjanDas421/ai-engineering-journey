with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\assignments\sample.txt","a+") as f:
 for i in range(5):
    data=input("Enter name to append in file:")
    f.write(data + "\n")

 f.seek(0)       

 print(f.read())  

