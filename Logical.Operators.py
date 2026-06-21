# and
# (both conditions must be True)

# not
# (inverts the condition (not False, not True))
# (False байсан бол True болгоно, True байсан бол False болно!)

temp=0
is_sunny=False

if temp>=28 and is_sunny:
    print("It is HOT outside")
    print("It is Sunny")
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is Sunny")
elif 28>temp>0 and is_sunny:
    print("It is WARM outside")
    print("It is Sunny")


elif temp>=28 and not is_sunny:
    print("It is HOT outside")
    print("It is Claudy")
elif temp <=0 and not is_sunny:
    print("It is COLD outside")
    print("It is Claudy")
elif 28>temp>0 and not is_sunny:
    print("It is WARM outside")
    print("It is Claudy")
