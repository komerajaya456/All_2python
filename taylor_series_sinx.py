import math as mt

def sin_x_val(deg):
	z=77
	sum=0
	asum='a'
	radian_vl=(deg*(mt.pi))/180
	for i in range(0,z*2):
		if i%2!=0:
			if asum=='a':
				sum=sum+(radian_vl**i)/(mt.factorial(i))
				asum=''
			else:
				sum=sum-(radian_vl**i)/(mt.factorial(i))
				asum='a'
	return sum





#print(mt.factorial(4))
print(sin_x_val(45))
for i in range(0,90):
	print(mt.sin((i*mt.pi)/180),(sin_x_val(i)))