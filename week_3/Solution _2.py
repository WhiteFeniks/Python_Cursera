n = float(input())
sum = 0
i = 1
while i <= n:
    s = 1.0/(i**2)
    sum += s
    i += 1
print('{0:.5f}'.format(sum))
