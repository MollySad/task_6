elements = [1, 3, 5]
sum = 0

for i in range(len(elements)):
    if i == 0 or i % 2 == 0:
        sum = sum + elements[i]

if sum != 0:
    print(sum * elements[-1])
else:
    print(0)