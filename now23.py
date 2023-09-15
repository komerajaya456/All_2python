dayiwant=input('Enter the amount U have:-')
rr=0
hh=0
leng4=len(dayiwant)
leng4=leng4-1
last1=dayiwant[leng4]
emp=''
eleofb='kkk'
non=0
numc=[]
for diw in dayiwant:
	if last1.isnumeric() :

			
			dayiwant=float(dayiwant)
			row1='a' 
	elif diw=='d' :
		
		rr=dayiwant.find(diw)
		
		gg=dayiwant[ :rr]
		hh=float(gg)
		dayiwant=0
		row1='d'
		break
print(hh,'hh')				#days

print(dayiwant)	#amount u have

c=0
tabwant=['hi']
sol=0
total=[]
tum=1
b='tumki'
nowtot=0
n=0
while (nowtot<=dayiwant and row1=='a') or (hh>=n and row1=='d'):
	print(c,'čcvbn')
	print(tabwant)
	tabwantleg=len(tabwant)
	print(tabwantleg,'lenghtt')
	print(tum,'tun')
	
	if   len(b)<2 or len(b)>10 and input()=='j':
			
		print(c,'č')
		
		if tabwantleg==tum or len(b)<2:
			print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\hi\\\\\\\\')	
			nowtot=0
			
			n=n+1
			tum=1
			
		
		b=tabwant[tum]
		
		tum+=1 
		lengt=len(b)
		
	
	else :
		
		b=input('''Enter the name of tablet :-
		if Done press 'ENTER'  ''')
		
		emp=0
		lengt=len(b)
		val3=0
		
		okw=[]
		for ike in b:
	
			if ike.isnumeric() or ike=='.':
				okw.append(ike)
				ui=len(okw)
				emp=''	
				
				count=-1
				for jk in okw:
					emp=okw[count]+emp
					count=count-1
				lenemp=len(emp)
				finempw=emp[lenemp-1]
				findb=b.find(finempw)
				if not b[lengt-1].isnumeric():
					eleofb=b[findb+1]
			else:
				c=0
			emp=float(emp)
			print(emp,'emp')
	if lengt>=2 and  (hh>=c or nowtot<=dayiwant) :
		
		a=b.upper()
		tab=['CARDACE 2.5','CARCA 3.125','    FRUSELAC','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Jamension B12 1200mg',	'Formule forte','Hifenac-D','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1','Razo-D(dr.reddy LTD)','Tide plus 10mg']
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
		z=a[3]
		bb='Before Breakfast' 
		ab='After Breakfast' 
		bl='Before Lunch' 
		al='After Lunch'
		bd='Before Dinner' 
		ad='After Dinner' 
		nt=''
		
			
		
		if ji>=3 and msg=='CA' and z=='D':
			print('''	Name		=''',tab[0])
			if n==0 :
				print('hjkiiiiiijkjkjkjkjkjkjkjk')
				tabwant.append(tab[0])
			if tabwantleg==tum or len(b)<2:
				if emp>0:
					c=-1
					
				rev1=[]
				rev1len=len(rev1)
				rev1.append(c)
				
				if rev1len>1:
					replc=rev1[0]+1
					rev1=rev1.replace(rev1[1],replc)
					rev1.remove(rev1[0]) 
				c=rev1[0]+1
				
				
				
			s=15
			d=2 		#daily
			cost=5.20	##
			q=ab	##
			p=ad	##
				###
			w=7*d
			m=30*d
						
		elif ji>=3 and msg=='CA' and z=='C':
			print('''	Name		=''',tab[1])
			if n==0:
				tabwant.append(tab[1])
			if tabwantleg==tum or len(b)<2:
				print('evvvvvvyy')
				rev2=[]
				rev2len=len(rev2)
				rev2.append(c)
				if rev2len>1:
					replc=rev2[0]+1
					rev2=rev2.replace(rev2[1],replc)
					rev2.remove(rev2[0]) 
				c=rev2[0]+1
				print(c,'ccccccccc')
			s=15
			d=2 			#daily
			cost=2.94	##
			q=ab	##
			p=ad	##
			###
			w=7*d
			m=30*d
		elif ji>=3 and msg=='FR' :	####
			print('''	Name		=''',tab[2])
			if c==0:
				tabwant.append(tab[2])
			s=10
			d=0.5 		#daily
			cost=3.50	##
			q=ab	##
			p=nt	##
			###
			w=7*d
			m=30*d	
			
			
		elif ji>=3 and msg=='LA' :		####
			print('''	Name		=''',tab[3])	####
			if c==0:
				tabwant.append(tab[3])
			s=10
			d=0.5 		#daily
			cost=1.20	##
			w=5*d
			m=10
			q=ab	##
			p=nt	##
			###
			
		elif ji>=3 and msg=='EL' :	####
			print('''	Name		=''',tab[4])
			if c==0:
				tabwant.append(tab[4])
			s=120
			d=1 		#daily
			cost=1.25	##
			q=bb	##
			p=nt	##
			###
			w=7*d
			m=30*d
		
		elif ji>=3 and msg=='ST' :		####
			print('''	Name		=''',tab[5])	####
			if c==0:
				tabwant.append(tab[5])
			s=15
			d=1 		#daily
			cost=13.516	##
			w=7*d
			m=30*d
			q=ad	##
			p=nt	##
			###
		elif ji>=3 and msg=='TL' or msg=='T ' or msg=='LO' :		####
			print('''	Name		=''',tab[6])	####
			if c==0:
				tabwant.append(tab[6])
			s=10
			d=1 		#daily
			cost=8	##
			w=7*d
	
			m=30*d
			q=bb	##
			p=nt	##
			###
			
		
		elif ji>=3 and msg=='HI' :	####
			print('''	Name		=''',tab[9])
			if c==0:
				tabwant.append(tab[9])
			s=10
			d=2 		#daily
			cost=10.600	##
			q=ab	##
			p=ad	##
			###
			w=7*d
			m=30*d
		elif ji>=3 and msg=='OR' :	####
			print('''	Name		=''',tab[10])
			if c==0:
				tabwant.append(tab[10])
			s=6
			d=2 		#daily
			cost=102.5	##
			q=ab	##
			p=ad	##
			###
			w=7*d
			m=30*d
		elif ji>=3 and msg=='RE' :	####
			print('''	Name		=''',tab[11])
			if c==0:
				tabwant.append(tab[11])
			s=10
			d=1 		#daily
			cost=15.5	##
			q=nt	##
			p=ad	##
			###
			w=7*d
			m=30*d
	
		elif ji>=3 and msg=='EM' :	####
			print('''	Name		=''',tab[12])
			if c==0:
				tabwant.append(tab[12])
			s=15
			d=1		#daily
			cost=15.067	##
			q=ab	##
			p=nt	##
			###
			w=7*d
			m=30*d
	
		elif ji>=3 and msg=='GE' :	####
			print('''	Name		=''',tab[13])
			if c==0:
				tabwant.append(tab[13])
			s=15
			d=2 		#daily
			cost=7.74	##
			q=bb	##
			p=bd	##
			###
			w=7*d
			m=30*d
		
		elif ji>=3 and msg=='RA' :	####
			print('''	Name		=''',tab[14])
			if c==0 :
				tabwant.append(tab[14])
			
				
				
				
			s=15
			d=2 		#daily
			cost=19.9	##
			q=bb	##
			p=bd	##
			###
			w=7*d
			m=30*d
			
		elif ji>=3 and msg=='TI' :	####
			print('''	Name		=''',tab[15])
			if c==0:
				tabwant.append(tab[15])
			s=10
			d=0.5 		#daily
			cost=3.775	##
			q=al	##
			p=nt	##
			###
			w=7*d
			m=30*d
		elif ji<2:
			print('umegaaaaa')
		if eleofb=='t' or eleofb=='T':
			non=d
		elif eleofb=='d' or eleofb=='D':
			non=1
		elif eleofb=='s' or eleofb=='S':
			non=d/s
					
											
		
		if non==0:
			c1=emp/d

		else:	
			c1=emp/non
		print(c1,'c111')
		c=c-c1			
					
				
														
	
							
									
		time=','.join([q,p])
		print('''	daily(d)	=''',d,'''(d)''',time)
		print('''	weekly(w)	=''',w,'''(w)''')
		print('''	monthly(m)	=''',m,'''(m)''')
		print('''	strip(s)	=''',s,'''(s)''')
		print('')
		print('''	cost per each	= Rs''' ,cost)	
		print('')
			
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
		
		print(n,hh,'yyyyuuuu')		
		
	
		
	
		continue
	continue