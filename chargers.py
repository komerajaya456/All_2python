
a=[450,650,250,200]


count=0
while count<=11:
	s=0
	c=0
	count=count+1
	
	for i in a:
		for j in a:
			if i==450 and (j!=450) and count==1:
				s=j+c
				c=s
				sum1=s+i,'[3ports],[3usb,TypeC]'
				
			elif i==450 and (j==650 or j==250) and count==2:
				s=j+c
				c=s
				sum2=s+i,'[3ports],[2usb,TypeC]'
				
			elif i==450 and (j==650 or j==200) and count==3:
				s=j+c
				c=s
				sum3=s+i,'[3ports],[2usb]'
				
			elif i==450 and (j==250 or j==200) and count==4:
				s=j+c
				c=s
				sum4=s+i,'[1ports],[3usb,TypeC]'
				
			elif i==650 and (j==250 or j==200) and count==5:
				s=j+c
				c=s
				sum5=s+i,'[2ports],[2usb,TypeC]'
			
			
			elif i==450 and (j==650)  and count==6:
				s=j+c
				c=s
				sum6=s+i,'[3ports],[1usb]'
				
			elif i==450 and (j==250)  and count==7:
				s=j+c
				c=s
				sum7=s+i,'[1ports],[2usb,TypeC]'
			
			elif i==450 and (j==200)  and count==8:
				s=j+c
				c=s
				sum8=s+i,'[1ports],[2usb]'
				
			elif i==650 and (j==250)  and count==9:
				s=j+c
				c=s
				sum9=s+i,'[2ports],[1usb,TypeC]'
						
			elif i==650 and (j==200)  and count==10:
				s=j+c
				c=s
				sum10=s+i,'[2ports],[1usb]'
						
			elif i==250 and (j==200)  and count==11:
				s=j+c
				c=s
				sum11=s+i,'[2usb,TypeC]'
					
				
	continue
print('charger+cable	dual charger	usb,type-C(cable)	usb(cable)	=',sum1)
print('')	
print('charger+cable	dual charger	usb,type-C(cable)	--------	=',sum2)
print('')
print('charger+cable	dual charger	----------------	usb(cable)	=',sum3)
print('')	
print('------------	dual charger	usb,type-C(cable)	usb(cable)	=',sum5)
print('')
print('charger+cable	dual charger	-----------------	------------	=',sum6)
print('')		
print('charger+cable	-------------	usb,type-C(cable)	usb(cable)	=',sum4)
print('')
print('-------------	dual charger	usb,type-C(cable)	-------------	=',sum9)
print('')	
print('-------------	dual charger	----------------	usb(cable)	=',sum10)
print('')	
print('charger+cable	-------------	usb,type-C(cable)	------------	=',sum7)
print('')	
print('charger+cable	------------	-------------------	usb(cable)	=',sum8)
print('')	


print('--------------	-------------	usb,type-C(cable)	usb(cable)	=',sum11)
print('')	

