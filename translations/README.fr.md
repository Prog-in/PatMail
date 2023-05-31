# PatMail

PatMail est une application d'envoi automatisé d'emails entièrement réalisée en python, utilisant le module TKinter pour l'interface graphique.

## Documentation

PatMail permet à l'utilisateur d'importer un fichier .csv de contacts, contenant deux colonnes, dans l'ordre, "Nom" et "Email", et un fichier .txt, qui contiendra le message à envoyer aux contacts du fichier contacts. De plus, PatMail permet à l'utilisateur d'importer des pièces jointes à envoyer avec le message à envoyer aux contacts.

### Usage

1- Importez les fichiers en tapant le chemin du fichier ou en utilisant l'outil de recherche ;

2- Ajoutez des pièces jointes au corps du message, si vous le souhaitez ;

3- Entrez votre email et votre mot de passe ;

4- Ajoutez le sujet de l'e-mail ;

5- Cliquez sur « Envoyer des e-mails » ;

REMARQUE : Les étapes 1 à 4 peuvent être effectuées dans n'importe quel ordre.

## Fonctionnalités

- Envoi automatisé d'emails à plusieurs contacts ;
- Vous permet de joindre des fichiers à envoyer ;
- Dans le fichier message .txt, 2 variables peuvent être utilisées qui seront remplacées par les informations du destinataire :
     * ${NAME} : est remplacé par le nom du destinataire ;
     * ${EMAIL} : est remplacé par l'e-mail du destinataire ;
- Après avoir importé le fichier de contacts et le fichier de messages, dans l'onglet contacts, il sera possible de double-cliquer sur la ligne d'un destinataire pour ouvrir un aperçu du message pour ce destinataire spécifique.

## L'installation

Une fois que les conditions requises sont remplies, il y a deux façons principales d'installer le paquet.

### Exigences

- Python 3.6 ou supérieur (l'application n'a pas été testée sur toutes les versions, elle peut donc fonctionner sur des versions antérieures à celle-ci) ;
- pip install ;


### 1) utiliser comme paquet pip

- Télécharger le code source de PatMail ;
- Accédez à la racine du projet :

```bash
cd Chemin/Vers/CheminMail
```

- Installez l'application en tant que package Python :

```bash
installation de pip.
```

- Si pip n'est pas dans le PATH système :

```bash
python3 -m installation pip.
```

- Une fois l'installation terminée, PatMail sera installé en tant que package pip et pourra être ouvert avec :

```bash
PatMail
```

### 2) appeler directement le fichier de démarrage

Si la méthode 1 ne fonctionne pas ou si vous ne souhaitez pas laisser PatMail en tant que package pip, vous pouvez simplement télécharger les dépendances nécessaires et appeler le fichier qui démarre l'application :

```bash
pip install -r /Path/To/PatMail/requirements.txt
python3 /chemin/vers/PatMail/src/main.py
```

Remarque : Si vous choisissez la deuxième méthode d'installation, l'utilisation d'un "alias" peut faciliter le démarrage de l'application.


#### Un exemple en bash :

ajoutez à ~/.bashrc ou équivalent la ligne suivante :

```bash
alias PatMail='python3 /path/to/PatMail/src/main.py'
```


## Résolution des problèmes (Dépannage)

- PatMail utilise uniquement le serveur SMTP de Google pour envoyer des e-mails et sera donc limité aux éventuelles restrictions du serveur en question ;
- Si vous ne parvenez pas à vous connecter avec votre nom d'utilisateur et votre mot de passe, essayez de générer un mot de passe d'application dans vos paramètres d'utilisateur Google et utilisez-le comme mot de passe.
- Si PatMail n'autorise pas l'importation d'un fichier .csv, faites attention aux restrictions :
     * Dans l'en-tête (première ligne), elles ne doivent contenir que deux informations : "Nom"/"Nom" et "Email"/"E-Mail", dans cet ordre (l'application est insensible à la casse pour ces informations, afin rendre plus facile);
     * TOUTES les lignes doivent contenir deux colonnes contenant des caractères ;
- Si votre problème n'est pas répertorié ici ou si les solutions présentées n'ont pas résolu votre problème, ouvrez un problème détaillant la situation avec autant d'informations que possible, afin qu'il soit possible d'enquêter sur les causes du problème et de rechercher des solutions ;


## License

[MIT](https://choosealicense.com/licenses/mit/)
