####################################################################
# Project Euler Problem 6										   #								   
####################################################################

def sum_of_squares(n):
	s=0
	for i in range(n+1):
		s += i*i
	return s
	
def square_of_sum(n):
	return (n*(n+1)/2)**2
	
def diff_of_squareofsum_and_sumofsquares(n):
	return square_of_sum(n) - sum_of_squares(n)

#difference of first 100
print diff_of_squareofsum_and_sumofsquares(100)
