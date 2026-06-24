# Бодлого 7: Улирал тодорхойлох
sar = int(input("Сарыг оруул (1-12): "))

if sar in [12, 1, 2]:
    print("Өвөл")
elif sar in [3, 4, 5]:
    print("Хавар")
elif sar in [6, 7, 8]:
    print("Зун")
elif sar in [9, 10, 11]:
    print("Намар")
else:
    print("Буруу сарын дугаар!")
