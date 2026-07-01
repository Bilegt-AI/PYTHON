# 4. Тоон дараалал гурвалжин.
# Нүд бүрт дараалан өсөх тоо, гурвалжин хэлбэрт:

# 1
# 2 3
# 4 5 6
# 7 8 9 10

total=1
for i in range(4):
    for b in range(i*1+1):
        print(total,end=" ")
        total+=1
    print()
