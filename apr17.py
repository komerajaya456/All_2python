inp=input('enter all outcomes=')
ranpos=int(input('enter the range='))
num=[]
leninp=len(inp)
totout=(leninp)**(ranpos)
last=inp[-1]
for i in range(0,ranpos):
	num.append(0)
	print(inp[0]) 
print(num)
exe=0
asu=''
ourout=''
while exe<totout:
	ourout=''
	exe+=1
	print(num)

			   
	for j in range(ranpos-1,-1,-1):
		ourout=inp[num[j]]+ourout
	print(ourout)
	
	for ik in range(0,len(ourout)):
		lstnum=0
		asu=''
		if asu=='ok':
			break
		if ourout[ik]==last:
			cutlst=ourout[ik: ]
			print(ourout[ik: ])
			for il in cutlst:
				if il==last:
					
					lstnum+=1
				else:
					asu.append('no')
					
			if len(cutlst)==lstnum:
				asu='ok'
				break
				print('yeskkkkk',cutlst)

	for ij in range(ranpos-1,-1,-1):
		rem1=[]
		exp=abs((ij-(ranpos-1)))
		dmtr=(leninp)**exp
		
		rem=exe%dmtr
		if rem==0:
			rem1.append('0')
		else:
			rem1.append('1')
		if rem1[abs(ij-(ranpos-1))]=='0' and exp==0:
			num[ij]+=1
			print(num,'num',exe,'thi')
		if rem1[abs(ij-(ranpos-1))]=='0' and asu=='ok':
			num[ij]+=1
