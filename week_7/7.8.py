data = ""
count = {}
f_r = open('input.txt', 'r', encoding='utf8')
for line in f_r:
    data = data + ' ' + line.replace('\n', '')
f_r.close()
data = data.split()
count = int(data[0])
del data[0]
key_list = []
value_list = []
i = 0
while i < len(data):
    if not i % 2 == 0:
        key_list.append(data[i])
    else:
        value_list.append(data[i])
    i += 1
my_dict_keys = dict(zip(key_list, value_list))
my_dict_values = {v:k for k, v in my_dict_keys.items()}


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


if data[count * 2] in key_list:
    print(get_key(my_dict_values, data[count * 2]))
else:
    print(get_key(my_dict_keys, data[count * 2]))
