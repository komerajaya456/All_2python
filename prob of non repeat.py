a=[1,0.1,0.01,0.001]

m=0
while m<len(a):
	a=[1,0.1,0.01,0.001]

	a[m]=0
	sum=0
	for i in a:
		print('a',a)
		
		i=i+sum
		
		sum=i
	m=m+1
	print(i)