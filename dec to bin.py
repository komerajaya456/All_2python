num=int(input('enter decimal number='))
div=2

binnum=''
while div>0:
	rem=num%2
	rem=str(rem)
	div=num//2
	num=div
	binnum=rem+binnum
print(binnum)	