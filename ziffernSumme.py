"""Schreiben Sie ein Programm, welches die Ziffernsumme einer Zahl x berechnet und ausgibt. (4711 ergibt die Ziffernsumme 13)"""

x = int(input())
j = 10
z = 0
while x / j != 0:
    a = x % j
    z = z + a
    x = (x - a)/10

print(z)