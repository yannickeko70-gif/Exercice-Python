#==========================
# Question 1
#==========================
def calculer_moyenne_classe(classe):
    total = 0
    for e in classe:
        total += e["note_cc"] * 0.4 + e["note_examen"] * 0.6
    return total / len(classe)

#==========================
# Question 2
#==========================
def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    if note >= seuil_bien:
        return "BIEN"
    return "PASSABLE"

#==========================
# Question 3
#==========================
def statistiques(notes):
    return sum(notes) / len(notes), min(notes), max(notes)   

#==========================
# Question 4
#==========================
def compter_reussites(notes, seuil=10):
    compteur = 0
    for n in notes:
        if n >= seuil:
            compteur += 1
    return compteur

#==========================
# Question 5
#==========================
classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
]
print(calculer_moyenne_classe(classe))              
print(mention(8), mention(12), mention(15))         
moyenne, mini, maxi = statistiques([12.5, 14.0, 13.5, 16.0, 15.5])
print(moyenne, mini, maxi)
print(compter_reussites([8, 12, 15, 17, 10, 6]))    