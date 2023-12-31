import random
import time

class Monde:

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

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


# Création d'une instance de Monde
monde = Monde(20, 10)  # Largeur et hauteur du monde

# Initialisation de la grille
grille = [["💧" for _ in range(monde.largeur)] for _ in range(monde.hauteur)]

# Demande à l'utilisateur combien de poissons et de requins il souhaite
nombre_de_poissons = int(input("Combien de poissons voulez-vous créer ? "))
nombre_de_requins = int(input("Combien de requins voulez-vous créer ? "))

# Création des poissons et des requins
liste_de_poissons = [Poisson(monde) for _ in range(nombre_de_poissons)]
liste_de_requins = [Requin(monde) for _ in range(nombre_de_requins)]

chronon = 0
chronon_reproduction_poisson = 0
chronon_reproduction_requin = 0
energie = 5


while True:

    # POISSONS
    for poisson in liste_de_poissons:

        # Reproduction des poissons
        if chronon_reproduction_poisson == 2:

            nouveaux_poissons = []

            for poisson in liste_de_poissons:

                nouveau_poisson = Poisson(monde)
                nouveau_poisson.x = poisson.x
                nouveau_poisson.y = poisson.y
                nouveaux_poissons.append(nouveau_poisson)

            # Ajouter les nouveaux poissons à la liste des poissons existants
            liste_de_poissons.extend(nouveaux_poissons)
            chronon_reproduction_poisson = 0

        # Déplacements des poissons
        grille = poisson.deplacements_poissons(grille)
        

    # REQUINS
    for requin in liste_de_requins:
        
        # Reproduction des requins
        if chronon_reproduction_requin == 4:

            nouveaux_requins = []

            for requin in liste_de_requins:

                nouveau_requin = Requin(monde)
                nouveau_requin.x = requin.x
                nouveau_requin.y = requin.y
                nouveaux_requins.append(nouveau_requin)
                energie += 2
                chronon_reproduction_requin = 0

            # Ajout des nouveaux requins à la liste des requins existants
            liste_de_requins.extend(nouveaux_requins)
            
        # Déplacements des requins
        grille = requin.deplacements_requins(grille, liste_de_poissons)
        
        # Contrôle et/ou Mort des requins
        requin.energie_vitale(grille)

                    
    chronon += 1
    chronon_reproduction_requin += 1
    chronon_reproduction_poisson += 1

    # print("\033[H", end="")
    print("\033c", end="")

    # Affichage de la grille mise à jour
    for row in grille:
        print("".join(row))

    print(f"Total poissons : {len(liste_de_poissons)}")
    print(f"Total requins : {len(liste_de_requins)}")
    print(f"Total de chronons passés : {chronon}")
    print(f"Reproduction des poissons ({chronon_reproduction_poisson} chronons / 2) ")
    print(f"Reproduction des requins ({chronon_reproduction_poisson} chronons / 5) ")

    # Mise en pause du programme pendant 1 seconde pour créer l'effet d'animation
    time.sleep(1)