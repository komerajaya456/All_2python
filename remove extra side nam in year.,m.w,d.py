aio='1year'
if aio[len(aio)-1].isnumeric():
	tottab1q=float(aio)
	glen=0
else:
	nhj=1
	appendnam=[]
	glen=1
	glk=''
	lastbrk=''
	while glen>0 :
		nhj=0
	
		if lastbrk=='brk':
			break
	
		for imo in aio :
			if lastbrk=='brk':
				break
		
			if not imo.isnumeric() :
				if nhj==2 :
			
					break
				for iforw in range(len(aio)):
				
					if lastbrk=='brk':
						break
					if aio[iforw]==imo:
					
						for romnam in aio[iforw: ]:			#after we found y----7 remomed
							if lastbrk=='brk':
								break
							if romnam.isnumeric() :
								
							
								appendnam.append(aio[ :iforw+1])
								akl=aio[iforw: ]
								locrom=aio[iforw: ].find(romnam)
								bik=aio[iforw: ][ :(locrom)]
								app=[]
								app1=[]
								for il in akl:
									app.append(il)
								for jl in bik:
									app1.append(jl)
								
								for y1 in range(len(app1)):
									
									for hk in range(len(app)):
			
										if app1[y1]==app[hk]:
											
											app.remove(app[hk])
				
											break 
								
								dipl=''
								for addalapp in app:
									dipl=dipl+addalapp
								aio=dipl
								
								
								
								nhj=2
								glk=aio[iforw: ]
								break
							else:
								glk=aio[iforw: ]
								
								for stoplop in glk:
									if not stoplop.isnumeric() and stoplop!='.':
										glk=glk.replace(stoplop,'')
										
										glen=len(glk)
										
									if glen==0:
										appendnam.append(aio[ :iforw+1])
										lastbrk='brk'
										
										break
						break 
	print(appendnam)

	appendot=[]
	comtot=''
	for comdot in appendnam:
		print(comdot,'uu')
		comtot=comtot+comdot
		print(comtot)
		
		if not comdot[len(comdot)-1].isnumeric() and comdot[len(comdot)-1]!='.':
			appendot.append(comtot)
			comtot=''
			continue
	print(appendot)
	tottab1q=0
	for montab1q in appendot:
		mong1q=''
		for montab1q1 in montab1q[-1::-1]:
			if not montab1q1.isnumeric() and montab1q1!='.':
				locmontab1q1=montab1q.find(montab1q1)
				montnum1q=montab1q[ :locmontab1q1]
				mong1q=montnum1q+mong1q
				montnum1q=float(montnum1q)
				
				if montab1q1=='y':
					monnum1q=montnum1q*365
				elif montab1q1=='m':
					monnum1q=montnum1q*30
				elif montab1q1=='w':
					monnum1q=montnum1q*7
				elif montab1q1=='d':
					monnum1q=montnum1q
					
				tottab1q=monnum1q+tottab1q
							
print(round(tottab1q,2))
		