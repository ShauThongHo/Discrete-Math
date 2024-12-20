# Done
import time, math

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]
	
def f(K):
    primes = list_primes(10**6)
    total = 0
    curr = 1
    for p in primes:
        total += curr*(1/((p**(K+1))*(p-1)))
        curr *= (p - 1)/p
    return round(total, 12)
    
if __name__ == "__main__":
  while True:
    a = int(input("Input an integer: "))
    start_time = time.time()
    print(f(a))
    break
  print("--- %s seconds ---" % (time.time() - start_time))