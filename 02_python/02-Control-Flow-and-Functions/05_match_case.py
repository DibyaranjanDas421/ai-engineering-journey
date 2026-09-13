color=input("Enter a color:")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case _:
       print("wrong color!")
