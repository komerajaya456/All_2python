x=float(input('Enter the value of X0='))
y=float(input('Enter the value of Y0='))
h=float(input('h='))
c=float(input('for what value of (x) we need to find (y)='))
y_=(x)-(y**2)							#change
y0=(y)+(h*y_)

j=c-h
x1=0
j=round(j,4)

while x<=j:
	if True:

		y_=(x)-(y**2)				#change
		y_=round(y_,4)
		y0=(y)+(h*y_)
		y0=round(y0,4)
		
		while True:
			if True:
				while True:
					x1=h+x
					x1=round(x1,4)
					
					z=(x1)-(y0**2)						#x=x1,y=y0
					z=round(z,4)
					y1=(y)+((h/2)*(y_+z))
					y1=round(y1,4)
					print(y1)
					if y1==y0:
						break
					y0=y1
					continue
			print('\nx1=',x1)			
			print('y1(',str(x1)+')=',y1)
			
				
			if True:
					break
		
				
			continue
		x=h+x
		x=round(x,4)
		y=y1			
		
		continue

			