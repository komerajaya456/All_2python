for i in [1]:
	i=str(i)
	for j in [2,4]:
		j=str(j)
		jo1=i+j
		print(jo1)
		if j=='2':
			for ij in [1,4,5,6,3]:
				ij=str(ij)
				jo2=jo1+ij
				
				for iy in jo2:
					c=0
					for jy in jo2:
						if iy==jy:
							c=c+1
							if c>=2:
								jo2=''
								break
							else:			
								jo2=jo2	
				print(jo2)
			elif 