a=input()
lend=len(a)
addkin=''
for kin in a[-1::-1]:
	if not kin.isnumeric() and kin!='.':
		kinl=a.find(kin)
		for kin2 in a[kinl-lend+1::-1]:
			print(kin2)
			if kin2.isnumeric() or kin2=='.':
				addkin=kin2+addkin
				print(addkin)
				kin2l=a.find(kin2)
				del a[kin2l]
			elif not kin2.isnumeric() and kin2!='.':
				break