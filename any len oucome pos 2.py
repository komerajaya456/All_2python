inpt=int(input('Enter the length:'))
rang=input('Enter the outcomes of 1 turn =' )
lenrang=len(rang)
low_rang=rang[0]
high_rang=rang[lenrang-1]
indrang=[]
for i in range(0,inpt):
	indrang.append(low_rang)
print(indrang)
wik=0
while wik<lenrang:
	wik=0
	for il in indrang:
		if il==rang[lenrang-1]:
			wik+=1
	if wik==lenrang:
		break
	for ik in range(0,lenrang):
		indrang[-1]=rang[ik]
		print(indrang)
		for ki in range(0,len(indrang)):
			if indrang[ki]==rang[-1]:
				print('hi',indrang[ki],ki)
				locran=rang.find(indrang[ki-1])
				print(locran)
				indrang[ki]=rang[0]
				print(indrang[ki])
				
				indrang[ki-1]=rang[locran+1]
		if ik==(lenrang-1) and input()!='k':
			break	
	
		
	
	
	
	
	
	
	
	
	
	