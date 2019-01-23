import csv  
import re

with open('audio.csv') as myFile:  
	reader = csv.DictReader(myFile)
	print(type(reader))
	bigls=[]
	for row in reader:
		local_string=row['labels']
		local_string=local_string.replace(" ","")
		#print(local_string)
		rege=r"[()#]+"
		ls=re.split(rege,local_string)
		while("" in ls) : 
			ls.remove("")
		bigls+=ls
	print(bigls)	

	