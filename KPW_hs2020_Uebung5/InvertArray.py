"""Schreiben Sie eine Methode invert(a), die eine gegebene Reihenfolge der Elemente eines Arrays a umkehrt."""

import array
import numpy


def arrayreverse(x):
    x.reverse()

a = array.array('d', [1.1, 3.5, 4.5])

arrayreverse(a)

print(a)

"""Schreiben Sie eine Methode transpose(a), die eine gegebene quadratische Matrix a transponiert, d.h. an ihrer Hauptdiagonale spiegelt."""


def transposematrix(y):
    print(numpy.transpose(y))
    print(y)

b = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

transposematrix(b)