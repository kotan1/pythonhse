n = int(input())

formatstr1 = "The next number for the number {:d} is {:d}."
formatstr2 = "The previous number for the number {:d} is {:d}."

print(formatstr1.format(n, n + 1))
print(formatstr2.format(n, n - 1))
