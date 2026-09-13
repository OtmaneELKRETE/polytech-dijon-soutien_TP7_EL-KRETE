"""
Classe qui représente une tentative
"""
class Tentative:
    def __init__(self):
        self.correct_compteur = 0
        self.partiel_compteur = 0
        self.resultats = {
            "Correct": self.correct_compteur,
            "Partiel": self.partiel_compteur
        }

    """
    Gestion de la propostion d'un joueurs
    """
    def propositionJoueur(self,code):
        self.correct_compteur = 0
        self.partiel_compteur = 0
        self.resultats.clear()

        try:
            proposition = str(input("Proposez une solution avec uniquement les initials des couleurs ((R, V, B, J, M, N)) : " ))

            for i,couleur in enumerate(proposition):
                if code.couleurs[couleur].lower() == code.code[i].lower():
                    self.correct_compteur += 1
                    self.resultats["Correct"] = self.correct_compteur
                else:
                    for couleurCode in code.code:
                        if code.couleurs[couleur].lower() == couleurCode.lower():
                            self.partiel_compteur +=1
                            self.resultats["Partiel"] =  self.partiel_compteur

        except ValueError:
            print("Entrée invalide : la valeur saisie n'ai pas reconnu")


    def affichageResutat(self,code,tentative):
        tentative = code.maxTentative - (tentative + 1)
        if self.resultats:
            for cle,valeur in self.resultats.items():
                print(f"Voici le résultat à l'issue de ce tour : {cle} : {valeur}")
            print(f"il te reste encore {tentative} tentatives")
        else:
            print (f"Tu as eu aucune bonne proposition lors de ce tour , il te reste encore {tentative} tentatives")