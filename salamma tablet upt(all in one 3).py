dayiwant=input('''Enter the amount U have 
	or Days u want
press ENTER to choose:-''')
nowtot=0
diwasu=dayiwant	
rr=0
po=0
tottab=0
emp=''
eleofb='kkk'
appendot1qq=['sample']
vala1num=0
non=0
numc=[]
jusva=0
row1='ki'
jusva1z=0
checkflt='alp'
finlnum=0
jf=0
nope=1
b='wer'
tabcoou=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rep=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hh=0
leng4=len(dayiwant)
leng4=leng4-1
if len(dayiwant)>1:
	b='tumki'
	last1=dayiwant[leng4]
	for diw in dayiwant:
		
		dayiwant=diwasu
		if last1.isnumeric() and nope==1:
			
			dayiwant=float(dayiwant)
			nope=2
			row1='a'
			break
			
			
		elif not last1.isnumeric() and len(dayiwant)>1:
			if  jusva==2:
				lend1=0
				
				dayiwant=0
				break
			
			
			
			row1='d'
			aio=diwasu
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
			
				comtot=comtot+comdot
			
	
				if not comdot[len(comdot)-1].isnumeric() and comdot[len(comdot)-1]!='.':
					appendot.append(comtot)
					comtot=''
					continue
			
			tottab1q=0
			for montab1q in appendot:
				mong1q=''
				for montab1q1 in montab1q[-1::-1]:
					if not montab1q1.isnumeric() and montab1q1!='.':
						locmontab1q1=montab1q.find(montab1q1)
						montnum1q=montab1q[ :locmontab1q1]
						mong1q=montnum1q+mong1q
						montnum1q=float(montnum1q)
						montab1q1=montab1q1.lower()
						if montab1q1=='y':
							monnum1q=montnum1q*365
						elif montab1q1=='m':
							monnum1q=montnum1q*30
						elif montab1q1=='w':
							monnum1q=montnum1q*7
						elif montab1q1=='d':
							monnum1q=montnum1q
				
						tottab1q=monnum1q+tottab1q
						
			
			hh=round(tottab1q,2)
			dayiwant=0 
			break
		
else:
	
	row1='z'
	dayiwant=0


	
print('Total days u selected:- ',hh)
c=0
tabwant=['hi']
sol=0
total=[]
tum=1


n=-1



