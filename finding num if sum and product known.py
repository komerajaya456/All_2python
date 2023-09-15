a=int(input('sum='))
b=int(input('product='))
cou=0
while cou<b:
	cou=cou+1
	rem=b%cou
	if rem==0:
		
		ano=b//cou
		sum1=ano+cou
		if sum1==a:
			def nums():
				
				print(ano,cou)
			nums()
			continue
			
