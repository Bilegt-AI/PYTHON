# 2. Үнэний хямдрал тооцоологч (arithmetic, format specifiers)
# Хэрэглэгчээс барааны үнэ болон хямдралын хувийг (%) асууж аваад, 
# хямдарсан эцсийн үнийг тооцоолж, 2 орны нарийвчлалтай хэвлэ.

price=float(input("Give Me A Price Your Priduct! "))
margin=float(input("What's The Margin! "))
discount_price=price*margin/100
last_price=price-discount_price
print(f"Your Product Real Price is {last_price:.2f}")
