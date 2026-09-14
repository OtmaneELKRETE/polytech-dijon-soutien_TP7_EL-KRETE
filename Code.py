import random

"""
Classe qui représente le code que l'on doit trouver dans le jeu MasterMind.
"""
class Code:

    """
    Constructor de la classe Code
    """
    def __init__(self, longueurCode, maxTentative):
        self.couleurs = {
            "R": "Rouge",
            "V": "Vert",
            "B": "Bleu",
            "J": "Jaune",
            "M": "Mauve",
            "N": "Noir"
        }
        self.longueur_code = longueurCode
        self.maxTentative = maxTentative
        self.code = self.generate_code()

    """
    Méthode pour générer un code aléatoire
    """
    def generate_code(self):
        leCode =[]
        for i in range(self.longueur_code):
            lettre = random.choice(list(self.couleurs.values()))
            leCode.append(lettre)        

        return leCode

    """
    Affichage du code secret
    """     
    def display(self):
        return self.code
