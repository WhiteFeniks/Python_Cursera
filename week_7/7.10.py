def open_file():
    f_r = open('input.txt', 'r', encoding='utf8')
    data = f_r.read().replace('\n', ' ')
    return data


def count_dict(data):
    my_dict = {}
    for word in data.split():
        my_dict[word] = my_dict.get(word, 0) + 1
    return my_dict


def sort_value(d):
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    lst = []
    for i in list_d:
        lst.append(i)
    lst = sorted(lst, key=lambda x: (x[1], x[0]), reverse=False)
    return dict(lst)


def find_first(list_values, i):
    j = 0
    while not list_values[j] == i:
        j += 1
    return j


def find_second(list_values, i):
    j = find_first(list_values, i)
    while list_values[j] == i:
        if j + 1 == len(list_values):
            break
        elif list_values[j + 1] > i:
            break
        j += 1
    return j


def print_end(first, second, list_keys):
    while first <= second:
        print(list_keys[first])
        first += 1


def func_values(list_keys, list_values):
    if not len(list_values) == 0:
        i = max(list_values)
        while i > 0:
            if len(list_values) == 1:
                print(list_keys[0])
                break
            elif len(list_values) == 0:
                break
            first = find_first(list_values, i)
            second = find_second(list_values, i)
            print_end(first, second, list_keys)
            i -= 1


def print_dict(d):
    list_keys = list(d.keys())
    list_values = list(d.values())
    func_values(list_keys, list_values)


data = open_file()
d = count_dict(data)
d = sort_value(d)
print_dict(d)
