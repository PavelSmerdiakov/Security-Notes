Énumération :

`uname -a` : Donne tout les détails à propos du système  
`cat /proc/version` : Donne des détails à propos du kernel  
`cat /etc/os-release`

`cat /etc/issue` : Fichier contenant un message à afficher au début d'une connexion

`ps` : Voir les processus en cours pour le shell. Ajouter -A pour voir tous les processus. Ajouter axjf pour voir un arbre de processus. Ajouter aux pour voir les utilisateurs des processus

`cat/etc/passwd | cut -d ":" -f 1` : Pour voir que les noms d'user de chaque ligne ou mettre grep home a la place pour voir les vrai users

- **LinPeas**: [https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS "https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS")
- **LinEnum:** [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum "https://github.com/rebootuser/LinEnum")
- **LES (Linux Exploit Suggester):** [https://github.com/mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester "https://github.com/mzet-/linux-exploit-suggester")
- **Linux Smart Enumeration:** [https://github.com/diego-treitos/linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration "https://github.com/diego-treitos/linux-smart-enumeration")
- **Linux Priv Checker:** [https://github.com/linted/linuxprivchecker](https://github.com/linted/linuxprivchecker "https://github.com/linted/linuxprivchecker")


Description :

Permet de voir les permissions que l'utilisateur actuel a (peut pas voir pour les autres).

Exemple :  
```
user@debian:~$ sudo -l  
Matching Defaults entries for user on this host:                        |

env_reset, env_keep+=LD_PRELOAD,                                        | c'est des options pour les variables d'environnement

env_keep+=LD_LIBRARY_PATH                                                    |

User user may run the following commands on this host:  
    (root) NOPASSWD: /usr/sbin/iftop  
    (root) NOPASSWD: /usr/bin/find  
    (root) NOPASSWD: /usr/bin/nano  
    (root) NOPASSWD: /usr/bin/vim  
    (root) NOPASSWD: /usr/bin/man  
    (root) NOPASSWD: /usr/bin/awk  
    (root) NOPASSWD: /usr/bin/less  
    (root) NOPASSWD: /usr/bin/ftp  
    (root) NOPASSWD: /usr/bin/nmap  
    (root) NOPASSWD: /usr/sbin/apache2  
    (root) NOPASSWD: /bin/more
```

user peut alors executer les commandes iftop, find, nano...

Vulnérabilité :

Privilege escalation : en cherchant sur [https://gtfobins.github.io/](https://gtfobins.github.io/ "https://gtfobins.github.io/") la commande executable par moi, (iftop par exemple) puis en allant sur sudo, on peut essayer de grimper en privilèges.

