"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  21
Noms et matricules : Édouard Renaud (2384807), Nom2 (Matricule2)
"""
import csv
import datetime
########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 
#(titre,auteur,année,cote)
# TODO : Écrire votre code ici
csvfileCollectionDeBase = open('collection_bibliotheque.csv')
FilereadCDB=csv.reader(csvfileCollectionDeBase)
bibliotheque=dict()
for row in FilereadCDB:
    bibliotheque[row[3]]={"titre":row[0], "auteur":row[1], "année":row[2]}
print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfileNouvelleCollection=open("nouvelle_collection.csv")
FilereadNC=csv.reader(csvfileNouvelleCollection)
for row in FilereadNC:
    if(not row[3] in bibliotheque):
        bibliotheque[row[3]]={"titre":row[0], "auteur":row[1], "année":row[2]}
        print(f"Le livre {row[3]} ---- {row[0]} par {row[1]} ---- a été ajouté avec succès")
    else:
        print(f"Le livre {row[3]} ---- {row[0]} par {row[1]} ---- est déjà présent dans la bibliothèque")

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
listValeursÀModifier=[]
for clé in bibliotheque:
    if(bibliotheque[clé]["auteur"]=="William Shakespeare"):
        listValeursÀModifier.append(clé)
for clé in listValeursÀModifier:
    value=bibliotheque.pop(clé)
    bibliotheque["W"+clé]=value
print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')
########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici
csvfileEmprunts=open("emprunts.csv")
FileReadEmprunts=csv.reader(csvfileEmprunts)
for cote in bibliotheque:
    bibliotheque[cote]["emprunts"]="disponible"
for row in FileReadEmprunts:
    bibliotheque[row[0]]["emprunts"]="emprunté"
    bibliotheque[row[0]]["date_emprunt"]=row[1]


print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')
########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

for cote in bibliotheque:
    if(bibliotheque[cote]["emprunts"]=="emprunté"):
        dateEmprunt=datetime.date(year=int(bibliotheque[cote]["date_emprunt"][0:4]),month=int(bibliotheque[cote]["date_emprunt"][5:7]),day=int(bibliotheque[cote]["date_emprunt"][8:10]))
        nbJoursEmprunt=(datetime.date.today()-dateEmprunt).days
        if(nbJoursEmprunt>30):
            bibliotheque[cote]["frais-retard"]=f"{min(100,(nbJoursEmprunt-30)*2)}$"
            print(f"Le livre {cote} ---- {bibliotheque[cote]['titre']} par {bibliotheque[cote]['auteur']} ---- est en retard. Frais de retard : {bibliotheque[cote]['frais-retard']}")
            if(nbJoursEmprunt>=365):
                bibliotheque[cote]["livre_perdus"]="livre_perdu"
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')







