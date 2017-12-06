a = int(input())
b = int(input())
n = int(input())

costkop = a * 100 * n + b * n
rub = costkop // 100
kop = costkop % 100

print(rub, kop)
