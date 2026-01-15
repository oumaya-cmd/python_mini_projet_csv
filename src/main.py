import pandas as pd
import matplotlib.pyplot as plt
import os

def analyser_csv(fichier):
    """Analyse un fichier CSV et affiche des statistiques et un graphique scatter."""
    
    if not os.path.exists(fichier):
        print(f"Erreur : le fichier {fichier} n'existe pas.")
        return
    
    # Charger le fichier CSV
    data = pd.read_csv(fichier)

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

if __name__ == "__main__":
    fichier_csv = "../data/exemple.csv"  # Chemin relatif depuis src/
    analyser_csv(fichier_csv)

