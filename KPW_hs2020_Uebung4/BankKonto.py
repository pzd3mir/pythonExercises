"""Auf einem Bankkonto erhalten Sie jedes Jahr 3.5% Zinsen (p). Im ersten Jahr legen Sie 100 CHF. auf dieses Konto. Berechnen Sie mit Hilfe einer Schleife,
nach wie vielen Jahren sich über 1000 CHF. auf ihrem Konto befinden (Lösung:  Nach dem 67. Jahr befinden sich 1002.31 CHF. auf ihrem Konto).
Die Berechnung soll in einer separaten Methode getAmount(p)  erfolgen."""

# -*- coding: utf-8 -*-
# @author: Pirmin Özdemir


p = 1.035 #interest
i = 100 #initial value
z = 0 #itteration counter
while i < 1000:
    i = i * p
    z = z + 1

x = x = round(i, 2)

print("Bei einem Anfangsbetrag von 100 CHF ist der Betrag ist nach", z, "Jahren auf", x, "CHF angewachsen.")

