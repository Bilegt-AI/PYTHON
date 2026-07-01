# 6. Тэгш хэмт гурвалжин
# Голоос тэгш хэмтэй пирамид хэлбэр гарга:

#     *
#    ***
#   *****

n=3
for i in range(n):
    for b in range(n-1-i):
        print(" ",end="")
    for b in range(2*i+1):
        print("*",end="")
    print()
