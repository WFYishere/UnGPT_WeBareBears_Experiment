import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
data = pd.read_csv('happiness_2021.csv')
data_for_pca = data.drop(columns=['Country name', 'Regional indicator'])
data_for_pca = data_for_pca.fillna(data_for_pca.median())
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_for_pca)

# Apply PCA
pca = PCA(n_components=2) 
pca_result = pca.fit_transform(data_scaled)

pc_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
pc_df['Ladder score'] = data['Ladder score']

# PCA Biplot
plt.figure(figsize=(12, 8))
plt.scatter(pc_df['PC1'], pc_df['PC2'], alpha=0.5, c=pc_df['Ladder score'], cmap='viridis', s=50)
plt.colorbar(label='Ladder Score')

for i, feature in enumerate(data_for_pca.columns):
    plt.arrow(0, 0, pca.components_[0, i] * 10, pca.components_[1, i] * 10, head_width=0.5, head_length=0.5, fc='k', ec='k')
    plt.text(pca.components_[0, i] * 10.5, pca.components_[1, i] * 10.5, feature, color='k')

plt.title('PCA Biplot: PC1 vs PC2')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()

# 3D Scatter Plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(pc_df['PC1'], pc_df['PC2'], pc_df['Ladder score'], c=pc_df['Ladder score'], cmap='viridis', s=50)
cbar = plt.colorbar(scatter)
cbar.set_label('Ladder Score')

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Ladder Score')
ax.set_title('3D Scatter Plot of PC1, PC2, and Ladder Score')

plt.show()
