# 8. Ээлжлэн солигдох гурвалжин
# * ба # ээлжлэн солигдоно:

#    *
#    # #
#    * * *
#    # # # #


for Akaza in range(4):
    if Akaza%2==0:
        Demon="*"
    else:
        Demon="#"
    for Rengoku in range(Akaza*1+1):
        print(Demon,end="")
    print()
