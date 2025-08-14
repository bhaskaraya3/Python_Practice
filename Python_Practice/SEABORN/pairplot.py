import seaborn as sns
import matplotlib.pyplot as plt
s = sns.get_dataset_names()
# print(s)

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")
tips = sns.load_dataset("tips")

sns.pairplot(titanic.select_dtypes(['number']),hue="pclass")
plt.show()