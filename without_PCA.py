import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data_2021 = pd.read_csv('happiness_2021.csv')
data_relevant = data_2021.drop(columns=['Country name', 'Regional indicator'])

# Scatter Plots
features = data_relevant.columns[2:] 

for feature in features:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data_2021[feature], y=data_2021['Ladder score'])
    plt.title(f'Scatter Plot: Ladder Score vs. {feature}')
    plt.xlabel(feature)
    plt.ylabel('Ladder Score')
    plt.show()
