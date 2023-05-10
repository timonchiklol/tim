
from random import randint
import time
win = 0
loss = 0
while True:
    lol = input(" are you ready? ")
    if lol == 'yes':
        kek = int(input("choose one: (rock = 1, papir = 2, Scissors = 3) "))
        print("1", end = " ")
        time.sleep(1)
        print("2", end = " ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        a = randint(1, 3)
        if a == 1:
          print("Rock")
        if a == 2:
          print("Papir")
        if a == 3:
          print("Scissors")
        if kek == 1 and a == 3:
          print("You WIN :)")
          win = win + 1
          print("                               wins                             ", win)
          print("                               losses                           ", loss)
        elif kek == 2 and a == 1:
          print("You WIN :)")
          win = win + 1
          print("                               wins                             ", win)
          print("                               losses                           ", loss)
        elif kek == 3 and a == 2:
          print("You WIN :)")
          win = win + 1
          print("                               wins                             ", win)
          print("                               losses                           ", loss)
        elif kek == a:
          print("Draw :|")
          print("                               wins                             ", win)
          print("                               losses                           ", loss)
        else:
          print("You loss :(")
          loss = loss + 1
          print("                               wins                             ",win)
          print("                               losses                           ",loss)

