import os
import time

def clear():
    time.sleep(2)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


userfile = r'user.txt'
modeOuverture = 'r'
modeAjout = 'a'
modeEcriture = 'w'

def Get_nom_user(ligne):
    l=ligne.split(":")
    Nom_user = l[0]
    return Nom_user

def Get_prenom_user(ligne):
    l=ligne.split(":")
    Prenom_user = l[1]
    return Prenom_user

def Get_Login(ligne):
    l=ligne.split(":")
    login = l[2]
    return login

def Get_password(ligne):
    l=ligne.split(":")
    password=l[3]
    return password

def Get_role(ligne):
    l=ligne.split(":")
    role=l[4]
    return role

def Get_etat_user(ligne):
    l=ligne.split(":")
    etat_user=l[5]
    return etat_user

def Menu_gest():
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

def Menu_vendeur():
    print("Faite votre choix \n")
    print("*" *50)
    print("1- Afficher les plats du jour \n")
    print("*" *50)
    print("2- Faire une vente \n")
    print("*" *50)
    print("3- Voir facture client \n")
    print("*" *50)
    print("4- Quitter \n")

def Menu_client():
    print("Faite votre choix \n")
    print("*" *50)
    print("1- Afficher les plats du jour \n")
    print("*" *50)
    print("2- Voir sa facture \n")
    print("*" *50)
    print("3- Quitter \n")

def verifconnexion(login,password):
    with open(userfile,modeOuverture)as f:
        for ligne in f:
            if(login == Get_Login(ligne) and password == Get_password(ligne) and Get_etat_user == "1"):
                return Get_role(ligne)
        return False

def connexion():
    print("===========Page de connexion============")
    login = input("Login: ".center(20,"*")+"\n")
    password = input("Password: ".center(20,"*")+"\n")
    role = verifconnexion(login,password)
    while not role:
        clear()
        print("===========Page de connexion============")
        login = input("Login: ".center(20,"*")+"\n")
        password = input("Password: ".center(20,"*")+"\n")
        role = verifconnexion(login,password)
    return role



