from monde import Monde
from poisson import Poisson
import random

class Requin(Poisson):

    def __init__(self, monde, shark="🦈"):
        self.shark = shark
        self.energie = 6
        self.x = random.randint(0, monde.largeur - 1) % monde.largeur
        self.y = random.randint(0, monde.hauteur - 1) % monde.hauteur
        super().__init__(monde, shark)
        

    def deplacements_requins(self, grille, poissons):

        poissons_adjacents = []

        distances = []

        # Vérifier s'il y a un poisson dans les cases adjacentes au requin
        for poisson in poissons:

            if abs(self.x - poisson.x) <= 1 and abs(self.y - poisson.y) <= 1:
                poissons_adjacents.append(poisson)

            else:
                distance = abs(self.x - poisson.x) + abs(self.y - poisson.y)
                distances.append((distance, poisson))

        if poissons_adjacents:
            # Déplacer le requin vers le poisson adjacent s'il y en a un ( SEULEMENT DEPLACEMENT (pas d'alimentation))
            poisson_adjacent = random.choice(poissons_adjacents)
            grille[self.y][self.x] = "💧"
            self.x, self.y = poisson_adjacent.x, poisson_adjacent.y
            grille[self.y][self.x] = self.shark
            poissons.remove(poisson_adjacent)
            requin.energie += 1

        for r in liste_de_requins:
            if r.energie == 0:
                liste_de_requins.remove(r)

        else:  # Si pas de poissons dans les cases adjacentes, alors déplacement normal
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

                # Vérification des nouvelles coordonnées pour rester dans les limites de la grille
                if 0 <= nouvel_x < self.monde.largeur and 0 <= nouvel_y < self.monde.hauteur:
                    # Vérification de la grille avec les nouvelles coordonnées
                    if grille[nouvel_y][nouvel_x] == "💧":
                        indices_adjacents.append((nouvel_x, nouvel_y))

            if indices_adjacents:
                nouvel_x, nouvel_y = random.choice(indices_adjacents)
                grille[self.y][self.x] = "💧"
                self.x, self.y = nouvel_x, nouvel_y
                grille[self.y][self.x] = self.shark

        return grille