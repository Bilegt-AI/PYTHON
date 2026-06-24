# Бодлого 4: Гурван тооноос хамгийн том
a = int(input("a оруул: "))
b = int(input("b оруул: "))
c = int(input("c оруул: "))

if a >= b and a >= c:
    print(f"Хамгийн том: {a}")
elif b >= a and b >= c:
    print(f"Хамгийн том: {b}")
else:
    print(f"Хамгийн том: {c}")
