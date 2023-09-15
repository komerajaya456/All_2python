#	NOTE:	please copy and paste this in another new to RUN

import numpy as np

a=np.array([[1,2,3],[4,5,6]])		#matrice of 2x3
print(1,a)
print('')
print(a.shape)							#shape mxn
print('')
print(a.size)								#size no of elements
print('')
prit(type(a))								#type of array 

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

ar1=np.array([[1,2]])
ar2=np.array([[1],[2]])						#subtraction of matrices
print(np.subtract(ar1,ar2))
print(np.subtract(ar2,ar1))

print(num1+2)
b=np.array([1,2,3])
print('')
print(a+b)								#sumation

div=np.divide(a,b)
print('')
print(div)
print(a/b)							#division in float
print(np.divide([2,4,6],2))
print(np.floor_divide([2,4,5],2))  	#division for only integer

print('')
print(np.math.sqrt(10))					#squareroot

print('')
print(np.random.standard_normal((3,4)))		#3,4 (rows,coloums)

print('')
ld=np.random.uniform(1,12,(2,3))				#float			
print(ld)

print('')
print(np.random.randint(1,50,(2,3)))		#integer  (1-50)b/t 2,3 r&c

print('')
print(np.random.random(1,50,(2,3))


print('')
print(np.zeros((3,4)))						#zero matrice

print('')
print(np.ones((3,4)))						#ones matrice

print('')
ud=np.random.randint(1,50,(3,4))			#1,50 random 3X4
trfa=np.logical_and(ud>30,ud<50)			#if b/t 30,50,, it prints true
print(ud)
print(trfa)


print('')
print(ud[trfa])

print('')
list=np.array([1,2,3,3,4,5,6])
print(np.mean(list))						#mean
print(np.median(list))			#median middle value
print(np.var(list))						#variance  
print(np.std(list))					#standard deviation