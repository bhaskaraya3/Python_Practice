import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(tips["tip"],kde=True,bins=15)
# sns.displot(tips["tip"],kde=True,bins=15)
plt.title("Histogram of Total Bill")
plt.show()