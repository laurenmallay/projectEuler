###########################################################
# Project Euler Problem 24								  #
# Finds the nth permutation of a set of numbers organized #
# lexographically										  #								   
###########################################################

from math import factorial

def lexographical_permutation(n, *numbers):
	numbers.enumerate()
	return numbers 
			
print lexographical_permutation(3, 0, 1, 2)
