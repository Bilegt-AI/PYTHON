# Бодлого 8: BMI тооцоолох
jin = float(input("Жин (кг): "))
undur = float(input("Өндөр (м): "))

bmi = jin / (undur ** 2)
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Турал")
elif bmi < 25:
    print("Хэвийн жин")
elif bmi < 30:
    print("Илүүдэл жин")
else:
    print("Таргалалт")
