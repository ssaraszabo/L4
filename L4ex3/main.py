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
    cont = 3
    while cont >> 0:        #< 3
        menu()
        x = random.choice(mylist)
        opt = int(input("choose: "))
        print(x)
        score += logic(opt, x)
        cont -= 1

    if score >> 0:
        print("\nYOU WON!\n")
    elif score << 0:
        print("\nYOU LOST!\n")
    else:
        print("\nNO WINNER!\n")

main()

