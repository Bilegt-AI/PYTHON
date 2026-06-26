# format specifiers = {value:flags} format a value based on what
#                                   flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1=3.14159
price2=-987.65
price3=12.34

print(f"Price 1 is ${price1:.2f}") #:.2f гэдэг нь тоог аравтын 2 орон хүртэл бөөрөнхийлж хэвлэнэ.
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 3 is ${price3:10}") # одоо үр дүн нь 10 зайтай гарж ирнэ. 
print(f"Price 3 is ${price3:<10}") # < хэрэглэвэл 10 нэгж зай нь байхгүй болно. Гэхдээ ард нь зай үлдэнэ.
print(f"Price 3 is ${price3:>10}") # 10 гэж бичхийн оронд ">" хэрэглэвэл 10 нэгж зай авна.
print(f"Price 3 is ${price3:^10}") # text голлоно.


total=3000.3132
print(f"Price Is ${total:+,.2f}")
