try:
 with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\assignments\cities.json1","r") as f:
    print(f.read())
except FileNotFoundError:
    print("File not found!")
 
