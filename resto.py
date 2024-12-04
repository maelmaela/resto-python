import os
import time

def clear():
    time.sleep(2)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

filename = r'resto.txt'
userfile = r'user.txt'
modeOuverture = 'r'
modeAjout = 'a'
modeEcriture = 'w'


def Menu_Principal():
    print("Faite votre choix \n")
    print("*" *50)
    print("1- Afficher les plats du jour \n")
    print("*" *50)
    print("2- Creer un plat \n")
    print("*" *50)
    print("3- Ajouter un plat à la liste \n")
    print("*" *50)
    print("4- Afficher la composition du plat \n")
    print("*" *50)
    print("5- Modifier Plat \n")
    print("*" *50)
    print("6- Faire une vente \n")
    print("*" *50)
    print("7- Quitter \n")

# Fichier user.txt



# Fichier resto.txt

def Get_Nom_Plat(ligne):
    l = ligne.split(":")
    Nom_Plat = l[0]
    return Nom_Plat

def Get_Qte_Plat(ligne):
    l = ligne.split(":")
    Qte_Plat = l[1]
    return Qte_Plat

def Get_Prix_Plat(ligne):
    l = ligne.split(":")
    Prix_Plat = l[2]
    return Prix_Plat

def Get_Composition_Plat(ligne):
    l = ligne.split(":")
    Composition_Plat = l[3]
    return Composition_Plat

def Get_Etat_Plat(ligne):
    l=ligne.split(":")
    Etat_Plat =l[4].replace("\n","")
    return Etat_Plat


def Afficher_Plat(filename,modeOuverture):
    with open(filename,modeOuverture)as f:
        cpt = 0
        for lign in f:
            cpt = cpt + 1
            Nom_Plat = Get_Nom_Plat(lign)
            Qte_Plat = Get_Qte_Plat(lign)
            Prix_Plat = Get_Prix_Plat(lign)
            Composition_Plat = Get_Composition_Plat(lign)
            Etat_Plat = Get_Etat_Plat(lign)
            print(f"{cpt}.Nom plat : {Nom_Plat}")
            print(f"{cpt}.Quantite  : {Qte_Plat}")
            print(f"{cpt}.Prix plat  : {Prix_Plat}")
            print(f"{cpt}.Composition plat  : {Composition_Plat}")
            print(f"{cpt}.Etat du plat  : {Etat_Plat}")
            print("-"*50)
        
def Ajouter_Plat():
    Nom = input("Entrez le nom du plat \n")
    Qte = input("Entrez la quantite  \n")
    Prix = input("Entrez le prix du plat \n")
    comp = []
    rep = input("Voulez-vous enter un ingredient (O/N) ?")
    while(rep.upper == "o"):
        Compo = input("Entrez la composition du plat \n")
        comp.append(Compo)
        rep = input("Voulez-vous enter un ingredient (O/N) ?")
    Composition = (",").join(comp)
    Etat = input("Entrez l'etat du plat \n")
    plat = f"\n{Nom}:{Qte}:{Prix}:{Composition}:{Etat}\n"
    return plat

def Ajout_Plat(filename,modeAjout):
    with open(filename,modeAjout)as f:
        f.write(Ajouter_Plat)

def Creation_Plat():
    liste_modifie = []
    Creer_Plat = False
    question = input("Voulez-vous créer un plat (O/N)?\n")
    if question.upper() == "O":
        nom_plat = input("Entrez le nom du plat :\n")
        qte_plat = input("Entrez la quantité du plat :\n")
        prix_plat = input("Entrez le prix du plat :\n")
        comp = []
        rep = input("Voulez-vous entrer un ingrédient (O/N) ?\n")
        while rep.upper() == "O":
            Compo = input("Entrez la composition du plat \n")
            comp.append(Compo)
            rep = input("Voulez-vous entrer un ingrédient (O/N) ?\n")    
        Composition = (",").join(comp)
        etat = "1"
        with open(filename, modeOuverture) as f:
            for ligne in f:
                creation = ligne.strip().split(":")
                creation[0] = nom_plat
                creation[1] = qte_plat
                creation[2] = prix_plat
                creation[3] = Composition
                creation[4] = etat
            liste_modifie.append(":".join(creation) + "\n")
            Creer_Plat = True
    else:
        with open(filename, modeOuverture) as f:
            for ligne in f:
                liste_modifie.append(ligne)
    if Creer_Plat:
        with open(filename, modeEcriture) as f:
            f.writelines(liste_modifie)
        print("Le plat a été créé \n")
    else:
        print("Aucun plat créé")

