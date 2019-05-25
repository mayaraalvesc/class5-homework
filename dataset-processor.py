import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

wine_df = pd.read_csv('wine.data', sep=',', header=0)
wine_df.columns=['Class','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'OD Diluted Wines', 'Proline']

print(wine_df.to_string())
print()

#compute and print summary statistics
print(wine_df.describe(include='number'))

#Visualize the data, 1-feature (column) at a time, i.e. line or histogram and save the figures to filesos.makedirs('plots', exist_ok=True)
#print(wine_df['Alcohol'])
plt.hist(wine_df['Alcohol'], bins=3, color='g')
plt.title('Alcohol')
plt.xlabel('Alcohol')
plt.ylabel('Count')
plt.savefig(f'plots/Alcohol_hist.png', format='png')
plt.clf()
# print(wine_df['Malic Acid'])
plt.hist(wine_df['Malic Acid'], bins=3, color='g')
plt.title('Malic Acid')
plt.xlabel('Malic Acid')
plt.ylabel('Count')
plt.savefig(f'plots/MalicAcid_hist.png', format='png')
plt.clf()
# print(wine_df['Ash'])
plt.hist(wine_df['Ash'], bins=3, color='g')
plt.title('Ash')
plt.xlabel('Ash')
plt.ylabel('Count')
plt.savefig(f'plots/Ash_hist.png', format='png')
plt.clf()
# print(wine_df['Magnesium'])
plt.hist(wine_df['Magnesium'], bins=3, color='g')
plt.title('Magnesium')
plt.xlabel('Magnesium')
plt.ylabel('Count')
plt.savefig(f'plots/Magnesium_hist.png', format='png')
plt.clf()
# print(wine_df['Total Phenols'])
plt.hist(wine_df['Total Phenols'], bins=3, color='g')
plt.title('Total Phenols')
plt.xlabel('Total Phenols')
plt.ylabel('Count')
plt.savefig(f'plots/Total Phenols_hist.png', format='png')
plt.clf()
# print(wine_df['Flavanoids'])
plt.hist(wine_df['Flavanoids'], bins=3, color='g')
plt.title('Flavanoids')
plt.xlabel('Flavanoids')
plt.ylabel('Count')
plt.savefig(f'plots/Flavanoids_hist.png', format='png')
plt.clf()
# print(wine_df['Nonflavanoid Phenols'])
plt.hist(wine_df['Nonflavanoid Phenols'], bins=3, color='g')
plt.title('Nonflavanoid Phenols')
plt.xlabel('Nonflavanoid Phenols')
plt.ylabel('Count')
plt.savefig(f'plots/Nonflavanoid Phenols_hist.png', format='png')
plt.clf()
# print(wine_df['Proanthocyanins'])
plt.hist(wine_df['Proanthocyanins'], bins=3, color='g')
plt.title('Proanthocyanins')
plt.xlabel('Proanthocyanins')
plt.ylabel('Count')
plt.savefig(f'plots/Proanthocyanins_hist.png', format='png')
plt.clf()
# print(wine_df['Color Intensity'])
plt.hist(wine_df['Color Intensity'], bins=3, color='g')
plt.title('Color Intensity')
plt.xlabel('Color Intensity')
plt.ylabel('Count')
plt.savefig(f'plots/Color Intensity_hist.png', format='png')
plt.clf()
# print(wine_df['Hue'])
plt.hist(wine_df['Hue'], bins=3, color='g')
plt.title('Hue')
plt.xlabel('Hue')
plt.ylabel('Count')
plt.savefig(f'plots/Hue_hist.png', format='png')
plt.clf()
# print(wine_df['OD Diluted Wines'])
plt.hist(wine_df['OD Diluted Wines'], bins=3, color='g')
plt.title('OD280 OD315 of Diluted Wines')
plt.xlabel('OD Diluted Wines')
plt.ylabel('Count')
plt.savefig(f'plots/OOD Diluted Wines_hist.png', format='png')
plt.clf()
# print(wine_df['Proline'])
plt.hist(wine_df['Proline'], bins=3, color='g')
plt.title('Proline')
plt.xlabel('Proline')
plt.ylabel('Count')
plt.savefig(f'plots/Proline_hist.png', format='png')
plt.clf()