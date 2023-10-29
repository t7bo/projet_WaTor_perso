import random
import time
import copy

# Dimensions de la grille
nb_lignes = 8
nb_colonnes = 20

# Initialisation de la grille
grille = [["💧" for _ in range(nb_colonnes)] for _ in range(nb_lignes)]



# Initialisation du poisson à un emplacement aléatoire

class Animaux:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Poisson(Animaux):
    
    def __init__(self, x, y, fish="🐠"):
        super().__init__(x, y)  # Appelez le constructeur de la classe parente avec les arguments x et y
        self.fish = fish

    def __str__(self):
        return self.fish
    
         
    def deplacements(self):
        
        global grille
        
        for poisson in liste_de_poissons:
        
            # Liste des indices adjacents valides pour le poisson
            indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y),
                                (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
            
            # Sélectionnez un indice aléatoire parmi les indices adjacents
            nouvel_x, nouvel_y = random.choice(indices_adjacents)
        
            # Si le nouvel emplacement est valide dans la grille
            if 0 <= nouvel_x < nb_lignes and 0 <= nouvel_y < nb_colonnes and grille[nouvel_x][nouvel_y] == "💧":
                # Déplacez le poisson
                grille[poisson.x][poisson.y] = "💧"  # Remplacez l'emplacement actuel du poisson par de l'eau
                poisson.x, poisson.y = nouvel_x, nouvel_y  # Mettez à jour les indices du poisson
                grille[poisson.x][poisson.y] = "🐠"  # Mettez à jour la grille avec le nouveau emplacement du poisson
                    

#Demandez à l'utilisateur combien de poissons il souhaite créer
nombre_de_poissons = int(input("Combien de poissons voulez-vous créer ? "))

# Créez une liste pour stocker les poissons
liste_de_poissons = []

# Créez les poissons et ajoutez-les à la liste
for _ in range(nombre_de_poissons):
    poisson = Poisson(random.randint(0, nb_lignes - 1), random.randint(0, nb_colonnes - 1))
    liste_de_poissons.append(poisson)




class Requin(Poisson):
    def __init__(self, x, y, shark="🦈"):
        super().__init__(x, y)  # Appelez le constructeur de la classe parente avec les arguments x et y
        self.shark = shark
        
    def __str__(self):
        return self.shark
    

    def deplacements_requins(self):
        
        global grille
        
        for requin in liste_de_requins:
        
            # Liste des indices adjacents valides pour le requin
            indices_adjacents_requins = [(requin.x-1, requin.y), (requin.x+1, requin.y),
                                (requin.x, requin.y-1), (requin.x, requin.y+1)]
            
            # Sélectionnez un indice aléatoire parmi les indices adjacents
            nouvel_x_r, nouvel_y_r = random.choice(indices_adjacents_requins)
            
            # Si le nouvel emplacement est valide dans la grille
            if 0 <= nouvel_x_r < nb_lignes and 0 <= nouvel_y_r < nb_colonnes and grille[nouvel_x_r][nouvel_y_r] == "💧":
                # Déplacez le requin
                grille[requin.x][requin.y] = "💧"  # Remplacez l'emplacement actuel du requin par de l'eau
                requin.x, requin.y = nouvel_x_r, nouvel_y_r  # Mettez à jour les indices du requin
                grille[requin.x][requin.y] ="🦈"  # Mettez à jour la grille avec le nouveau emplacement du poisson  
            
            if 0 <= nouvel_x_r < nb_lignes and 0 <= nouvel_y_r < nb_colonnes and grille[nouvel_x_r][nouvel_y_r] == "🐠":
                grille[requin.x][requin.y] = "💧"  # Remplacez l'emplacement actuel du requin par de l'eau
                requin.x, requin.y = poisson.x, poisson.y
                grille[requin.x][requin.y] = "🦈"  # Remplacez l'emplacement actuel du poisson par de le requin
        
        
        
#Demandez à l'utilisateur combien de poissons il souhaite créer
nombre_de_requins = int(input("Combien de requins voulez-vous créer ? "))

# Créez une liste pour stocker les poissons
liste_de_requins = []

# Créez les poissons et ajoutez-les à la liste
for _ in range(nombre_de_requins):
    requin = Requin(random.randint(0, nb_lignes - 1), random.randint(0, nb_colonnes - 1))
    liste_de_requins.append(requin)
    
    
    




chronon = 0
chronon_reproduction = 0


# Affichez la grille initiale une fois
for row in grille:
    print("".join(row))


# Animation du déplacement du poisson
while True:


    #REPRODUCTION ET DEPLACEMENTS   

    # Nouvelle liste pour stocker les nouveaux poissons
    nouveaux_poissons = []
    nouveaux_requins = []

    for poisson in liste_de_poissons:
        for requin in liste_de_requins:
            if chronon_reproduction == 3:
                nouveau_poisson = Poisson(poisson.x, poisson.y)
                nouveau_requin = Requin(requin.x, requin.y)
                nouveaux_poissons.append(nouveau_poisson)
                nouveaux_requins.append(nouveau_requin)
                chronon_reproduction = 0
            
    # Ajoutez les nouveaux poissons à la liste existante
    liste_de_poissons.extend(nouveaux_poissons)
    liste_de_requins.extend(nouveaux_requins)
    
    Poisson.deplacements(poisson)
    
    for requin in liste_de_requins:
        requin.deplacements_requins() 
        
    

    # Déplacez le curseur vers le haut gauche de la console
    print("\033[H", end="")
    
    chronon += 1
    chronon_reproduction +=1
    
    print(f"{chronon_reproduction}/3 chronons passés pour la reproduction")
    print(f"Total poissons : {len(liste_de_poissons)}, Total de requins : {len(liste_de_requins)}")
    
    # Affichez la grille mise à jour
    for row in grille:
        print("".join(row))
    
    # Mettez en pause le programme pendant 1 seconde pour créer l'effet d'animation
    time.sleep(1)