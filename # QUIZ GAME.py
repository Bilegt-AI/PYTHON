# QUIZ GAME.

questions = [
    "Python хэдэн онд гарсан бэ?" "a) 1991" "b) 2000" "c) 1985",
    "Python interpreted хэл мөн үү? " "a) Тийм" "b) Үгүй",
    "print() функц юу хийдэг вэ? " "a) Хэвлэдэг" "b) Устгадаг" "c) Хадгалдаг"
]

answers = ["a", "a", "a"]
score=0
print(questions[0])
user_answer=input("Та хариултаа бичээрэй!")

if user_answer.lower()==answers[0]:
    print("Зөв!")
    score+=1
else:
    print(f"Буруу хариулт: {answers[0]}")
print(f"Таны оноо: {score}")


print(questions[1])
user_answer=input("Та хариултаа бичээрэй!")

if user_answer==answers[1]:
    print(f"Таны хариулт зөв байна!")
    score+=1
else:
    print(f"Таны хариулт буруу байна: {answers[1]}")
print(f"Таны оноо: {score}")


print(questions[2])
user_answer=input("Таны хариулт!")

if user_answer==answers[2]:
    print(f"Зөв хариулт {answers[2]}")
    score+=1
else:
    print(f"Таны хариулт буруу байна! {answers[2]}")
print(f"Таны оноо {score}")
