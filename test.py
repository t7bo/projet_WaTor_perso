import time
import pygame, sys
import random

class Animaux:

    def __init__(self, image = pygame.image.load('img/poisson1.png')): #, chronon, chronon_count, chronon_count_reproduction, chronon_count_requins):
        self.image = image
        #self.pos = image.get_rect().move(0, height)
        # self.chronon = chronon
        # self.chronon_count = chronon_count
        # self.chronon_count_reproduction = chronon_count_reproduction
        # self.chronon_count_requins = chronon_count_requins

    def deplacement(self): #si dépasse 1000 (taille max) alors retourne à gauche à 0

        # self.pos = self.pos.move(self.speed, 0)
        # if self.pos.right > max(WIDTH):
        #     self.pos.left = 0

        # directions possibles pour le déplacement, ce sera jamais 0 0 car c'est le parent
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        random.shuffle(directions)  # Mélanger les directions pour choisir au hasard

        # à modifier dans poisson et dans requin


    def timer(self):

        while self.chronon_count < 2:
            for seconds in range(1, self.chronon+1):
                print(seconds)
                time.sleep(1)
            
            self.chronon_count += 1
            self.chronon_count_reproduction += 1
            # self.energie -= 1 (pour les requins uniquement)
            print(f"Un nouveau jour vient de passer, ({self.chronon_count} chronon(s))")
            time.sleep(2) #temps d'attente entre chaque chronon/jour

# temps = time.time() 
# temps.timer(5)



class Poisson(Animaux):

    def __init__(self, x, y, image_poisson = pygame.image.load('img/poisson1.png')): #image, element par défaut donc dernier argument
        Animaux.__init__(self)
        # super().__init__()


        self.image_poisson = image_poisson
        self.x = x
        self.y = y
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.temps_reproduction_poisson = 0  # age du poisson en chronons


    def deplacement(self):

        deplacement_poisson = super().deplacement()
        
        # if not pygame.Rect.contains(image_poisson):
        #     deplacement_poisson

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        random.shuffle(directions)  # Mélanger les directions pour choisir au hasard

        ancienne_position_x = self.rect.x
        ancienne_position_y = self.rect.y

        for dx, dy in directions:
            nouvelle_position_x = self.rect.x + dx * CASE_SIZE
            nouvelle_position_y = self.rect.y + dy * CASE_SIZE

            # # #gerer le tp
            # if nouvelle_position_x > largeur 

            if (0 <= nouvelle_position_x < WIDTH and 0 <= nouvelle_position_y < HEIGHT and 
                not grille[nouvelle_position_y // CASE_SIZE][nouvelle_position_x // CASE_SIZE]):

                # Libérer l'ancienne position
                grille[ancienne_position_y // CASE_SIZE][ancienne_position_x // CASE_SIZE] = False

                # Mettre à jour la nouvelle position
                grille[nouvelle_position_y // CASE_SIZE][nouvelle_position_x // CASE_SIZE] = True
                self.rect.x = nouvelle_position_x
                self.rect.y = nouvelle_position_y
                break  # Arrêter après avoir trouvé une position libre

    def update(self):
        self.deplacement()

    


    # def afficher_poisson(self):

    #     x = (WIDTH/10 - image_poisson_largeur) // 2 #pour centrer dans la case //2
    #     y = (HEIGHT/10 - image_poisson_hauteur) // 2 #pour centrer dans la case //2


    #     case_x = random.randint(0, WIDTH // (WIDTH*0.1) - 1) * (WIDTH*0.1)
    #     case_y = random.randint(0, HEIGHT // (HEIGHT*0.1) - 1) * (HEIGHT*0.1)



    #     coordinates = [i for i in range(0, 1001, 100)]

    #     # fish_position_x = random.randint(min(coordinates), max(coordinates))
    #     # fish_position_y = random.randint(min(coordinates), max(coordinates))


    #     fish_position = case_x, case_y
        
    #     fish = Poisson(self.image_poisson, (case_x*x), (case_y*y))
    #     screen.blit(self.image_poisson, fish_position)






class Requins(Animaux):

    def __init__(self, chronon, chronon_count, energie, requin, chronon_count_requins):
        Animaux.__init__(self, chronon, chronon_count, chronon_count_requins)
        self.energie = energie
    
    def reproduction(self, chronon_count, energie):
        reproduction_requins = super().reproduction(chronon_count)
        energie -= 1

    #def mort(self, chronon_count, energie):
       # if energie == 0: #or (self.chronon_count >= 4 and compteur nourriture requin == 0):
                            

    #def nourriture(self, chronon_count, energie, poissons_manges):
        # if poisson and requin dans la même case
            # requin mange poisson (poisson.kill())
            # energie += 1

        # elif energie == 0 or (self.chronon_count >= 4 and compteur nourriture requin == 0):
            # requin.kill()












#   GRILLE

pygame.init()

WIDTH = HEIGHT = 1000
#grille = pygame.Surface((WIDTH, HEIGHT))



screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(pygame.Color("white"))


grille = screen.copy()





#color borders cases
color = (0,0,0) #black







# CREATION DES POISSONS

image_poisson = pygame.image.load('img/poisson1.png')
image_poisson_largeur, image_poisson_hauteur = image_poisson.get_size()


positions_poissons = []

fish_number = 5

for num in range(fish_number):

    CASE_SIZE = WIDTH/10

    x = (CASE_SIZE - image_poisson_largeur) // 2 #pour centrer dans la case //2
    y = (CASE_SIZE - image_poisson_hauteur) // 2 #pour centrer dans la case //2

    coordinates = [i for i in range(0, 1001, 100)]

    fish_position_x = random.randint(min(coordinates), max(coordinates)) 
    fish_position_y = random.randint(min(coordinates), max(coordinates))

    fish_position = (fish_position_x, fish_position_y)
        
    case_x = random.randint(0, WIDTH // CASE_SIZE - 1) * CASE_SIZE
    case_y = random.randint(0, HEIGHT // CASE_SIZE - 1) * CASE_SIZE

    objet_poisson = screen.blit(image_poisson, (case_x + x, case_y + y))
    objet_poisson

# Dessiner l'image centrée dans la case












# BOUCLE PRINCIPALE > JEU


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()
            exit()

    poisson_test = Poisson(fish_position_x,fish_position_y)
    poisson_test.update()

    for x in range(0, WIDTH, 100): #grille de 10 cases 100x100
        pygame.draw.line(screen, color, (1,x), (WIDTH,x), 2)
        pygame.draw.line(screen, color, (x,1), (x,HEIGHT), 2)






    
    pygame.display.update()
    




    # screen.blit(fish,(pygame.Surface.get_width(screen)*0.1,pygame.Surface.get_width(screen)*0.1))
    # position = fish.get_rect()
    # new_position = fish.move((pygame.Surface.get_width(screen)*0.3), (pygame.Surface.get_width(screen)*0.3))
    # screen.blit()