a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (a <= d and b <= e) or (b <= d and a <= e) \
         or (b <= d and c <= e) or (c <= d and b <= e) \
         or (a <= d and c <= e) or (c <= d and a <= e):
    res = 'YES'
else:
    res = 'NO'

print(res)
