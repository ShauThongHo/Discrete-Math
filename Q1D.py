import math

def last_nine_digits_of_d(n):
    # Calculate D(n) = (2n)! / (n! * n!)
    numerator = math.factorial(2 * n)
    denominator = math.factorial(n) ** 2
    result = numerator // denominator
    return result % 10**9

# Calculate for N = 10000
n = 10000
print(last_nine_digits_of_d(n))
