# Projet Wa-Tor

Ce projet est une implémentation personnalisée du simulateur Wa-Tor, un modèle de simulation de l'écosystème marin. Dans cette version, vous pouvez observer l'interaction entre les poissons et les requins dans un monde aquatique simulé.

## Comment Ça Marche

### Représentation du Monde

Le monde est représenté par une grille 2D où chaque cellule peut être soit un poisson, représenté par "🐠", soit un requin, représenté par "🦈", soit de l'eau, représentée par "💧".

### Les Poissons

- Les poissons se déplacent librement dans l'eau.
- Ils se reproduisent tous les 2 chronons et donnent naissance à de nouveaux poissons.
- Les poissons se déplacent d'une cellule dans le monde chaque chronon.

### Les Requins

- Les requins se déplacent librement dans l'eau.
- Ils se reproduisent tous les 4 chronons et donnent naissance à de nouveaux requins.
- Les requins chassent les poissons pour se nourrir.
- Si un requin ne se nourrit pas pendant un certain nombre de chronons, il meurt.
- Energie vitale maximale d'un requin : 5 (chronons sans manger)

### Limites du Monde

Dans cette version, le monde est un espace torique, ce qui signifie que les bords du monde sont connectés entre eux. Par conséquent, un poisson ou un requin qui atteint le bord de la grille réapparaît de l'autre côté du monde.

## Comment Utiliser le Code

1. **Prérequis**: Assurez-vous d'avoir Python installé sur votre système.
2. **Clonage du Projet**: Clonez ce dépôt sur votre machine locale en utilisant la commande `git clone`.
3. **Exécution du Programme**: Exécutez le fichier principal `main.py` pour lancer la simulation. Suivez les instructions à l'écran pour spécifier le nombre initial de poissons et de requins.