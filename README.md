🧨 Démineur en Pygame

Bienvenue sur Démineur by Lesno : une version du célèbre jeu du Démineur réalisée en Python avec Pygame et Pygame GUI.
📋 Description

Ce projet est un jeu de Démineur interactif, qui propose :

    Un menu d'accueil pour choisir le nombre de bombes (entre 10 et 20).

    Une interface graphique moderne grâce à pygame_gui.

    Un chronomètre pour mesurer votre temps de jeu.

    Un système de sauvegarde des meilleurs scores dans un fichier JSON.

    La gestion des drapeaux et du clic droit pour marquer les mines.

🚀 Fonctionnalités

✅ Menu d'accueil avec champ de saisie et bouton "JOUER"
✅ Génération aléatoire du plateau avec placement des mines
✅ Affichage automatique des zones sans mine (zéro) de manière récursive
✅ Détection de victoire et de défaite
✅ Chronomètre en temps réel
✅ Sauvegarde du meilleur temps et affichage sur l'écran de jeu
✅ Utilisation intuitive des clics gauche (révéler) et droit (poser/enlever un drapeau)


🎮 Instructions
1️⃣ Lancer le jeu

Assurez-vous d’avoir Python 3 installé, ainsi que les bibliothèques nécessaires :

pip install pygame pygame_gui numpy

Puis lancez le script :

python demineur.py

2️⃣ Jouer

    Entrez le nombre de bombes (entre 10 et 20) et cliquez sur JOUER.

    Cliquez gauche pour révéler une case.

    Cliquez droit pour placer ou enlever un drapeau.

    Sauvegardez votre score en entrant votre pseudo et en cliquant sur SAVE une fois la partie gagnée.

3️⃣ Sauvegarde

Les scores sont enregistrés dans le fichier temps_demineur.json. Le meilleur score s'affiche en haut de l'écran.
📂 Fichiers importants

    demineur.py — le script principal du jeu.

    image_demineur.jpg — image affichée dans le menu.

    theme.json — thème personnalisé pour pygame_gui.

    temps_demineur.json — fichier JSON pour sauvegarder les scores.

🛠️ Dépendances

    pygame

    pygame_gui

    numpy

👨‍💻 Auteur

Développé par Lesno (Charles Noah)
