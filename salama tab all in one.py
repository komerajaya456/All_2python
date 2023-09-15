dayiwant=input('''Enter the amount U have 
	or Days u want:-''')
nowtot=0	
rr=0
po=0
emp=''
eleofb='kkk'
vala1num=0
non=0
numc=[]
jusva=0
row1='ki'
jusva1z=0
jf=0
nope=1
b='wer'
tabcoou=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rep=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hh=0
leng4=len(dayiwant)
leng4=leng4-1
if leng4>1:
	b='tumki'
	last1=dayiwant[leng4]
	for diw in dayiwant:
		if last1.isnumeric() and nope==1:
			dayiwant=float(dayiwant)
			nope=2
			row1='a'
			
			break 
		elif not last1.isnumeric() and leng4>1:
			if  jusva==2:
				lend1=0
				dayiwant=0
				break
		
			
			row1='d'
			df=dayiwant
			dv=dayiwant
			finlnum=0
			locva1=0
			lend1=len(dayiwant)
			numday=0
			for zic in dayiwant:
				if zic!='.' and not zic.isnumeric():
				
					loczic=dayiwant.find(zic)
					zicele=dayiwant[ :loczic]
					ziclen=len(zicele)
					break
			while lend1>0:
	
	
				jusva=0
				for gin in dayiwant[lend1-1::-1]:
					addva=''
		
					lend1=len(dayiwant)
		
					if jusva==1 :
			
						break
					elif  jusva==2:
						lend1=0
						dayiwant=0
						break
					elif not gin.isnumeric():
						print(gin,'gin')
						for ink1 in range(lend1):
							if dayiwant[ink1]==gin:
								locgin=ink1
				
						vala=dayiwant[locgin-1]
				
						if vala.isnumeric():
							for ink in range(lend1):
								if dayiwant[ink]==vala:
					
									locva=ink
				
							locvas=locva+1
				
							for vala1 in dayiwant[locva::-1] :
			
								if not vala1.isnumeric() and vala1!='.' :
									locva1=dayiwant.find(vala1)
									vala2=locva1+1
							
									numday=dayiwant[vala2:locvas]
									numday=float(numday)
									dayiwant=dayiwant.replace(dayiwant[locva1+1: ],'')
									
									if gin=='y':
										vala1num=numday*365
									elif gin=='m':
										vala1num=numday*30
									elif gin=='w':
										vala1num=numday*7
									elif gin=='d':
										vala1num=numday
									finlnum=vala1num+finlnum
									print(finlnum)
								
									jusva=1
									break
							
								else:
									addva=vala1+addva
									if gin==zic and len(addva)==ziclen:
										addva=float(addva)
										
										if gin=='y':
											vala1num=addva*365
										elif gin=='m':
											vala1num=addva*30
										elif gin=='w':
											vala1num=addva*7
										elif gin=='d':
											vala1num=addva
										finlnum=vala1num+finlnum
											
										
										jusva=2
										hh=float(finlnum)##days
										break
else:
	
	row1='z'
	dayiwant=0


	

c=0
tabwant=['hi']
sol=0
total=[]
tum=1


n=-1



