d=input()
f=1
a=1
g=[]
o=[]
qi=[]
alp='abcdefghijklmnopqrstuvwxyz'
for i in d:
	for j in alp:
		if i==j:
			b=d.find(i)
			if d[ :b]=='':
				f=1
				t=i
			else:
				e=d[ :b]
				g.append(e)
				h=map(float,g)
				l=list(h)
				t=i
				f=l[0]
m=d[b: ]
for ij in m:
				if ij.isnumeric() or ij=='.':
					o.append(ij)
					ui=len(o)
					emp=''
					count=-1
					for jk in o:
						emp=o[count]+emp
						count=count-1
qi.append(emp)
yute=map(float,qi)
yuti=list(yute)
a=yuti[0]
c=1
z=1
p=1
while True:
	if z==1:
		p=a-1
		r=a*f
		print('\n\nDifferentiation of (',f,t,'^',a,')       =',r,'(',t,')^',p)
	while p==1and input('''do want to differentiate again:
	if YES press ENTER
	if NO press SPACEBAR''')=='': 
		print('\n\nDifferentiation of (',r,'(',t,')^',p,'  =',  r)
		a=a
		p=p*0
		break
	if input('''do want to differentiate again:
	if YES press ENTER
	if NO press SPACEBAR''')==' ' and p!=1:
		
		break	
	z=z+1
	print('\n\nDifferentiation of (',r,'(',t,')^',p,'  =',r*p,'(',t,')^',p-1)
	r=r*p
	p=p-1


	continue

						
						
