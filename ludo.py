tot1=[]
hvn=[]
gow=[]
jk=[]
while True:
	a=input('Dice=  ')
	
	if a=='':
		break
	else:
		for i in a:
			if i=='g' or i=='G':
				a=a[1]
				tot1.append(a)
				gow.append(a)
			elif i=='t' or i=='T':
				a=a[1]
				tot1.append(a)
				hvn.append(a)
			elif i=='j' or i=='J' or i=='k' or i=='K':
				a=a[1]
				tot1.append(a)
				jk.append(a)

print('tot=',tot1)
osv=map(int,tot1)
tot1=list(osv)
o=map(int,hvn)
hvn1=list(o)
ot=map(int,gow)
gow1=list(ot)
op=map(int,jk)
kjk1=list(op)
print('gow dice=',gow1)
print('hvn dice=',hvn1)
print('kjk dice=',kjk1)
gow2=[]
hvn2=[]
kjk2=[]
tot2=[]
gowc=0
hvnc=0
kjkc=0
totc=0

for iz in tot1:
	com4=(totc+1)
	if com4>=len(tot1):
		totd=0-tot1[totc]
		tot2.append(totd)
	else:
		totd=tot1[com4]-tot1[totc]
		tot2.append(totd)
		
		totc=totc+1	
for ij in gow1:
	com1=(gowc+1)
	if com1>=len(gow1):
		gowd=0-gow1[gowc]
		gow2.append(gowd)
	else:
		gowd=gow1[com1]-gow1[gowc]
		gow2.append(gowd)
		
		gowc=gowc+1	
for ik in hvn1:
	com2=(hvnc+1)
	if com2>=len(hvn1):
		hvnd=0-hvn1[hvnc]
		hvn2.append(hvnd)
	else:
		hvnd=hvn1[com2]-hvn1[hvnc]
		hvn2.append(hvnd)
			
		hvnc=hvnc+1
for ki in kjk1:
	com3=(kjkc+1)
	if com3>=len(kjk1):
		kjkd=0-kjk1[kjkc]
		kjk2.append(kjkd)
	else:
		kjkd=kjk1[com3]-kjk1[kjkc]
		kjk2.append(kjkd)
			
		kjkc=kjkc+1	
				
print('gow dif=',gow2)						
print('hvn dif=',hvn2)								
print('kjk dif=',kjk2)								
print('tot dif=',tot2)												
														
																
																		
																				
																						
																										
	
	 
	
	
