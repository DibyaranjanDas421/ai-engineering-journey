info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

#list all unique course

unique_course=set()

for i in info:
    unique_course.add(i[1])

print(f"unique cours's are{unique_course}")

#list student enrolled in english
english_enrolled=[]
for i in info:
    if(i[1]=="English"):
        english_enrolled.append(i[0])

print(f"list student enrolled in english are {english_enrolled}")  


#create dictionary
student_info={}
for i in info:
  student=i[0]
  course=i[1]
  if student not in student_info:
    student_info[student]=[]
  student_info[student].append(course)    

print(f"dictiory of student's is {student_info}")