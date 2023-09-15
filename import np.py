import numpy as np

a=np.array([[1,2,3],[4,5,6]])		#matrice of 2x3
print(a)

num1=np.array([1,2])
num2=np.array([3,4])
num3=np.array([[0],[1]])
print('')													#mutiply do product
mul=num1@num2
print(num3[1][0])
print(num3)
print(mul+2)
print(np.dot(num1,num2))				#same as @


print('')												#multiplies each individual respectively
print(num1*num2)
print(np.multiply(num1,num2))	#same as above





