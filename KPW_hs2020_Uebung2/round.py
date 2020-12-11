"""Schreiben Sie einen Java/Python Ausdruck, der eine Zahl x auf das nächstliegende Vielfache von 100 rundet.
Der Wert 149 soll also auf 100 abgerundet werden."""

u= int(1) #want to have infinite loop

while u != 0:

    x = int(input()) #need to put int for calculation, by default inpuit is string
    y = x % 100
    z = (x//100)*100
    if y <= 50:
        e = z
    else:
        e =z+ 100

    print(e)


