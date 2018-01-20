#Read in the data form the seven files "monday.csv" to "friday.csv" into numpy arrays. Calculate the max, min and average of each data column for each day.
#Skip the 1st column for numpy, also the headers

#to access more than one file, start with:
#import glob

import numpy as np
import matplotlib.pyplot as pl
import math
import glob
alldays = glob.glob("*day.csv") #use global variable to read all files at once

max_data = np.zeros([7,4]) #declare to find the max of each column of each day
min_data = np.zeros([7,4]) #declare fo find the min of each column of each day
mean_data = np.zeros([7,4]) #declare to find the mean of each column of each day

counter1 = 0
counter2 = 0

for filename in alldays:
	dataarray = np.loadtxt(filename, delimiter = ",", skiprows = 1, usecols = (1,2,3,4))
	transpose_data = np.transpose(dataarray) #transpose data to read from top to bottom
	#print(dataarray)
	counter2 = 0
	for cols in transpose_data:
		print(max_data)
		#print(cols)
		max_data[counter1][counter2] = np.amax(cols)
		min_data[counter1][counter2] = np.min(cols)
		mean_data[counter1][counter2] = np.mean(cols)
		counter2 = counter2 +1
	counter1 = counter1 +1

print(max_data)
print(min_data)
print(mean_data)

days = np.linspace(0,6,7)
print(days)

pl.subplot(2,2,1) #to determine how far apart the subplots are from one another
pl.plot(days,max_data[:,0], "r--*") #plotting the data with red "r" line
pl.plot(days,min_data[:,0], "g--*")
pl.plot(days,mean_data[:,0], "y--*")
pl.xlabel("Time ($days$)") #display the x-axis in symbol form
pl.ylabel("Temperature (${}^0C$)") #display the y-axis in symbol form
pl.legend(["max","min","mean"])
pl.title("Graph of Time vs. Temperature")#creating a title for the graph

pl.subplot(2,2,2) #to determine how far apart the subplots are from one another
pl.plot(days,max_data[:,1], "r--*") #plotting the data with red "r" line
pl.plot(days,min_data[:,1], "g--*")
pl.plot(days,mean_data[:,1], "y--*")
pl.xlabel("Time ($days$)") #display the x-axis in symbol form
pl.ylabel("Pressure ($Bar$)") #display the y-axis in symbol form
pl.legend(["max","min","mean"])
pl.ylim(ymax = 1.5, ymin = 0) #setting the max-reach value on the x-axis
pl.title("Graph of Time vs. Pressure")#creating a title for the graph

pl.subplot(2,2,3) #to determine how far apart the subplots are from one another
pl.plot(days,max_data[:,2], "r--*") #plotting the data with red "r" line
pl.plot(days,min_data[:,2], "g--*")
pl.plot(days,mean_data[:,2], "y--*")
pl.xlabel("Time ($days$)") #display the x-axis in symbol form
pl.ylabel("Windspeed ($knots$)") #display the y-axis in symbol form
pl.legend(["max","min","mean"])
pl.ylim(ymax = 23, ymin = -2) #setting the max-reach value on the x-axis
pl.title("Graph of Time vs. Windspeed")#creating a title for the graph

pl.subplot(2,2,4) #to determine how far apart the subplots are from one another
pl.plot(days,max_data[:,3], "r--*") #plotting the data with red "r" line
pl.plot(days,min_data[:,3], "g--*")
pl.plot(days,mean_data[:,3], "y--*")
pl.xlabel("Time ($days$)") #display the x-axis in symbol form
pl.ylabel("Wind direction") #display the y-axis in symbol form
pl.legend(["max","min","mean"])
pl.ylim(ymax = 410, ymin = 150) #setting the max-reach value on the x-axis
pl.title("Graph of Time vs. Wind direction")#creating a title for the graph


pl.show()

#-------------------------------------------------------------------------
#this will do as above + show columns 1,2,3,4

#np.mean(dataarray2[:,0]) #will give the average of the data (which is )
#np.std(dataarray2[:,0]) #gives the standard derivation ()


#np.median(dataarray2[:,0]) #median value ()


#help(np.savetxt) #help function of how to save a text file

#Now press CTRL-D to open directory in which the txt file is saved in
#np.savetxt("cols23", dataarray2, delimiter = ",") #reading of column23
#-------------------------------------------------------------------------
