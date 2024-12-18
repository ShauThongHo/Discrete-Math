import sympy

def smallest_prime_factor(n):
    for p in sympy.primerange(2, n+1):
        if n % p == 0:
            return p
    return n

def p_adic_order(n, p):
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count

def f_K(n, K):
    p = smallest_prime_factor(n)
    alpha = p_adic_order(n, p)
    return (alpha - 1) * (p ** K)

def average_f_K(K, N):
    total = 0
    for n in range(2, N+1):
        total += f_K(n, K)
    return total / N

# Example usage
N = 100000  # Adjust N for better accuracy
K = 1
print(average_f_K(K, N))
