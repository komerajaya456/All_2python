#copy and paste on other new file to run

import time
import numpy as jk
import random
import sys
sta=time.time()
r=jk.array(1)

for i in range(0,10**4):
	rand_num=(random.randint(0,1000))
	r=jk.append(r,rand_num)
	

print(jk.set_printoptions(threshold=sys.maxsize))
print(r)
end=time.time()
numpy_time=(end-sta)
print(numpy_time)




star=time.time()
lis=[]
for i in range(0,10**4):
	
	lis.append(random.randint(0,1000))
	
print(lis)

endd=time.time()
array_list_time=(endd-star)

print(array_list_time)