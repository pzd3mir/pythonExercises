fobj = open("Histogram.txt", "r")

charStr = fobj.read()

fobj.close

charList = list(charStr)


s=set(charStr)
s="".join(s)

ls=list(s)

lenghtS = len(ls)

while lenghtS != 0:

    x = ls.pop()
    y = charList.count(x)
    print(x," ","*"*y)
    lenghtS = len(ls)


