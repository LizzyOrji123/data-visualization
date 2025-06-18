import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Loading seaborn built-in dataset
df = sns.load_dataset("tips")

# Line Plot
plt.plot(df['total_bill'])
plt.title("Line Plot of Total Bill")
plt.xlabel("Index")
plt.ylabel("Total Bill")
plt.show()

# Scatter Plot
plt.scatter(df['total_bill'], df['tip'])
plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Histogram
sns.histplot(df['total_bill'], kde=True)
plt.title("Histogram of Total Bill")
plt.show()

# Box Plot
sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Box Plot of Total Bill by Day")
plt.show()
