s = input()
letter = s.rfind(' ')
print(s[letter+1:] + ' ' + s[:letter])
