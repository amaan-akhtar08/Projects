# Function to cap outliers based on IQR
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../data/updated_file.csv")

def cap_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series.clip(lower_bound, upper_bound)

# Apply the outlier treatment
df_treated = df.copy()
numeric_vars = ['Income','Age','Total_Num_Purchases','Total_Spend']
for column in numeric_vars:
    df_treated[column] = cap_outliers(df_treated[column])

# plot


plt.figure(figsize=(15, 12))

count = 1
for i in numeric_vars: 
    plt.subplot(4,4, count)  
    sns.boxplot(x=df[i])
    plt.subplot(4,4, count+1)  
    sns.boxplot(x=df_treated[i])
    # plt.title(i)
    count+=2
