import requests #lib pour la partie web scraping
from bs4 import BeautifulSoup #lib  pour la  partie web scraping
import time
from subprocess import call

response = requests.get("https://cas.webcollege.seinesaintdenis.fr/login?ABAB")
URL = response.content

print("------------DIAMANTS-BOT-DEVOIRS-------------")
print("+          Version actuelle : v1.1.0        +")
print("+          --- Le Taille Crayon ---         +")
print("------------------//----//-------------------")
data = input("Diamants-Bot-Devoirs : Dans quel menu souhaitez-vous aller ?")
if(data=="Skolengo") or (data=="ENT"):
    dataS = "Skolengo"
    datab = input("Quelle rubrique ?")
elif(data=="devoirs"):
    print("1 matière est installée (v1.1.0)")
    mat = input("Qulle matière ?")
    data1 = ""
    datab = ""
    dataS = ""
    if(mat=="Arts-Plastiques") or (mat=="Arts"):
        print("Accès au répertoire 'Arts-plastiques'")
        call(["python", "Arts-Plastiques/scripts/Arts.py"])

if(datab=="devoirs") and (dataS=="Skolengo"):
    data1 = input("Quelles données souhaitez-vous obtenir ?")
elif(datab=="renommer un fichier"):
    print("Note v1.1.0 = L'URL d'accès au fichier DOIT IMPERATIVEMENT figurer dans le fichier ent.js sans quoi le processus ne fonctionnera PAS !")
    print("NodeJS et Puppeteer doivent être installés = Démarrage du programme...")
    call(["node", "Config/ent.js"]) 
    data1 = ""
elif(datab=="") and (dataS=="") :
    pass
else :
    data1 = ""
    print("Votre saisie n'a pas été reconnue, pour quitter, saisissez Ctrl+C")

bsObj = BeautifulSoup(URL, "lxml")
matiere = bsObj.find_all(class_="p-like b-like slug slug--xs")
matiere1 = str(matiere)
matiere2 = matiere1.replace('[<p class="p-like b-like slug slug--xs">', "")
matiere3 = matiere2.replace('<span class="pull-right">', "")
matiere4 = matiere3.replace('<span class="icon icon--sm icon--clock-primary"></span>', "")
matiere5 = matiere4.replace('</span>', "")
matiere6 = matiere5.replace('</p>, <p class="p-like b-like slug slug--xs">', "")
matiere7 = matiere6.replace('</p>]', "")
travail = bsObj.find_all(class_="p-like h-like--no-margin")
travail1 = str(travail)
travail2 = travail1.replace('[<p class="p-like h-like--no-margin">', "")
travail3 = travail2.replace('<a class="btn btn--sm btn--secondary js-async js-taf__btn-faire" href="sg.do?PROC=CDT&amp;ACTION=TRAVAIL_FAIT&amp;ID_ACTIVITE=', "")
travail4 = travail3.replace('&amp;DATECOURANTE=', "")
travail5 = travail4.replace('</a>', "")
travail6 = travail5.replace('</p>, <p class="p-like h-like--no-margin">', "")
travail7 = travail6.replace('</p>]', "")
travail8 = travail7.replace('&amp;FILTREMETIER=&amp;PROV=AFFICHER_ELEVES_TAF#a_', "")
travail9 = travail8.replace('" title="Déclarer fait">', "")
travail10 = travail9.replace('" title="Déclarer non fait">', "")
if(data1=="matières"):
    print("Connexion en cours à l'ENT Skolengo")
    time.sleep(2)
    print(matiere7)
elif(data1=="travail"):
    print("Connexion en cours à l'ENT Skolengo")
    time.sleep(2)
    print(travail10)