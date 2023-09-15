

#how to find cordinates iof intersection lines 



import numpy as jk
from matplotlib import pyplot as plt
import math

lw_rng=-7		#x values take from these range
hg_rng=9	#	change y_limt also
n=1				# also depend on max y value x=-1,1  y=-100,100	-->n=100
#down value always an +ve integer
spc_ech_val=(hg_rng-lw_rng+1)*1000 // 1	#no.of values x takes (hg_rng-lw_rng+1)=all values differe is 1 

#these are x-intercept point, for findind area between these 2 points
low_poi,hg_poi=3,7
	

x_lim=(lw_rng*1.5,hg_rng*1.5)	#x-axis units range between
#y_lim=(-1*1.59,1*1.59)				#limit for sines , cosines
y_lim=(((lw_rng*1.5)*1.59)*n,((hg_rng*1.5)*1.59)*n)	#(1.59) is multiplied to get y axis same length units when 'FIRETABLET' vertically placed



#FROM HERE ALL ARE CONSTANTS NO NEED TO CHANGE VALUE )except :- y equation)


plt.xlim(x_lim)
plt.ylim(y_lim)	#(1.59) is multiplied to get y axis same length units when 'FIRETABLET' vertically placed



def x_y_lin_quad_plot(x_lm,y_lm):
	plt.plot((x_lm[0],x_lm[1]),[0,0],'k')	#y co-ordinate =[0,0]	
	plt.plot([0,0],(y_lm[0],y_lm[1]),'k')
x_y_lin_quad_plot(x_lim,y_lim)


def y_equ(x):					#you can also change this 'y' to any equation
	#write ur equation
	#y=math.cos((x*math.pi)/180)
	y=math.sqrt(abs((-x+3)*(x-7)))
	#y=x**2
	return y


def find_area_under(x_cor,y_cor):
	
	x_width=x_cor[1]  -  x_cor[0]
	sum_height=0
	for i in range(len(y_cor)):
 		if low_poi <= x_cor[i] <= hg_poi:
 			sum_height=sum_height + y_cor[i]
	area=sum_height*x_width
	return area

def equ_plot():
	x=jk.linspace(lw_rng,hg_rng,spc_ech_val)
	y=[]
	for i in x:
		y.append(y_equ(i))
	u=find_area_under(x,y)
	plt.text(0,0,'{}'.format(u))
	plt.plot(x,y)
equ_plot()

#graph process proceeds from here on wards


plt.show()