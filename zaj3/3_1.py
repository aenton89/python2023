x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# wszystko jest dobrze z tym kodem, chociaz wszystkie sredniki poza pierwszym sa zbedne

for i in "axby": if ord(i) < 100: print (i)
# wszystko po pierwszym dwukropku powinno w nowej linii z wcieciem (np pojedynczym tabulatorem)

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# wszystko jest okej