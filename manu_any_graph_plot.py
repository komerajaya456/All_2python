from matplotlib import pyplot as plt
import numpy as jk
import math
x_lim=(-360,360)
scale=0.25 #diff of ech val

def y_equ(x):					
	#write ur equatio
	#use abs if sqrt of -ve
	#y=math.cos((x*math.pi)/180)

	y=x**2
	return y



def x_y_lin_quad_plot(x_lm,y_lm):
	plt.plot((x_lm[0],x_lm[1]),[0,0],'k')	#y co-ordinate =[0,0]	
	plt.plot([0,0],(y_lm[0],y_lm[1]),'k')



def equ_plot():
	x=jk.linspace(x_lim[0],x_lim[1],int(2*x_lim[1]/scale))
#	plt.text(0,0,'{}'.format(len(x)))
	y=[]
	for i in x:
		y.append(y_equ(i))
	y_max=(-1.5*max(y),1.5*max(y))
	
	x_y_lin_quad_plot(x_lim,y_max)

	plt.plot(x,y)
equ_plot()


plt.show()