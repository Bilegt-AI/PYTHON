# Python Compound Interest Calculator.

principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the Principle Amount:"))
    if principle<=0:
        print("Principle Can't be Less Than or Equel To Zero")

while rate<=0:
    rate=float(input("Enter the Interest Rate:"))
    if rate<=0:
        print("interest rate Can't be Less Than or Equel To Zero")

while time<=0:
    time=int(input("Enter the Time In Years:"))
    if time<=0:
        print("Time Can't be Less Than or Equel To Zero")

total=principle*pow((1+rate/100),time)
print(f"Balance After {time} Year/s: ${total:.2f}")
