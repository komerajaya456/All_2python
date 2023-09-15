inp1=int(input('Enter the length='))
rang=input('Enter the outcomes of 1 dive=')
ind=[]
inddub=[]
for ij in range(0,len(rang)):
	inddub.append(rang[0])

for i in range(0,inp1):
	ind.append(rang[0])
lenrang=len(rang)
print(ind)
tot_out=lenrang**inp1
now_out=0
while tot_out>now_out:
	
	
	for k in range(0,lenrang):
		ind[-1]=rang[k]
		print(ind)
		now_out+=1
		for asu in range(0,len(inddub)):
			inddub[asu]=now_out
		
		for z in range(0,len(ind)):
			if ind[z]==rang[-1]:
				asuloc=len(ind)-z
				print(inddub[z],now_out)
				pow=(lenrang**asuloc)
				div1=inddub[z]/pow
				print(pow,'kkkk')
				
				print(div1,'hi')
				for ih in range(0,lenrang):
					ink=ih+1
					if div1==ink:
						inddub[z]=0
						
						ind[z]=rang[0]
						loc=rang.find(ind[z-1])
						ind[z-1]=rang[loc+1]
					
			
			
				
	