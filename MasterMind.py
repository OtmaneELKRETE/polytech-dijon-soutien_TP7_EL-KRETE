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
        self.code = Code.Code(4,2)
        self.tentative = Tentative.Tentative()

    """
    Gestion du jeu
    """
    def jouabilite(self):
        print("1. Jouer") 
        print("2. Remettre à zéro les statistiques") 
        print("3. Quitter")

        valeur = self.verifSaisie()

        if valeur == 1:
            while valeur == 1:
                self.resetParam()
                ## Affichage sauvegarde
                self.partieMasterMind()
                print("1. Rejouer") 
                print("2. Remettre à zéro les statistiques") 
                print("3. Quitter")

                valeur = self.verifSaisie()
        elif valeur == 2:
            ## Gestion logique suppression fichier statistique (le vider)
            pass
        else:
            ## Gestion logique sauvegarde
            pass

    """
    Permet de réinitialiser les paramètres
    """
    def resetParam(self):
        self.code = Code.Code(4,2)
        self.tentative = Tentative.Tentative()
    """
    Déroulement d'une partie MasterMin
    """
    def partieMasterMind(self):
        print(f"Tu as {self.code.maxTentative} tentatives pour trouver le code de {self.code.longueur_code} couleurs")
        print(f"Voici les couleurs disponibles pour le jeux {self.code.couleurs.values()}")
        print(f"Code : {self.code.display()}")
        i=0
        while i<self.code.maxTentative and self.tentative.correct_compteur != self.code.longueur_code:
            self.tentative.propositionJoueur(self.code)
            self.tentative.affichageResutat(self.code,i)
            i+=1

        self.tentative.gestionDéfaite(self.code,i)

    """
    Permet de vérifier les saisies 
    """
    def verifSaisie(self):
        try:
            valeur = int(input("Faites votre choix en séléctionnant 1 2 ou 3 : "))
            return valeur
        except ValueError:
            print("Erreur de saisie, vous avez saisit une valeur invalide")

MasterMind().jouabilite()