# 1. Дөрвөлжин хэвлэх
# n=5 бол 5×5 хэмжээтэй *-аас бүрдсэн дөрвөлжин хэвлэ.

symbol=input("Enter * Here: ")
for rows in range(5):
    for columns in range(5):
        print(symbol, end="")
    print()
