#arrangment of datetime in ascending order

import re
import numpy as jk
import datetime
import csv
import sys
a=sys.path
print(a)
'''
#if csv file named 'Draft_time_table.csv' has in the same folder then uncomment this by removing \'' \"'at start and end
#import from csv file to numpy 2darray
c=0 #for looping one time
fil_nam='Draft_time_table.csv'
with open(fil_nam,'r') as file:
	csv_read=(csv.reader(file))
	
	for row in csv_read:
		#print(row)
		if c==0:
			arr=jk.array([row],object)
			c+=1
			continue
		#	heading=next(csv_read)
		arr=jk.append(arr,[row],axis=0)	
#combining both data & time
for eah_row in arr:
	eah_row[0]=eah_row[0]+'&'+eah_row[1]
	
arr=jk.delete(arr,1,1)#removes time column jk.delete(arr,obj,axis)
print(arr)

'''






#if you dont have csv file then use this array as time table
		
arr=[['date&time','subject code','subject name'],
 ['2023-01-16&14-00','18ec71','computer networks '],
 ['2023-01-19&14-00','18ec72','vlsi design '],
 ['2023-01-23&14-00','18ec731','real time signals '],
 ['2023-01-23&14-00','18ec732','satellite communications '], ['2023-01-23&14-00','18ec733','digital image processing '], ['2023-01-23&14-00','18ec734','dsp algorithm and architecture '],
 ['2023-01-27&14-00','18ec741','iot and wireless sensor networks '],
 ['2023-01-27&14-00','18ec742','automotive electronics '],
 ['2023-01-27&14-00','18ec743','multimedia communication '], ['2023-01-27&14-00','18ec744','cryptography '],
 ['2023-01-27&14-00','18ec745','machine learning with python '],
 ['2023-01-31&14-00','18ec751','communication theory'],
 ['2023-01-31&14-00','18ec752','neural networks'],
 ['2023-01-31&14-00','18ec753','arm embedded systems '],
 ['2023-01-31&14-00','18ec754','digital system design using vhdl'],
 ['2023-01-31&14-00','18cs751','introduction to big data analytics '],
 ['2023-01-31&14-00','18cs752','python application programming '],
 ['2023-01-31&14-00','18cs753','introduction to artificial intelligence '],
 ['2023-01-31&14-00','18cv753','environmental protection and management '],
 ['2023-01-31&14-00','18me753','industrial safety '],
 ['2023-02-13&14-00','18civ59','environmental studies '],
 ['2023-02-14&14-00','18cpc39','Constitution of India, professional ethics and cyber law'],
 ['2023-02-14&14-00','18cpc49','Constitution of India, professional ethics and cyber law'],
 ['2023-02-16&14-00','18ec51','technological innovation management and entrepreneurship time'],
 ['2023-02-17&9-30','18ec61','digital communication '],
 ['2023-02-17&14-00','18mat31','transform calculus, fourier series and numerical techniques'],
 ['2023-02-20&14-00','18mat41','complex analysis,probability and statistical methods and numerical techniques '],
 ['2023-02-21&14-00','18ec52','digital signal processing '], ['2023-02-22&9-30','18ec62','embedded systems '],
 ['2023-02-22&14-00','18ec32','network theory '],
 ['2023-02-23&14-00','18ec42','analogue circuits '],
 ['2023-02-24&14-00','18ec53','principles of communication systems '],
 ['2023-02-27&9-30','18ec63','microwave and antennas '],
 ['2023-02-27&14-00','18ec33','electronic devices '],
 ['2023-02-28&14-00','18ec43','control systems '],
 ['2023-03-01&14-00','18ec54','information theory and coding '],
 ['2023-03-02&9-30','18ec641','operating systems '],
 ['2023-03-02&9-30','18ec642','artificial neural networks'], ['2023-03-02&9-30','18ec643','data structures using c++ (dsc++)'],
 ['2023-03-02&9-30','18ec644','digital system design using verilog'],
 ['2023-03-02&9-30','18ec645','nano electronics '],
 ['2023-03-02&9-30','18ec646','Python application programming '],
 ['2023-03-02&14-00','18ec34','digital system design '],
 ['2023-03-03&14-00','18ec44','engineering statistics and algebra '],
 ['2023-03-06&14-00','18ec55','electro magnetic waves (emw)'],
 ['2023-03-07&9-30','18ec651','signal processing '],
 ['2023-03-07&9-30','18ec652','signals and signal conditioning '],
 ['2023-03-07&9-30','18ec653','virtual instrumentation '],
 ['2023-03-07&9-30','18ec654','micro controllers '],
 ['2023-03-07&9-30','18ec655','basic vlsi design '],
 ['2023-03-07&9-30','18cs651','mobile application development '],
 ['2023-03-07&9-30','18cs652','introduction to data structures and algorithms '],
 ['2023-03-07&9-30','18cs653','programming in java'],
 ['2023-03-07&9-30','18cs654','introduction to operating systems '],
 ['2023-03-07&9-30','18cs655','data mining and data warehousing '],
 ['2023-03-07&14-00','18ec35','computer organisation and architecture '],
 ['2023-03-08&14-00','18ec45','signals and systems '],
 ['2023-03-09&14-00','18ec36','power electronics and instrumentation '],
 ['2023-03-09&14-00','18ec56','verilog hdl'],
 ['2023-03-13&14-00','18ec46','microcontrollers ']]

