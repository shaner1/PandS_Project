import matplotlib.pyplot as plt
import pandas as pd

#get pandas to read in the csv file
iris = pd.read_csv("iris.csv")

#The first column of the dataset is "Id" which isnt a variable and makes    
# the summary look messy so I delete it by using del 
del iris['Id']


summary = str(iris.describe())

#open a text file called test and set it to write
with open('test.txt', 'w') as test:
    #then write the contents of summary to this file 
      test.writelines("\nThis is a summary of the variables in the iris dataset: \n")
      test.write(summary)
        
test.close()