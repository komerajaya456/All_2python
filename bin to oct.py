a=input()
leng=len(a)
img=''
b=-3
we=[]
while -1<leng:
	if (leng-3)<0:
		tree=a[ :leng]
		leng=(leng-3)	
	else:
		tree=a[(leng-3):leng]
		leng=(leng-3)
	print('tree',tree)
	list='komeras'
	cou=-6
	oct=0
	for j in list:
		num=7
		
		num=num+cou
		print('num',num)
		s=''
		while 0<num:
			rmdr=num%2
	
			rmdr=str(rmdr)
			s=rmdr+s
			
			lengh=len(s)
			num=num//2
			jk='0'+s
			kj='00'+s
		oct=oct+1
		cou=cou+1
		if s==tree or jk==tree or kj==tree :
			oct=str(oct)
			oct=oct+img
			print('heloo',oct)
			
			we.append(oct)
			
			break
	continue

we=we[-1::-1]
sr=''
for kh in we:
	print('hell',kh)
	
	
	
