#import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd     

    #set panda to read in the iris dataset and contain it in a dataframe called iris
iris = pd.read_csv("iris.csv") 

    #plot a histogram of Sepal Length. It should be orientated horizontally, coloured green 
    # and have a label of Sepal Length 

#grouping each flower type under a variable
setosa = iris.loc[iris['Species'] == 'Iris-setosa']

versicolor =  iris.loc[iris['Species'] == 'Iris-versicolor']

virginica =  iris.loc[iris['Species'] == 'Iris-virginica']

#creating a histogram by flower characteristic
#each histogram is 3 histogram (1 for each flowe type) overlayed ontop of each other
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

plt.hist(setosa['SepalWidthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['SepalWidthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['SepalWidthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Sepal_Width_CM')
plt.ylabel('Frequency')
plt.title('Sepal_Width')
plt.legend() 
plt.savefig("Sepal_Width_Hist.png")
plt.close()

plt.hist(setosa['PetalLengthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['PetalLengthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['PetalLengthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Petal_Length_CM')
plt.ylabel('Frequency')
plt.title('Petal_Length')
plt.legend()
plt.savefig("Petal_Length_Hist.png")
plt.close()

plt.hist(setosa['PetalWidthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Setosa')   
plt.hist(versicolor['PetalWidthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Versicolor')
plt.hist(virginica['PetalWidthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Virginica')
plt.xlabel('Petal_Width_CM')
plt.ylabel('Frequency')
plt.title('Petal_Width')
plt.legend()
plt.savefig("Petal_Width_Hist.png")
plt.close()