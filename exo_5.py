notes = [8, 12, 15, 17, 10, 6]

#==========================
# Question 1
#==========================
compteur = 0
for n in notes:
    if n >= 10:
        compteur += 1
print("Notes >= 10 :", compteur)       

#==========================
# Question 2
#==========================
for n in notes:
    if n < 10:
        print(n, "ÉCHEC")
    elif n >= 14:
        print(n, "MENTION")
    else:
        print(n, "PASSABLE")

#==========================
# Question 3
#==========================
score = 40
semaines = 0
while score <= 60:
    score = score * 1.03
    semaines += 1
print(f"{semaines} semaines nécessaires (score : {score:.2f})")   

#==========================
# Question 4
#==========================
notes_cc = [10, 12, 14, 9]
notes_examen = [12, 11, 15, 9]
for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print(f"Étudiant {i+1} : PROGRESSION")
    else:
        print(f"Étudiant {i+1} : PAS DE PROGRESSION")