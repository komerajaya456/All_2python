sol=0
total=[]
m=0
while True:
	m=m+1
	sol=sol+1
	
	print('						',sol)
	b=input('''Enter the name of tablet :- 
	press 'ENTER' to finalize :''')
	lengt=len(b)
	if lengt>=2:
		a=b.upper()
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.5','Jamension B12 1200mg',	'Formule forte']
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
			s=10
			d=1 		#daily
			cost=8	##
			w=7*d
			m=30*d
			q=bb	##
			p=nt	##
			###
		
		time=','.join([q,p])
		print('''	daily(d)	=''',d,'''(d)''',time)
		print('''	weekly(w)	=''',w,'''(w)''')
		print('''	monthly(m)	=''',m,'''(m)''')
		print('''	strip(s)	=''',s,'''(s)''')
		print('')
		print('''	cost per each	= Rs''' ,cost)	
		
		c=input('''	qty u want	= ''')
		print('')
		alp='dwmys'
		ap=[]
		app=[]

		ij=''
		count=0
		ntab=1
		
		for i in c:
			if i.islower():
					
					for j in alp:
						if i==j:
							if i=='d' or i=='w' or i=='m' or i=='y' or i=='s':
								z=c.find(i)
								oip=i
								op=c[ :z]
								for k in op:
									if k.isnumeric() or k=='.':
										app.append(k)
								
								ai=app
								j=''
								wi=[]
								opp=[]
								cou=0
								for i in ai:
									j=j+ai[cou]
		
									cou=cou+1
		
								
								wi.append(j)
								
								oiiu=map(float,wi)
								iu=list(oiiu)
								
								for ijk in alp:
										if ijk==oip:
											if ijk=='d':
												ijk=d
									
											elif ijk=='w':
												ijk=w
											elif ijk=='m':
												ijk=m
											elif ijk=='y':
												ijk=y
											elif ijk=='s':
												ijk=s
										
											opy=float(ijk)	
											ntab=iu[0]*opy
			elif not c.islower():		
										
				ntab=float(c)						
				
		print('''	no of tablets	=''',ntab)
		tamt=ntab*cost
		print('''	total amount	=''',tamt)
		total.append(tamt)
		
	else:
		
		break
	continue
print(total)
lo=0
tp=0
for t in total:
	tp=tp+total[lo]
	lo=lo+1
sum=tp
print('					MRP of',(sol-1),'tablets=',sum)
dis=float(input('					DISCOUNT	= '))
dpri =sum*(dis/100)
final=sum-dpri
print('					Discount MRP	=',final)
				
	