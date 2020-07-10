import math
a = float(input())
if (a-int(a)) >= 0.5:
    a = math.ceil(a)
elif (a-int(a)) < 0.5:
    a = math.floor(a)
print(a)
