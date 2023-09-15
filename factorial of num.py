a=int(input())
count=0
while count<=a:
	count=count+1
	fac=a%count
	if fac==0:
		print(count)
	