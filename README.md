# diamants-devoirs-bot
Ce bot fait vos devoirs à votre place (enfin presque...) ! Envie d'essayer ? Vous êtes au bon endroit ! This bot is only working in French for the moment, but a documentation in English is available !

# 🙄 Quoi de neuf dans la v1 / Whats new in v1 ?
Ajout de nouvelles fonctionnalités / Add new functionalities :
- Compatible avec les devoirs d'Arts Plastiques / Now working with Arts homework
- Supporte la communication avec l'ENT Skolengo (Testé en Seine-St-Denis uniquement) / Now accepting connection with Skolengo Workspace (tested in Seine-St-Denis only)

# ✅ Fonctionnalités / Functionalities
**Arts Plastiques / Arts**

- ✅ Détecte automatiquement la meilleure photographie (résoultions optimales) pour votre Portfolio / Automatically detects the best picture (Best resolution) for your Portfolio
- ✅ Rédige automatiquement votre texte d'intention en Français à partir de quelques données saisies dans la console (création automatique de phrases logiques) / Automatically write you description text in French from some words that you typed in Windows CMD (Auto create sentences)
- ❌Ne réalise pas les travaux manuels ! / Cannot do real arts work (draw, etc...) !

**Connection avec l'ENT Skolengo (Testé avec Webcollege93) / Connection with Skolengo ENT (Tested with Webcollege93) :**

- ✅ Connection au serveur (Contourne le processus d'authentification classique) / Connection to the server (Bypass traditional login process)
- ✅ Renommer des fichiers... (Voir Plus) / Rename files... (See More)
- ✅ Affichage des devoirs à faire avec possibilité de les connecter à des services externes (SMS, ToDoLists, etc...) / Show homeworks and connect them to externals services like SMS or external ToDoLists.
- 🕓 Affichez vos messages reçu et connectez-les à des services externes / Show your internal mail box and connect it to external services.
- ⚠ Attention : Nous n'avons aucun lien avec la société Kosmos possédant Skolengo ou le départment de la Seine-St-Denis, ce programme ne fait que "contourner" l'authentification classique en utilisant un token d'accès et une URL de type "Webhook" / We do not have affiliation with Kosmos company, Skolengo or Seine-St-Denis, our program just bypass traditional login process by usig an access token and a URL like a "standard webhook"

# ➡ Commencez dès maintenant ! / Get Started Now !
Notre programme est gratuit et repose sur du Python, JavaScript et NodeJS. / Our program is Free and use Python, JavaScript and NodeJS
Pour commencer, vous aurez besoin de : / For getting started, you'll need :
- ✅ Visual Studio Code
- ✅ Python installé sur l'appareil et PIP également / Python installed on your device and PIP too.
- (✅ Puppeteer pour envoyer des requêtes "humaines" à l'ENT Skolengo / Puppeteer for sending "humans" requests to Skolengo Workspace) #Optional/Optionnel

- Maintenant, téléchargez le fichier "diamants-devoirs-bot .zip", et décompressez l'archive. A présent, allez dans la matière souhaitée : / Now downloads the file "diamants-devoirs-bot .zip" and unzip the file. After, go into the subject that you want :
- Arts-Plastiques : Placez vos fichiers images (dans la limite de 4 fichiers images) nommés (IMG001, IMG002, IMG003, IMG004) dans "/Images (Import here pictures)". L'extension doit être .JPG !!! / Arts, put-in your images files (max. 4 files) named (IMG001, IMG002, IMG003, IMG004) in "/Images (Import here pictures)". Files extensions MUST BE in .JPG !
-  -> Ensuite, exécutez le fichier "setup.py" du répertoire principal en tapant "python setup.py" sans l'interpréteur de commande Windows / Then, execute the file "setup.py" by typing "python enttests.py" in Windows CMD !
-  -> Le résultat sera disponible dans le fichier "fiche_info.odt" du répertoire "Arts-Plastiques/Resultat" / The results will be available in the file "fiche_info.odt" in "Arts-Plastiques/Resultat" path.

# ❓ Comment ? La connexion avec l'ENT Skolengo ! / How to ? Connexion with Skolengo Workspace !
- Ouvrez une fenêtre de navigation privée dans Google Chrome
- Ouvrez la console "Network" du mode développeur (Ctr+Maj+I) et onglet "Network")
- Ouvrez ce lien en remplaçant clg-ville par le NOM DE FAMILLE de votre collège (ex : François Mitterand = Mitterand) et par la ville en collé (ex : saintdenis): https://clg-ville.webcollege.seinesaintdenis.fr/sg.do?PROC=TRAVAIL_A_FAIRE&ACTION=AFFICHER_ELEVES_TAF&filtreAVenir=true
- Vérifiez bien que la console "Network" est toujours ouverte et connectez-vous
- Une fois connectez ouvrez le fichier "login" qui est apparu et descendez tout en bas, cliquez sur "View source" et cliquez sur "Show More" autant de fois que possible. Copiez le tout qui devrait commencer par ça "username=XXpassword=XX"
- Ouvrez FIRST_SETUP.py, via le terminal Windows et collez cette suite de caractère à "système de devois" puis faites entrée.
