# Portfolio Project - Optimisation CAPM & Markowitz

## Description

Ce projet vise à construire un portefeuille d’actifs semblable au S&P 500, mais avec des poids ajustés en fonction de l’aversion au risque de l’investisseur.  
Nous utilisons le modèle CAPM pour estimer les rendements attendus et la théorie de Markowitz pour optimiser la composition du portefeuille.

## Fonctionnalités

- Récupération des prix ajustés via Yahoo Finance (`yfinance`)  
- Calcul des betas par covariance avec le benchmark (S&P 500)  
- Calcul des rendements attendus avec CAPM  
- Optimisation du portefeuille selon la fonction d’utilité de Markowitz avec un coefficient d’aversion au risque personnalisable  
- Visualisation des poids optimaux (bar chart)  
- Calcul et affichage de la performance cumulée en buy & hold  

## Structure du projet

- `src/` : fichiers source Python (`data_loader.py`, `risk_metrics.py`, `simple_CAPM.py`)  
- `notebooks/` : notebooks pour exploration, analyse, visualisation  
- `README.md` : ce fichier  
- `requirements.txt` : liste des dépendances Python  

## Installation

1. Cloner le repo :  
   ```bash
   git clone https://github.com/maximernandez/portfolio-project
   cd portfolio-project
2. Installer les dépendances :
  ```bash  
  pip install -r requirements.txt
3. Utilisation : 
Modifier la liste des tickers dans le notebook ou dans simple_CAPM.py

Lancer le pipeline CAPM pour récupérer betas, rendements attendus et matrice de covariance

Ajuster le coefficient d’aversion au risque et les bornes sur les poids pour optimiser le portefeuille : très important !

Visualiser les poids optimaux et la performance du portefeuille

## Résultats
Le portefeuille optimal tient compte du profil de risque de l’investisseur, en maximisant la fonction d’utilité de Markowitz.
Les poids s’ajustent selon l’aversion au risque, offrant un bon compromis rendement/risque.

## Remarques
Le projet est réalisé dans un style simple, adapté à un étudiant qui rentre en master en école d'ingénieur

Le modèle CAPM utilise la méthode classique (beta = covariance / variance) sans régression.

Les contraintes d’optimisation fixent une borne supérieure sur les poids pour éviter une concentration excessive.

## Auteur
Maxime Ernandez
[LinkedIn](https://www.linkedin.com/in/maxime-ernandez-aa4a4226a/)
