# Бодлого 6: Үсгийн төрөл тодорхойлох
t = input("Нэг үсэг оруул: ")

if t.isupper():
    print(f"'{t}' бол том үсэг")
elif t.islower():
    print(f"'{t}' бол жижиг үсэг")
elif t.isdigit():
    print(f"'{t}' бол тоо")
else:
    print(f"'{t}' бол тусгай тэмдэгт")
