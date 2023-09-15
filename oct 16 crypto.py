import random
alp='abcdefghijklmnopqrstuvwxyz'
givstr=input('enter the sentence:')
lensen=len(givstr)
def sentoran(a):					#conversion of sentence to random sentences
	print(a)
	a=list(a)
	for eachchar in range(0,len(a)):
		if a[eachchar] in alp: 
			a[eachchar]=random.choice(alp)
	a=''.join(a)
	print(a)
sentoran(givstr)






