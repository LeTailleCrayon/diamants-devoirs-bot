import fileinput

print("------------DIAMANTS-BOT-DEVOIRS-------------")
print("+          Version actuelle : v1.1.0        +")
print("+          --- Le Taille Crayon ---         +")
print("------------------//----//-------------------")
print("--------------WELCOME FIRST SETUP------------")
print("Bienvenue dans la page de configuration de Diamants-Bot-Devoirs")
print("Merci d'avoir installé notre programme !")
print("La configuration vous permettra de cous connecter à des services externes ! : ENT Skolengo (Webcollege93) et d'autres à venir !")

askW = input("Avez-vous un compte Skolengo ENT/Webcollège93 élève ?")
if(askW=="oui"):
    ask1 = "1"
else :
    ask1 = "0"
    idAnswer = "non"

if(ask1=="1"):
    print("Commençons par configurer le système de fichier ! (Complexe et optionnel)")
    idAnswer = input("La procédure est complexe et optionnelle, d'autant plus qu'elle ne figure pas dans la DOCUMENTATION ! Nous vous déconseillons de l'activer ! Voulez-vous configurer le système de fichier ?")
    if(idAnswer==oui):
        idS = input("Collez-ici les données nécessaires ! (les données restent privées en local)")
    else :
        idS = ""
    print("Configurons maintenant le système de devoirs !")
    idS2 = input("Collez-ici les données demandées dans la Documentation !")
if(ask1=="1") and (idAnswer="oui"):
    with fileinput.FileInput("Config/ent.js", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("ABAB", idS), end='')
if(ask1=="1"):
    with fileinput.FileInput("setup.py", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("ABAB", idS2), end='')
