import operator
f_w = open('output.txt', 'w', encoding='utf8')
with open('input.txt', 'r', encoding='utf8') as f_r:
    nums = f_r.read().splitlines()[1:]
    test_list = nums
res = [tuple(map(str, sub.split(' '))) for sub in nums]
res.sort(key=lambda x: int(x[1]), reverse=True)
i = 0
while i < len(res):
    print(res[i][0])
    f_w.write(res[i][0])
    f_w.write("\n")
    i += 1
