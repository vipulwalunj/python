data = [1, 3, 3, 5, 6, 4, 5, 1, 4, 1]

tempt = {}

for dt in data:
    if dt in tempt:
        tempt[dt] += 1

    else:
        tempt[dt] = 1

print(tempt)
