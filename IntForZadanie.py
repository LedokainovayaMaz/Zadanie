 = open('BF.txt')
c = [0,0,0,0,0,0,0,0,0,0]
b = a.read()
d = 0
for i in b:
    if i == '+':
        c[d] += 1
    elif i == '>':
        d += 1
    elif i == '<':
        d -= 1
    elif i == '-':
        c[d] -= 1
    elif i == '.':
        print(c[d])
    elif i == ',':
        c[d] = input('Vvod')
    elif i == '[':
        if c[d] > 0:
            d += 1
        elsea