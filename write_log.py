# IPython log file

get_ipython().run_line_magic('logstart', '')
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("iris.csv")   
df.describe(exclude = 'Id')  
df.describe(exclude = [Id]) 
df.drop(column=['Id'])    
df.drop(['Id'])    
with open('test.txt', 'w') as test:
    test.writelines("\nThis is a summary of the variables in the iris dataset\n" summary)
with open('test.txt', 'w') as test:
    test.write("\nThis is a summary of the variables in the iris dataset\n)
with open('test.txt', 'w') as test:
    test.write("\nThis is a summary of the variables in the iris dataset\n")
    
with open('test.txt', 'a') as test:
    test.write("Add another line")
    
    
with open('test.txt', 'a') as test:
    test.write()
    
    
exit()
