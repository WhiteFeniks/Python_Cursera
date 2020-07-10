s = input()
letter1 = s.find('h')
letter2 = s.rfind('h')
expression = s[:letter1] + s[letter2+1:]
print(expression)
