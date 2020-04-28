#import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd     

#set panda to read in the iris dataset and contain it in a dataframe called iris
iris = pd.read_csv("iris.csv") 

#plot a histogram of Sepal Length. It should be orientated horizontally, coloured green 
# and have a label of Sepal Length    
plt.hist(iris['SepalLengthCm'], orientation='horizontal', color= 'Green', label= 'Sepal_Length')   

#save the plot as a png to the current folder 
plt.savefig("Sepal_Length_Hist.png")
