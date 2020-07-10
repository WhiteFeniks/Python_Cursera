f_r = open('input.txt', 'r', encoding='utf8')
data = f_r.read().replace('\n', ' ')
my_dict = {}
for word in data.split():
    my_dict[word] = my_dict.get(word, 0) + 1


def max_dict(d):
    max_val = max(d.values())
    final_dict = {k: v for k, v in d.items() if v == max_val}
    return final_dict


def lex_sort(my_dict):
    list_keys = list(my_dict.keys())
    list_keys.sort()
    return list_keys[0]


print(lex_sort(max_dict(my_dict)))
