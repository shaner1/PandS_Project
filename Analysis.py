
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


iris = pd.read_csv("iris.csv")

del iris['Id']

summary = str(iris.describe())

with open('Summary.txt', 'w') as text:
    text.write(summary)

plt.hist(iris['SepalLengthCm'], orientation='horizontal', color= 'Green', label= 'Sepal_Length')     
plt.savefig("Sepal_Length_Hist.png")

plt.hist(iris['SepalWidthCm'], orientation='horizontal', color= 'Green', label= 'Sepal_Width')     
plt.savefig("Sepal_Width_Hist.png")

plt.hist(iris['PetalLengthCm'], orientation='horizontal', color= 'Green', label= 'Petal_Length')     
plt.savefig("Petal_Length_Hist.png")

plt.hist(iris['PetalWidthCm'], orientation='horizontal', color= 'Green', label= 'Petal_Width')     
plt.savefig("Petal_Width_Hist.png")

sns.pairplot(iris, hue="Species", diag_kind="kde")
plt.show()