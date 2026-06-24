# Бодлого 10: Хямдралын тооцоо
dun = float(input("Нийт дүн (₮): "))

if dun >= 100000:
    huvi = 20
elif dun >= 50000:
    huvi = 15
elif dun >= 20000:
    huvi = 10
elif dun >= 10000:
    huvi = 5
else:
    huvi = 0

hyamdral = dun * huvi / 100
print(f"Хямдрал: {huvi}% = {hyamdral:.0f}₮")
print(f"Төлөх дүн: {dun - hyamdral:.0f}₮")
