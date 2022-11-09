elements = [10, -2.2, 0, 1.1, 0.5]

if len(elements) == 0:
    print("0")
else:
    result = max(elements) - min(elements)
    print(f'{result:.3f}')