# Хэрэглэгчээс нууц үг оруулахыг хүс
# Зөв нууц үг: "1234"
# Буруу бол: "Буруу байна, дахин оруулна уу"
# Зөв бол: "Тавтай морил!"

num=int(input("Enter Any Number You Want: "))
while not num==1234:
    print("Буруу байна, дахин оруулна уу! ")
    num=int(input("Enter Any Number You Want: "))
print(f"Your Number Is Right{num}")
