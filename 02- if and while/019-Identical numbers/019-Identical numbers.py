a = int(input())
b = int(input())
c = int(input())

if (a == b) and (b == c):
    res = 3
elif (a == b) or (b == c) or (a == c):
    res = 2
else:
    res = 0

print(res)
