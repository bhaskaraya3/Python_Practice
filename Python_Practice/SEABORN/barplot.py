import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")


sns.barplot(x="sex",y="tip",data=tips)
plt.title("Average Bill by Day")
plt.show()