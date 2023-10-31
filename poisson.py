import random
from monde import Monde

class Poisson(Monde):

    def __init__(self, monde, fish="🐠"):
        self.monde = monde
        self.x = random.randint(0, monde.largeur - 1) % monde.largeur
        self.y = random.randint(0, monde.hauteur - 1) % monde.hauteur

        self.fish = fish

    def deplacements_poissons(self, grille):

        indices_adjacents = []

        haut = (self.y - 1) % self.monde.hauteur
        bas = (self.y + 1) % self.monde.hauteur
        gauche = (self.x - 1) % self.monde.largeur
        droite = (self.x + 1) % self.monde.largeur

        directions = [(self.x, haut), (self.x, bas),
                      (gauche, self.y), (droite, self.y)]

        indices_adjacents = []

        for x, y in directions:
            # Calcul des nouvelles coordonnées avec bord connecté
            nouvel_x = x % self.monde.largeur
            nouvel_y = y % self.monde.hauteur

            # Vérification de la grille avec les nouvelles coordonnées
            if grille[nouvel_y][nouvel_x] == "💧":
                indices_adjacents.append((nouvel_x, nouvel_y))

        if indices_adjacents:
            nouvel_x, nouvel_y = random.choice(indices_adjacents)
            grille[self.y][self.x] = "💧"
            self.x, self.y = nouvel_x, nouvel_y
            grille[self.y][self.x] = self.fish

        return grille
    