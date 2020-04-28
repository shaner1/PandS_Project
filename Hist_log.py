# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas 
import pandas as pd
iris = pd.read_csv("iris.csv")
plt.hist(iris['SepalLengthCm'])
import matplotlib.pyplot as plt
import pandas as pd                                                                                                                                         
iris = pd.read_csv("iris.csv") 
plt.hist(iris['SepalLengthCm'])    
plt.hist(iris['SepalLengthCm'], orientation='horizontal')     
plt.hist(iris['SepalLengthCm'], orientation='horizontal', color=Green)     
plt.hist(iris['SepalLengthCm'], orientation='horizontal', color= 'Green')     
plt.hist(iris['SepalLengthCm'], orientation='horizontal', color= 'Green', label= 'Sepal_Length')     
plt.savefig("Sepal_Length_Hist.png")
exit()
