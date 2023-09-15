

def daysconverter(dayiwant):
	df=dayiwant
	dv=dayiwant
	finlnum=0
	locva1=0
	lend1=len(dayiwant)
	numday=0
	for zic in dayiwant:
		if zic!='.' and not zic.isnumeric():
			print(zic)
			loczic=dayiwant.find(zic)
			zicele=dayiwant[ :loczic]
			ziclen=len(zicele)
			break
	while lend1>0:
	
	
		jusva=0
		for gin in dayiwant[lend1-1::-1]:
			addva=''
			lend1=len(dayiwant)
			if jusva==1 :
				break
			elif  jusva==2:
				lend1=0
				break
			elif not gin.isnumeric():
				print(gin,'gin')
				for ink1 in range(lend1):
					if dayiwant[ink1]==gin:
						locgin=ink1
			
				vala=dayiwant[locgin-1]
				if vala.isnumeric():
					for ink in range(lend1):
						if dayiwant[ink]==vala:
					
							locva=ink
				
					locvas=locva+1
				
					for vala1 in dayiwant[locva::-1] :
			
						if not vala1.isnumeric() and vala1!='.' :
							locva1=dayiwant.find(vala1)
							vala2=locva1+1
						
							numday=dayiwant[vala2:locvas]
							numday=float(numday)
							dayiwant=dayiwant.replace(dayiwant[locva1+1: ],'')
							print(numday,'nuk',gin)
							if gin=='y':
								vala1num=numday*365
							elif gin=='m':
								vala1num=numday*30
							elif gin=='w':
								vala1num=numday*7
							elif gin=='d':
								vala1num=numday
							finlnum=vala1num+finlnum
							print(finlnum)
							
							jusva=1
							break
						
						else:
						
					
						
							addva=vala1+addva
						
						
						
							if gin==zic and len(addva)==ziclen:
								addva=float(addva)
								print(addva)
								if gin=='y':
									vala1num=addva*365
								elif gin=='m':
									vala1num=addva*30
								elif gin=='w':
									vala1num=addva*7
								elif gin=='d':
									vala1num=addva
								finlnum=vala1num+finlnum
								print(finlnum)	
							
								jusva=2
								break
					
daysconverter(input())							