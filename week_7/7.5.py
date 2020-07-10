f_r = open('input.txt', 'r', encoding='utf8')
data = f_r.read().splitlines()
i = 0
res = set()
count = data[0]
buf = []
while i <= int(count):
    buf.append(i)
    i += 1
i = 0
while i < len(buf):
    buf[i] = str(buf[i])
    i += 1
buf = set(buf)
i = 0
while i < len(data):
    if str(data[i]) == "HELP":
        break
    else:
        if str(data[i + 1]) == "YES":
            buf &= set(data[i].split())
            i += 1
        elif str(data[i + 1]) == "NO":
            buf -= set(data[i].split())
    i += 1
print(*sorted(buf))
