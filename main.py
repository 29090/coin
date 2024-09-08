import random

while True:

    user=input("Укажите орел или решкро: ")
    computer=random.choice(["орел", "решко"])

    if user !=computer:
        print("Вы проиграли!")
    else:
        print("Вы выиграли!")