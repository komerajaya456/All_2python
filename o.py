d=input()
f=1
g=[]
o=[]
alp='abcdefghijklmnopqrstuvwxyz'
for i in d:
	for j in alp:
		if i==j:
			print(i)
			b=d.find(i)
			print(b)
			e=d[ :b]
			print(e)
			g.append(e)
			h=map(float,g)
			l=list(h)
			f=l[0]
			m=d[b: ]
			print(m)
			for ij in m:
				if ij.isnumeric() or ij=='.':
					print('hi',ij)
					o.append(ij)
					for jk in o:
						print(jk)
						
			
			