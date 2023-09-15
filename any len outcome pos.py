inp=int(input('Enter the length='))
ran=input('Range=')
for k in ran[-1::-1]:

	if not k.isnumeric():
		loc=ran.find(k)
		print('hi')
low_ran=int(ran[ :loc])
high_ran=int(ran[loc+1: ])
print(low_ran+high_ran)
ind=[]
for i in range(0,inp):
	ind.append(low_ran)
print(ind[0])
n=0
while n<inp and input()!='k':
		n=0
		for bre in ind:
			if bre==high_ran:
				n+=1
				print(n)
			if n==inp:
				break
		
		ind[inp-1]+=1
		print(ind,'llll')
		
		for ij in range(0,len(ind)):
			if ind[ij]==high_ran:
				if ij==(len(ind)-1):
					print('hi',low_ran,high_ran)
						
					ind[ij-1]+=1
					ind[ij]=low_ran
					print(ind,'kkk')
				else:
					fuex=ind[ij: ]
					for fuexi in fuex:
						if fuexi==high_ran:
							p+=1
					if p==len(fuex):
						ind[ij-1]+=1
						ind[ij]=low_ran
						print(ind)
					else:
						print('kkkkk')
						fuex[-1]+=1
						print(fuex)
					


