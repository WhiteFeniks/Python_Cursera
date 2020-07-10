from math import sqrt

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c

if b == 0 and c == 0:
    print(0)
elif a < 0 and c == 0:
    x3 = 0
    x4 = b/(-a)
    print(x3, x4)
elif b < 0 and c == 0:
    x3 = 0
    x4 = (-b)/a
    print(x3, x4)
else:
    if D > 0:
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif D == 0:
        x = (-b/(2*a))
        print(x)
    elif D < 0:
        print()
