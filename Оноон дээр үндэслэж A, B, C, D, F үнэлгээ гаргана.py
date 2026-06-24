# Бодлого 2: Дүнгийн үнэлгээ
onoo = int(input("Оноо оруул (0-100): "))

if onoo >= 90:
    unelgee = "A"
elif onoo >= 80:
    unelgee = "B"
elif onoo >= 70:
    unelgee = "C"
elif onoo >= 60:
    unelgee = "D"
else:
    unelgee = "F"

print(f"Таны үнэлгээ: {unelgee}")
