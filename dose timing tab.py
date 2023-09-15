timing=['Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner']
yoo=['ab','bl']

for dose in timing:
		add1=''
		for dose1 in dose:
		    if dose1.isupper():
		        add1=add1+dose1
		        print(add1)()
		        if add1==yoo[0].lower():
		            print(dose)
		        
		