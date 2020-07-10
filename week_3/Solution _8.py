a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0:
    x1 = (b * f - e * d) / (c * b - a * d)
    if d != 0:
        x2 = (f - c * x1) / d
        print(x1, x2)
elif b != 0:
    x2 = (e * c - f * a) / (c * b - d * a)
    if c != 0:
        x1 = (f - d * x2) / c
        print(x1, x2)
