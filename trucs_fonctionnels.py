import random
import fichier_principal
import time
import copy


class Monde():

    def __init__(self, nb_lignes, nb_colonnes):
    
        # Dimensions de la grille
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes

        # Initialisation de la grille
        self.grille = [["💧" for _ in range(self.nb_colonnes)] for _ in range(self.nb_lignes)]

        # self.nb_poissons = nb_poissons
        # self.nb_requins = nb_requins
        # self.chronon = chronon
        # self.chronon_reproduction_poisson = chronon_reproduction_poisson
        # self.chronon_reproduction_requin = chronon_reproduction_requin
        # self.energie = energie


    def afficher_monde(self, sleep_time=1):
        
        grille_copy = copy.deepcopy(self.grille)

        for y in range(self.nb_lignes):
            for x in range(self.nb_colonnes):
                if grille_copy[y][x].__class__ is Poisson:
                    grille_copy[y][x] = "🐠"


    def peupler_le_monde(self):
    
    # lister les coordonnées possibles dans toute la grille

        coordonnees = []
        for y in range (self.nb_lignes):
            for x in range (self.nb_colonnes):
                coordonnees.append((y, x))






















class Poisson(Monde):
    
    def __init__(self, x, y, fish="🐠"):
        super().__init__()  # Appelez le constructeur de la classe parente avec les arguments x et y
        self.x = x
        self.y = y
        self.fish = fish

    def __str__(self):
        return self.fish


    # ajouter chronon_reproduction

    def cases_vides_adjacentes(self):       #pour le déplacement des poissons

        haut = (self.y-1) % Monde.nb_lignes
        bas = (self.y+1) % Monde.nb_lignes
        droite = (self.x+1) % Monde.nb_colonnes
        gauche = (self.x-1) % Monde.nb_colonnes


    def cases_poissons_adjacentes(self): #(pour classe Requin)

        cases_poissons = []
    
        haut = (self.y-1)% Monde.nb_lignes
        bas = (self.y+1)% Monde.nb_lignes
        gauche = (self.x-1)% Monde.nb_colonnes
        droite = (self.x+1) % Monde.nb_colonnes
    
        if Monde.grille[haut][self.x].__class__ is Poisson:
        # or if monde.grille[haut][self.x] == 0: #0 veut dire case vide, donc nous on remplace 0 par la goutte d'eau
            cases_poissons.append((haut, self.x))

        if Monde.grille[bas][self.x].__class__ is Poisson:
            cases_poissons.append((bas, self.x))

        if Monde.grille[self.y][gauche].__class__ is Poisson:
            cases_poissons.append((self.y, gauche))

        if Monde.grille[self.y][droite].__class__ is Poisson:
            cases_poissons.append((self.y, droite))




    # def se_deplacer(self, animaux, actions_possibles:list, *args, **kwargs):
    #         energie = kwargs.get("energie", None)          #pour les requins uniquement mais dans la classe poisson

    #         if not len(actions_possibles):            #(si pas de coordonnées adjacentes dispo, si liste de coordonnées vides, alors arrête fonction, ne fais rien,  alors return rien, il reste sur placr)
    #             return
    #         else:
    #             y, x = random.choice(actions_possibles)


    #         liste de coordonnes possibles.append(self.y, gauche) 

    #         retuern liste_de_coordonnes_possibles


    #         if self.chronon_reproduction > ...:
    #             if self.__class__ is Poisson:
    #                 self.se_reproduite(monde=monde, animal=Poisson(coordonnes=(self.y, self.x), chrnonon_reproduction=animaux.chronon_reproduction), y_target=y, x_target=x)

    #         return super().se_deplacer ....



    def deplacements(self):
        
        global grille
        
        for poisson in liste_de_poissons:
        
            # Liste des indices adjacents valides pour le poisson
            indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y),
                                (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
            
            # Sélectionnez un indice aléatoire parmi les indices adjacents
            nouvel_x, nouvel_y = random.choice(indices_adjacents)
        
            # Si le nouvel emplacement est valide dans la grille
            if 0 <= nouvel_x < self.nb_lignes and 0 <= nouvel_y < self.nb_colonnes and self.grille[nouvel_x][nouvel_y] == "💧":
                # Déplacez le poisson
                grille[poisson.x][poisson.y] = "💧"  # Remplacez l'emplacement actuel du poisson par de l'eau
                poisson.x, poisson.y = nouvel_x, nouvel_y  # Mettez à jour les indices du poisson
                grille[poisson.x][poisson.y] = "🐠"  # Mettez à jour la grille avec le nouveau emplacement du poisson



        
        # if monde.grille[self.y][gauche] == 0:
        
    def se_deplacer(self, animaux, actions_possibles:list, *args, **kwargs)
            #energie = kwargs.get("energie", None)          #pour les requins uniquement mais dans la classe poisson

            # if not len(actions_possibles):            (si pas de coordonnées adjacentes dispo, si liste de coordonnées vides, alors arrête fonction, ne fais rien,  alors return rien, il reste sur placr)
            #     return
            # else:
            #     y, x = random.choice(actions_possibles)


            # liste de coordonnes possibles.append(self.y, gauche) ?????????????

            #retuern liste_de_coordonnes_possibles


























class Requin(Monde):

    def __init__(self, x, y, shark="🦈"):
        super().__init__()  # Appelez le constructeur de la classe parente avec les arguments x et y
        self.x = x
        self.y = y
        self.shark = shark

    def __str__(self):
        return self.shark
    



