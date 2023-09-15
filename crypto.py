a='abcdefghijklmnopqrstuvwxyz'
b=input()
c=int(input('enter the key='))
h=''
for i in b:
	loc=a.find(i)
	alploc=loc+c
	if i in a:
		if alploc>25:
			alploc=alploc-26
		h=h+a[alploc]
	else:
		h=h+i
	
	print(i,loc,h)
print(h)