import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(x="day",data=tips)
plt.title("Count of Daya")
plt.show()