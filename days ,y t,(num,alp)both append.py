a='1.5y2.22m3w4d'
endlop='en'

appendst=[]
lendst=len(a)
while len(a)>0:
	if endlop=='end':
		break
	print('kiouio')
	for stir in a[-1::-1]:
		if endlop=='end':
			break
		addlasnum=''
		print('jk',a,stir)
		if not stir.isnumeric():
			print('hi')
			for exloc in range(len(a)):
				if a[exloc]==stir:
					locstir=exloc			#last location
			for antalp in a[locstir-1::-1]:
				
				if not antalp.isnumeric() and antalp!='.':
					for exloc1 in range(len(a)):
						if a[exloc1]==antalp:
							locstir1=exloc1			#last location
					now12=a[locstir1+1:locstir+1]
					
					appendst.append(now12)
					a=a.replace(a[locstir1+1:locstir+1],'')
					print('appen',appendst)
					break
					
				else:
					addlasnum=antalp+addlasnum
					print('jakass',a,addlasnum)
					if len(addlasnum)+1==len(a):
						appendst.append(a)
						print('yes')
						endlop='end'
print(appendst,'koi')

for jk in appendst:
	print('hi')
	addpi=''
	for kj in jk[-1::-1]:
		
		if not kj.isnumeric() and kj!='.':
			
			print(kj)
			lockj=jk.find(kj)
			pi=jk[ :lockj]
			
			addpi=pi+addpi 
			print(addpi)			
