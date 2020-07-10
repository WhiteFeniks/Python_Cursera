vilage = int(input())
dist_v = list(map(int, input().split()))
bomb = int(input())
dist_b = list(map(int, input().split()))
m = []
n = []
i = 0
while i < vilage:
    m.insert(i, (dist_v[i], i))
    i += 1
i = 0
while i < bomb:
    n.insert(i, (dist_b[i], i))
    i += 1
tup_v = []
tup_b = []
i = 0
while i < vilage:
    tup_v.insert(i, (dist_v[i], i))
    i += 1
i = 0
while i < bomb:
    tup_b.insert(i, (dist_b[i], i))
    i += 1
v = tup_v
b = tup_b
i = 0
while i < vilage:
    j = 0
    minimal = abs(b[j][0] - v[i][0])
    buf = j
    while j < bomb:
        if abs(v[i][0] - b[j][0]) < minimal:
            minimal = abs(v[i][0] - b[j][0])
            buf = j
        j += 1
    print(tup_b[buf][1] + 1, end=" ")
    i += 1
