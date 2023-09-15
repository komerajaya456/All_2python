import copy
inp=int(input('enter rows u want:'))
pi=['']

asu=[]

def list(len):
	Numlis=[]
	for i in range(1,len+1):
	
		lis=[0]*(i+2)
		
		
		
		for k in range(0,i):
			one=1
			if i==1:
				lis[one]=1
			else:
				
				lis[k+1]=pi[k+1]+pi[k]
	
		asu.append(lis)
		latasu=asu[-1]
		
		cpylatasu=copy.copy(latasu)
		del(cpylatasu[0:2])
		del(cpylatasu[-1])
		Numlis.append(cpylatasu)	
		print(latasu)
		print(cpylatasu)
		pi=lis
		
	return Numlis
ou=list(inp)
print(ou)
