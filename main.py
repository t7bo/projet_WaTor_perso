import time
from monde import *
from poisson import Poisson
from requin import Requin

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