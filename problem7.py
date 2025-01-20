# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# Input
input_data = input().split()
s = input_data[0]
k = int(input_data[1])

# Sort the string
sorted_s = sorted(s)

# Generate and print combinations
for size in range(1, k + 1):
    for combo in combinations(sorted_s, size):
        print(''.join(combo))
