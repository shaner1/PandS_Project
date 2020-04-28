import matplotlib.pyplot as plt
import pandas as pd

#get pandas to read in the csv file
iris = pd.read_csv("iris.csv")

#The first column of the dataset is "Id" which isnt a variable and makes    
# the summary look messy so I delete it by using del 
del iris['Id']

#creating a variable called summary. Summary is a string containing the output from the describe() function
summary = str(iris.describe())

#open a text file called test and set it to write
with open('test.txt', 'w') as test:
    #then write the contents of summary to this file 
    test.write(summary)
