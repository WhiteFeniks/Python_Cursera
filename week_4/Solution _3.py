from math import sqrt
n = int(input())


def MinDivisor(n):
    i = 2
    root = sqrt(n)
    while n % i != 0:
        if i >= root:
            print(n)
            return
        i = i + 1
    print(i)


MinDivisor(n)
