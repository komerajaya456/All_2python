val3=0
b=input()
o=[]
for ike in b:
	
	if ike.isnumeric() or ike=='.':
		o.append(ike)
		ui=len(o)
		emp=''	
		count=-1
		for jk in o:
			emp=o[count]+emp
			count=count-1
print(float(emp)+2)
	