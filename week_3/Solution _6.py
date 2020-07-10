import math

p = int(input())
x = int(input())
y = int(input())

a = x*100+y
a = int(a * (100 + p) / 100)
c = a // 100
k = a % 100
print(c, k)
