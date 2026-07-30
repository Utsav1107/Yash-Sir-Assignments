def student_detail():
    name = "hitesh"
    age = 22
    course = "BCA"
    return name , age , course

d,b,y = student_detail()

print("Name :",d)
print("Age :",b)
print("Course :",y)




x = 10


def show():
    x = 5
    print("Local X :",x)

def display():
    global x
    x = x + 6
    print("Modified X :",x)

show()
print("Global X before function call:",x)
display()

print("Global X after function call:",x)