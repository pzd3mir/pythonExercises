"""Suchmuster (Pattern) werden oft durch eine Zeichenfolge beschrieben, die den Platzhalter * enthält. Ein * bedeutet eine möglicherweise leere Folge beliebiger Zeichen.
Das Pattern T*.java passt also zum Text Test.java. Schreiben Sie folgende Methode

static boolean matches(String t, String pat)

die prüft ob das Muster pat zu  Text t passt. Als Vereinfachung gilt, dass * in pat höchstens einmal vorkommt.

Verwenden Sie für das PatternMatching eine Built-In Methode,  in Java matches()  oder in Python fullmatch()."""


import re

pattern = '(asd)*.java'

textA = "asdasdasd.java"
textB = "asdasdasd.xyz"

def patterncheck(patternX, textX):
    if re.fullmatch(patternX, textX) != None:
        print("match found for ", patternX," in ", textX)
        return True
    else:
        print("no match found for ", patternX," in ", textX)
        return False

patterncheck(pattern, textA)
patterncheck(pattern, textB)





