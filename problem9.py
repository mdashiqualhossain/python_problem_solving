# Input
n = int(input())
scores = list(map(int, input().split()))

# Find unique scores and sort them
unique_scores = sorted(set(scores))

# The runner-up score is the second-to-last in the sorted list
print(unique_scores[-2])

    