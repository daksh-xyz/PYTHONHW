# i = 1
# while(x>0):
#     i = i*x
#     x =x-1
#     print(x)
#     i -= 1


# y = 1
# while x > 1:
#     y = x*y
#     print("y---",y)
#     x =x-1
#     print("x ---",x  )
# print("fac is ",y)




# def factorial():
#     try:
#         x = int(input('Enter a number: '))
#     except ValueError:
#         print('not an integer value!')
#     i = 1
#     while x > 1:
#         i *= x
#         x -= 1
#     print(i)
# factorial()

i = 1
s= 0
while i<=10:
    s += i
    i += 1
print(s)
