k = -1
i = 0
j = 0
x = int(input())
while x != 0:
    if k == x:
        i += 1
    else:
        k = x
        j = max(j, i)
        i = 1
    x = int(input())
j = max(j, i)
print(j)
