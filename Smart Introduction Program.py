#Smart Introduction Program
condition=True
while condition:
    name=input("Enter the name: ")
    f=0
    for ch in name:
        if ch.isspace():
            print("Enter a valid name.")
            f=1
            break
    if(f==1):
        continue
    elif(f==0):
        condition=False
    
condition=True
while condition:
    gender=input("Enter the gender: ")
    f=0
    for ch in gender:
        if ch.isspace():
            print("Enter a valid gender.")
            f=1
            break
        if(f==1):
            continue
        elif(f==0):
            condition=False
gender=gender.upper()
if(gender=='MALE'):
    print("Hello",name,",sir")
elif(gender=='FEMALE'):
    print("Hello",name,",ma'am")
else:
    print("Entered an invalid gender.")

condition=True
while condition:
    age=input("Enter age: ")
    f=0
    for ch in age:
        if ch.isspace():
            print("Enter a valid age.")
            f=0
            break
        if ch.isdigit():
            f=1
            break
    if(f==1):
        condition=False
    elif(f==0):
        print("Input age in numbers.")
        continue

age=int(age)
if(gender=='MALE'):
    if(age>20):
        print("You are eligble to enroll for Python Fundamental Course.")
    else:
        print("You are not eligible to enroll for Python Fundamental Course.")
else:
    if(age>19):
        print("You are eligble to enroll for Java Course.")
    else:
        print("You are not eligible to enroll for Java Course.")
        
        
    
