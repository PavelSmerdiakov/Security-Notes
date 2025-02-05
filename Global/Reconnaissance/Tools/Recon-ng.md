Outils giga puissant pour faire de la recon. C'est un framework qui ressemble vachement à metasploit donc c'est plus facile de s'y adapter.


- **Prise en main du framework :**

C'est exactement comme metasploit donc on rentre dans le framework et on a plusieurs commandes à disposition.

**Commandes :**


Entrer dans le framework : `recon-ng`
Recharger directement un workspace : `recon-ng -w workspace_name`
Afficher les commandes possibles : `help`
Executer des commandes shell : s`hell command`
Voir les informations de la cible qu'on possède : `show item_qu'on_veut`
Quitter le framework : `exit`
Revenir dans le contexte précédent : `back`
Lister mes clé API : `keys list`
Ajouter une nouvelle clé API à un service : `keys add service_name API_key`
Retirer une clé API d'un service : `keys remove service_name`


- **Workspace :**

On peut créer un workspace pour revenir dessus plus tard et donc récupérer toutes les données.

**Commandes :**


Créer un workspace : `workspaces create workspace_name`
Lister les workspaces : `workspaces list`
Revenir sur un workspace : `workspaces load workspace_name`
Supprimer un workspace : `workspace remove`


- **Marketplace :**

Le marketplace c'est ce qui regroupe tous les modules qu'on peut installé ou qui sont déjà installé.

**Commandes :**


Voir commandes marketplace : `marketplace help`
Voir tous les modules : `marketplace search`
Chercher un modules précis : `marketplace search nom_module`
Voir les détails d'un module : `marketplace info nom_module`
Installer un module : `marketplace install nom_module`
Supprimer un module sur ta machine : `marketplace remove nom_module`


- **Modules :**

Les modules c'est tous les outils, script, fonctionnalités qu'on va utiliser pour faire de la recon.

**Commandes : **


Utiliser un module : `modules load nom_module`
Voir les commandes possible dans le contexte du module : `help`
Voir les détails d'utilisation du module : `info`
Voir les options globales de recon-ng : `goptions list`
Changer la valeur d'une option globale : `goptions set options_name value`
Voir les options du module : `options list`
Changer la valeur d'une option : `options set options_name value`
Executer le module : `run`


**Différente catégorie de modules :**


Discovery : De la recon un peu global. C'est un peu un fourre-tout (y'a que deux modules)

Exploitation : Comme son nom l'indique, c'est juste des petits exploit

Recon/companies : De la recon sur des entreprises

Recon/contacts : De la recon sur des personnes avec leur moyen de contacts

Recon/domains : De la recon sur les domaines donc ça inclut les info DNS par exemple

Recon/hosts : De la recon sur les hôtes donc adresse ip par ex

Recon/locations : De la recon sur des lieux géographique

Recon/profiles : De la recon sur des personnes

Reporting : C'est pour générer des rapports avec les infos qu'on a choper avant.



**Explication des modules :**


    - **xssed :**
        - Utilité : Permet de voir les vulnérabilité xss déjà reporté sur le site. Il semble ne pas avoir un grand intêret mais on pourrai regarder les vuln xss sur les grand sites pour ensuite comparer avec les target. EDIT : xssed n'est plus du tout entretenu depuis 2015 donc sa sert à rien en fait. C'est que des vieilles vulnérabilités.

        - Utilisation :


1 seule option c'est la source qu'on doit mettre sur le domaine cible.

```
    - **HackerTarget :**
        - Utilité : C'est pour chopper des noms de domaines et de sous-domaines.

        - Utilisation :
```

1 seule option c'est la source qu'on doit mettre sur le domaine cible.
