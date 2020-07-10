a = list(map(int, input().split()))
size = a[0]
count = a[1]
i = 0
fill = 0
b = []
while i < count:
    b.append(int(input()))
    i += 1
b.sort()
i = 0
while i < len(b):
    if fill + b[i] <= size:
        fill = fill + b[i]
    else:
        break
    i += 1
print(i)
