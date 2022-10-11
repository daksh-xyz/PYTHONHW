from random import randint, choice
import numpy as np

a = []
b = [0,1,2,3,4,5,6,7,8,9]
t = [0,0,0,0,0,0,0,0,0,0]

i = 1
while i <11:
    y = randint(0,9)
    a.append(y)
    i += 1

print(a)

M = [['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#']]

for i in range(len(a)):
    M[a[i]][b[i]] = "O"
    for q in range(len(a)):
        t[q] = a[q] + 1
        while t[q] < 10:
            M[t[q]][b[q]] = choice(['|','/','/','\\','\\'])
            t[q] = t[q] + 1 
        t[q] = t[q] - 1
        t[q] = a[q] - 1
        while t[q] >= 0:
            M[t[q]][b[q]] = ' '
            t[q] = t[q] - 1

x = np.array(M)

for s in x:
    for f in s:
        print(f, end=' ')
    print()
def balloonburst():
    d = int(input('yo: '))
    d = 9 - d
    # print(d)
    # print(a)
    k = 0
    while k < 10:
        if d == a[k]:
            print('balloon popped')
            while t[k] < 10:
                M[t[k]][b[k]] = ' '
                t[k] = t[k] + 1
            d += 1
        k += 1
        

    x = np.array(M)

    for h in x:
        for g in h:
            print(g, end = ' ')
        print()
    balloonburst()
balloonburst()   