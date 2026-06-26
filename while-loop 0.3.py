# while loop = execute some code WHILE some condition remains true.

food = input("Enter a Food You Like(q to quit)")

while not food=="q":
    print(f"You Like {food}")
    food = input("Enter Another Food You Like(q to quit)")
print("Bye")
