
def alloutcomes(a,b):
	tot=a**b
	assnum1=0
	for i in range(0,tot):
		assnum1+=1
		lis_each_char_pos=[]
		if i<a:
			lis_each_char_pos.append(i)
			
		else:
			
			while i>=a:
				div=i//a
				rem=i%a
				i=div
				
				lis_each_char_pos=[rem]+lis_each_char_pos
				if i<a:
					
					lis_each_char_pos=[div]+lis_each_char_pos
		
		if len(lis_each_char_pos)<b and input()=='k':
			for j in range(0,(b-len(lis_each_char_pos))):
				lis_each_char_pos=[0]+lis_each_char_pos
		print(lis_each_char_pos)
		
		if 	assnum1==tot:
			print('Total outcomes     =       ',	assnum1)
				
alloutcomes(26,2)