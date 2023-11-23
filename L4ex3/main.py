from logic import *
import random

def menu():
    print("""
    1 - schere
    2 - stein
    3 - papier
    
    """)

def main():
    mylist = ['schere', 'stein', 'papier']
    cont = 0
    y1 = 0              #punctaj calculator
    y2 = 0              #punctaj jucator
    while cont < 3:
        menu()
        opt = int(input("choose: "))
        x = random.choice(mylist)
        print(x)
        if test(opt, x):
            if logic(opt, x):
                y2 += 1             #returneaza True daca jucatorul castiga
            else:
                y1 += 1             #returneaza False --"--
        cont += 1

    if y1 >> y2:
        print("\nYOU LOST!\n")
        print(y1, ':', y2)
    elif y1 << y2:
        print("\nYOU WON!\n")
        print(y2, ':', y1)
    else:
        print("\nNO WINNER!\n")
        print(y1, ':', y2)

main()

