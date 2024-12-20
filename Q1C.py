# Done
def count_divisors(limit):
    divisors = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            divisors[j] += 1
    return divisors

def consecutive_divisors(limit):
    divisors = count_divisors(limit)
    count = 0
    for n in range(2, limit):
        if divisors[n] == divisors[n + 1]:
            count += 1
    return count

# Set the limit to 10^7
limit = 10**7
result = consecutive_divisors(limit)
print(result) # 986262