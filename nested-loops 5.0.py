# 4. Тэмдэгт ялгаатай тэгш өнцөгт
# 2 мөр, 6 баганатай, гэхдээ сондгой мөрөнд *, тэгш мөрөнд # ашигла:

for i in range(2):
    if i==0:
        symbol="*"
    else:
        symbol="#"
    for b in range(6):
        print(symbol,end="")
    print()
    
