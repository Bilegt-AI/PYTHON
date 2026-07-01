# 5. Зүүн талын гурвалжин
# *-уудыг баруун талд тэгшлэж хэвлэ (зай ашиглан):

#     *
#    **
#   ***
#  ****
# *****

n=5
for i in range(n):
    for b in range(n-1-i):
        print(" ",end="")
    for b in range(i+1):
        print("*",end="")
    print()
