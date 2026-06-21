#input()

name=input("What's your name?: ")
age=int(input("How old are you?"))

    #age=age+1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old!")

        #Exercise 1.

length=float(input(" Enter the length: "))
width=float(input(" Enter the width: "))
area=length * width

print(f"The area is: {area}cm²")

item=input("What item would you like to buy?: ")
price=float(input("What is the price?: "))
quantity=int(input("How many would you like?: "))
total= price*quantity

print(f"You have bought {quantity} X {item}/s ")
print(f"Your total is: ${total}")
