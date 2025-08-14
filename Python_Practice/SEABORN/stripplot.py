import matplotlib.pyplot as plt
import seaborn as sns

s = sns.get_dataset_names()
# print(s)

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")

sns.stripplot(x="day",y="tip",data=tips,hue="sex",dodge=True)
plt.show()