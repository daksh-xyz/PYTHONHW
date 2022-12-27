from time import sleep
x = input("Enter string: ")
y = ['']*2000
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
i = 0
j = 0
try:
    while x != y:
        # sleep(0.05)
        if x[i] != alpha[j]:
            y[i] = alpha[j]
            z = ''.join(y)
            print(z)
            y.pop()
            j+=1
        elif x[i] == alpha[j]:
            y[i] = alpha[j]
            z = ''.join(y)
            print(z)
            i+=1
            j = 0
except IndexError:
    pass