#==========================
# Question 1 et 2
#==========================
class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6

    def afficher(self):
        print(f"{self.nom} : CC = {self.note_cc}, examen = {self.note_examen}")


#==========================
# Question 3
#==========================
class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        total = 0
        for e in self.etudiants:
            total += e.moyenne()
        return total / len(self.etudiants)


#==========================
# Question 4
#==========================
class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"Je suis {self.nom}, délégué(e) de la filière {self.filiere}."


#==========================
# Question 5
#==========================
groupe = Groupe()
groupe.ajouter(Etudiant("Amina", 12.0, 15.5))
groupe.ajouter(Etudiant("Brice", 10.0, 11.0))
groupe.ajouter(Etudiant("Chloé", 14.0, 16.0))

print(f"Moyenne générale : {groupe.moyenne_generale():.2f} / 20")    

meilleur = groupe.etudiants[0]
for e in groupe.etudiants:
    if e.moyenne() > meilleur.moyenne():
        meilleur = e
print(f"Meilleur étudiant : {meilleur.nom} ({meilleur.moyenne():.2f})")   

d = Delegue("David", 13.0, 14.0, "Génie Logiciel")
print(d.presenter())