# Pong - Jeu de Tennis de table

Pong est une version simplifiée du jeu de tennis de table classique, développée en Python à l'aide de Pygame.

## Objectif du jeu

Le but du jeu est de marquer des points en faisant rebondir une balle sur les raquettes adverses tout en évitant que la balle ne passe derrière votre raquette.

## Contrôles

- **Raquette gauche** :

  - **S** : Descendre la raquette
  - **W** : Monter la raquette

- **Raquette droite** :

  - **Flèche Haut** : Monter la raquette
  - **Flèche Bas** : Descendre la raquette

- **Fermer le jeu** : Cliquez sur le bouton "Fermer" en haut à droite de la fenêtre du jeu.

## Règles du jeu

- La partie commence avec une balle au centre de l'écran, se déplaçant dans une direction aléatoire.
- Les raquettes peuvent se déplacer verticalement pour frapper la balle.
- Si la balle passe derrière une raquette, l'adversaire marque un point.
- Le jeu continue jusqu'à ce qu'un joueur atteigne un score prédéfini ou que les joueurs décident de terminer la partie.

## Statistiques affichées

- **Temps de jeu** : Affiche le temps écoulé depuis le début de la partie.
- **Nombre de coups joués** : Compte le nombre total de mouvements de raquette effectués.
- **Nombre de coups ratés** : Indique le nombre de fois que chaque joueur a manqué de renvoyer la balle.

## Installation et exécution

Pour exécuter le jeu sur votre machine :

1. Assurez-vous d'avoir Python 3.x installé.
2. Installez la bibliothèque Pygame en utilisant la commande suivante :
   ''' pip install pygame '''
3. Téléchargez ou clonez ce dépôt Git sur votre machine.
4. Naviguez jusqu'au répertoire contenant le fichier `pong.py`.
5. Lancez le jeu en exécutant la commande suivante dans votre terminal :
   '''python main.py'''

## Développement

Ce jeu a été développé avec Python 3.x et Pygame. Il utilise des concepts de base de la programmation de jeux tels que la gestion des événements, les collisions, et le rendu graphique.

## Auteur

Ce jeu a été développé par Marion Maurice.
