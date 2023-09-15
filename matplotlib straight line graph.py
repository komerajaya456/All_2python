#CPN(COPY,PASTE IN ,NEW)


from matplotlib import pyplot as plt
from matplotlib import style 


a=[1,2,3]
b=[10,20,30]


plt.plot(a,b,'g',label="current",linewidth=6) 	#label for legend, 'g' is color 
plt.title("testing")

plt.ylabel("per%")
plt.xlabel("year")


plt.legend()
plt.grid(True,color='k')


plt.show()

