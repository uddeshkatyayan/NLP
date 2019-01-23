import numpy as np
import csv
import re

def CountFrequency(my_list):
    freq={}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print freq
    # freq = {key:len(list(group)) for key, group in groupby(np.sort(data))}
    # print freq


if __name__ == "__main__":
    with open('data.csv') as myFile:
    	reader = csv.DictReader(myFile)
    	#print(type(reader))
    	bigls=[]
    	for row in reader:
    		local_string=row['labels']
    		rege=r"[()#]+"
    		ls=re.split(rege,local_string)
    		while(" " in ls) :
    			ls.remove(" ")
    		ls.remove("")
    		ls.pop()
    		bigls+=ls
        print(bigls)
        if "male" in bigls:
            print("hjavsjxvvxyvayx\n")
        CountFrequency(bigls)
