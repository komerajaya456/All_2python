a=(float(input('1)no.of qty of CARDACE2.5: ')))
crd2=5.20
A=crd2*a
arx1=5.5553
AA=arx1*a
print(a)
print(' cost of each tablet=',crd2) 
print(' the total amt for [',str(a)+ '] CARDACE2.5=',A)
print(' cost in ind.pvt.ltd=',arx1)

b=(float(input('''
2)no.of qty of CARCA3.125: ''')))
cac3=2.94
B=cac3*b
arx2=3.5
AB=arx2*b
print(b)
print(' cost of each tablet=',cac3) 
print(' the total amt for [',str(b)+ '] CARCA3.125=',B)
print(' cost in ind.pvt.ltd=',arx2)

c=(float(input('''
3)no.of qty of FRUSELAC: ''')))
fsl=3.50
C=fsl*c
arx3=4.665
AC=arx3*c
print(c)
print(' cost of each tablet=',fsl) 
print(' the total amt for [',str(c)+ '] FRUSELAC=',C)
print(' cost in ind.pvt.ltd=',arx3)

d=(float(input('''
4)no.of qty of LANOXIN0.25mg: ''')))
lnx=1.20
D=lnx*d
arx4=1.318
AD=arx4*d
print(d)
print(' cost of each tablet=',lnx) 
print(' the total amt for [',str(d)+ '] FRUSELAC=',D)
print(' cost in ind.pvt.ltd=',arx4)

e=(float(input('''
5)no.of qty of STORVAS20mg: ''')))
srv2=13.516
E=srv2*e
arx5=14.834
AE=arx5*e
print(e)
print(' cost of each tablet=',srv2) 
print(' the total amt for [',str(e)+ '] STORVAS20mg=',E)
print(' cost in ind.pvt.ltd=',arx5)

f=(float(input('''
6)no.of qty of LODOZ2.5mg: ''')))
ldz2=6.856
F=ldz2*f
arx6=8.067
AF=arx6*f
print(f)
print(' cost of each tablet=',ldz2) 
print(' the total amt for [',str(f)+ '] LODOZ2.5mg=',F)
print(' cost in ind.pvt.ltd=',arx6)

g=(float(input('''
7)no.of qty of ELTROXIN100mg: ''')))
eltx=125
G=eltx*g
arx7=159.45
AG=arx7*g
print(g)
print(' cost of each tablet=',eltx) 
print(' the total amt for [',str(g)+ '] ELTROXIN100mg=',G)
print(' cost in ind.pvt.ltd=',arx7)
ind=AA+AB+AC+AD+AE+AF+AG

print('''
tot amt=''',str(A)+'''+''',str(B)+'''+''',str(C)+'''+''',str(D)+'''+''',str(E)+'''+''',str(F)+'''+''',str(G)+'''=''',A+B+C+D+E+F+G)

print('ind.pvt=',str(AA)+'+',str(AB)+'+',str(AC)+'+',str(AD)+'+',str(AE)+'+',str(AF)+'+',str(AG)+'=',ind)
D1=ind*15                           #-----------------------------dis
D2=D1/100
dis=ind-D2 
print('ind discount price=',dis)

print('''
	
	               THANK YOU FOR SHOPPING''')
#1) CARDACE2.5
#2) CARCA3.125 
#3) FRUSELAC
#4)	LANOXIN0.25mg               
#5)	STORVAS20mg       
#6) LODOZ2.5mg	             
#7) ELTROXIN100mg
