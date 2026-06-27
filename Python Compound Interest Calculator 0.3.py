# Python Compound Interest Calculator.

principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the Principle Amount:"))
    if principle<0:
        print("Principle Can't be Less Than Zero")
    else:
        break

while True:
    rate=float(input("Enter the Interest Rate:"))
    if rate<0:
        print("interest rate Can't be Less Than Zero")
    else:
        break

while True:
    time=int(input("Enter the Time In Years:"))
    if time<0:
        print("Time Can't be Less Than Zero")
    else:
        break

total=principle*pow((1+rate/100),time)
print(f"Balance After {time} Year/s: ${total:.2f}")
