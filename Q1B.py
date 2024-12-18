from fractions import Fraction

def generate_inverse_squares(limit):
    return [Fraction(1, i**2) for i in range(2, limit + 1)]

def find_combinations(inverse_squares, target, start=0, current_sum=Fraction(0), current_combination=[]):
    if current_sum == target:
        return [current_combination]
    if current_sum > target or start == len(inverse_squares):
        return []
    
    combinations = []
    for i in range(start, len(inverse_squares)):
        new_combination = current_combination + [inverse_squares[i]]
        combinations += find_combinations(inverse_squares, target, i + 1, current_sum + inverse_squares[i], new_combination)
    
    return combinations

# Set the limit to 80
limit = 80
inverse_squares = generate_inverse_squares(limit)
target = Fraction(1, 2)

combinations = find_combinations(inverse_squares, target)
print(f"Number of ways to write 1/2 as a sum of inverse squares: {len(combinations)}")
