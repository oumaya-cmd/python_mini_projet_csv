import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
data = pd.read_csv("../data/exemple.csv")  # "../" si Projet.py est dans src/

# Afficher un aperçu des données
print("Aperçu des données :")
print(data.head())

# Statistiques descriptives
print("\nStatistiques :")
print(data.describe())

# Créer un graphique scatter
plt.scatter(data['Temps'], data['Note'])
plt.title("Relation Temps d'étude / Note")
plt.xlabel("Temps d'étude (heures)")
plt.ylabel("Note obtenue")
plt.grid(True)
plt.show()
