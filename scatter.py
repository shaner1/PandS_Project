#import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#get panda to read the iris dataset into the dataframe called df
df = pd.read_csv("iris.csv")

#used seaborn to create a scatter plot for each pair of variables 
sns.pairplot(df, hue="Species", diag_kind="kde")

#need to use matplotlib to display the plot as seaborn is an addition on top of plt
plt.show()