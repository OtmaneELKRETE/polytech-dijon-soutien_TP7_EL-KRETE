import Code
import Tentative

"""
Classe MasterMind permettant de lancer et gérer le jeu
"""
class MasterMind:

    """
    Constructeur de MasterMind
    """
    def __init__(self):
        self.code = Code.Code(4,12)
        self.tentative = Tentative.Tentative()
    """
    Déroulement d'une partie MasterMin
    """
    def partieMasterMind(self):
        print(f"Tu as {self.code.maxTentative} tentatives pour trouver le code de {self.code.longueur_code} couleurs")
        print (f"Voici les couleurs disponibles pour le jeux {self.code.couleurs.values()}")
        self.code.display()
        i=0
        while i<self.code.maxTentative and self.tentative.correct_compteur != self.code.longueur_code:
            self.tentative.propositionJoueur(self.code)
            self.tentative.affichageResutat(self.code,i)


MasterMind().partieMasterMind()