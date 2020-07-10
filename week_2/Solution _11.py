x = int(input())
y = int(input())
i = 1
while y > x:
    x = x + 0.1*x
    i = i + 1
print(i)
