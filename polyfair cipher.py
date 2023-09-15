import numpy as jk
alp='abcdefghijklmnopqrstuvwxyz'
playfair_key='montage'
both=playfair_key+alp
print(both)
arr=jk.empty((5,5),str)
print(arr)
count=0
for i in range(0,5):
	for j in range(0,5):
		
		if not both[count] in arr:
			print(both[count])
			arr[i][j]=both[count]
		
		count+=1
print(arr)
print(not 'm' in arr)