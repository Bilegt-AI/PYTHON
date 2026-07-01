# 5. Эгнээ бүрт өсөж буй тоо
# 3 мөр, 3 баганатай, гэхдээ нүд бүрт 1-ээс эхлэн дараалан 
# өсөх тоо бич (мөр болгонд биш, нийт):

counter=1
for b in range(3):
    for i in range(3):
        print(counter,end=" ")
        counter+=1
    print()
