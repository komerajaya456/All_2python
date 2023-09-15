#cn is missing
import csv
import numpy as jk

 


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
 ['2023-02-14&14-00','18cpc39'
  'Constitution of India, professional ethics and cyber law'],
 ['2023-02-14&14-00','18cpc49'
  'Constitution of India, professional ethics and cyber law'],
 ['2023-02-16&14-00','18ec51'
  'technological innovation management and entrepreneurship time'],
 ['2023-02-17&9-30','18ec61','digital communication '],
 ['2023-02-17&14-00','18mat31'
  'transform calculus, fourier series and numerical techniques'],
 ['2023-02-20&14-00','18mat41'
  'complex analysis,probability and statistical methods and numerical techniques '],
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
 ['2023-03-07&9-30','18cs652'
  'introduction to data structures and algorithms '],
 ['2023-03-07&9-30','18cs653','programming in java'],
 ['2023-03-07&9-30','18cs654','introduction to operating systems '],
 ['2023-03-07&9-30','18cs655','data mining and data warehousing '],
 ['2023-03-07&14-00','18ec35','computer organisation and architecture '],
 ['2023-03-08&14-00','18ec45','signals and systems '],
 ['2023-03-09&14-00','18ec36','power electronics and instrumentation '],
 ['2023-03-09&14-00','18ec56','verilog hdl'],
 ['2023-03-13&14-00','18ec46','microcontrollers ']]

arr1=jk.array(arr,object)
print(type(arr1))
'''

#write your all subject codes only will full subject code with qoutes


your_unarg_timetbl=jk.array()
your_subject_codes=[	]


sub_code=sub_code.lower()

print(sub_code)