###############################################################
# Project Euler Problem 1				      #
# Sum of multiples of some divisor(s) less than some number n #
###############################################################

def divisibles(mx, *divisors):
	return (n for n in xrange(mx) if 0 in (n % d for d in divisors))

#prints sum of multiples of 3 and 5 less than 1000
print sum(divisibles(1000,3,5))
