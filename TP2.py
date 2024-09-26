"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  21
Noms et matricules : Sacha Turgeon (2373772), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici

import csv

collection_bibliotheque_file = open("collection_bibliotheque.csv", newline="")
collection_bibliotheque = csv.reader(collection_bibliotheque_file)

bibliotheque = {}
for index, row in enumerate(collection_bibliotheque):
    if index != 0:
        bibliotheque[row[3]] = {"titre": row[0], "auteur": row[1], "date_publication": row[2]}

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

nouvelle_collection_file = open("nouvelle_collection.csv", newline="")
nouvelle_collection = csv.reader(nouvelle_collection_file)

for index, row in enumerate(nouvelle_collection):
    if index != 0:
        if row[3] in bibliotheque:
            print(f"Le livre {row[3]} ---- {row[0]} par {row[1]} ---- est déjà présent dans la bibliothèque")
        else:
            bibliotheque[row[3]] = {"titre": row[0], "auteur": row[1], "date_publication": row[2]}
            print(f"Le livre {row[3]} ---- {row[0]} par {row[1]} ---- a été ajouté avec succès")

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

SW_cote = []

for cote in bibliotheque:
    if cote[0] == "S" and bibliotheque[cote]["auteur"] == "William Shakespeare":
        SW_cote.append(cote)

for cote in SW_cote:
    nouvelle_cote = "WS" + cote[1:]
    bibliotheque[nouvelle_cote] = bibliotheque[cote]
    del bibliotheque[cote]

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

emprunts_file = open("emprunts.csv", newline="")
emprunts = csv.reader(emprunts_file)

liste_emprunts = []
for emprunt in emprunts:
    liste_emprunts.append(emprunt)

for cote in bibliotheque:
    for emprunt in liste_emprunts:
        if cote == emprunt[0]:
            bibliotheque[cote]["emprunts"] = "emprunté"
            bibliotheque[cote]["date_emprunt"] = emprunt[1]
            break
    else:
        bibliotheque[cote]["emprunts"] = "disponible"
        bibliotheque[cote]["date_emprunt"] = None

print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

import datetime

for cote in bibliotheque:
    for emprunt in liste_emprunts:
        if cote == emprunt[0]:
            date = emprunt[1].split("-")
            retard = datetime.date.today() - datetime.date(int(date[0]), int(date[1]), int(date[2]))
            frais = 0
            if retard > datetime.timedelta(days = 365):
                bibliotheque[cote]["frais_retard"] = 100
                bibliotheque[cote]["livres_perdus"] = True
                print(f"{cote} est en retard avec un frais de 100$")
                break
            elif retard > datetime.timedelta(days = 30):
                frais += (retard.days - 30) * 2
                if frais <= 100:
                    bibliotheque[cote]["frais_retard"] = frais
                    bibliotheque[cote]["livres_perdus"] = False
                    print(f"{cote} est en retard avec un frais de {frais}$")
                    break
                else:
                    bibliotheque[cote]["frais_retard"] = 100
                    bibliotheque[cote]["livres_perdus"] = False
                    print(f"{cote} est en retard avec un frais de 100$")
                    break
            else:
                bibliotheque[cote]["frais_retard"] = 0
                bibliotheque[cote]["livres_perdus"] = False
                break
    else:
        bibliotheque[cote]["frais_retard"] = None
        bibliotheque[cote]["livres_perdus"] = False

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')
