x = int(input())
y = int(input())
z = int(input())

a1 = min(x, y, z)
c1 = max(x, y, z)
b1 = x + y + z - a1 - c1
# print(a1, b1, c1)

x = int(input())
y = int(input())
z = int(input())

a2 = min(x, y, z)
c2 = max(x, y, z)
b2 = x + y + z - a2 - c2
# print(a2, b2, c2)

equal = 'Boxes are equal'
smaller = 'The first box is smaller than the second one'
larger = 'The first box is larger than the second one'
incomparable = 'Boxes are incomparable'

if (a1 == a2):
    if (b1 == b2):
        if (c1 == c2):
            res = equal
        elif (c1 < c2):
            res = smaller
        else:  # c1 > c2
            res = larger
    elif (b1 < b2):
        if (c1 <= c2):
            res = smaller
        else:  # c1 > c2
            res = incomparable
    else:  # b1 > b2
        if (c1 >= c2):
            res = larger
        else:  # c1 < c2
            res = incomparable
elif (a1 < a2):
    if (b1 <= b2):
        if(c1 <= c2):
            res = smaller
        else:  # c1 > c2)
            res = incomparable
    else:  # b1 > b2
        res = incomparable
else:  # a1 > a2
    if (b1 == b2):
        if (c1 >= c2):
            res = larger
        else:  # c1 < c2
            res = incomparable
    elif (b1 < b2):
        res = incomparable
    else:  # b1 > b2
        if(c1 >= c2):
            res = larger
        else:  # c1 < c2
            res = incomparable

print(res)
