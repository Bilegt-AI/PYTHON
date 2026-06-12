def calculator():
    print("=== Тооны машин ===")
    print("Гарах: 'q'")
    
    while True:
        try:
            a = input("\nЭхний тоо: ")
            if a == 'q': break
            
            op = input("Үйлдэл (+, -, *, /): ")
            
            b = input("Хоёр дахь тоо: ")
            if b == 'q': break
            
            a, b = float(a), float(b)
            
            if op == '+':   print("Хариу:", a + b)
            elif op == '-': print("Хариу:", a - b)
            elif op == '*': print("Хариу:", a * b)
            elif op == '/':
                if b == 0:  print("Алдаа: тэгд хуваах боломжгүй")
                else:       print("Хариу:", a / b)
            else:
                print("Буруу үйлдэл")
        except ValueError:
            print("Алдаа: тоо оруулна уу")

calculator()
