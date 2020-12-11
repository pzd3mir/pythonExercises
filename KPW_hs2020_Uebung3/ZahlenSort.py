"""Schreiben Sie ein Programm das drei Zahlen a,b,c von einer Datei einliest und sie in sortierter Reihenfolge ausgibt."""

fobj = open ("ZahlenSort.txt", "r")
x = (fobj.read())
fobj.close
x.split(' ')
x = [int(i) for i in x.split(' ')]
x.sort()
print(x)