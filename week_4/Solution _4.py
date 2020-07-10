from math import sqrt
n = int(input())


def IsPrime(n):
    i = 2
    root = sqrt(n)
    while n % i != 0 and i <= root:
            i = i + 1
    return i > root


if IsPrime(n):
    print('YES')
else:
    print('NO')
