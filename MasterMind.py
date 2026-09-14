import Code
import Tentative
import Sauvergarde

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
        self.sauvergarde = Sauvergarde.Sauvegarde()

    """
    Gestion du jeu
    """
    def jouabilite(self):
        print(f"Voici votre historique de score : {self.sauvergarde.lireScore()}")
        print("1. Jouer") 
        print("2. Remettre à zéro les statistiques") 
        print("3. Quitter")

        valeur = self.verifSaisie()

        while valeur<3 and valeur>0:
            if valeur == 1:   
                print(f"Voici votre historique de score : {self.sauvergarde.lireScore()}")        
                self.resetParam()
                self.partieMasterMind()
                print("1. Rejouer") 
                print("2. Remettre à zéro les statistiques") 
                print("3. Quitter")

                valeur = self.verifSaisie()
                self.sauvergarde.parties_jouees+=1
                self.sauvergarde.ecrireScore()
            elif valeur == 2:
                self.sauvergarde.reinitialiserScore()
                self.sauvergarde.ecrireScore()
                print("1. Rejouer") 
                print("2. Remettre à zéro les statistiques") 
                print("3. Quitter")

                valeur = self.verifSaisie()
            else:
                print("Mauvaise saisie !")

        if valeur == 3:
            print("Au revoir !")
                
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
            self.tentative.affichageResutat(self.code,i,self.sauvergarde)
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