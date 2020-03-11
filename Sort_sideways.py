#!/usr/bin/env python3

'''Output is the same set of columns but sorted alphabetically (ignoring case)'''

import sys

def sorter(t):
    tmp = "".join(t).lower()
    return tmp

def main():
    s = [l.strip() for l in sys.stdin]
    grid = []
    for t in s:
        a = []
        for l in t:
            a.append(l)
        grid.append(a)

    a = []
    for i in range(len(grid[0])):
        letter = ""
        for n in grid:
            letter += n[i]
        a.append(list(letter))

    new = sorted(a, key=sorter)

    b = []
    for j in range(len(new[0])):
        letter = ""
        for p in new:
            letter += p[j]
        b.append(list(letter))

    for word in b:
        print("".join(word))

if __name__ == '__main__':
    main()
