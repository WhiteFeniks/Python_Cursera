s = input()
pos = 0
if s.find('f', pos) == -1:
    print()
elif s.find('f', pos) == s.rfind('f', pos):
    print(s.find('f', pos))
else:
    print(s.find('f', pos), s.rfind('f', pos))
