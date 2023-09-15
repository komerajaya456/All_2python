a=[1,2,3,4,5]
del a[4]						#delete
print(a)
a.remove(3)				#remove( use location a[1],   'item name')
print(a)
a.pop(1)
print(a)
print()
'''{lis1=['hello','komera','jaya','krishna']
x1,y1,z1=lis1					#x,y assing to 3rd will assing remaining all elements
print(x1,y1,z1)'''

lis=['hello','krishna','jaya']
x,y,z=lis			#assign as three
print(z,*y,x)

vhi=2.3
rhi=3
che=isinstance(vhi,float)				#check whether float,int,alphabet
che1=not isinstance(vhi,float)
che12=isinstance(rhi,int)
print(che,che1,che12)

print('')
print('he\'s like me')			#\used if there is (')
print('a\nb\nc')					#'\n' used to new line
print('this is \t tab space')#'\t' used to tab space

print('')
word=['hi','there']				#insert
index=1
word.insert(index,'added insert')
print(word)

print('')
ind=['card','thi','ytha','thi']		#index
print(ind.index('thi'))
print(max(ind))							#last term of ind
print(min(ind))							#1st term
print(ind.count('thi'))				#count how many of ' thi '  in list
print(ind.reverse())

print('')
print('')
az=1
print(complex(az),'kkkkkk')

print('')
print('')
tuple1=('apple','banana','mango')				#tuple as same as list lightly
print(tuple1)
print(len(tuple1))
print(tuple1.index('apple'))

print('')
print('')
tuple2=('apple','banana','mango','kiwi')		#tuple doesn't support to assigh or append
tuple2=list(tuple2)									#so we convert as list from tuple
tuple2[2]='custard apple'					
print(tuple2)

print('')
print('')
tuple3=('apple','banana','mango','kiwi')
add_to_tuple3=('orange','cheery')
tuple3+=add_to_tuple3
print(tuple3)

print('')
print('')
tuple4=('apple','banana','mango','cheery')
tuple4=list(tuple4)
tuple4.remove(tuple4[1])					#remove( use location a[1],   'item name')
tuple4.remove('apple')
print(tuple4)

print('')
print('')
tuple5=('apple','banana','mango','cheery')
tuple5=list(tuple5)
del tuple5[1: ]					#when using del we should convert as list
print(tuple5)

print('')
print('')
tuple6=('apple','banana','coconut green')
red,yellow,green=tuple6
print(red)
print(yellow)
print(green)

print('')
print('')
tuple7=('apple','banana','coconut green','fig')
red,*yellow,green=tuple7			# '*'  it will display all the remaning elements upto green element
print(red)										# '*' (asterisk)
print(yellow)
print(green)

print('')
print('')
tuple8=('apple','banana','coconut green','pomegranate')
for tup8 in range(len(tuple8)):
	print(tuple8[tup8])
	
print('')
print('')
tuple9=('a','b','c')
tuple10=(1,2,3)
add_tup_9_10=tuple10+tuple9
print(add_tup_9_10)

print('')
print('')
tuple11=(1,2,3,4)
for tup11 in range(len(tuple11)):
	if tup11==3:
		print('tup11	3')
		break
else:
	print('tuple11 for else') 




print('')
print('')
check='thzis is how it works'
print('z' in check)				#check wheather letter present or not in a word or not
check1=['r','d','o',2]
print('o' in check1)
print('z' not in check1)

print('')
print('')
af='hello world'					#split the space with ' , ' 
print(af)
print(af.split())




print('')
print('')
a='      hello world    '			#remove extra spaces at start and end
print(a.strip())
print(a)



print('')
b=['hello','komera']
b[0]='g'							#changing
print(b)
b[-1]='z'
print(b)

c=[1,2,3]
c=c+[4,5,6]					#adding list
print(c )

d=['a']
d=5*d							#multiple the list
print(d)

e=[1,2,3,4,5,6]			
print(e[1:-1])

f=[[1,2],[3,4],[5,6],[7,8]]
print(f[0])
print(f[2][0])					#sub divided used in matrices


g='hello me'
h=g.replace(g[0],'z')			#replace
print(h)
print(h.replace('me','world'))

i='hello'
print(i[-1::-1])    					#reverse the list

j=[1,2,3]
k='{1}{1}{2}'.format(j[0],j[1],j[2])		#arrange in format
print(k)

l='{x}+{y}'.format(x=5,y=6)
print(l)

m='there'														#there will add in b\t words
print(m.join(['hello',' spam',' world']))

print('')
n='My ,name, is krishna'
print(n.startswith('my'))
print(n.endswith('krishna'))				#name ending and starting with true or false
print(n.upper())									#upper and lower case of sentence									
print(n.lower())
print(n.split('hi'))									#split the words,	opposite of join


def func():								#print when ever u need y creating own
	print('jai')
	print('jai')
	print('jai')
func()

def mul():									#we can print multiple times
	print('krish')
mul()
mul()	
mul()	

print('')
def addingword(sen):				#we cn any word we want
	print(sen+'@')
addingword('hi')
addingword('komera')

def num(num):					#we can also add input()
	print(num*3)
num(3)
	
print('')									#we can use 2,3..., numbers or string by uUSING ' , '
def twice(x,y):
	print(x+y)
	print(x*y)
twice(3,2)
print('kkkkkkkkkk')

print('')
def max(x,y):							#return same as print,we shoould use compulsory print
	if x>=y:
		return x
	else:
		return y
print(max(4,7))
z=max(8,5)						#return value will assing ,print not
print(z)
print('end')	
	
print('')
def stops(x,y):						#after , return print will not execute
	add=x+y
	return add
	print('this will not printed ')
r=stops(3,5)
print(r )

print('')							#'''..,''' same as # (sentence not consider)  
def sou(y):
		'''hello is there								
		any one in the 1bhk 
		flat'''
		print(y+'hi')
sou('steve')


print('hi'.center(20,'['))  #add centers at end

lis3=[0,0,0]*7
print(lis3)				#print muliplt ist list
		
apo=[1,3,3,1]
print(sum(apo)) 			#prints sum of list		
				
					
						
							
								
									
											

	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	