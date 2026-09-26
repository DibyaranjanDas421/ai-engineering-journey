with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\assignments\log.txt","a+") as f:
 data=input("Enter name to append in file:")
 f.write(data + "\n")

 f.seek(0)       

 print(f.read())  

