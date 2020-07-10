def open_file():
    f_r = open('input.txt', 'r', encoding='utf8')
    data = f_r.read().split('\n')
    return data


data = open_file()
my_dict = {}
for let in data:
    my_dict[let] = my_dict.get(let, 0) + 1
my_dict = [(key, val) for val, key in my_dict.items()]


def my_sort(val):
    return -val[0], val[1]


my_dict.sort(key=my_sort)
if float(my_dict[0][0]) / float(len(data)) > 0.5:
    print(my_dict[0][1])
else:
    print(my_dict[0][1])
    print(my_dict[1][1])
