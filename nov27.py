dayiwant=input('Enter the amount U have:-')
rr=0
twoz=0
onez=0
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

c=0
tabwant=['hi']
sol=0
total=[]
tum=1
b='tumki'
nowtot=0
n=0
hh=hh+1




while (nowtot<=dayiwant and row1=='a') or (hh>=n and row1=='d' and hh!=0):
	tabwantleg=len(tabwant)
	print('					hiiïyyyyttttrrrrrr')

	if   len(b)<2 or len(b)>10:
		if tabwantleg==tum or len(b)<2:
			nowtot=0
			c+=1	
			n=n+1
			tum=1
			if n>hh:
				break
		
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
		emp=float(emp)
	if lengt>=2 and  (hh>n or nowtot<=dayiwant) :
		
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
		
		if n==0:
			jusfor=[0,1]
		else:
			jusfor=[1]
		for jf in jusfor:
			print(jusfor,'jusfor')
			if ji>=3 and msg=='CA' and z=='D':
				print(c,'cc')
				print(jf,'jfjfjfjf')
				c=0
				if n==0 and jf==0:
					tabwant.append(tab[0])
				if jf==0:
					
					tabrownum=[]
				print(tabrownum)
				print('''	Name		=''',tab[0])
				rem2=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem2.append(st)
				if len(rem2)>0 and n==0:
					remele=rem2[0]
				
					twoz=rem2[0]
					tabrownum.remove(tabrownum[0])
				if n>0:	
					twoz=twoz+1
				c=twoz
				print(n,'nnn')
				print(twoz,twoz)
			
				s=15
				d=2 		#daily
				cost=5.20	##
				q=ab	##
				p=ad	##
				###
				w=7*d
				m=30*d
						
			elif ji>=3 and msg=='CA' and z=='C':
				c=0
				if n==0 and jf==0:
					tabwant.append(tab[1])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[1])
				rem1=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem1.append(st)
				if len(rem1)>0 and n==0:
					remele=rem1[0]
					
					onez=rem1[0]
					tabrownum.remove(tabrownum[0])
				if n>0:
					onez=onez+1
				c=onez
				s=15
				d=2 			#daily
				cost=2.94	##
				q=ab	##
				p=ad	##
				###
				w=7*d
				m=30*d
		
			if jf==0:
				if eleofb=='t' or eleofb=='T':
					non=d
				elif eleofb=='d' or eleofb=='D':
					non=1
				elif eleofb=='s' or eleofb=='S':
					non=d/s
					
											
			if n==0 and jf==0:			
				if non==0:
					print('xxxxxxx')
					c1=emp/d

				else:	
					c1=emp/non
				print(c1,'c111')
				c=c-c1
				print('cwant')
				tabrownum.append(c)
				print(tabrownum)				
						
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