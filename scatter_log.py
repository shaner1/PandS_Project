# IPython log file

get_ipython().run_line_magic('logstart', '')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("iris.csv")
sns.pairplot(iris, hue="species")
sns.pairplot(iris, hue="Species")
sns.pairplot(df, hue="Species")
sns.pairplot(df, hue="Species", diag_kind="kde")
exit()
