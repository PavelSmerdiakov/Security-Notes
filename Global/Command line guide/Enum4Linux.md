enum4linux est un outil open source utilisé pour collecter des informations à partir de systèmes Windows en utilisant le protocole SMB (Server Message Block). Il est principalement utilisé pour effectuer des opérations d'enumération (collecte d'informations) sur les systèmes cibles.

Options :

-U : info sur les users de la cible

-S : Info sur les dossier et fichier. Qu'est ce qu'on peut en tirer ? :

- **Mappé** : Lorsqu'un partage est "mappé", cela signifie que enum4linux a pu identifier et établir une connexion au partage. Cela indique généralement que l'adresse IP cible possède des partages de fichiers accessibles.
- **Lister** : Une fois qu'un partage est mappé, enum4linux tente d'énumérer (lister) les fichiers et dossiers présents dans le partage. Si l'énumération est autorisée (indiquée par "OK"), cela signifie que l'attaquant peut voir les fichiers et dossiers dans le partage. Cela peut être utile pour identifier des informations sensibles ou des configurations potentiellement vulnérables.
- **Écrit** : Si l'option d'écriture est autorisée (indiquée par "OK"), cela signifie que l'attaquant pourrait écrire des fichiers dans le partage. Cela pourrait potentiellement être exploité pour lancer des attaques de dépassement de tampon ou pour téléverser des fichiers malveillants.

En tant qu'attaquant, ces informations peuvent être utilisées pour évaluer la sécurité d'un système. Par exemple :

- **L'absence de mappage** : Si un partage ne peut pas être mappé, cela peut indiquer que les partages de fichiers ne sont pas correctement configurés ou que des mesures de sécurité restrictives sont en place.
- **Lister des fichiers** : Si vous pouvez lister les fichiers et dossiers dans un partage, cela peut vous permettre de repérer des informations sensibles (comme des fichiers de mots de passe, des documents confidentiels, etc.) qui pourraient être exploitables.
- **Autorisation d'écriture** : Si vous avez l'autorisation d'écriture, cela pourrait permettre des attaques de dépassement de tampon, le téléchargement de fichiers malveillants, ou la manipulation de fichiers pour compromettre le système.

-P : info sur les mots de passe  
-o : info sur l'os

-l : info sur le serveur LDAP. En gros c'est un annuaire avec des infos comme des noms, des adresse mails et tout le tralala.

-n : info sur le bios comme l'adresse mac par exemple  
-a : toute les infos
