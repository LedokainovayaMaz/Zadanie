#!/usr/bin/env python3
import sys

a = open('sys.argv[1]')
c = {0: 0}
d, i = 0, 0
f = a.read()


def generateCycles(commands):
    i = 0
    blocks = {}
    opened = []
    while i < len(commands):
        if commands[i] == '[':
            opened.append(i)
        elif commands[i] == ']':
            blocks[i] = opened[-1]
            blocks[opened[-1]] = i
            opened.pop()
        i += 1
    return blocks

cycles = generateCycles(f)

while i < len(f):
    if f[i] == '+':
        c[d] += 1
    elif f[i] == '>':
        d += 1
        c.setdefault(d, 0)
    elif f[i] == '<':
        d -= 1
        c.setdefault(d, 0)
    elif f[i] == '-':
        c[d] -= 1
    elif f[i] == '.':
        print(chr(c[d]), end ='')
    elif f[i] == ',':
        c[d] = sys.stdin.read(1)
    elif f[i] == '[' and c[d] <= 0:
        i = cycles[i]
    elif f[i] == ']' and c[d] != 0:
        i = cycles[i]
    i += 1