def isPalindrome(string):
	firsthalf = string[:int(len(string)/2)]
	secondhalf = string[int(len(string)/2):]
	if (firsthalf[::-1] == secondhalf):
		return True
	else:
		return False

def largest_palindrome_product(digits):
	n=""
	for x in range(1,digits+1):
		n += "9"
	n1 = int(n)
	n2 = int(n) - 8
	product = n1 * n2
	for
		if(isPalindrome(str(product))):
			return str(n1) + " " + str(n2)
			break
		else:
			n2 -= 10
			continue
	
print largest_palindrome_product(3)

