# bot_python

# Les premier commande 

``
    python3 -m venv nom_de_l_environnement
``

### Sur Linux/Mac :
``
    source venv/bin/activate
``

### Sur Windows (PowerShell) :
``
    ven/Scripts/Activate.ps1
``

### Sur Windows (CMD) :
``
    venv/Scripts/activate.bat
``

### Finir avec l'installation des Packages :
``
    pip install -r requirements.txt
``

# Obtention d'un jeton pour un bot Discord

Pour créer un bot Discord, vous devez suivre les étapes suivantes pour obtenir un jeton d'accès :

## Étapes :

1. Rendez-vous sur le [portail des développeurs Discord](https://discord.com/developers/applications).
2. Cliquez sur le bouton "New Application" pour créer une nouvelle application.
3. Donnez un nom à votre application et cliquez sur "Create".
4. Dans le panneau de gauche, sélectionnez "Bot".
5. Cliquez sur le bouton "Add Bot" pour ajouter un bot à votre application.
6. Dans la section "Token", cliquez sur "Copy" pour copier votre jeton d'accès.

## Utilisation du jeton dans votre code :

Une fois que vous avez obtenu le jeton pour votre bot Discord, vous pouvez l'utiliser dans votre code Python en tant que variable pour l'authentification de votre bot.

Dans ce code j'appel mon token a partir d'un stript congif.py et mon token et contenu dans une dictionaire qui peux resembler a ceci:

```py
    MY_CONFIG = {
    'token' : '<le token ici>',
    'info_bdd' : {
        'login': '<le login>',
        'mot_de_passe': '<le mot de passe>',
        'hôte': '<l\'hôte de la base de données>',
        'port': '<le port de la base de données>',
        'nom_bdd': '<le nom de la base de données>',
        }
    }
```


## Gestion des message :

Il est possible D'avoir un souci avec 'intents', il suffit de donner les droits au bot dans le coter bot dans la partie applications du portail.

