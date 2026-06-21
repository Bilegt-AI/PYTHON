#Хэрэглэгчээс тойргийн радиус асууж аваад тойргийн урт болоод талбайг олох бодлого!

import math

print("Та тойргийн радиус оруулаарай! ")
radius=float(input("Radius: " ))
circumference=2*math.pi*radius
print(f"Тойргийн урт {round(circumference, 2)} байна")

print("Та талбайн тайлбайг олохын тулд радиусыг оруулаарай! ")
area=input("Area: ")
area=math.pi*pow(radius, 2)
print(f"Тойргийн талбайн хэмжээ {round(area, 2)} байна!")