arr=jk.array(arr,object)
#print(arr)




#date & time format (yy : mm : dd & 24hh : m_m)

def convt_str_to_datetime(str_date_time):
	rem_char=''
	for each_num in range(0,len(str_date_time)):
		if not str_date_time[each_num].isnumeric() and not str_date_time[each_num] in rem_char:
			rem_char=rem_char+str_date_time[each_num]+'|'
		
	#print(rem_char[:-1])
	aftr_split=re.split(rem_char[:-1],str_date_time)
	if len(aftr_split[0])<4:
		aftr_split[0]='20'+aftr_split[0]
	#print(aftr_split)
	aftr_split=[int(i) for i in aftr_split if i.isnumeric()]

	#print(aftr_split)
	dic={'yy': 0,	'mm':0,	'dd':0,	'hh':0,	'm_m':0}
	for i,j in zip(dic,aftr_split):
		dic[i]=j
	
	dt_t= (datetime.datetime(dic['yy'],dic['mm'],dic['dd'],dic['hh'],dic['m_m']))
	dt_t=(dt_t.strftime('%d %b %Y '))
	
	return dt_t



#write your all subject codes only will full subject code with qoutes


your_subject_codes=['18eC56','18Ec71','18EC53','18EC72','18ec732','18eC744']

#appending subject in array in  unarraged manner

for low_eah_sub in range(0,len(your_subject_codes)):
	your_subject_codes[low_eah_sub]=your_subject_codes[low_eah_sub].lower()
print(your_subject_codes)
unarg_ur_sub_arr=jk.array([['date&time','subject code','subject name']],object)
#finding all subjects in array
for ech_sub in your_subject_codes:
	for ech_row in arr:
		if ech_row[1]==ech_sub:
			print(ech_row[1])
			print('hi')
			unarg_ur_sub_arr=jk.append(unarg_ur_sub_arr,[ech_row],axis=0)
			break
#print(unarg_ur_sub_arr)
chk=[]
for ech_row in (unarg_ur_sub_arr[1:]):
	ech_row[0]=(convt_str_to_datetime(ech_row[0]))
	chk.append(ech_row[0])
unarg_ur_sub_arr=(unarg_ur_sub_arr[1:][0])
print(unarg_ur_sub_arr[1:])
print(unarg_ur_sub_arr[:,0].argsort())

#print((unarg_ur_sub_arr[unarg_ur_sub_arr[ :, 1].argsort()]))
#chk=sorted(chk,key=lambda t: datetime.strptime(t[0], '%Y/%m/%d%H:%M:%S '))
#print(chk[:,0].argsort())
#chk=sorted(chk,key=date_key)

#unarg_ur_sub_arr=jk.concatenate((dates.reshape(len(dates),1),values))
#unarg_ur_sub_arr=jk.sort(unarg_ur_sub_arr,axis=0)
#print(unarg_ur_sub_arr)

