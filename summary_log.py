# IPython log file

get_ipython().run_line_magic('logstart', '')
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("iris.csv")
df.describe()
summary = df.describe()
print(summary)
with open('test.txt', 'w') as test:
test.write("Hello")
with open('test.txt', 'w') as test:
    test.write("Hello")

with open('test.txt', 'w') as test:
    test.write(summary)

summary = str(df.describe())
with open('test.txt', 'w') as test:
    test.write(summary)

del iris['Id']
del df['Id']
with open('test.txt', 'w') as test:
    test.write(summary)

del df['Id']
with open('test.txt', 'w') as test:
    test.write(summary)

exit()
