a = open('BF.txt')
c = [0,0,0,0,0,0,0,0,0,0]
b = a.read()
d = 0
for i in b:
    if i == '+':
        c[d] += 1