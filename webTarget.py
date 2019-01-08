# fonction permettant de lire et écrire dans un fichier
def ecrire(Adresslist):
    Adress = open("listeAdress.csv","a")
    Adress.write(Adresslist)
    Adress.write("\n")
    Adress.close()
def lire():
    Adress = open("listeAdress.csv", "r")
    print(Adress.read())
    Adress.close()
#fonction qui vérifie la présence de doublons
def doublons(Adresslist):
    Adress = open("listeAdress.csv", "r")
    for ligne in Adress:
          if Adresslist in ligne:
              Adress.close()
              return True
    else:
        Adress.close()
        return False
def test_ping(Adresslist):
    #fonction permettant de tester les nom de domaines
    domain = Adresslist.split('@')
    print("ping de l'adresse veuillez patienter...")
    os.system('ping -c 2' + ' ' + domain[1] + '>pingtest.txt')
    if os.path.getsize("pingtest.txt") == 0:
        print("KO")
        return 1
    else:
        print("OK")
        return 0
#-------------------Début du programme-------------------#
import os
car="@"
com=".com"
fr=".fr"
while True:
    Adresslist=input("veuillez entrer une adresse mail valide:\n")
    if car in Adresslist:
        if com in Adresslist:
            twice=doublons(Adresslist)
            if twice==True:
                print("Adresse déjà sauvegarder")
            else:
                print("adresse correct !")
                break


        elif fr in Adresslist:
            twice = doublons(Adresslist)
            if twice == True:
                print("Adresse déjà sauvegarder")
            else:
                print("adresse correct !")
                break
    print("adress mail incorrect !")

ping=test_ping(Adresslist)
if ping==1:
    print("adresse mail nom pingable")
elif ping==0:
    print("adresse mail pingable ajout à la mailing list")
    ecrire(Adresslist)
    print("vous avez rentrer 1 adresse:",Adresslist)






