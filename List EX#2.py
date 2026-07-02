# Даалгавар 2: Өөрчлөлт хийх
# Дээрх animals list дээр:

# a) "lion"-ийг "panda" болгож солих (index ашиглан)
# b) list-ийн эхэнд (0-р index) "fish" нэмэх (insert ашиглан)
# c) "tiger"-ийг list-ээс устгах (remove ашиглан)
# d) list-ийн төгсгөлд "zebra" нэмэх (append ашиглан)
# e) Үр дүнг хэвлэ

animals = ["dog", "cat", "elephant", "lion", "tiger"]

animals[3]="panda"
print(animals)

animals.insert(0,"fish")
print(animals)

animals.remove("tiger")
print(animals)

animals.append("zabra")
print(animals)
