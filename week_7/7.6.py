f_r = open('input.txt', 'r', encoding='utf8')
data = f_r.read().splitlines()
dig = int(data[0])
i = 0
all_languge = set()
while i < len(data):
    if data[i].isdigit():
        i += 1
    else:
        if data[i] not in all_languge:
            all_languge.add(str(data[i]))
        else:
            i += 1
all_languge = list(all_languge)
i = 0
count = [0] * len(all_languge)
while i < len(all_languge):
    j = 0
    while j < len(data):
        if all_languge[i] == data[j]:
            count[i] += 1
        j += 1
    i += 1
i = 0
k = 0
while i < len(count):
    if count[i] == dig:
        k += 1
    i += 1
print(k)
i = 0
while i < len(count):
    if count[i] == dig:
        print(all_languge[i])
    i += 1
print(len(all_languge))
for i in all_languge:
    print(i)
