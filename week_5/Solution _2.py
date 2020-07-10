A = int(input())
B = int(input())
if A < B:
    print(*tuple(range(A, B + 1, 1)))
else:
    print(*tuple(range(A, B - 1, -1)))
