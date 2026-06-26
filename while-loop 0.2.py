# while loop = execute some code WHILE some condition remains true.

age = int(input("Enter Your Age"))
while age<0:
    print("Age Can't be Negative")
    age = int(input("Enter Your Age"))
print(f"You Are {age} Years Old! ")
