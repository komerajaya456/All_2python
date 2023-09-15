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
		
		if ourout[ik]==last:
			cutlst=ourout[ik: ]
			print(ourout[ik: ])
			for il in cutlst:
				if il==last:
					
					lstnum+=1
			if len(cutlst)==lstnum:
				asu='ok'
				print('yeskkkkk')
	if asu=='ok':
		print('there')
		for ih in range(0,len(num)):
			if num[ih]==(leninp-1):
				num[ih]=0
	for ij in range(ranpos-1,-1,-1):
		dmtr=(leninp)**ij
		rem=exe%dmtr
		if rem==0:
			print('hi',ij)
			num[(ranpos-1)-ij]+=1
			
			print((ranpos-1)-ij,'kkkkkk')
		if rem==0 and asu=='ok':
			num[ij]+=1
			