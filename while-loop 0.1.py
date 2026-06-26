# while loop = execute some code WHILE some condition remains true.

name = input("Enter Your Name: ")


while name == "":
    print("You Did Not Enter Your Name: ")
    name = input("Enter Your Name: ")
print(f"Hello {name}")
