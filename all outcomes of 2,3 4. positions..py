def alloutcomes(a,b):

	tot=a**b
	for i in range(0,tot):
		
		if i<a:
			outrem=i
			outrem=str(outrem)
		else:
			outrem=''
			while i>=a:
				div=i//a
				rem=i%a
				i=div
				rem=str(rem)
				outrem=rem+outrem
				if i<a:
					div=str(div)
					outrem=div+outrem
		
		if len(outrem)<b:
			for j in range(0,(b-len(outrem))):
				outrem='0'+outrem
		print(outrem)		
alloutcomes(10,3)  