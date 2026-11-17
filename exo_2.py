# 2.10

#==========================
# Question 1
#==========================
note_cc = 12
note_examen = 15
coef_examen = 0.6
moyenne_ponderee = note_cc * (1 - coef_examen) + note_examen * coef_examen
print("Moyenne pondérée est de :", moyenne_ponderee, "%")            

#==========================
# Question 2
#==========================
somme_notes = 187.5
nb_copies = 15
note_validation = 10
moyenne_classe = somme_notes / nb_copies
print("Moyenne de la classe :", moyenne_classe)             
print("Écart avec la validation :", moyenne_classe - note_validation)  

#==========================
# Question 3
#==========================
note_str = "16.75"
print(float(note_str) * 3)                      

#==========================
# Question 4
#==========================
print("Meilleure note :", max(15.10, 15.04))    