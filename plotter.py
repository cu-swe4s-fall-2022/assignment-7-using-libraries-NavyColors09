import matplotlib.pyplot as plt
import pandas as pd 

iris = pd.read_csv('iris.data',header=None) 
iris.columns = ['sepal_length','sepal_width', 'petal_width', 'petal_length','species']
names = ['sepal_length','sepal_width', 'petal_width', 'petal_length'] 
plt.boxplot(iris[names],labels=names)
plt.ylabel('cm')
plt.savefig("iris_boxplot.png") 
plt.show() 

for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name] #Create a new dataframe
    plt.scatter(iris_subset['sepal_width'],iris_subset['sepal_length'],label=species_name,s=12)

plt.legend(loc='upper right') 
plt.xlabel('sepal_length (cm)')
plt.ylabel('sepal_width (cm)') 
plt.savefig("petal_width_v_length_scatter.png") 
plt.show() 

fig,axes = plt.subplots(1,2)
fig.set_size_inches(12,5)

axes[0].boxplot(iris[names],labels=names)
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False) 
axes[0].set_ylabel('cm')

for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name] #Create a new dataframe
    axes[1].scatter(iris_subset['sepal_width'],iris_subset['sepal_length'],label=species_name,s=12)
    
axes[1].legend(loc='upper right')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False) 
axes[1].set_xlabel('sepal_length (cm)')
axes[1].set_ylabel('sepal_width (cm)') 
plt.savefig("multi_panel_figure.png") 
#plt.tight_layout()
plt.show() 
