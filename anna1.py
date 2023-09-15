index=[]
input=int(input('enter the N='))
a=['H','T']
ourget=''
exp=(2**input)
brac=[]
bin=[]
for i in range(0,exp):
	num=i
	div=2

	binnum=''
	while div>0:
		rem=num%2
		rem=str(rem)
		div=num//2
		num=div
		binnum=rem+binnum
	
	while len(binnum)<input:
		binnum='0'+binnum
	print(binnum)
	bin.append(binnum)
print(bin)	
if 1<=input<=(10**5):
	for j in bin:
		ourbrac=''
		for z in j:
			z=int(z)
			ourbrac=ourbrac+a[z]
		brac.append(ourbrac)
		print(ourbrac)
print(brac)