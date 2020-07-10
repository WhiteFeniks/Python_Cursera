f_r = open('input.txt', 'r', encoding='utf8')
f_w = open('output.txt', 'w', encoding='utf8')
lines = f_r.readlines()
lines.sort()
i = 0
while i < len(lines):
    print((lines[i].split())[0], end=" ")
    print((lines[i].split())[1], end=" ")
    print((lines[i].split())[3])
    f_w.write((lines[i].split())[0])
    f_w.write(" ")
    f_w.write((lines[i].split())[1])
    f_w.write(" ")
    f_w.write((lines[i].split())[3])
    f_w.write("\n")
    i += 1
f_r.close()
f_w.close()
