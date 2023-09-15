
aio1t=input()
if aio1t[len(aio1t)-1].isnumeric():
	tottab1t=float(aio1t)
	glen1t=0
else:
	nhj1t=1
	appendnam1t=[]
	glen1t=1
	glk1t=''
	lastbrk1t=''
	while glen1t>0 :
		nhj1t=0
	
		if lastbrk1t=='brk':
			break
	
		for imo1t in aio1t :
			if lastbrk1t=='brk':
				break
		
			if not imo1t.isnumeric() :
				if nhj1t==2 :
			
					break
				for iforw1t in range(len(aio1t)):
				
					if lastbrk1t=='brk':
						break
					if aio1t[iforw1t]==imo1t:
					
						for romnam1t in aio1t[iforw1t: ]:			#after we found y----7 remomed
							if lastbrk1t=='brk':
								break
							if romnam1t.isnumeric() :
								
							
								appendnam1t.append(aio1t[ :iforw1t+1])
								akl1t=aio1t[iforw1t: ]
								locrom1t=aio1t[iforw1t: ].find(romnam1t)
								bik1t=aio1t[iforw1t: ][ :(locrom1t)]
								app1t=[]
								app1t1=[]
								for il1t in akl1t:
									app1t.append(il1t)
								for jl1t in bik1t:
									app1t1.append(jl1t)
								
								for y11t in range(len(app1t1)):
									
									for hk1t in range(len(app1t)):
			
										if app1t1[y11t]==app1t[hk1t]:
											
											app1t.remove(app1t[hk1t])
				
											break 
								
								dipl1t=''
								for addalapp1t in app1t:
									dipl1t=dipl1t+addalapp1t
								aio1t=dipl1t
								
								
								
								nhj1t=2
								glk1t=aio1t[iforw1t: ]
								break
							else:
								glk1t=aio1t[iforw1t: ]
								
								for stoplop1t in glk1t:
									if not stoplop1t.isnumeric() and stoplop1t!='.':
										glk1t=glk1t.replace(stoplop1t,'')
										
										glen1t=len(glk1t)
										
									if glen1t==0:
										appendnam1t.append(aio1t[ :iforw1t+1])
										lastbrk1t='brk'
										
										break
						break 
	print(appendnam1t)

	appendot1t=[]
	comtot1t=''
	for comdot1t in appendnam1t:
		print(comdot1t,'uu')
		comtot1t=comtot1t+comdot1t
		print(comtot1t)
		
		if not comdot1t[len(comdot1t)-1].isnumeric() and comdot1t[len(comdot1t)-1]!='.':
			appendot1t.append(comtot1t)
			comtot1t=''
			continue
	print(appendot1t)
	tottab1t=0
	for montab1t in appendot1t:
		mong1t=''
		for montab1t1 in montab1t[-1::-1]:
			if not montab1t1.isnumeric() and montab1t1!='.':
				locmontab1t1=montab1t.find(montab1t1)
				montnum1t=montab1t[ :locmontab1t1]
				mong1t=montnum1t+mong1t
				montnum1t=float(montnum1t)
				
				if montab1t1=='y':
					monnum1t=montnum1t*365
				elif montab1t1=='m':
					monnum1t=montnum1t*(m/d)
				elif montab1t1=='w':
					monnum1t=montnum1t*w
				elif montab1t1=='d':
					monnum1t=montnum1t
				elif montab1t1=='s':
					monnum1t=(montnum1t*s)/d
				elif montab1t1=='t':
					monnum1t=montnum1t/d	
				tottab1t=monnum1t+tottab1t
							
print(round(tottab1t,2))
		