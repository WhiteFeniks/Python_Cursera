s = input()
letter1 = s.find('f')
letter2 = s.find('f', s.find('f')+1)
if letter1 == -1 and letter2 == -1:
    print('-2')
elif letter1 != letter2:
    print(letter2)
elif letter1 == letter2:
    print('-1')
