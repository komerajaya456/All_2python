dayiwant=input('''Enter the amount U have 
	or Days u want:-''')
rr=0
s=[15,15,10,10,120,15,10,10,6,10,15,15,15,10]
d=[2,2,0.5,0.5,1,1,1,2,2,1,1,2,2,0.5]
cost=[5.20,2.94,3.50,1.20,1.25,13.516,8,10.6,102.5,15.5,15.067,7.74,19.9,3.775]
q=[ab,ab,ab,ab,bb,ad,b,ab,ab,nt,ab,bb,bb,al]
p=[ad,ad,nt,nt,nt,nt,nt,ad,ad,ad,nt,bd,bd,nt]
tabcou=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
n=-1


while (nowtot<=dayiwant and row1=='a') or (hh>n and row1=='d' and hh!=0):
	tabwantleg=len(tabwant)
	

	if   len(b)<2 or len(b)>10:
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
		z=a[3]
		timing=['Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner']
		yoo=['ab','bl']

		for dose in timing:
			add1=''
			for dose1 in dose:
		 	   if dose1.isupper():
		  	      add1=add1+dose1
		   	     print(add1)
		    	    if add1==yoo[0].upper():
		     	       print(dose)
		        
		
		if n==-1:
			jusfor=[0,1]
		else:
			jusfor=[1]
		for jf in jusfor:
		    if n==-1:
		        forlop=tab
		    else:
		        forlop=tabwant
		     for zv in forlop:
		        let=zv[0]+zv[1]
		        let=let.upper()
		        z='Z'
		        if let=='CA':
		            zem=zv[3]
		            zem=z.upper()
		        
		    	if ji>=3 and msg==let and (z==zem or z=='Z'):
				print('')
				print('')
				print('')
				
				tabnumber=tab.index(zv)
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(zv)
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',zv)
				
				if len(tabrownum)>0 and n==-1:
					tab[tabnumber]=tabrownum[0]
				if n>-1:
					tab[tabnumber]=tab[tabnumber]+1
				c=tab[tabnumber]
				s=s[tabnumber]
				d=d[tabnumber]		#daily
				cost=cost[tabnumber]	##
				q=q[tabnumber]	##
				p=p[tabnumber]	##
				###
				w=7*d
				m=30*d
						
			elif ji>=3 and msg=='CA' and z=='C':
				print('')
				print('')
				print('')
				tabnumber=1
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
		
					
				if len(tabrownum)>0 and n==-1:
					tab[tabnumber]=tabrownum[0]
				if n>-1:
					tab[tabnumber]=tab[tabnumber]+1
				c=tab[tabnumber]
				s=15
				d=2 			#daily
				cost=2.94	##
				q=ab	##
				p=ad	##
				###
				w=7*d
				m=30*d
			elif ji>=3 and msg=='FR' :	####
				print('')
				print('')
				print('')
				tabnumber=2
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem3=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem3.append(st)
				if len(rem3)>0 and n==-1:
					remele=rem3[0]
					
					tabcou[tabcounum]=rem3[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10
				d=0.5 		#daily
				cost=3.50	##
				q=ab	##
				p=nt	##
				###
				w=7*d
				m=30*d
			
			
			elif ji>=3 and msg=='LA' :		####
				print('')
				print('')
				print('')
				tabnumber=3
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem4=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem4.append(st)
				if len(rem4)>0 and n==-1:
					remele=rem4[0]
					
					tabcou[tabcounum]=rem4[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10                                ####
				d=0.5 		#daily
				cost=1.20	##
				w=5*d
				m=10
				q=ab	##
				p=nt	##
				###
			
			elif ji>=3 and msg=='EL' :	####
				print('')
				print('')
				print('')
				tabnumber=4
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem5=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem5.append(st)
				if len(rem5)>0 and n==-1:
					remele=rem5[0]
					
					tabcou[tabcounum]=rem5[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=120
				d=1 		#daily
				cost=1.25	##
				q=bb	##
				p=nt	##
				###
				w=7*d
				m=30*d
		
			elif ji>=3 and msg=='ST' :		####
				print('')
				print('')
				print('')
				tabnumber=5
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem6=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem6.append(st)
				if len(rem6)>0 and n==-1:
					remele=rem6[0]
					
					tabcou[tabcounum]=rem6[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=15
				d=1 		#daily
				cost=13.516	##
				w=7*d
				m=30*d
				q=ad	##
				p=nt	##
				###
		
			elif ji>=3 and msg=='TL' or msg=='T ' or msg=='LO' :		####
				print('')
				print('')
				print('')
				tabnumber=6											#######
				tabcounum=tabnumber+1
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem7=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem7.append(st)
				if len(rem7)>0 and n==-1:
					remele=rem7[0]
					
					tabcou[tabcounum]=rem7[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10
				d=1 		#daily
				cost=8	##
				w=7*d
				m=30*d
				q=bb	##
				p=nt	##
				###
			
		
			elif ji>=3 and msg=='HI' :	####
				tabnumber=9											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem8=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem8.append(st)
				if len(rem8)>0 and n==-1:
					remele=rem8[0]
					
					tabcou[tabcounum]=rem8[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10
				d=2 		#daily
				cost=10.600	##
				q=ab	##
				p=ad	##
				###
				w=7*d
				m=30*d
	
			elif ji>=3 and msg=='OR' :	####
				tabnumber=10											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem9=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem9.append(st)
				if len(rem9)>0 and n==-1:
					remele=rem9[0]
					
					tabcou[tabcounum]=rem9[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=6
				d=2 		#daily
				cost=102.5	##
				q=ab	##
				p=ad	##
				###
				w=7*d
				m=30*d
		
			elif ji>=3 and msg=='RE' :	####
				tabnumber=11											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem10=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem10.append(st)
				if len(rem10)>0 and n==-1:
					remele=rem10[0]
					
					tabcou[tabcounum]=rem10[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10
				d=1 		#daily
				cost=15.5	##
				q=nt	##
				p=ad	##
				###
				w=7*d
				m=30*d
		
			elif ji>=3 and msg=='EM' :	####
				tabnumber=12											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem11=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem11.append(st)
				if len(rem11)>0 and n==-1:
					remele=rem11[0]
					
					tabcou[tabcounum]=rem11[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=15
				d=1		#daily
				cost=15.067	##
				q=ab	##
				p=nt	##
				###
				w=7*d
				m=30*d
		
			elif ji>=3 and msg=='GE' :	####
				tabnumber=13											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem12=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem12.append(st)
				if len(rem12)>0 and n==-1:
					remele=rem12[0]
					
					tabcou[tabcounum]=rem12[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=15
				d=2 		#daily
				cost=7.74	##
				q=bb	##
				p=bd	##
				###
				w=7*d
				m=30*d
			
			elif ji>=3 and msg=='RA' :	####
				tabnumber=14											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem13=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem13.append(st)
				if len(rem13)>0 and n==-1:
					remele=rem13[0]
					
					tabcou[tabcounum]=rem13[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=15
				d=2 		#daily
				cost=19.9	##
				q=bb	##
				p=bd	##
				###
				w=7*d
				m=30*d
			
			elif ji>=3 and msg=='TI' :	####
				tabnumber=15											#######
				tabcounum=tabnumber+1
				print('')
				print('')
				print('')
				c=0
				if n==-1 and jf==0:
					tabwant.append(tab[tabnumber])
				if jf==0:	
					tabrownum=[]
				print('''	Name		=''',tab[tabnumber])
				rem14=[]
				if len(tabrownum)>0:
					st=tabrownum[0]
					rem14.append(st)
				if len(rem14)>0 and n==-1:
					remele=rem14[0]
					
					tabcou[tabcounum]=rem14[0]
					tabrownum.remove(tabrownum[0])
				if n>-1:
					tabcou[tabcounum]=tabcou[tabcounum]+1
				c=tabcou[tabcounum]
				s=10
				d=0.5 		#daily
				cost=3.775	##
				q=al	##
				p=nt	##
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
					
											
			if n==-1 and jf==0:			
				if non==0:
					
					c1=emp/d

				else:	
					c1=emp/non
				
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
		
		
		
	
		
	
		continue
	continue
dis=float(input('					DISCOUNT	= '))

dpri =nowtot*(dis/100)

final=nowtot-dpri
print('					Discount MRP	=',final)
				
