dayiwant=input('''Enter the amount U have 
	or Days u want:-''')
nowtot=0
diwasu=dayiwant	
rr=0
po=0
tottab=0
emp=''
eleofb='kkk'

vala1num=0
non=0
numc=[]
jusva=0
row1='ki'
jusva1z=0

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
		print(diw,'ss',dayiwant)
		dayiwant=diwasu
		if last1.isnumeric() and nope==1:
			print('hik')
			dayiwant=float(dayiwant)
			nope=2
			row1='a'
			break
			
			
		elif not last1.isnumeric() and len(dayiwant)>1:
			if  jusva==2:
				lend1=0
				print('hik11')
				dayiwant=0
				break
			
			
			print('hik')
			row1='d'
			aio=diwasu
			nhj=1
			glen=1
			appendnam=[]
			glk=''
			lastbrk=''
			while True :
				nhj=0
	
				if lastbrk=='brk':
					break
	
				for imo in aio :
					if lastbrk=='brk':
						break
		
					if not imo.isnumeric() and imo!='.':
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
							
										locrom=aio[iforw: ].find(romnam)
										appendnam.append(aio[ :iforw+1])
										akl=aio[iforw: ]

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
else:
	
	row1='z'
	dayiwant=0


	

c=0
tabwant=['hi']
sol=0
total=[]
tum=1


n=-1



