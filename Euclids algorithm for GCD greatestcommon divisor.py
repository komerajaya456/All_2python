
def euclid_gcd(a,b):#gcd of 2 numbers
	max_num=max(a,b)
	min_num=min(a,b)
	rem=1. #we can kept anything other than 0
	while rem!=0:
		rem=max_num%min_num
		max_num=min_num
		min_num=rem
	print(max_num)
euclid_gcd(150,50)
	