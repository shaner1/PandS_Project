# IPython log file

ˇ
import matplotlib.pyplot as plt
import pandas as pd  
get_ipython().run_line_magic('logstart', '')
import matplotlib.pyplot as plt
import pandas as pd  
iris = pd.read_csv("iris.csv")
species = iris.groupby("Species")
species
print(species)
species.describe()
plt.hist(species['Iris-setosa'])
import matplotlib.pyplot as plt
import pandas as pd  
iris = pd.read_csv("iris.csv")
iris.loc[iris['Species'] == 'Iris-setosa']
setosa =  iris.loc[iris['Species'] == 'Iris-setosa']
setosa
plt.hist(setosa['SepalLengthCm'])
versicolor =  iris.loc[iris['Species'] == 'Iris-versicolor']
plt.hist(versicolor['SepalLengthCm'])
virginica =  iris.loc[iris['Species'] == 'Iris-virginica']
plt.hist(virginica['SepalLengthCm'])
exit()
