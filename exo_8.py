#==========================
# Question 1
#==========================
etudiant = {"nom": "Amina", "age": 20, "filiere": "Génie Logiciel", "moyenne": 14.3}
for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")

#==========================
# Question 2
#==========================
classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
    {"nom": "Chloé", "note_cc": 14.0, "note_examen": 16.0},
]
total = 0
for e in classe:
    m = e["note_cc"] * 0.4 + e["note_examen"] * 0.6
    total += m
    print(f"{e['nom']} : {m:.2f} / 20")
print(f"Moyenne générale de la classe : {total / len(classe):.2f} / 20")   

#==========================
# Question 3
#==========================
bulletins = [(10.5, 17.5, 14.2), (9.0, 16.0, 12.8), (11.0, 18.0, 15.1)]
for note_min, note_max, moyenne in bulletins:
    print(f"Écart : {note_max - note_min:.2f}")

#==========================
# Question 4
#==========================
print(etudiant.get("mention", "aucune"))        