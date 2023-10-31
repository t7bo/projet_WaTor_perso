import random
import time

class Monde:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

class Poisson:
    def __init__(self, monde, fish="🐠"):
        self.monde = monde
        self.x = random.randint(0, monde.largeur - 1)
        self.y = random.randint(0, monde.hauteur - 1)
        self.fish = fish

    def deplacements_poissons(self, grille):
        indices_adjacents = []
        haut = (self.y - 1) % self.monde.hauteur
        bas = (self.y + 1) % self.monde.hauteur
        gauche = (self.x - 1) % self.monde.largeur
        droite = (self.x + 1) % self.monde.largeur

        directions = [(self.x, haut), (self.x, bas), (gauche, self.y), (droite, self.y)]
        indices_adjacents = [(x, y) for x, y in directions if grille[y][x] == "💧"]

        if indices_adjacents:
            nouvel_x, nouvel_y = random.choice(indices_adjacents)
            grille[self.y][self.x] = "💧"
            self.x, self.y = nouvel_x, nouvel_y
            grille[self.y][self.x] = self.fish
        return grille

class Requin(Poisson):
    def __init__(self, monde, shark="🦈"):
        super().__init__(monde, shark)

    def deplacements_requins(self, grille, poissons):
        distances = []
        for poisson in poissons:
            distance = abs(self.x - poisson.x) + abs(self.y - poisson.y)
            distances.append((distance, poisson))

        if distances:
            distance_min, poisson_plus_proche = min(distances, key=lambda x: x[0])
            if distance_min > 1:  # Se déplacer seulement si le poisson n'est pas adjacent
                if self.x < poisson_plus_proche.x:
                    self.x = (self.x + 1) % self.monde.largeur
                elif self.x > poisson_plus_proche.x:
                    self.x = (self.x - 1) % self.monde.largeur
                if self.y < poisson_plus_proche.y:
                    self.y = (self.y + 1) % self.monde.hauteur
                elif self.y > poisson_plus_proche.y:
                    self.y = (self.y - 1) % self.monde.hauteur
                grille[self.y][self.x] = self.fish
                grille[poisson_plus_proche.y][poisson_plus_proche.x] = "💧"
                poissons.remove(poisson_plus_proche)
        return grille

# Créez une instance de Monde
monde = Monde(20, 10)  # Largeur et hauteur de votre monde

# Initialisation de la grille
grille = [["💧" for _ in range(monde.largeur)] for _ in range(monde.hauteur)]

# Demandez à l'utilisateur combien de poissons et de requins créer
nombre_de_poissons = int(input("Combien de poissons voulez-vous créer ? "))
nombre_de_requins = int(input("Combien de requins voulez-vous créer ? "))

# Créez les poissons et les requins
liste_de_poissons = [Poisson(monde) for _ in range(nombre_de_poissons)]
liste_de_requins = [Requin(monde) for _ in range(nombre_de_requins)]

while True:
    # Déplacez les requins
    for requin in liste_de_requins:
        grille = requin.deplacements_requins(grille, liste_de_poissons)

    # Déplacez les poissons
    for poisson in liste_de_poissons:
        grille = poisson.deplacements_poissons(grille)

    print(f"Total poissons : {len(liste_de_poissons)}")
    print(f"Total requins : {len(liste_de_requins)}")

    # Affichez la grille mise à jour
    print("\033[H", end="")
    for row in grille:
        print("".join(row))

    # Mettez en pause le programme pendant 1 seconde pour créer l'effet d'animation
    time.sleep(1)
