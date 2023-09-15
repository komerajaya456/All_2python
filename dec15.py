dayiwant=input('''Enter the amount U have 
	or Days u want:-''')
rr=0
po=0

tabcoou=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rep=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hh=0
leng4=len(dayiwant)
leng4=leng4-1
last1=dayiwant[leng4]
emp=''
eleofb='kkk'
non=0
numc=[]
jf=0
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
		z=a[3].upper()
		timing=['Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner']
		

		for dose in timing:
			add1=''
			for dose1 in dose:
		 	   if dose1.isupper():
		  	      add1=add1+dose1
		tab=['CARDACE 2.5','CARCA 3.125','FRUSELAC   ','LANOXIAN 0.25mg',		'ELTROXIN 100mcg','STORVAS 20mg','T Lodoz 2.	5','Hifenac-D   ','Orpenem ER 300mg','Remetor CV 10mg','Embeta-TM 25mg','Geminor 	M1 ','Razo-D(dr.reddy LTD)','Tide plus 10mg','Jamension B12 1200mg',	'Formule forte']  	    
		        

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
		        		q=q[tabnumber]	##
		        		p=p[tabnumber]	##
		        
		        	if q=='nt':
		        		q=''
		        	if p=='nt':
		        		p=''	 
		        	w=7*d
		        	m=30*d
		        	if let=='LA':
		        		w=5*d
		        		m=10
		        	
		        if jf==0 and msg==let and z==zem :
		        	if eleofb=='t' or eleofb=='T':
		        		non=d
		        	elif eleofb=='d' or eleofb=='D':
		        		non=1
		        	elif eleofb=='s' or eleofb=='S':
		        		non=d/s
		        if n==-1 and jf==0 and msg==let and z==zem :
		      
		        	c=0
		      
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
		print('')
		total.append(tamt)
		print(tabwant)
		
		
		
	
		
	
		continue
	continue
dis=float(input('					DISCOUNT	= '))

dpri =nowtot*(dis/100)

final=nowtot-dpri
print('					Discount MRP	=',final)
				
