def fibonacci():
    x = 1
    y = 1
    z = x + y
    a = 0
    while x < 4000000:
        z = x + y
        x = y
        y = z
        if x % 2 == 0 :
            print(x)
            a = a + x
    print("final value:" + str(a))
    return(a)


fibonacci()
