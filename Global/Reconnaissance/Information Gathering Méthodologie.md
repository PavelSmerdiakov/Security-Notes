**Footprinting/Recon :**

**Les objectif principaux :**

L'objectif c'est d'avoir le contexte global de la cible. Donc ca inclut ca position financière, système de sécurité, les employés cible potentiels ou encore une map du network.

**Footprinting through Search Engines**

- [Netcraft](https://sitereport.netcraft.com/ "https://sitereport.netcraft.com/") pour chopper plein d'information générale sympa qui mènent sur des pistes.
- [Shodan.io](https://www.shodan.io/ "https://www.shodan.io/") mais j'ai l'impression qu'il faut avoir vraiment de la chance pour trouver un truc sur une entreprise spécifique
- Après y'a tout les trucs de map :
    - [Google Earth](https://earth.google.com/ "https://earth.google.com/")
    - [Google Map](https://www.google.com/maps "https://www.google.com/maps")
    - [Bing Map](https://www.bing.com/maps "https://www.bing.com/maps")
    - [Wikimapia](https://wikimapia.org/ "https://wikimapia.org/")
- On a aussi les sites pour la recherche de personne :
    - [privateeye](https://www.privateeye.com/ "https://www.privateeye.com/")
    - [peoplesearchnow](https://www.peoplesearchnow.com/ "https://www.peoplesearchnow.com/")
    - [backgroundchecks](https://backgroundchecks.org/ "https://backgroundchecks.org/")
    - [anywho](https://www.anywho.com/ "https://www.anywho.com/")
    - [intelius](https://www.intelius.com/ "https://www.intelius.com/")
    - [peoplefinders](https://www.peoplefinders.com/ "https://www.peoplefinders.com/")
- Quand on a une grosse entreprise, on a potentiellement envie de savoir sa situation financière :
    - [Google Finance](http://www.google.com/finance "http://www.google.com/finance")
    - [Yahoo Finance](http://finance.yahoo.com "http://finance.yahoo.com")
- Et après y'a la recon avec les forum, blog, réseau sociaux même si c'est un peu plus long que ca.

**Footprinting through Advance Google Hacking**

- El famoso google dork.
    - Pour en voir plein -> [GHDB](https://www.exploit-db.com/google-hacking-database "https://www.exploit-db.com/google-hacking-database")
    - site:    Recherche les pages à partir d'un domaine
    - related:   Recherche des pages similaires
    - cache:   Affiche les pages stockées dans le cache
    - link:   Liste les sites qui contiennent dans leur pages un lien qui pointe vers le lien spécifié
    - allintext:   Recherche les sites contenant des mots spécifiques
    - intext:   Comme allintext sauf que c'est pour qu'un mot
    - intitle:
    - allintitle:
    - allinurl:
    - inurl:

**Footprinting through Social Networking Sites**

- Social Engineering mais bon pour l'instant c'est trop complexe pour s'y intéresser pleinement.
- Footprinting using Social Engineering on Social Networking Sites
    - Le tableau parle de lui-même :

![1000004188.jpg](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/1000004188.jpg)

**Footprinting through Websites**

- Zaproxy :
    
    - Je crois que ça va vraiment te sauver la vie, c'est un peu comme burpsuite mais en gratuit et Open source. C'est pas pour autant que ca remplace le titan Burpsuite.
- Web Spider/Web Crawler c'est un peu la même chose
    
    - C'est pour mapper un site web.
    - Tools sympa pour ça :
        - Gospider
- Mirroring :
    
    - C'est copier le site web pour le tester sans toucher au vrai
    - Tools sympa avec guide qui vont avec (quand j'aurai pas la flemme). Cherche en lien torrent si possible :
        - [HTTrack](https://www.httrack.com/page/2 "https://www.httrack.com/page/2")
        - [Surf Offline](http://www.surfoffline.com "http://www.surfoffline.com")
        - [Black Widow](https://softbytelabs.com/wp/blackwidow/ "https://softbytelabs.com/wp/blackwidow/")
        - [NCollector Studio](https://ncollector-studio-lite.software.informer.com/ "https://ncollector-studio-lite.software.informer.com/")
        - [Website Ripper Copier](http://websiterippercopier.com/ "http://websiterippercopier.com/")
        - [Teleport Pro](https://teleport-pro.fr.softonic.com/ "https://teleport-pro.fr.softonic.com/")
        - [BackStreet Browser](https://backstreet-browser.fr.softonic.com/ "https://backstreet-browser.fr.softonic.com/")
        - [GNU Wget](https://eternallybored.org/misc/wget/ "https://eternallybored.org/misc/wget/")
- [Waybackmachine](https://archive.org/web/ "https://archive.org/web/") pour voir les anciennes version de l'app et comprendre les anciennes vulnérabilités
    
- Les monitoring tools pour voir les changement et les mis a jour des app.
    
- Tools :
    
    - [Change Detection](https://changedetection.io/ "https://changedetection.io/")
    - [Follow That Page](https://www.followthatpage.com/ "https://www.followthatpage.com/")
    - [Watch That Page](http://www.watchthatpage.com/ "http://www.watchthatpage.com/")
    - [Check4Change extension](https://addons.mozilla.org/en-US/firefox/addon/check4change/ "https://addons.mozilla.org/en-US/firefox/addon/check4change/")
    - [Update Scanner extension](https://addons.mozilla.org/fr/firefox/addon/update-scanner/ "https://addons.mozilla.org/fr/firefox/addon/update-scanner/")

**Footprinting through Email**

- On peut utiliser un email tracer pour révéler pas mal d'info potentielles. Par exemple :
    - Destination address
    - Sender's IP address
    - Sender's Mail server
    - Time & Date information
    - Authentication system information of sender's mail server
- Tools :
    - Polite Mail
    - Email Tracker Pro
    - Email Lookup
    - Yesware
    - Who Read Me
    - Contact Monkey
    - Read Notify
    - Did They Read It
    - Get Notify
    - Point of Mail
    - Trace Email
    - G-Lock Analytics

**Footprinting through Competitive Intelligence**

- Regarder des infos en rapport avec les ops de l'entreprise. Les sources possibles :
    - Official Websites
    - Job Advertisements
    - Press releases
    - Annual reports
    - Product catalogs
    - Analysis reports
    - Regulatory reports
    - Agents, distributors & Suppliers
- Les tools sympa :
    - [EDGAR](https://www.sec.gov/edgar "https://www.sec.gov/edgar")
    - [LexisNexis](https://risk.lexisnexis.com/ "https://risk.lexisnexis.com/")
    - [BusinessWire](https://www.businesswire.com/portal/site/home/ "https://www.businesswire.com/portal/site/home/")
    - [CNBC](https://www.cnbc.com/world/?region=world "https://www.cnbc.com/world/?region=world")
- Avec tous ca, on peut avoir quelque infos tel que :
    - When did the company begin?
    - Evolution of the company
    - Authority of the company
    - Background of an organization
    - Strategies and planning
    - Financial Statistics

**Footprinting through WHOIS**

- Le whois lookup peut inclure les info :
    - Registrant information
    - Registrant Organization
    - Registrant Country
    - Domain name server information
    - IP Address
    - IP location
    - ASN
    - Domain Status
    - WHOIS history
    - IP history,
    - Registrar history,
    - Hosting history
- Les tools sympa pour ca :
    - [LanSpy](https://lizardsystems.com/lanspy/ "https://lizardsystems.com/lanspy/")
    - [TialSoft](http://tialsoft.com "http://tialsoft.com")
    - [http://www.nirsoft.net](http://www.nirsoft.net "http://www.nirsoft.net")
    - [UltraTools](https://www.whois.com/whois/ultratools.com "https://www.whois.com/whois/ultratools.com")
    - Et évidemment whois en command-line.

**Footprinting through DNS**

- DNSRecon pour avoir tous les RR donc voir la note dessus.

![1000004202.jpg](file:///home/wpkaliuser/.config/joplin-desktop/resources/a562fd0d473dbfd8c5a971d6d9774d24.jpg)

- Les tools pour ca y'en a plein :
    - [http://www.dnsstuff.com](http://www.dnsstuff.com "http://www.dnsstuff.com")
    - [http://network-tools.com](http://network-tools.com "http://network-tools.com")
    - [http://www.kloth.net](http://www.kloth.net "http://www.kloth.net")
    - [http://www.mydnstools.info](http://www.mydnstools.info "http://www.mydnstools.info")
    - [http://www.nirsoft.net](http://www.nirsoft.net "http://www.nirsoft.net")
    - [http://www.dnswatch.info](http://www.dnswatch.info "http://www.dnswatch.info")
    - [http://www.domaintools.com](http://www.domaintools.com "http://www.domaintools.com")
    - [http://www.dnsqueries.com](http://www.dnsqueries.com "http://www.dnsqueries.com")
    - [http://www.ultratools.com](http://www.ultratools.com "http://www.ultratools.com")
    - [http://www.webmaster-toolkit.com](http://www.webmaster-toolkit.com "http://www.webmaster-toolkit.com")

**Footprinting through Network**

- On peut chopper des infos general comme :
    - Network address ranges
    - Hostnames
    - Exposed hosts
    - OS and application version information
    - Patch state of the host and the applications
    - Structure of the applications and back-end servers
- Les tools c'est simple c'est juste les ping, tracert, whois ou encore nslookup
- Pour le traceroute :
    - [Keycdn](https://tools.keycdn.com/traceroute "https://tools.keycdn.com/traceroute")
    - [DotCom](https://www.dotcom-tools.com/network-trace-test "https://www.dotcom-tools.com/network-trace-test")
    - [HackerTarget](https://hackertarget.com/online-traceroute/ "https://hackertarget.com/online-traceroute/")

**Footprinting through Social Engineering**

- Pour le se y'a des technique du genre :
    - Eavesdropping
    - Shoulder Surfing
    - Dumpster Diving
    - Impersonation
- Le butin possible :
    - Credit card information.
    - Username & Passwords.
    - Security devices & Technology information.
    - Operating System information.
    - Software information.
    - Network information.
    - IP address & name server’s information.
- Mais pour l'instant y'a pas forcément besoin de s'y interesser.

**Network Scan :**

**Les objectif principaux :**

- To identify live hosts on a network
- To identify open & closed ports
- To identify operating system information
- To identify services running on a network
- To identify running processes on a network
- To identify the presence of Security Devices like firewalls
- To identify System architecture
- To identify running services
- To identify vulnerabilities

**Checking for live systems**

- ICMP request généralement via un ping sweep (host discovery mais sur une large range d'addr en fait).
- Les tools pour ça c'est simple :
    - Angry IP Scanner (ipscan dans le shell)
    - nmap
    - masscan
    - nping
    - hping

**Discovering open ports**

```
- nmap ou hping3
```

**Scanning beyond IDS**  
![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/9cde67c02f0034813f2471b3ca0cf5ee.png)

- Pour echapper au firewall ya plusieurs technique :
    - Decoy Scanning :
        - Avec nmap, on peut faire la commande ** nmap -D RND:10 **où -D spécifie qu'on génére 10 adresse ip aléatoires. La commande **nmap -D IP1,IP2,IP3,IP4,IP5,IP6 **c'est pareil sauf qu'on doit préciser les adresses (ca peut être des adresses aléatoire, on s'en blc).
    - Idle Scanning :
        - C'est le scan où on a un intermédiaire (un zombie) dont on va se servir pour faire le scan direct avec la cible. On va analyser le IPID. C'est une technique sympa si tu veux vraiment être discret mais trop chiante à mettre en place pour le résultat qu'on obtient.
    - Packets Fragmentation :
        - hping3 --scanflags --flood --rand-source --fragment --destport <Target_IP>
        - Explication :
        - `--scanflags <flags>` : Spécifie les indicateurs TCP à utiliser. Vous pouvez spécifier ici les indicateurs appropriés pour votre type de balayage (par exemple, `-S` pour un balayage SYN).
        - `--flood` : Envoie les paquets aussi rapidement que possible.
        - `--rand-source` : Utilise des adresses IP sources aléatoires pour chaque paquet, ce qui peut rendre plus difficile la corrélation des paquets par les IDS.
        - `--fragment` : Fragmente les paquets. Cela divise le paquet en fragments plus petits.
        - `--destport <port>` : Spécifie le port de destination que vous souhaitez balayer.
        - `<Target_IP>` : L'adresse IP de la cible.
    - [https://securiumsolutions.org/scanning-beyond-ids-and-firewall/](https://securiumsolutions.org/scanning-beyond-ids-and-firewall/ "https://securiumsolutions.org/scanning-beyond-ids-and-firewall/") pour plus de technique mais le principal est là.

**Banner grabbing / OS Fingerprinting**

- En gros c'est le processus dans lequel on choppe toute les info d'un système précis d'un réseau et les services qu'il utilise et accessible sur des ports.
- Tools :
    - ID server
    - Netcraft
    - Netcat
    - Telnet
    - Xprobe
    - pof
    - Maltego
    - wget
    - curl
- nmap -o target_ip ca compte dedans aussi pour découvrir l'os de la cible.

**Scanning Vulnerabilities**

**Network Diagram**

- C'est pour visualiser un peu l'architecture de la cible.
- Tools :
    - Network Topology Mapper
    - OpManager
    - Network View
    - LANState Pro

**Proxies**

`- Utilité :`

`- Hiding Source IP address for bypassing IP address blocking.`

`- Impersonating.`

`- Remote Access to Intranet.`

`- Redirecting all requests to the proxy server to hide identity.`

`- Proxy Chaining to avoid detection.`

![1000004229.jpg](file:///home/wpkaliuser/.config/joplin-desktop/resources/f21a7adaef77794aaf7b41a4dc2b3ac9.jpg)

- Tools :
    
    - Proxy Switcher (payant)
    - Proxy Workbench
    - TOR
    - CyberGhost
    - Proxychains
- Anonymizers for mobile :
    
    - orbot
    - psiphon
    - opendoor

IP spoofing

**Enumeration :**

- C'est le moment de la recon active où on établit des vraies connexion avec la cible. En général, c'est là le début des problèmes juridiques car on commence à chopper des infos pas vraiment public.
    
    - Ces informations peuvent être :
        - Routing Information
        - SNMP Information
        - DNS Information
        - Machine Name
        - User Information
        - Group Information
        - Application and Banners
        - Network Sharing Information
        - Network Resources
- **Ne jamais oublier Metasploit qui peut être ultra utile.**
    
    - Techniques d'énumération :
        - Default Credential
            - Y'a souvent des moments où les admins sont des abrutis et oublient de changer les default cred donc toujours tester. On peut par exemple aller sur les sites des fabricants des software et check les guide d'utilisation où ils donnent souvent les default credential (qu'ils devraient à mon avis données seulement quand on achète le produit).
        - SNMP
        - Brute Force sur l'active directory
            - L'AD c'est probablement la plus grosse cible car c'est un annuaire avec tous les utilisateurs sur le réseaux. Il définit les accès et la hiérarchie. LDAP (le protocol de l'AD)  c'est donc à prendre au sérieux et ne pas le laisser de coté.
        - Petit rappel :
        - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/f1f3e1da0fd9ade02bbb3b5c46d21160.png)
- Bon enfin pour tous ca, ils faut connaitre les services utilisés par la cible.
    
    - On peut donc utiliser nmap pour faire de la recon de services :
        - nmap -sU -p 161 target_ip pour voir si la cible utilise SNMP (essaye aussi avec 162)
        - nmap -sS target_ip pour voir les services et port ouverts.
        - nmap -sSV -v -O target_ip pour trouver l'os et les versions des services utilisés.
- **NETBIOS**
    
    - C'est un protocole utilisé pour la  communication des périphériques en LAN. Les périphériques sont désigné par un nom sur 15 caractère ASCII (un 16ème pour désigner le service) contenant seulement des maj, des numéros, des _ ou $. Exemple : FILESERVER_Y.
        
    - Comme dit avant, le 16 caractère va servir pour identifier le service.
        
    - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/2abfdfeb56b3913d5491c7a1b2376e8f.png)
        
    - Ports utilisés :
        
        - UDP 137 : name service pour la résolution des noms
        - UDP 138 : Datagram service pour les communications en datagram (messages court, non fiables pour la com entre ordinateur)
        - TCP 139 : Session service pour les communications fiables et bidirectionnels entre les devices comme le partage de fichier entre les imprimantes par exemple.
    - Les informations pouvant être obtenues sont interéssantes :
        
        - List of Machines within a domain
        - File Sharing
        - Printer Sharing
        - Username
        - Group information
        - Password
        - Policies
    - Tools :
        
        - nbtscan :
            - nbtscan target_ip pour faire une recon ciblé sur une ip
            - nbtscan -v -s : 192.168.1.0/24 pour chopper toute les infos netbios sur tout les devices.
        - Metasploit
        - Et pas grand chose d'autre pour linux. Sinon pour windows y'a Hyena, nbstat, Nsauditor Network security auditor (payant).
- **SMB**
    
    - Server Message Block c'est vraiment le protocole d'échange de fichier, de suppression à distance, lecture ou autre. A la différence de NETBIOS où il était en réalité plutôt utilisé comme une couche de transport pour SMB pour la résolution de nom... NETBIOS sera peu à peu remplacé par d'autre protocoles.
    - Port utilisés :
        - TCP 445 ou 139
    - Tools :
        - Metasploit
        - nmap pour avoir la version :
            - nmap -p445 --script smb-protocols target_ip teste aussi pour p139
            - nmap -sC -p 139,445 -sV target_ip c'est un peu mieux que la première commande.

A COMPLETER ET À ENTRAINER CAR IMPORTANT ET PAS MAL DE LAB JE CROIS. mini guide [https://arnavtripathy98.medium.com/smb-enumeration-for-penetration-testing-e782a328bf1b](https://arnavtripathy98.medium.com/smb-enumeration-for-penetration-testing-e782a328bf1b "https://arnavtripathy98.medium.com/smb-enumeration-for-penetration-testing-e782a328bf1b")

- **SNMP**
    
    - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/a65926bbac00cbba7ea7fee2966e234f.png)
    - Simple Network Management Protocol c'est un protocole hyper important car il permet aux admins de gérer tous le réseau. C'est sur le port udp 161/162. Il est principalement constitué de 3 éléments :
        - **SNMP Manager :** C'est en gros l'endroit principal où l'admin gère le réseau. C'est un peu la tour de contrôle.
        - **SNMP Agents : **C'est tous les périphériques du réseau donc ça comprend les imprimantes, les pc, les caméras, les routeurs (qui peuvent également faire partie du snmp manager) etc...
        - **Management Information Base (MIB) :** C'est la database virtuel dans laquelle sont désignées hiérarchiquement les données relatives aux devices.** Elle ne contient pas les données mais indiquent où les trouver.** Elle se trouve sur tous les appareils du réseau. En gros, elle est sous forme d'arbre dans lequel chaque noeud (objet) est désigné par un Object Identifiers (OIDs). Cet OID est sous la forme d'une suite d'entier par exemple 1.3.6.1.4.1.343 pour désigner l'intel corporation.
    - Dans la v1, v2 de SNMP, y'a pas d'encryption du tout. Dans la v3, y'a trois modèle : NoAuthNoPriv où y'aura pas d'encryption ni de hasking. AuthNoPriv où y'a qu'un des deux qui sera utilisés et enfin AuthPriv où encryption et hashing sont utilisé pour le traffic.
    - Y'a une notion importante dans le protocole SNMP c'est les community string. En gros c'est une clé qui gère les accès aux autres devices.
        - **SNMP Read-Only** : Permet d'énumérer les info d'un device (à distance évidemment)
        - **SNMP Read-Write** : Permet de même les modifier
        - **SNMP Trap** : La trap c'est quand le device envoie une information au manager sans qu'il ait demandé. Comme une erreur ou un truc du genre.
    - Dans les grands réseaux, les SNMP manager utilisent des outils comme OPManager, PRTG ou Solarwinds.
    - Tools pour énumérer :
        - Metasploit
        - SNMPWalk
        - OpUtils
        - NsAuditor
    - [https://book.hacktricks.xyz/generic-methodologies-and-resources/brute-force#snmp](https://book.hacktricks.xyz/generic-methodologies-and-resources/brute-force#snmp "https://book.hacktricks.xyz/generic-methodologies-and-resources/brute-force#snmp")
- **LDAP**
    
    - Lightweight Directory Access Protocol c'est un protocole pour les dossiers partagé d'un réseau. Le client créer une session LDAP en envoyant une requête au Directory System Agent (DSA, c'est le server LDAP qui stocke et gère les données et les annuaires) sur le port **TCP 389.**
    - Les services qui utilisent LDAP incluent :
        - Active Directory
        - Open Directory
        - Oracle IPlanet
        - Novell eDirectory
        - OpenLDAP
    - [https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap](https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap "https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap")
    - Tools :
        - [JXplorer](https://jxplorer.org/ "https://jxplorer.org/")
        - [LDAP Administration Tool](https://sourceforge.net/projects/ldapadmin/ "https://sourceforge.net/projects/ldapadmin/")
        - [LDAP Account Manager](https://www.ldap-account-manager.org/lamcms/ "https://www.ldap-account-manager.org/lamcms/")
        - [Active Directory Explorer](https://learn.microsoft.com/fr-fr/sysinternals/downloads/adexplorer "https://learn.microsoft.com/fr-fr/sysinternals/downloads/adexplorer")
        - LDAPsearch (command line kali linux)
        - enum4linux
        - [windapsearch](https://github.com/ropnop/windapsearch "https://github.com/ropnop/windapsearch")
        - nmap évidemment pour découverte de port ouvert
- **NTP**
    
    - Network Time Protocol c'est un protocole qui sert à synchroniser tous les devices du réseau sur le même plan horaire et séquentiel. C'est hyper important pour les logs, les certificats parfois, les planificateurs de tâches ou autre. Un stratum c'est comme un TTL qui diminue à chaque hop. Si y'a un stratum 10 sur le router local, le server NTP est donc à 9 hop. NTP est important dans le pentest car les attaquants peuvent induire en erreur le forensic.
    - Pour la configuration de NTP, le server doit authentifier tous les devices. Sans ça, les devices du réseau ne vont pas considérer le server comme safe et vont donc pas l'utiliser.
    - Pour l'énumération, l'attaquant peut envoyer une requête au server NTP et donc extraire des données tels que :
        - Host information connected to NTP server
        - Client IP address, Machine name, Operating System information
        - Network information such as Internal IPs depends upon deployment of
        - NTP server, i.e., if NTP server is deployed in DMZ.
    - Tools :
        - Nmap mini guide [https://www.geeksforgeeks.org/what-is-ntp-enumeration/](https://www.geeksforgeeks.org/what-is-ntp-enumeration/ "https://www.geeksforgeeks.org/what-is-ntp-enumeration/")
            - nmap target_ip -sU -Pn -p123 --script ntp-info
        - ntpq (command line)
        - Wireshark (possible avec monitor mode je crois)
        - Metasploit (encore oit)
- **SMTP**
    
    - Simple Mail Transfer Protocol c'est simplement le protocole utilisé pour les mails. Y'a un Email server et des client au travers d'internet via le port TCP 25 ou de temps en temps 587 pour des communications chiffrées.
    - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/9d36e582f1178fa1f0ce3da06c02b621.png)
    - Tools :
        - smtp-user-enum
            - [https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum "https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum")
        - Metasploit
- **HTTP**
	- *ETag*
		- Si les [[Protocoles#**HTTP** Hyper Text Transfer Protocol|ETag]] du serveur sont généré à partir des [[Trucs cools à savoir#^9a4a17|inodes]], alors on peut récupérer des informations sur les fichiers et sur le contexte en général. A approfondir. 
- **Les contre-mesures à prendre en comptes :**
    
    - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/ae16b04473a064744b9b87d2c7754eb4.png)

**Vulnerability Analysis :**

- Y'a 4 types d'évaluations de vuln :
    - **Évaluation active : **
        - Cela requiert une connexion direct avec les hôtes ce qui peut être moins discret. On peut carrément interferer avec le traffic habituel donc niveau furtivité, c'est pas simple.
    - **Évaluation passive :**
        - C'est un peu pareil sauf qu'on interfere pas avec le traffic, on créer pas de problème potentiel en fait. Ca peut inclure le sniffing, l'analyse de logs ou autre tu vois lgenre.
    - **Évaluation externe :**
        - Ça c'est sympa c'est l'évaluation mais d'extérieur donc quand on en fait, on cherche des vulnérabilité possible alors qu'on est en dehors du réseau.
    - **Évaluation interne :**
        - Bah là c'est en ayant un accès au réseau.
- Avant même de tester et repérer des vulnérabilités sur un protocole, un device ou autre, tu dois toujours avoir une compréhension parfaite du software. C'est comme ca qu'on trouve les meilleurs vulnérabilités. C'est en étant créatif et frapper là où on s'y attend pas. Pour ça, il faut connaître chaque détails du software.
- Scanning tools :
    - Nessus
    - OpenVAS
    - Nexpose
    - Retina
    - GFI LanGuard (payant)
    - Qualys (payant)

![1000004190.jpg](file:///home/wpkaliuser/.config/joplin-desktop/resources/ec5bcbd84b3549bbdd1f6a69e5224ead.jpg)
