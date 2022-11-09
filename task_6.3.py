def sorting(elements):
    return sorted(elements, key=abs)

print(sorting((-1, -2, -3, 0)))