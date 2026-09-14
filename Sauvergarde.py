"""
Classe permettant de gérer la sauvegarde
"""
class Sauvegarde:

    """
    Constructeur de Sauvegarde
    """
    def __init__(self):
        self.parties_jouees=0
        self.parties_gagnees=0
        self.score = 0

        self.analyseScore()

    """
    Permet d'écrire dans le fichier .txt
    """
    def ecrireScore(self):
        if self.parties_jouees !=0: 
            self.score = self.parties_gagnees/self.parties_jouees
        with open("resultats.txt", "w", encoding="utf-8") as fichier:
            fichier.write(f"Parties jouées: {self.parties_jouees} | Parties gagnées: {self.parties_gagnees} | Score: {self.score}\n")

    """
    Permet de lire dans le fichier .txt
    """
    def lireScore(self):
        try:
            with open("resultats.txt", "r", encoding="utf-8") as fichier:
                valeur = fichier.read() 
        except FileNotFoundError:
            valeur = 0
            self.ecrireScore()

        return valeur

    """
    Analyse du score dans le fichier texte et récupération
    """
    def analyseScore(self):
        res = self.lireScore()

        if res != 0:
            for kObjet in res.split("|"):
                kObjet = kObjet.strip()
                key,value = kObjet.split(':')
                if key.__contains__("jouées"):
                    if int(value) != 0:
                        self.parties_jouees = int(value.strip())
                    else:
                        self.parties_jouees = 1
                elif key.__contains__("gagnées"):
                    self.parties_gagnees = int(value.strip())
                else:
                    self.score = self.parties_gagnees/self.parties_jouees

    """
    Permet de réinitialiser le score
    """
    def reinitialiserScore(self):
        self.parties_jouees=0
        self.parties_gagnees=0
        self.score=0