while ((nowtot<=dayiwant and row1=='a') or (hh>n and row1=='d' and hh!=0) or (len(b)>1 and row1=='z'))  :
	
	tabwantleg=len(tabwant)
	
	
	tab11=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Torget Plus 10mg','Bylenta M50','Atocor Cv 10mg (Dr Reddy\'s LAB Ltd)']
	for tabrun in tab11:
		if tabrun==b:
			break
	

	if   len(b)<2 or b==tabrun :
		if tabwantleg==tum or len(b)<2:
			
			c+=1	
			n=n+1
			tum=1
			if n>=hh and row1=='d':
				
				break
			nowtot=0
		
		b=tabwant[tum]
		
		tum+=1 
		lengt=len(b)
		
		
	else :
		print('')
		print('')
		
		b=input('''Enter the name of tablet :-
		if Done press 'ENTER'  ''')
		row12=''
		emp=0
		lengt=len(b)
		val3=0	
		okw=[]
	
		row123=''
		for ike32 in b:
		
			if row12=='kom':
				break
			if ike32.isnumeric():
				locike1q=b.find(ike32)
				row12='kom'
				appendot1qq=[]
				row123='kom1'
				aio1qq=b[locike1q: ]
				
				if aio1qq[len(aio1qq)-1].isnumeric():
					tottab1q=float(aio1qq)
					appendot1qq.append(tottab1q)
					glen1qq=0
				else:
					tottab1q=0
					nhj1qq=1
					appendnam1qq=[]
					glen1qq=1
					glk1qq=''
					lastbrk1qq=''
					while glen1qq>0 :
						nhj1qq=0
	
						if lastbrk1qq=='brk':
							break
	
						for imo1qq in aio1qq :
							if lastbrk1qq=='brk':
								break
		
							if not imo1qq.isnumeric() :
								if nhj1qq==2 :
			
									break
								for iforw1qq in range(len(aio1qq)):
				
									if lastbrk1qq=='brk':
										break
									if aio1qq[iforw1qq]==imo1qq:
					
										for romnam1qq in aio1qq[iforw1qq: ]:			#after we found y----7 removed
											if lastbrk1qq=='brk':
												break
											if romnam1qq.isnumeric() :
												appendnam1qq.append(aio1qq[ :iforw1qq+1])
												akl1qq=aio1qq[iforw1qq: ]
												locrom1qq=aio1qq[iforw1qq: ].find(romnam1qq)
												bik1qq=aio1qq[iforw1qq: ][ :(locrom1qq)]
												app1qq=[]
												app1qq1=[]
												for il1qq in akl1qq:
													app1qq.append(il1qq)
												for jl1qq in bik1qq:
													app1qq1.append(jl1qq)
							
												for y11q in range(len(app1qq1)):
								
													for hk1qq in range(len(app1qq)):
		
														if app1qq1[y11q]==app1qq[hk1qq]:
										
															app1qq.remove(app1qq[hk1qq])
			
															break 
							
												dipl1qq=''
												for addalapp1qq in app1qq:
													dipl1qq=dipl1qq+addalapp1qq
												aio1qq=dipl1qq
							
												nhj1qq=2
												glk1qq=aio1qq[iforw1qq: ]
												break
											else:
												glk1qq=aio1qq[iforw1qq: ]
							
												for stoplop1qq in glk1qq:
													if not stoplop1qq.isnumeric() and stoplop1qq!='.':
														glk1qq=glk1qq.replace(stoplop1qq,'')
										
														glen1qq=len(glk1qq)
										
													if glen1qq==0:
														appendnam1qq.append(aio1qq[ :iforw1qq+1])
														lastbrk1qq='brk'
										
														break
										
										break 
					print(appendnam1qq,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
					

					appendot1qq=[]
					comtot1qq=''
					for comdot1qq in appendnam1qq:
						
						comtot1qq=comtot1qq+comdot1qq
					
		
						if not comdot1qq[len(comdot1qq)-1].isnumeric() and comdot1qq[len(comdot1qq)-1]!='.':
							appendot1qq.append(comtot1qq)
							comtot1qq=''
							continue
					
				
				checkflt=isinstance(appendot1qq[0],float)
				
				
					
			
	if lengt>=2 and  (hh>n or nowtot<=dayiwant) :
	
		a=b.upper()
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Torget Plus 10mg','Bylenta M50','Atocor Cv 10mg (Dr Reddy\'s LAB Ltd)']
		leng=len(tab)

			
		count=0
		while count<leng:
	 	
			j=''
			ji=0
			for i in a:
		
				z=tab[count].replace(j,'',1)
		
				for j in z:
					if i==j:
			
						ji=ji+1
				
				
						break
			count=count+1
			if ji>=3:
				
				break
		
		msg='{0}{1}'.format(a[0],a[1])
		z=a[3].upper()
		timing=['Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner']
		

		for dose in timing:
			add1=''
			for dose1 in dose:
		 	   if dose1.isupper():
		  	      add1=add1+dose1
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','TLodoz 2.5        ','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Torget Plus 10mg','Bylenta M50','Atocor Cv 10mg (Dr Reddy\'s LAB Ltd)']  	    
		        

		if n==-1:
			jusfor=[0,1]
		else:
			jusfor=[1]
			po=='po'
		for jf in jusfor:
		    
		    if n==-1:
		        forlop=tab
		    else:
		        
		        forlop=tabwant
		        
		    for zv in forlop:
		        if zv=='hi':
		        	continue
		        let=zv[0]+zv[1]
		        let=let.upper()
		        zem=zv[3]
		        zem=zem.upper()
		        
		        
		        if let=='CA':

		            zem=zv[3]
		           
		      
		        	
		        	
		           
		        if ji>=3 and msg==let and (z==zem or z=='Z') :
		        	
		        	tabnumber=tab.index(zv)
		        	
		        	tabcounum=tabnumber+1
		        	c=0
		        	if True:
		        	
		        		s=[15,15,10,10,120,15,10,10,6,10,15,15,15,10,10,15,10]			######
		        		d=[2,2,0.5,0.5,1,1,1,2,2,1,1,2,2,0.5,0.5,1,1]			######
		        		cost=[5.20,2.94,3.50,1.20,1.25,13.516,8,10.6,102.5,15.5,15.067,7.74,19.9,3.775,10.380,14,16.176]	######
		        		q=['ab','ab','ab','ab','bb','ad','bb','ab','ab','nt','ab','bb','bb','al','ab','ab','ad']	######
		        		p=['ad','ad','nt','nt','nt','nt','nt','ad','ad','ad','nt','bd','bd','nt','nt','nt','nt']	######
		        	if n==-1 and jf==0:
		        		tabwant.append(zv)
		        	if jf==0:
		        	
		        		tabrownum=[]
		        		print('')
		        		print('')
		        		print('')
		        		print('''	Name		=''',zv)
		        		print(tabnumber)
		        	
		      		
		        	
		        	
		        	if len(tabrownum)>0 and n==-1:
		        		rep[tabnumber]=tabrownum[0]
		        		tabcoou[tabnumber]=tabrownum[0]
		        		print(float(tabcoou[tabnumber]),'this is reduced')
		        	if n>-1:
		        		
		        		tabcoou[tabnumber]+=1
		        	
		        	c=tabcoou[tabnumber]
		        	
		       
		        	
		        	
		        	if jf==0 or True:
		        		s=s[tabnumber]
		        	
		        		d=d[tabnumber]		#daily
		        		cost=cost[tabnumber]	##
		        		q=q[tabnumber]
		        		q=q.upper()
		        		p=p[tabnumber]
		        		p=p.upper()
		        		
		        		
		        		
		        		for udi in [1,2]:
		        			timing=['Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner']
		        			for dose in timing:
		        				add1=''
		        				for dose1 in dose:
		        					if dose1.isupper():
		        						add1=add1+dose1
		        						
		        						if q==add1 :
		        						
		        							q=dose
		        						elif  p==add1:
		        							p=dose
		        						
		        	if q=='nt' or q=='NT':
		        		q=''
		        	if p=='nt' or p=='NT':
		        		p=''	 
		        	w=7*d
		        	m=30*d
		        	if let=='LA':
		        		w=5*d
		        		m=10
		        	tottab=0
		        	loprow=''
		        	print(appendot1qq)
		        	if appendot1qq[0].isnumeric() and jf==0:
		        		tottab=appendot1qq[0]/d
		        		c=tottab
		        		loprow='kit1'
		        		row123=''
		        	
		        	if row123=='kom1' and n==-1 and jf==0:
		        		
		        		loprow='kit'
		        		
		        		for montab in appendot1qq:
		        			mong=''
		        			for montab1 in montab[-1::-1]:
		        				if not montab1.isnumeric() and montab1!='.':
		        					locmontab1=montab.find(montab1)
		        					montnum=montab[ :locmontab1]
		        					mong=montnum+mong
		        					montnum=float(montnum)
		        					montab1=montab1.lower()
		        		
		        					if montab1=='y':
		        						monnum=montnum*365
		        					elif montab1=='m':
		        						monnum=montnum*(m/d)
		        					elif montab1=='w':
		        						monnum=montnum*(w/d)
		        					elif montab1=='d':
		        						monnum=montnum
		        					elif montab1=='s':
		        						monnum=(montnum*s)/d
		        					elif montab1=='t':
		        						monnum=montnum/d
		        					tottab=monnum+tottab
		        				
		        					c=tottab
					
		        	
		        
		        if n==-1 and jf==0 and msg==let and z==zem :
		        	c=0
		        	if loprow=='kit' or loprow=='kit1':
		        		c1=tottab
		        		
		        		
		        	else:
		        		c1=0
		        		c1=0
		        	c=c-c1
		        	if row1=='d':
		        		
		        		c=c
		        		
		        	tabrownum.append(c)
		        	
		        	break
		        	
		      
		       
		
		
		strcos=s*cost				
		time=','.join([q,p])
		print('''	daily(d)	=''',d,'''(d)''',time)
		print('''	weekly(w)	=''',w,'''(w)''')
		print('''	monthly(m)	=''',m,'''(m)''')
		print('''	strip(s)	=''',s,'''(s)	cost of Strip = ''',strcos)
		print('')
		print('''	cost per each	= Rs''' ,cost)	
		print('')
		
		
		
		
		if row1=='z' and n==-1:
			
			lesday=c
			
			
			aio1t=input('''	qty u want	= ''')
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
									for romnam1t in aio1t[iforw1t: ]:
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
				print(appendnam1t,'hhhhhhhhhhhhhhhhhhhhhh')
				appendot1t=[]
				comtot1t=''
				for comdot1t in appendnam1t:
					
					comtot1t=comtot1t+comdot1t
					
					if not comdot1t[len(comdot1t)-1].isnumeric() and comdot1t[len(comdot1t)-1]!='.':
						appendot1t.append(comtot1t)
						comtot1t=''
						continue
				
				tottab1t=0
				for montab1t in appendot1t:
					mong1t=''
					for montab1t1 in montab1t[-1::-1]:
						if not montab1t1.isnumeric() and montab1t1!='.':
							locmontab1t1=montab1t.find(montab1t1)
							montnum1t=montab1t[ :locmontab1t1]
							mong1t=montnum1t+mong1t
							montnum1t=float(montnum1t)
							montab1t1=montab1t1.lower()
							if montab1t1=='y':
								monnum1t=montnum1t*365
							elif montab1t1=='m':
								monnum1t=montnum1t*(m/d)
							elif montab1t1=='w':
								monnum1t=montnum1t*(w/d)
							elif montab1t1=='d':
								monnum1t=montnum1t
							elif montab1t1=='s':
								monnum1t=(montnum1t*s)/d
							elif montab1t1=='t':
								monnum1t=montnum1t/d
							tottab1t=monnum1t+tottab1t
				
																						
																																										
			c=tottab1t+lesday
			dayiwant=-1

											
		
		
		if hh<n+1 and row1!='a':
			
			c=hh+rep[tabnumber]
		
		ntab=c*d
			
		qtystp=ntab/s
		qtystp=round(qtystp,2)
		print('''	no of tablets	=''',ntab,'''(days:-''',c,''')    {''',qtystp,'''strip}''')
		tamt=ntab*cost
		tamt=round(tamt,2)
		nowtot=nowtot+tamt
		nowtot=round(nowtot,2)
		print('''	total amount	=''',tamt,'''				    Sub total=''',nowtot)
		
		total.append(tamt)
		print(tabwant)
		
		
		
		
	
		
	
		continue
	continue
dis=float(input('					DISCOUNT	= '))

dpri =nowtot*(dis/100)

final=nowtot-dpri
print('					Discount MRP	=',final)
				

	