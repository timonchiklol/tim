from random import randint
import time
l = 3
c = 0
d = input("choose difficulty: easy,normal,hard. ")
if d == 'easy':
    l += 2
if d == 'hard':
    l -= 2
print("you are in front of a terrible haunted house")
time.sleep(3)
print("you are terribly cold")
time.sleep(3)
print("you see three doors")
time.sleep(3)
print("behind in one of the doors a ghost")
time.sleep(3)
print("behind in one of the doors a first-aid kit that will give you one life")
time.sleep(4)
print("behind in one of the doors a cat just a cat")
time.sleep(3)
print("the choice is yours")
while True:
    a = randint(1, 3)
    b = int(input("choose the door 1,2,3 "))
    if a == 1:
        print("buuuuuu i am  ghost -1 life ")
        if d == 'easy':
            c += 1
        elif d == 'hard':
            c += 3
        else:
            c += 2
        l -= 1
        if c == 30:
            print(" You Win:) ")
            break
        if l == 0:
            print("goodbye you died")
            break
        print("lives",l)
    elif a == 2:
        print(" You found a first aid kit")
        if d == 'easy':
            c += 1
        elif d == 'hard':
            c += 3
        else:
            c += 2
        l += 1
        if c == 30:
            print(" You Win:) ")
            break
    elif a == 3:
        print(" You found cat just cat")
        if d == 'easy':
            c += 1
        elif d == 'hard':
            c += 3
        else:
            c += 2
        if c == 30:
            print(" You Win:) ")
            break

print("you pass",c,"doors")