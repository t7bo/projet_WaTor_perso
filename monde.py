class Monde:

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

# Création d'une instance de Monde
monde = Monde(20, 10)  # Largeur et hauteur du monde

# Initialisation de la grille
grille = [["💧" for _ in range(monde.largeur)] for _ in range(monde.hauteur)]