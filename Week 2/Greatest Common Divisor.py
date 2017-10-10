def gcd(a,b):
	if b == 0:
		return(a)
	else:
		c = a % b
		return gcd(b,c)

print(gcd(357,234))