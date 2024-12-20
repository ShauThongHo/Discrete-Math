from fractions import Fraction
from itertools import combinations

# List of integers from 2 to 80
numbers = list(range(2, 81))

# Calculate the inverse squares
inverse_squares = [Fraction(1, n**2) for n in numbers]

# Target sum
target = Fraction(1, 2)

# Function to find combinations that sum to the target
def find_combinations(numbers, target):
    # Code review comment -> Consider using a more descriptive variable name than 'r'
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            # Code review comment -> Using 'sum(combo) == target' can be inefficient for large combinations. Consider using a more efficient algorithm.
            if sum(combo) == target:
                yield combo

# Find and print all valid combinations
valid_combinations = list(find_combinations(inverse_squares, target))
for combo in valid_combinations:
    # Code review comment -> This line assumes that each element in 'combo' is unique in 'inverse_squares'. If not, this could lead to incorrect results.
    print([numbers[inverse_squares.index(x)] for x in combo])
