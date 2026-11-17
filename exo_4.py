#==========================
# Question 1
#==========================
notes = [12.5, 14.0, 13.5, 16.0, 15.5, 17.0]
print("Première :", notes[0])
print("Dernière :", notes[-1])
print("3 premières :", notes[:3])

#==========================
# Question 2
#==========================
print(f"Max : {max(notes)} | Min : {min(notes)} | Moyenne : {sum(notes)/len(notes):.2f}")

#==========================
# Question 3
#==========================
notes.append(16.5)      
notes.pop(0)            
print("notes :", notes)

#==========================
# Question 4
#==========================
etudiants = [["Amina", 19, 14.5], ["Brice", 21, 12.0], ["Chloé", 20, 16.5]]
print("Nom du 2e étudiant :", etudiants[1][0])
moyenne_generale = sum(e[2] for e in etudiants) / len(etudiants)
print(f"Moyenne générale : {moyenne_generale:.2f}")         

#==========================
# Question 5
#==========================
original = [1, 2, 3]
copie = original.copy()
copie.append(99)
print("Original :", original)   
print("Copie :", copie)         