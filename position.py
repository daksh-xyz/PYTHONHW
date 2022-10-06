from random import randint
z =[]

def counter():
    i = 1
    while i < 6:  
        y = randint(1,10)
        z.append(y)
        i += 1    
counter()
array = []
for _ in range(len(z)):
    array.append(z,'#')
