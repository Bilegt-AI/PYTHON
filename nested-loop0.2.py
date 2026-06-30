# Nested Loop = a loop whthin another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows=int(input("Enter The # Of Rows: "))
columns=int(input("Enter The # Of Columns: "))
symbol=input("Enter A Symbol To Use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
