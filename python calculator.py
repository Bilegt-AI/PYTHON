# PYTHON calculator.
operator=input("Enter an operaator(+ - * /):")
num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2ns number:"))
if operator=="+":
    result=num1+num2
    print(round(result, 3))
elif operator=="_":
    result=num1-num2
    print(round(result, 3))
elif operator=="*":
    result=num1*num2
    print(round(result, 3))
elif operator=="/":
    result=num1/num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")
