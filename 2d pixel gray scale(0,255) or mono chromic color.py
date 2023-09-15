import random
import numpy as jk

row=10
clmn=10

arr=jk.empty((row,clmn),int)

for m in range(0,row):
	for n in range(0,clmn):
		rand_val=(random.randint(0,255))
	
		arr[m][n]=rand_val
			
print(arr)