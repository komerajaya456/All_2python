#we can create our own function by def()

def function():
	print('hi')
	print('there')
function()

print('')
print('')
def add(y):
	print(y+2)		#also use like(y+'hi') give y='steve'
add(2)				#here y is argument
add(4)

print('')
print('')
def add1(y):
	print(y+2)
	print(y*2)
	print(y/3)
add1(2)

print('')
print('')
def twoargs(x,y):		#using 2 argument's'
	
	print(x+'arguments'+y)
	if x==y:
		print('kkkkkkkkkkk')
twoargs('1st','1st')


print('')
print('')
password = input()
repeat = input()
def validate(text1, text2):
	if text1==text2:
		print('correct')
	else:
		print('wrong')
validate(password,repeat)

print('')
print('')

