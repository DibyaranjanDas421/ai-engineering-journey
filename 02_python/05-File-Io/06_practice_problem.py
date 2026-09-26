with open(r"D:\AI-Engineering-Journey\02_python\05-File-Io\sample.txt", "r") as f:

    for line in f:
        if "python" in line:
            print("python word is there!")