while ((nowtot<=dayiwant and row1=='a') or (hh>n and row1=='d' and hh!=0) or (len(b)>1 and row1=='z'))  :
	tabwantleg=len(tabwant)
	
	
	tab11=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Jamension B12 1200mg',	'Formule forte']
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
				locike32=b.find(ike32)
				
				row12='kom'
				row123='kom1'
				
				
				
				a12=b[locike32: ]
			
				endlop='en'
				appendst=[]
				lendst=len(a12)
				while len(a12)>0:
					if endlop=='end':
						break
					for stir in a12[-1::-1]:
						if endlop=='end':
							break
						addlasnum=''
				
						if not stir.isnumeric():
						
							for exloc in range(len(a12)):
								if a12[exloc]==stir:
									locstir=exloc			#last location
							for antalp in a12[locstir-1::-1]:
				
								if not antalp.isnumeric() and antalp!='.':
									for exloc1 in range(len(a12)):
										if a12[exloc1]==antalp:
											locstir1=exloc1			#last location
									now12=a12[locstir1+1:locstir+1]
						
									appendst.append(now12)
									a12=a12.replace(a12[locstir1+1:locstir+1],'')
									
									break
					
								else:
									addlasnum=antalp+addlasnum
								
									if len(addlasnum)+1==len(a12):
										appendst.append(a12)
										
										endlop='end'
			
										
			
				
						
				
		
			
	if lengt>=2 and  (hh>n or nowtot<=dayiwant) :
	
		a=b.upper()
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Jamension B12 1200mg',	'Formule forte']
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
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','TLodoz 2.5        ','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Jamension B12 1200mg',	'Formule forte']  	    
		        

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
		        	
		        		s=[15,15,10,10,120,15,10,10,6,10,15,15,15,10]
		        		d=[2,2,0.5,0.5,1,1,1,2,2,1,1,2,2,0.5]
		        		cost=[5.20,2.94,3.50,1.20,1.25,13.516,8,10.6,102.5,15.5,15.067,7.74,19.9,3.775]
		        		q=['ab','ab','ab','ab','bb','ad','bb','ab','ab','nt','ab','bb','bb','al']
		        		p=['ad','ad','nt','nt','nt','nt','nt','ad','ad','ad','nt','bd','bd','nt']
		        	if n==-1 and jf==0:
		        		tabwant.append(zv)
		        	if jf==0:
		        	
		        		tabrownum=[]
		        		print('')
		        		print('')
		        		print('')
		        		print('''	Name		=''',zv)
		        	
		      		
		        	
		        	
		        	if len(tabrownum)>0 and n==-1:
		        		
		        		tabcoou[tabnumber]=tabrownum[0]
		        		print(tabcoou[tabnumber],'this is reduced')
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
		        			
		        			if q==add1 or p==add1:
		        				q=dose
		        				p=dose
		   			     
		        	if q=='nt':
		        		q=''
		        	if p=='nt':
		        		p=''	 
		        	w=7*d
		        	m=30*d
		        	if let=='LA':
		        		w=5*d
		        		m=10
		        	tottab=0
		        	loprow=''
		        	if row123=='kom1' and n==-1 and jf==0:
		        		
		        		loprow='kit'
		        		
		        		for montab in appendst:
		        			mong=''
		        			for montab1 in montab[-1::-1]:
		        				if not montab1.isnumeric() and montab1!='.':
		        					locmontab1=montab.find(montab1)
		        					montnum=montab[ :locmontab1]
		        					mong=montnum+mong
		        					montnum=float(montnum)
		        		
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
		        	if loprow=='kit':
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
			dayiwant=input('''	qty u want	= ''')
			tottab1y=0
			a1y=dayiwant
			end1ylop1y='en'
			appendst1y=[]
			lend1yst1y=len(a1y)
			while len(a1y)>0:
				if end1ylop1y=='end1y':
					break
	
				for stir1y in a1y[-1::-1]:
					if end1ylop1y=='end1y':
						break
					addlasnum1y=''
	
					if not stir1y.isnumeric():
			
						for exloc1y in range(len(a1y)):
							if a1y[exloc1y]==stir1y:
								locstir1y=exloc1y			#last location
						for antalp1y in a1y[locstir1y-1::-1]:
				
							if not antalp1y.isnumeric() and antalp1y!='.':
								for exloc1y1 in range(len(a1y)):
									if a1y[exloc1y1]==antalp1y:
										locstir1y1=exloc1y1			#last location
								now121y=a1y[locstir1y1+1:locstir1y+1]
					
								appendst1y.append(now121y)
								a1y=a1y.replace(a1y[locstir1y1+1:locstir1y+1],'')
					
								break
					
							else:
								addlasnum1y=antalp1y+addlasnum1y
				
								if len(addlasnum1y)+1==len(a1y):
									appendst1y.append(a1y)
						
									end1ylop1y='end1y'
		
			for montab1y in appendst1y:
				mong1=''
				for montab1y1 in montab1y[-1::-1]:
					if not montab1y1.isnumeric() and montab1y1!='.':
						locmontab1y1=montab1y.find(montab1y1)
						montnum1y=montab1y[ :locmontab1y1]
						mong1=montnum1y+mong1
						montnum1y=float(montnum1y)
			
						if montab1y1=='y':
							monnum1y=montnum1y*365
						elif montab1y1=='m':
							monnum1y=montnum1y*(m/d)
						elif montab1y1=='w':
							monnum1y=montnum1y*(w/d)
						elif montab1y1=='d':
							monnum1y=montnum1y
						elif montab1y1=='s':
							monnum1y=(montnum1y*s)/d
						elif montab1y1=='t':
							monnum1y=montnum1y/d
						tottab1y=monnum1y+tottab1y
						
						c=tottab1y+lesday
						dayiwant=-1

											
		
			
		
		
		ntab=c*d
				
		qtystp=ntab/s
		qtystp=round(qtystp,2)
		print('''	no of tablets	=''',ntab,'''(days:-''',c,''')    {''',qtystp,'''strip}''')
		tamt=ntab*cost
		tamt=round(tamt,2)
		nowtot=nowtot+tamt
		nowtot=round(nowtot,2)
		print('''	total amount	=''',tamt,'''				    Sub total=''',nowtot)
		print('')
		total.append(tamt)
		print(tabwant)
		
		
		
		
	
		
	
		continue
	continue
dis=float(input('					DISCOUNT	= '))

dpri =nowtot*(dis/100)

final=nowtot-dpri
print('					Discount MRP	=',final)
				

	