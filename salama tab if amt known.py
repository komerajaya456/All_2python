amthas=int(input('Enter the amount U have:-'))
print('')
tabwant=['hi']
b='after'
tum=0
while True:
	print('')
	print(tabwant)
	if len(b)<2 and tum<=2:
		
		print('happenfrghjkjhgfdsdfghjhgfdsasdfghjhgfdsa')
		tum+=1 
	else:	
		b=''
		b=input('''Enter the name of tablet :-
		if Done press 'ENTER'  ''')
		lengt=len(b)
		if lengt>=2:
			a=b.upper()
			tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Jamension B12 1200mg',	'Formule forte','Hifenac-D','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1','Razo-D(dr.reddy LTD)','Tide plus 10mg','enough','stop','completed']
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
			print(a)
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
				tabwant.append(tab[0])
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
				tabwant.append(tab[1])
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
			
			time=','.join([q,p])
			print('''	daily(d)	=''',d,'''(d)''',time)
			print('''	weekly(w)	=''',w,'''(w)''')
			print('''	monthly(m)	=''',m,'''(m)''')
			print('''	strip(s)	=''',s,'''(s)''')
			print('')
			print('''	cost per each	= Rs''' ,cost)	
		
			print(tabwant)
		
			
		else:
			print('umegaaaaaaa')
		
	
		continue
	continue