while (nowtot<=dayiwant and row1=='a') or (hh>n and row1=='d' and hh!=0) or (len(b)>1 and row1=='z'):
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
		
		emp=0
		lengt=len(b)
		val3=0	
		okw=[]
		for ike in b:
			if  jusva1z==2:
				lend11z=0
				break
			if ike.isnumeric() or ike=='.':
				
				locike=b.find(ike)
				non=1
				dayiwant1z=b[locike: ]
				dfz=dayiwant1z
				dv1z=dayiwant1z
				finlnum1z=0
				locva11zz11z=0
				lend11z=len(dayiwant1z)
				numday1z=0
				for zic1z in dayiwant1z:
					if zic1z!='.' and not zic1z.isnumeric():
						print(zic1z)
						loczic1z=dayiwant1z.find(zic1z)
						zic1zele=dayiwant1z[ :loczic1z]
						zic1zlen=len(zic1zele)
						break
				while lend11z>0:
	
	
					jusva1z=0
					for gin1z in dayiwant1z[lend11z-1::-1]:
	
	
						addv1za=''
		
						lend11z=len(dayiwant1z)
		
						if jusva1z==1 :
			
							break
						elif  jusva1z==2:
							lend11z=0
							break
						elif not gin1z.isnumeric():
							print(gin1z,'gin1z')
							for ink1zz11z in range(lend11z):
								if dayiwant1z[ink1zz11z]==gin1z:
									locgin1z=ink1zz11z
			
							vala1z=dayiwant1z[locgin1z-1]
							if vala1z.isnumeric():
								for ink1zz in range(lend11z):
									if dayiwant1z[ink1zz]==vala1z:
										locva11zz=ink1zz
				
								locva11zzs=locva11zz+1
				
								for vala1z1 in dayiwant1z[locva11zz::-1] :
			
									if not vala1z1.isnumeric() and vala1z1!='.' :
										locva11zz11z=dayiwant1z.find(vala1z1)
										vala1z2=locva11zz11z+1
						
										numday1z=dayiwant1z[vala1z2:locva11zzs]
										numday1z=float(numday1z)
										dayiwant1z=dayiwant1z.replace(dayiwant1z[locva11zz11z+1: ],'')
										print(numday1z,'nuk',gin1z)
										if gin1z=='y':
											vala1z1num=numday1z*365
										elif gin1z=='m':
											vala1z1num=numday1z*30
										elif gin1z=='w':
											vala1z1num=numday1z*7
										elif gin1z=='d':
											vala1z1num=numday1z
										finlnum1z=vala1z1num+finlnum1z
										print(finlnum1z)
							
										jusva1z=1
										break
						
									else:
										addv1za=vala1z1+addv1za
										if gin1z==zic1z and len(addv1za)==zic1zlen:
											addv1za=float(addv1za)
											print(addv1za)
											if gin1z=='y':
												vala1z1num=addv1za*365
											elif gin1z=='m':
												vala1z1num=addv1za*30
											elif gin1z=='w':
												vala1z1num=addv1za*7
											elif gin1z=='d':
												vala1z1num=addv1za
											finlnum1z=vala1z1num+finlnum1z
											print(finlnum1z)	
						
											jusva1z=2
											break
					
							
			
				
			
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
		        	
		        
		        if n==-1 and jf==0 and msg==let and z==zem :
		      
		        	c=0
		      
		        	if non==0:
		      
		        		c1=0
		        	else:
		        		c1=finlnum1z
		        	c=c-c1
		      
		        	tabrownum.append(c)
								
		strcos=s*cost				
		time=','.join([q,p])
		print('''	daily(d)	=''',d,'''(d)''',time)
		print('''	weekly(w)	=''',w,'''(w)''')
		print('''	monthly(m)	=''',m,'''(m)''')
		print('''	strip(s)	=''',s,'''(s)	cost of Strip = ''',strcos)
		print('')
		print('''	cost per each	= Rs''' ,cost)	
		print('')
		print(c,'this is reduced')
		
		if row1=='z':
			lesday=c
			dayiwant=input('''	qty u want	= ''')
			df=dayiwant
			dv=dayiwant
			finlnum=0
			locva1=0
			lend1=len(dayiwant)
			numday=0
			for zic in dayiwant:
				if zic!='.' and not zic.isnumeric():
			
					loczic=dayiwant.find(zic)
					zicele=dayiwant[ :loczic]
					ziclen=len(zicele)
					break
			while lend1>0:
	
	
				jusva=0
				for gin in dayiwant[lend1-1::-1]:
	
	
					addva=''
		
					lend1=len(dayiwant)
		
					if jusva==1 :
			
						break
					elif  jusva==2:
						dayiwant=-1
						lend1=0
						break
					elif not gin.isnumeric():
						
						for ink1 in range(lend1):
							if dayiwant[ink1]==gin:
								locgin=ink1
			
						vala=dayiwant[locgin-1]
						if vala.isnumeric():
							for ink in range(lend1):
								if dayiwant[ink]==vala:
					
									locva=ink
				
							locvas=locva+1
				
							for vala1 in dayiwant[locva::-1] :
			
								if not vala1.isnumeric() and vala1!='.' :
									locva1=dayiwant.find(vala1)
									vala2=locva1+1
						
									numday=dayiwant[vala2:locvas]
									numday=float(numday)
									dayiwant=dayiwant.replace(dayiwant[locva1+1: ],'')
								
									if gin=='y':
										vala1num=numday*365
									elif gin=='m':
										vala1num=numday*30
									elif gin=='w':
										vala1num=numday*7
									elif gin=='d':
										vala1num=numday
									elif gin=='t':
										
										tabld=numday/d
										vala1num=tabld
									elif gin=='s':
										stripday=numday*s
										vala1num=stripday/d
									finlnum=vala1num+finlnum
									
							
									jusva=1
									break
						
								else:
									addva=vala1+addva
									if gin==zic and len(addva)==ziclen:
										addva=float(addva)
										
										if gin=='y':
											vala1num=addva*365
										elif gin=='m':
											vala1num=addva*30
										elif gin=='w':
											vala1num=addva*7
										elif gin=='d':
											vala1num=addva
										elif gin=='t':
											tabld=addva/d
											vala1num=tabld
										elif gin=='s':
											stripday=addva*s
											vala1num=stripday/d
										
										finlnum=vala1num+finlnum
											
						
										jusva=2
										c=finlnum+lesday
										ntab=c*d
										
										break
											
		else:
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
				

	