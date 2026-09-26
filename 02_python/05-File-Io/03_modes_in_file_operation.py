#append mode(new text will apear at the end of the file)
f=open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt","a")

f.write("New being appended \n to the file")


f.close()

#x mode (create and opne file for writing)

f=open("sample2.txt","x")

f.write("Some random text")

f.close()

#rt,rb,wt,wb(b-for binary we will deal with this in CNN)
f=open("D:\AI-Engineering-Journey\02_python\05-File-Io\sample2.txt","rb")

data=f.read()
print(data)

f.close()



#r+,w+,a+
f=open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt","r+")

f.write("New being appended \n to the file")


f.close()


f=open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt","a+")

f.write("New being appended \n to the file")


f.close()


f=open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt","w+")

f.write("New being appended \n to the file")


f.close()