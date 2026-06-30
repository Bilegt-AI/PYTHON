# 2. Үнэний хямдрал тооцоологч (arithmetic, format specifiers)
# Хэрэглэгчээс барааны үнэ болон хямдралын хувийг (%) асууж аваад, 
# хямдарсан эцсийн үнийг тооцоолж, 2 орны нарийвчлалтай хэвлэ.

first=float(input("Price "))
second=float(input("Margin "))
base_price=first*second
result=base_price/100
last_price=first-result
print(f"Хямдарсан үнэ {last_price:.2f}")
