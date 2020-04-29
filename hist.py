#import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd     

    #set panda to read in the iris dataset and contain it in a dataframe called iris
iris = pd.read_csv("iris.csv") 

    #plot a histogram of Sepal Length. It should be orientated horizontally, coloured green 
    # and have a label of Sepal Length 
    # 
setosa = iris.loc[iris['Species'] == 'Iris-setosa']

versicolor =  iris.loc[iris['Species'] == 'Iris-versicolor']

virginica =  iris.loc[iris['Species'] == 'Iris-virginica']

plt.hist(setosa['SepalLengthCm'], 20, orientation='vertical', facecolor='blue', alpha=0.5, label= 'Sepal_Length')   
plt.hist(versicolor['SepalLengthCm'], 20, orientation='vertical', facecolor='green', alpha=0.5, label= 'Sepal_Length')
plt.hist(virginica['SepalLengthCm'], 20, orientation='vertical', facecolor='orange', alpha=0.5, label= 'Sepal_Length')
#save the plot as a png to the current folder 
plt.savefig("Sepal_Length_Hist.png")

