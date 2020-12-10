# -*- coding: utf-8 -*-

# Schreiben Sie ein Programm, welches einen Integer Wert von Sekunden einliest und in Anzahl Stunden, Minuten und Sekunden auf der Console im Format hh:mm:ss ausgibt.


x = (input("Bitte geben Sie eine Sekundenzahl an, um diese in das format hh:mm:ss umzurechnen\n"))

while x.isdigit() == False:  # check if input is string

    x = (input("Bitte geben sie eine ganzzahlige Zahl ein\n"))

else:
    x = int(x)  # input to int
    h = x // 3600  #
    m = (x // 60 - (h * 60))
    s = x - ((x // 60) * 60)

    if h < 10:  # put 0 in front if it is less than 10
        q = "0" + str(h)
    else:
        q = str(h)

    if m < 10:
        w = "0" + str(m)
    else:
        w = str(m)

    if s < 10:
        e = "0" + str(s)
    else:
        e = str(s)

    print(q + ":" + w + ":" + e)
