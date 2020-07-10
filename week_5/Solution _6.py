def pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(a*a, (n/2))
    return a * pow(a, n-1)


a = float(input())
n = float(input())
print(pow(a, n))
