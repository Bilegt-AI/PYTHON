    #print(help(str)) #энэ нь python дээр байгаа бүхий л method-ыг харуулдаг.
#VALIDATE USER INPUT EXERCISE.

#if len(username)>12:
    #print("Your username can't be more than 12 characters")
#else:
    #print(f"Welcome {username}")

username=input("Enter a username:")

if len(username)>12:
    print("Your username can't be more than 12 charecters!")
elif not username.find(" ")==-1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
