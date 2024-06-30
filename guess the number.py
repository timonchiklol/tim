from random import randint
c = 0
a = randint(1, 10)
while True:
    b = int(input("Write a number from 1 to 10: "))
    c += 1
    if b < a:
        print("your number less then my")
    elif b > a:
        print("your number bigger then my")
    else:
        print("You win!  Yesssss")
        print("            it took you",c,"attempts")
        break