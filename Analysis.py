
#The purpose of this program is to help analysis of the iris data set. 
# This program will read in the data set, write a summary to a text, output histograms of each variable and output a scatter plot of each pair pf variables

#import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#The first part of this project will read in the data set and output a summary to a text file.

# Reading in the data set and assign it to a variable called iris
iris = pd.read_csv("iris.csv")

#The first column of the dataset is "Id" which isnt a variable and makes    
# the summary look messy so I delete it by using del 
del iris['Id']

#creating a variable called summary. Summary is a string containing the output from the describe() function
summary = str(iris.describe())

with open('Summary.txt', 'w') as text:
    #then write the contents of summary to this file 
      text.writelines("\nThis is a summary of the variables in the iris dataset: \n")
      text.write("\n")
      text.write(summary)

#The section of the project will output a histogram for each variable of the data set

#plot a histogram of Sepal Length. It should be orientated horizontally, coloured green 
# and have a label of Sepal Length 

#grouping each flower type under a variable
setosa = iris.loc[iris['Species'] == 'Iris-setosa']

versicolor =  iris.loc[iris['Species'] == 'Iris-versicolor']

virginica =  iris.loc[iris['Species'] == 'Iris-virginica']

#creating a histogram by flower characteristic
#each histogram is 3 histogram (1 for each flower type) overlayed ontop of each other

#Create a histogram for Sepal Length
plt.hist(setosa['SepalLengthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['SepalLengthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['SepalLengthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Sepal_Length_CM')
plt.ylabel('Frequency')
plt.title('Sepal_Length')
plt.legend()

#save the plot as a png to the current folder 
plt.savefig("Sepal_Length_Hist.png")
#close out the histogram so the next histograms are not built ontop of each other 
plt.close()

#Create a histogram for Sepal Width
plt.hist(setosa['SepalWidthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['SepalWidthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['SepalWidthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Sepal_Width_CM')
plt.ylabel('Frequency')
plt.title('Sepal_Width')
plt.legend() 
plt.savefig("Sepal_Width_Hist.png")
plt.close()

#Create a histogram for Petal Length
plt.hist(setosa['PetalLengthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['PetalLengthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['PetalLengthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Petal_Length_CM')
plt.ylabel('Frequency')
plt.title('Petal_Length')
plt.legend()
plt.savefig("Petal_Length_Hist.png")
plt.close()

#Create a histogram for Petal Length
plt.hist(setosa['PetalWidthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['PetalWidthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['PetalWidthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Petal_Width_CM')
plt.ylabel('Frequency')
plt.title('Petal_Width')
plt.legend()
plt.savefig("Petal_Width_Hist.png")
plt.close()

#The section of the project will output a scatter plot for each pair of variables of the data set

#Use seaborn to create a matrix of scatter plots. Each specie of flower with have a different colour assigned
sns.pairplot(iris, hue="Species", diag_kind="kde")
plt.show()

#Feedback to let the user know the program has finished
print("Program is finished")