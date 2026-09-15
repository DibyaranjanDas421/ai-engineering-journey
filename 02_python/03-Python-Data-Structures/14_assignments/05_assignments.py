stud_info={
}






def add_stud():
    name=input("Enter your name:")
    mark=int(input("Enter your mark:"))
    stud_info.update({
        name:mark
    })

def update_mark():
    name=input("Enter your name to update mark:")
    mark=int(input("Enter your mark:"))
    stud_info.update({
        name:mark
    }) 
    print("mark updated:")  


def search():
    name=input("Enter a name to search:")
    print(f"{stud_info.get(name)} data found:")

def display():
    print(f"data of all students{stud_info.values()}")    

def menu_program(menu):
    match menu:
        case "A":
            add_stud()
        case "B":
            update_mark()
        case "C":
            search()
        case "D":
            display()
        case _:
            print("Wrong choice!")            




while True:
 menu=input("Enter Quit for close choice A,B,C,D:")
 if(menu=="Quit"):
    break
 menu_program(menu)

 print(stud_info)