####################################################################
# Project Euler Problem 2										   #
# Sum of all fibonacci numbers less than mx which are divisible by #
# some divisor. Where f1 is the fibonacci number preceeding f2     #
# and s is the sum of the divisors.								   #													   
####################################################################

def fibonacci(mx, divisor):
	f1 = 0
	f2 = 1
	s = 0
	while f2 <= mx:
		if (f2 % divisor) == 0:
			s += f2 
		f1, f2 = f2, f1 + f2
	return s

#prints sum of even fibonacci numbers less than 4000000	
print fibonacci(4000000, 2)
