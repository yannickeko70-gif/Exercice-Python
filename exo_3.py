#==========================
# Question 1
#==========================
print(f"Le serveur de l'école stocke {3.10e+12} octets de données pour 412 étudiants inscrits.")

#==========================
# Question 2
#==========================
nb_etudiants = "50"
temps_par_copie = 12.4
temps_total = int(nb_etudiants) * temps_par_copie
print("Le temps est de : ", temps_total)                              

#==========================
# Question 3
#==========================
releve = [("Amina", 12, 14.75), ("Brice", 10, 13.5)]
print("Affichage de relevé : ")
for nom, credits, note in releve:
    print(f"{nom:<8}{credits:>5}{note:>10.2f} / 20")