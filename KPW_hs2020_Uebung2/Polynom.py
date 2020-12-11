"""Schreiben Sie ein Programm, welches die Koeffizienten a, b, c, d sowie den Wert
x des Polynoms y=a * x3 + b * x2 + c * x + d berechnet"""


print('Um den Wert zugehörigen y Wert von y =a * x3 + b * x2 + c * x + d auszurechnen, bitte geben sie folgende Werte ein')

print('Bitte geben sie den Wert für a ein')
a = int(input())
print('Bitte geben sie den Wert für b ein')
b = int(input())
print('Bitte geben sie den Wert für c ein')
c = int(input())
print('Bitte geben sie den Wert für d ein')
d = int(input())
print('Bitte geben sie den Wert für x ein')
x = int(input())

y = a * x**3 + b * x**2 + c * x + d

print('Das Ergebnis (y) ist ', y)