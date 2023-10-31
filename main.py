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

    # rajouter "nb_poissons", "nb_requins", "temps de reproduction pour poissons et requins, energie..." avec des self.

    # def afficher le monde(self, sleep_time=1):
        
        # grille_copy = copy.deepcopy(self.grille)

        #     for y in range(self.hauteur):
        #         for x in range(self.largeur):
        #             if grille[y][x].__class__ is Poisson:
        #                 grille[y][x] = "poisson emoji"

    # def peupler le monde
        # lister les coordonnées possibles

        # coordonnes = []
        # for y in range (self.hauteur):
        # for x in range (self.largeur)
             # coordonnes.append((y, x))

    # coordonnes_requins : random.sample(coordonnées, self.nb, self.nb_poissons)
    
        #for coordonnes_poisson in coordonnes_poissons:
            #coordonnes.remove(coordonnes_poisson)

        # for y, x in coordonnes_poissons:
        # print(x,y)
        # poisson = Poisson(coordonnees=(y,x), temps_de_reproduction=())

        #déplacements requins en 1er et ensuite les poissons
        # deux déplacements différents, pas en mm temps
        # donc deux chronons différents?

        # tirer une séquence de l'aimant , séquences différentes de coordonnées (aucune coordonnée identique avec sample)
        

class Poisson(Animaux):
    
    def __init__(self, x, y, fish="🐠"):
        super().__init__(x, y)  # Appelez le constructeur de la classe parente avec les arguments x et y
        self.fish = fish

    def __str__(self):
        return self.fish
    

    # ajouter chronon_reproduction

    # def cases_vides_adjacentes(self, Animaux)         PAS DE DIAGONALES, juste haut, bas, gauche, droite

        #haut = (self.y+1) % Animaux.hauteur
        #bas = (self.y-1) % Animaux.hauteur
        #droite = (self.x+1) % Animaux.largeur
        #gauche = (self.y-1) % Animayx.largeur

        
        #refaire 3 fois avec les modulos pour gérer les bords de la grille
    




    # def cases_poissons_adjacentes (pour classe Requin)
    #     cases_poissons = []
    #     haut = (self.y-1)% monde.hauteur
    #     bas = (self.y+1)% monde.hauteur
    #     gauche (self.x-1)% monde.largeur
    #     droite = (self.x+1) % monde.largeur
    
    #     if monde.grille[haut][self.x].__class__ is Poisson:
        # or if monde.grille[haut][self.x] == 0: #0 veut dire case vide, donc nous on remplace 0 par la goutte d'eau
        #     liste_de_coordonnes_possibles.append((haut, self.x))
        
        # if monde.grille[self.y][gauche] == 0:
        
    

    # def se_deplacer(self, animaux, actions_possibles:list, *args, **kwargs)
        #energie = kwargs.get("energie", None)          #pour les requins uniquement mais dans la classe poisson

        # if not len(actions_possibles):            (si pas de coordonnées adjacentes dispo, si liste de coordonnées vides, alors arrête fonction, ne fais rien,  alors return rien, il reste sur placr)
        #     return
        # else:
        #     y, x = random.choice(actions_possibles)


        # liste de coordonnes possibles.append(self.y, gauche) ?????????????

        #retuern liste_de_coordonnes_possibles


        # if self.chronon_reproduction > ...:
            # if self.__class__ is Poisson:
                #self.se_reproduite(monde=monde, animal=Poisson(coordonnes=(self.y, self.x), chrnonon_reproduction=animaux.chronon_reproduction), y_target=y, x_target=x)

        #return super().se_deplacer ....




    #def se reproduire(self, animal, y_target: int, x_target: int)

        # nouvelle_entite = animal

        # Animaux.grille(self,y][self.x] ) nouvelle entite

        # if animal.__class__ is Poisson:
        #     monde.liste_poissons.append(nouvelle_entite)
        # else: 
        #     monde.liste_requins.append(nouvele_entite)


        # monde.grille[y_target][x_target] = self       (self = un poisson parce qu'on est dans la classe poisson)
        # self.y = y_target
        # self.x = x_target

        # self.chronon_reproduction = 0
         
    def deplacements(self):
        
        global grille

        #for poisson in liste_de_poissons:
        for poisson in liste_de_poissons:

            indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y), (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
            nouvel_x, nouvel_y = random.choice(indices_adjacents)


        #nouvel_x, nouvel_y = self.x, self.y


            if nouvel_x > 0 and nouvel_x < nb_colonnes:

                indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y),
                                (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
            
                nouvel_x, nouvel_y = random.choice(indices_adjacents)

            if nouvel_x < 0:
                nouvel_x = nb_colonnes-1
            
            if nouvel_x > nb_colonnes-1:
                nouvel_x = 0

            if nouvel_y < 0:
                nouvel_y = nb_lignes 

            if nouvel_y > nb_lignes:
                nouvel_y = 0



            # #if poisson.x != poisson[-1] and poisson.y != poisson[-1]:
            # if poisson.x % nb_colonnes == 0 and poisson.y % nb_colonnes == 0:

            #     indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y),
            #                         (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
                
            #     nouvel_x, nouvel_y = random.choice(indices_adjacents)


            # elif poisson.x % nb_colonnes != 0 and poisson.y % nb_colonnes == 0:

            #     indices_y = [poisson.y, poisson.y-1, poisson.y+1]

            #     modulo_x = poisson.x%nb_colonnes
            #     nouvel_x = modulo_x
            #     nouvel_y = random.choice(indices_y)


            # elif poisson.x % nb_colonnes == 0 and poisson.y % nb_colonnes != 0:

            #     indices_x = [poisson.x, poisson.x-1, poisson.x+1]

            #     modulo_y = poisson.y%nb_colonnes
            #     nouvel_x = random.choice(indices_x)
            #     nouvel_y = modulo_y

        
            # Liste des indices adjacents valides pour le poisson
            #indices_adjacents = [(poisson.x-1, poisson.y), (poisson.x+1, poisson.y),
                               # (poisson.x, poisson.y-1), (poisson.x, poisson.y+1)]
            
            # Sélectionnez un indice aléatoire parmi les indices adjacents
            #nouvel_x, nouvel_y = random.choice(indices_adjacents)
        
            # Si le nouvel emplacement est valide dans la grille

        #if 0 <= nouvel_x < nb_lignes and 0 <= nouvel_y < nb_colonnes and grille[nouvel_x][nouvel_y] == "💧":
        if grille[nouvel_x][nouvel_y] == "💧":
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

            indices_adjacents_requins = [(requin.x-1, requin.y), (requin.x+1, requin.y), (requin.x, requin.y-1), (requin.x, requin.y+1)]
            nouvel_x_r, nouvel_y_r = random.choice(indices_adjacents_requins)

            if nouvel_x_r < 0:
                nouvel_x_r = nb_colonnes
            
            if nouvel_x_r > nb_colonnes:
                nouvel_x_r = 0

            if nouvel_y_r < 0:
                nouvel_y_r = nb_lignes 

            if nouvel_y_r > nb_lignes:
                nouvel_y_r = 0
        
            # if requin.x % nb_colonnes and requin.y % nb_colonnes == 0:
            #     indices_adjacents_requins = [(requin.x-1, requin.y), (requin.x+1, requin.y),
            #                     (requin.x, requin.y-1), (requin.x, requin.y+1)]
            #     nouvel_x_r, nouvel_y_r = random.choice(indices_adjacents_requins)

            # elif requin.x % nb_colonnes != 0 and requin.y % nb_colonnes == 0:

            #     indices_y_r = [requin.y, requin.y-1, requin.y+1]

            #     modulo_x_r = requin.x % nb_colonnes
            #     nouvel_x_r = modulo_x_r
            #     nouvel_y_r = random.choice(indices_y_r)

            # elif requin.y % nb_colonnes == 0 and requin.y % nb_colonnes != 0:

            #     indices_x_r = [requin.x, requin.x-1, requin.x+1]
            #     modulo_y_r = requin.y%nb_colonnes
            #     nouvel_x_r = random.choice(indices_x_r)
            #     nouvel_y_r = modulo_y_r


            # print(nouvel_x_r)

            # Sélectionnez un indice aléatoire parmi les indices adjacents
            #nouvel_x_r, nouvel_y_r = random.choice(indices_adjacents_requins)
            
        
        # if 0 <= nouvel_x_r < nb_lignes and 0 <= nouvel_y_r < nb_colonnes and grille[nouvel_x_r][nouvel_y_r] == "🐠":
        #     grille[requin.x][requin.y] = "💧"  # Remplacez l'emplacement actuel du requin par de l'eau
        #     requin.x, requin.y = poisson.x, poisson.y
        #     liste_de_poissons.pop()
        #     grille[requin.x][requin.y] = "🦈"  # Remplacez l'emplacement actuel du poisson par de le requin

        if 0 <= nouvel_x_r < nb_lignes and 0 <= nouvel_y_r < nb_colonnes and grille[nouvel_x_r][nouvel_y_r] == "💧":
                # Déplacez le requin
                grille[requin.x][requin.y] = "💧"  # Remplacez l'emplacement actuel du requin par de l'eau
                requin.x, requin.y = nouvel_x_r, nouvel_y_r  # Mettez à jour les indices du requin
                grille[requin.x][requin.y] ="🦈"  # Mettez à jour la grille avec le nouveau emplacement du poisson  



        # if monde.grille[y][x].__class__ is Poisson and self.__class__ is Requin:
        #     monde.liste_de_poissons.remove(monde.grille[y_target][x_target])
        
        # self.y = y_target
        # self.x = x_target
        # monde.grille[y_target][x_target] = self
        


        
        
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
    
    poisson.deplacements()
    
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