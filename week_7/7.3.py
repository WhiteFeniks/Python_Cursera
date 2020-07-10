a = list(map(int, input().split()))
b = set()
for i in a:
    if i not in b:
        b.add(i)
        print("NO")
    else:
        print("YES")
