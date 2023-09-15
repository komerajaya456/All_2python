a=int(input('Enter:'))
fibnum=0
b=1
res=0
for i in range(0,a):
	if i<2:
		print(i)
	else:
		res=fibnum+b
		print(res)
		fibnum=b
		b=res
	
	