a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
    print('YES')
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
    print('YES')
elif a % 2 == 0 and b % 2 == 0 and c % 2 != 0 and d % 2 != 0:
    print('YES')
elif a % 2 != 0 and b % 2 != 0 and c % 2 == 0 and d % 2 == 0:
    print('YES')
else:
    print('NO')
