import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import numpy as np  

file_path = 'C:/Users/elfad/OneDrive/Documents/for me/data-sell4all.xlsx'  
data = pd.read_excel(file_path)  
data.columns = data.columns.str.strip()  

valid_countries = ['France', 'Germany', 'Spain', 'Italy', 'UK', 'USA', 'Canada', 'Australia', 'Japan', 'Brazil']  
data = data[data['Pays'].isin(valid_countries)]  

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')  
data['Dépenses des clients'] = pd.to_numeric(data['Dépenses des clients'], errors='coerce') 
data.dropna(subset=['Age', 'Dépenses des clients'], inplace=True)
cleaned_data = data[data['Dépenses des clients'] >= 10].drop_duplicates() 

age_median = data['Age'].median()  
age_mean = data['Age'].mean()  
spending_median = data['Dépenses des clients'].median()  
spending_mean = data['Dépenses des clients'].mean()  
print("Médiane de l'âge:", age_median)  
print("Moyenne de l'âge:", age_mean)  
print("Médiane des dépenses des clients:", spending_median)  
print("Moyenne des dépenses des clients:", spending_mean)  

spending_by_country = cleaned_data.groupby('Pays')['Dépenses des clients'].sum().sort_values()  
colors = plt.cm.viridis((spending_by_country - spending_by_country.min()) / (spending_by_country.max() - spending_by_country.min()))  
plt.figure(figsize=(15, 8))  
barplot = plt.bar(spending_by_country.index, spending_by_country.values, color=colors, edgecolor='black')  

for index, value in enumerate(spending_by_country.values):  
  plt.text(index, value, f'{value:.2f} €', ha='center', va='bottom', fontsize=12, color='black') 

plt.title("Dépenses des Clients par Pays", fontsize=20, fontweight='bold', color='darkblue')  
plt.xlabel("Pays", fontsize=14, fontweight='bold')  
plt.ylabel("Dépenses (en €)", fontsize=14, fontweight='bold')  
plt.xticks(rotation=45, fontsize=12)  
plt.yticks(fontsize=12)  
      [
        plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')  

plt.tight_layout()  
plt.show()  

final_data = cleaned_data[['Pays', 'Age', 'Genre', 'Dépenses des clients']]  
final_data.to_csv('cleaned_data_sell4all.csv', index=False)  