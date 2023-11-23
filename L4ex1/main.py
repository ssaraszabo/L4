from letters import *

f = open('datei.txt', 'w')
f.close()

def menu():
    print(
    """
    W - der Stift bewegt sich 10 Pixel vorwärts
    S - der Stift bewegt sich 10 Pixel rückwärts
    D - der Stift dreht sich um 45 Grad nach rechts
    A - der Stift dreht sich um 45 Grad nach links
    F - hebt den Stift nach oben (Zeichnen stoppt)
    G - legt den Stift wieder ab (Zeichnen wird fortgesetzt)
    stop - exit
    """)

f = open("datei.txt", "a")

def main():
    while True:
        menu()
        com = input("choose: ")
        if com == 'w':
            W()
            f.write('w')
        if com == 's':
            S()
            f.write('s')
        if com == 'a':
            A()
            f.write('a')
        if com == 'd':
            D()
            f.write('d')
        if com == 'f':
            F()
            f.write('f')
        if com == 'g':
            G()
            f.write('g')
        if com == 'stop':
            print(f)
            break



main()
f.close()
