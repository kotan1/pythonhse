n = int(input())

rem = n % 10

if (n >= 11) and (n <= 19):
    res = ''
elif (rem == 1):
    res = 'a'
elif (rem == 2) or (rem == 3) or (rem == 4):
    res = 'y'
else:
    res = ''

res = str(n) + ' korov' + res

print(res)
