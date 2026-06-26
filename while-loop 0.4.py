# while loop = execute some code WHILE some condition remains true.

num = int(input("Enter a # Between 1 - 10: "))
while num<1 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a # Between 1 - 10: "))
print(f"Your Number Is {num}")
