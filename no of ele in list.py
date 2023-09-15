a=[1,2,3,3,3,1,4,4,4,4,4]
cou=len(a)-1
for i in a:
	num=1
	for j in a:
		if i==j:
			print(j,num)
			num=num+1	