from poisson import Poisson
import random

# Class requin est la classe enfant de Poisson
class Requin(Poisson):

    def __init__(self, monde, shark="🦈"):
        self.shark = shark
        self.energie = 5
        self.x = random.randint(0, monde.largeur - 1) % monde.largeur
        self.y = random.randint(0, monde.hauteur - 1) % monde.hauteur
        super().__init__(monde, shark)
        
        
    def energie_vitale(self, grille):
        
        if len(liste_de_requins) == 0:
            pass
        else:
            # Contrôle de l'énergie du requin (non fonctionnel)                
            if self.energie == 0: #mort du requin
                grille[self.y][self.x] = "💧"
                grille = liste_de_requins.remove(requin)
            else:
                self.energie -= 1 
            

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

        else:  # Si pas de poissons dans les cases adjacentes, alors déplacement normal
            
            haut = (self.y - 1) % self.monde.hauteur
            bas = (self.y + 1) % self.monde.hauteur
            gauche = (self.x - 1) % self.monde.largeur
            droite = (self.x + 1) % self.monde.largeur

            directions = [(self.x, haut), (self.x, bas),
                          (gauche, self.y), (droite, self.y)]
            
            indices_adjacents = []
            
            # Calcul des nouvelles coordonnées avec bord connecté
            for x, y in directions:
                nouvel_x = x % self.monde.largeur
                nouvel_y = y % self.monde.hauteur

                if grille[nouvel_y][nouvel_x] == "💧":
                    indices_adjacents.append((nouvel_x, nouvel_y))

            if indices_adjacents:
                nouvel_x, nouvel_y = random.choice(indices_adjacents)
                grille[self.y][self.x] = "💧"
                self.x, self.y = nouvel_x, nouvel_y
                grille[self.y][self.x] = self.shark

        return grille