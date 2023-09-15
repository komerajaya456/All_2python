inp1=int(input('Enter the length='))
rang=input('Enter the outcomes of 1 dive=')
ind=[]
for i in range(0,inp1):
	ind.append(rang[0])
lenrang=len(rang)
print(ind)
tot_out=lenrang**inp1
now_out=-1
while tot_out>now_out:
	now_out+=1
	for k in range(len(ind)-1,-1,-1):
		
		for i in range(0,lenrang):
			ind[k]=now_out/(lenrang**i)
			print(ind[k],ind)
		
	opp=now_out
	ind[-1]=rang[opp-1]
	