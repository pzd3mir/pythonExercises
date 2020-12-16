# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:18:14 2020

@author: urs
"""

factor = 10;


def max(a, b):
    """ 3 """
    if (a > b):
        return a
    else:
        return b


def compute(x):
    """ 2 """
    y = factor * max(x, 0);
    return y


def main():
    """ factor """
    n = 0
    n = int(input("Bitte Zahl eingeben"))
    print(compute(n))


main()
