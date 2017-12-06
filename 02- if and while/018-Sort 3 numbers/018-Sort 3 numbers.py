a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c)
minimum = min(a, b, c)
average = a + b + c - maximum - minimum

print(minimum, average, maximum)
