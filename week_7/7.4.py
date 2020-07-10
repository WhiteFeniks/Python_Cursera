f_r = open('input.txt', 'r', encoding='utf8')
data = set(f_r.read().split())
print(len(data))
f_r.close()
