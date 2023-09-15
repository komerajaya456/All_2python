eq=input()
leng=len(eq)
asp=0
for cv in eq:
	print('eq',eq)
	if cv=='+' or cv=='-':
		pos=eq.find(cv)
	
		print(eq[asp:pos])
		eq=eq.replace(eq[pos],'')
		asp=pos+1
		
	