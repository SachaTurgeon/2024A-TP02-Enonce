"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
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

S_cote = []

for cote in bibliotheque:
    if cote[0] == "S" and bibliotheque[cote]["auteur"] == "William Shakespeare":
        S_cote.append(cote)

for cote in S_cote:
    nouvelle_cote = "WS" + cote[1:]
    bibliotheque[nouvelle_cote] = bibliotheque[cote]
    del bibliotheque[cote]

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






