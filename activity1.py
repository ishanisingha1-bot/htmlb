import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')
df=df.dropna()
print(df.head())
print(df.info())
sns.barplot(x='day',y='total_bill',hue='sex',data=df)
plt.title('Average Total Bill per day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.countplot(x='day',hue='sex',data=df)
plt.title('Number of Diners per day by gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day',y='total_bill',data=df)
plt.title('Spread of Total bill per day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
sns.stripplot(x='day',y='total_bill',data=df,jitter=True)

sns.swarmplot(x='day',y='total_bill',data=df)
plt.title('Every Bill Amount per day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()
