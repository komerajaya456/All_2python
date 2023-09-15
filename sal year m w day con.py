a=input()
lend=len(a)
a=a.lower()
mn6=''
dn=''
wn6=''
for diw in a[-1::-1]:
	if diw=='d':
		dl=a.find(diw)
		dl1=dl-lend
		print(a[ dl1::-1])
		for dn1 in a[ dl1::-1]:
			if not dn1.isnumeric() and dn1!='d' and dn1!='.':
				dn1l=a.find(dn1)
				dn11=a[dn1l+1:dl]
				dn11=float(dn11)
				print(dn11,'jjj')   ##no of days if m given
				break
			elif dn1!='d' and (dn1.isnumeric() or dn1=='.'):
				
				dn=dn1+dn
				dn5=float(dn)	##if only days given
				print(dn5,'days')
	
	
	
	elif diw=='w':
		wl=a.find(diw)
		wl1=wl-lend
	
		print(a[wl1::-1],'mrev')
		for wn1 in a[wl1::-1] :
			print(wn1,'all')
			if not wn1.isnumeric() and wn1!='w' and wn1!='.':
				wn1l=a.find(wn1)
				wn111=float(a[wn1l+1:wl])
				print(wn111,'kkk')				#if month is given
			elif wn1.isnumeric() or wn1=='.':
				wn6=wn1+ wn6
				print(wn6,'hhh',wn1)
				
				wn11=float(wn6)
				print(wn11,'beforem')		###if only w and d given
	
	elif diw=='m':
		ml=a.find(diw)
		ml1=ml-lend
	
		print(a[ml1::-1],'mrev')
		for mn1 in a[ml1::-1] :
			print(mn1,'all')
			if not mn1.isnumeric() and mn1!='m' and mn1!='.':
				mn1l=a.find(mn1)
				mn111=float(a[mn1l+1:ml])
				print(mn111,'kkk')				#if years is given
			elif mn1.isnumeric() or mn1=='.':
				mn6=mn1+ mn6
				print(mn6,'hhh',mn1)
				
				mn11=float(mn6)
				print(mn11,'beforem')		###if only m and d given
			
	elif diw=='y':
		yl=a.find(diw)
		yn=a[ :yl]
		yn=yn*365			