def sum():
    a = int(input())
    if a == 0:
        return 0
    return a + sum()


print(sum())
