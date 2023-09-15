import numpy as jk
row=100
clmn=100
arr=jk.empty((row,clmn),int)

for m in range(0,row):
	for n in range(0,clmn):
		if (m+n)%2==0:  #values changes from here
			arr[m][n]=1
		else:
			arr[m][n]=0
			
print (arr)