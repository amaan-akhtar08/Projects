import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../data/updated_file.csv")
plt.figure(figsize=(15, 9))

x_vars = ['Income','Age','Total_Num_Purchases','Total_Spend']
count = 1
for i in x_vars: 
    plt.subplot(2,2, count)  
    sns.boxplot(x=df[i])
    # plt.title(i)
    count+=1