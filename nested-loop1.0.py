# 1. Тэгш өнцөгт хэвлэх
# n мөр, m багана бүхий * тэмдэгтээс бүрдсэн тэгш өнцөгт хэвлэ.

rows=int(input("Enter Row #: "))
columns=int(input("Enter Columns #: "))
symbol=input("Enter Your Symbol: ")

for a in range(rows):
    for b in range(columns):
        print(symbol, end="")
    print()
