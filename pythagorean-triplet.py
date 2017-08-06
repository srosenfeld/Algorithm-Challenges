x = 1
b = 1

while x < 500:
    x +=1
    b = 1
    while b < 500:
        c = (x**2 + b**2)**0.5
        if x + b + c == 1000:
            a = x*b*c
        b+=1
        
print(a)

'''
a = 1
b = 1
c = 1
for x in range(1,1001):
    a = x
    for y in range(1,1001):
        b = y
        for z in range(1,1001):
            c = z
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a)
                    print(b)
                    print(c)
'''
