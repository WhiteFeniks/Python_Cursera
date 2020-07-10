def check(data):
    for x in data:
        if x < 40:
            return 0
    return sum(data)


def account(lst):
    if len(lst) <= n:
        return 0
    elif lst.count(max(lst)) > n:
        return 1
    list_max = lst[:n]
    lst = lst[n:]
    while min(list_max) in lst:
        list_max.remove(min(list_max))
    return min(list_max)


list_good = []
with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    for data in f.readlines():
        data = list(map(int, data.split()[-3::]))
        a_point = check(data)
        if a_point:
            list_good.append(a_point)
print(account(list_good))
