"""
Project Euler Problem 3
Largest prime factor up to some number mx
"""
def isPrime(n):
	for i in range(2, int(n**(0.5)) + 1):
		if n%i == 0:
			return False
	return True

def largest_prime_factor(mx):
	if int(mx**(0.5)) % 2 == 0:
		rng = int(mx**(0.5)) - 1
	else:
		rng = int(mx**(0.5))
	for i in range(rng,1,-2):
		if mx % i == 0:
			if (i % 2 != 0 and isPrime(i)):
				return i
				break
	return 2
				
#prints largest prime factor of 600851475143
x = largest_prime_factor(600851475143)
print x

#Verifies that the factor is prime
print isPrime(x)
