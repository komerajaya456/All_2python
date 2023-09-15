jo2='121'
for i in jo2:
	c=0
	for j in jo2:
		if i==j:
			c=c+1
			if c>=2:
				jo2=''
				break
			else:			
				jo2=jo2
print(jo2)