a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = set(a) & set(b)
print(*sorted(c))
