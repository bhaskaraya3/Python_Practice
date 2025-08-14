import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="tip", data=tips,hue="sex")
plt.title("Bill Distribution by Day")
plt.show()