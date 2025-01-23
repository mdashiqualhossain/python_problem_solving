# Input
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Generating all possible combinations
result = [
    [x, y, z]
    for x in range(a + 1)
    for y in range(b + 1)
    for z in range(c + 1)
    if x + y + z != d
]

# Output in lexicographic order
print(result)