def Afficher_Composition(filename,modeOuverture):
    with open(filename,modeOuverture) as f:
        nom_plat = input("Entrez le nom du plat dont vous voulez la composition \n")
        for ligne in f:
            if(nom_plat == Get_Nom_Plat(ligne)):
                composition = Get_Composition_Plat(ligne)
                print(f"la composition de {nom_plat} est : {composition}")
    
def plat_modifier():
    new_nom = input("Entrez le nom du nouveau plat \n")
    new_qte = input("Entrez la nouvelle quantité \n")
    new_prix = input("Entrez le nouveau prix \n")
    comp = []
    rep = input("Voulez-vous enter un ingredient (O/N) ?")
    while(rep.upper == "o"):
        Compo = input("Entrez la composition du plat \n")
        comp.append(Compo)
        rep = input("Voulez-vous enter un ingredient (O/N) ?")
    Composition = (",").join(comp)
    etat = "1"
    return f"{new_nom}:{new_qte}:{new_prix}:{Composition}:{etat}\n"

def modifier_Plat(filename,modeOuverture):
    plat_modifie = None
    nom = input("Entrez le nom du plat à modifier \n")
    with open(filename,modeOuverture)as f:
        nouvelles_lignes = []
        for ligne in f:
            if (nom == Get_Nom_Plat(ligne)):
                plat_modifie = plat_modifier()
                nouvelles_lignes.append(plat_modifie)
            else:
                nouvelles_lignes.append(ligne) 
        if plat_modifie is None:
            print("Le plat n'existe pas.")
        else:
            with open(filename, modeEcriture) as f:
                f.writelines(nouvelles_lignes) 
                print("Le plat a été modifié avec succès.")

def modification(filename,modeOuverture):
    rep = input("Voulez-vous modifier un plat ? (O/N) : ")
    if (rep.upper() == "O"):
        modifier_Plat(filename,modeOuverture)
    else:
        print("Modification annulée.")

def Vente():
    qte = int(input("Entrez la quantité de plats à vendre :\n"))
    return qte

def Faire_vente(filename, modeOuverture):
    nom = input("Entrez le nom du plat à vendre : ")
    with open(filename, modeOuverture) as f:
        nouvelle_vente = []
        for ligne in f:
            if nom == Get_Nom_Plat(ligne):
                qte_a_vendre = Vente()
                qte = int(Get_Qte_Plat(ligne)) - qte_a_vendre
                if qte < 0:
                    print(f"Quantité insuffisante pour le plat {nom}.")
                    nouvelle_vente.append(ligne)  
                else:
                    vente = ligne.strip().split(":")
                    vente[0]=nom
                    vente[1] = str(qte)
                    vente[2] = Get_Prix_Plat(ligne)
                    vente[3] = Get_Composition_Plat(ligne)
                    vente[4] = Get_Etat_Plat(ligne)
                    nouvelle_vente.append(":".join(vente) + "\n")
            else:
                nouvelle_vente.append(ligne)
        if not nouvelle_vente:
            print("Le plat n'existe pas.")
        else:
            with open(filename, modeEcriture) as f:
                f.writelines(nouvelle_vente)
                print("La vente a été faite avec succès.\n")

def Verif_Vente(filename, modeOuverture):
    rep = input("Voulez-vous faire une vente ? (O/N) : ")
    if rep.upper() == "O":
        Faire_vente(filename, modeOuverture)
    else:
        print("Vente annulée.")


def Gerer_Menu_Principal():
    while True:
        Menu_Principal()
        choix = int(input("Entrez votre choix: \n"))
        if choix == 1:
            Afficher_Plat(filename, modeOuverture)
        elif choix == 2:
            Creation_Plat()
        elif choix == 3: 
            Ajout_Plat(filename, modeAjout)
        elif choix == 4: 
            Afficher_Composition(filename, modeOuverture)
        elif choix == 5: 
            modification(filename, modeOuverture)
        elif choix == 6: 
            Verif_Vente(filename, modeOuverture)
        elif choix == 7:
            print("Quitter le programmqe. Au revoir !")
            break 
        else:
            print("Option invalide, veuillez réessayer.")

Gerer_Menu_Principal()
