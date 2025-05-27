num = int(input("Enter the number of Students: "))
d ={}
for i in range(num):
    name = input("Enter the name of the students: ")
    marks = int(input("Enter the marks of the students: "))
    d[name] =marks
print("The Students name and their marks are: ")
for ch in d:
    print("The name of the Students is",ch, "and the marks is", d[ch])