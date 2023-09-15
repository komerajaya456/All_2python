#why
#if  abcdefghi all possible outcome
#one outcome abcde
#abdgfd coming length is more than given


import time
inpt=input('Enter the all posibilities:')		#string all possibles(01,)
op=''

while True:
	if op=='came':
		break
		
	strinpt=input('Enter the any outcome:')		#first outcome(1,1)
	l=0
	for kl in strinpt:
		if kl in inpt:
			l+=1
		
		if l==len(strinpt):
			op='came'
			break
	else:
		print('It is not outcome of\'',inpt,'\' enter again')
		continue
time_start=time.time()
leninpt=len(inpt)							#length of 1st sring
lenstrinpt=len(strinpt)					#length of our 1st outcome
tot_out=leninpt**lenstrinpt			#totoal possible outcomes
our_1out=''
non_repeated_char_str=[]
def check_non_repeat_char_outcome(strout):
	str_count=0
	for char_str in strout:
		no_of_char=strout.count(char_str)
		str_count+=1
		if no_of_char>1:
			break
		elif str_count==len(strout):
			non_repeated_char_str.append(strout)


def convt_num_str(our_1out):

	our_outc=''
	for ik in our_1out:
		ik=int(ik)
		our_outc=our_outc+inpt[ik]
	print(our_outc)
	check_non_repeat_char_outcome(our_outc)
	

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
		
		if len(lis_each_char_pos)<b :
			for j in range(0,(b-len(lis_each_char_pos))):
				lis_each_char_pos=[0]+lis_each_char_pos
		print(lis_each_char_pos)
		convt_num_str(lis_each_char_pos)
		
		if 	assnum1==tot:
			print('Total outcomes     =       ',	assnum1)
				
alloutcomes(26,2)

				
alloutcomes(leninpt,lenstrinpt)  
print(non_repeated_char_str)
print(len(non_repeated_char_str))
time_end=time.time()
print(time_start,'   ',time_end)
print((time_end-time_start)*(10**6))

	