x=float(input('x='))
y=float(input('y='))
h=float(input('h='))
c=float(input('for what value of (x) we need to find (y)='))
y_=(x)-((y)**2)								#change
y0=(y)+(h*y_)
y1=7
j=c-h
x1=0
while x<=j:
	if True:
		print('x=',x)

		y_=(x)-((y)**2)				#change
		y_=round(y_,4)
		y0=(y)+(h*y_)
		y0=round(y0,4)
		while True:
			if True:
				while True:
					x1=h+x
					x1=round(x1,3)
					print('x1=',x1)
					z=(x1)-((y0)**2)							#x=x1,y=y0
					y1=(y)+((h/2)*(y_+z))
					y1=round(y1,4)
					if y1==y0:
						break
					y0=y1
					continue		
			print('y1=',y1)
			print(y0,y1)
			
				
			if True:
					break
		
				
			continue
		x=h+x
		x=round(x,3)
		y=y1			
		continue

			