def smallest_prime_factors(n):
    spf = list(range(n + 1))  # Smallest prime factor for each number
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # Update only if it hasn't been updated
                    spf[j] = i
    return spf

def calculate_average_f1(N):
    spf = smallest_prime_factors(N)
    total_sum = 0.0
    
    for n in range(2, N + 1):
        num = n
        p = spf[n]  # Smallest prime factor
        alpha = 0
        
        # Calculate alpha(n)
        while num % p == 0:
            num //= p
            alpha += 1
        
        # Calculate f_1(n)
        f_1 = (alpha - 1) / p
        total_sum += f_1

    average_f_1 = total_sum / (N - 1)  # N - 1 because we start from n=2
    return average_f_1

def main():
    N = 1000000  # Set a large N for better accuracy
    average_f_1 = calculate_average_f1(N)
    
    print(f"Average value of f_1(n) from 2 to {N}: {average_f_1:.12f}")

if __name__ == "__main__":
    main()
