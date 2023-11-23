import turtle

t = turtle.Pen()

"""
W - der Stift bewegt sich 10 Pixel vorwärts
S - der Stift bewegt sich 10 Pixel rückwärts
D - der Stift dreht sich um 45 Grad nach rechts
A - der Stift dreht sich um 45 Grad nach links
F - hebt den Stift nach oben (Zeichnen stoppt)
G - legt den Stift wieder ab (Zeichnen wird fortgesetzt)
"""
def W():
    t.forward(10)

def S():
    t.right(180)
    t.forward(10)

def D():
    t.right(45)

def A():
    t.left(45)

def F():
    t.penup()

def G():
    t.pendown()
