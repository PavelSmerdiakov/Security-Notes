**Définition :**

- **DNS :**
    - Ca transforme les noms de server "human-readable" vers des adresses ip ou inversement. On appelle ca la résolution DNS.
    - Cheat sheet DNS Resolver :

![how_dns_work.jpg](file:///home/wpkaliuser/.config/joplin-desktop/resources/fc3ef1dff4c9df95b3c56b310de4cfbf.jpg)

- **TLD :**
    
    - Top-level-domain. C'est .net, .com etc...
- **Zone file :**
    
    - Fichier txt sur un server qui stocke les RR. Chaque ligne désigne une RR différente mais si elle sont trop grande, on utilise des parenthèses.
- **Ressource Record (RR) :**
    
    - Données associés à la résolution de nom de domaine.
        
    - RR list (à compléter si besoin) :
        
        1. **A (Address) Record** : Associe un nom de domaine à une adresse IPv4.
            
        2. **AAAA (IPv6 Address) Record** : Associe un nom de domaine à une adresse IPv6.
            
        3. **CNAME (Canonical Name) Record** : Crée un alias pour un autre nom de domaine, permettant ainsi de rediriger un nom vers un autre. Par exemple, un CNAME peut être utilisé pour rediriger "www" vers le domaine principal.
            
        4. **MX (Mail Exchange) Record** : Spécifie les serveurs de messagerie (serveurs de courrier) responsables de la réception des courriers électroniques pour un domaine. Il indique la priorité des serveurs de messagerie en cas de plusieurs serveurs MX.
            
        5. **TXT (Text) Record** : Stocke des informations textuelles arbitraires, souvent utilisées pour des enregistrements de vérification pour les services tels que SPF (Sender Policy Framework) ou DKIM (DomainKeys Identified Mail).
            
        6. **NS (Name Server) Record** : Indique les serveurs de noms autoritaires pour un domaine. Ces serveurs de noms sont responsables de la gestion des enregistrements DNS pour le domaine.
            
        7. **SOA (Start of Authority) Record** : Contient des informations sur la zone DNS, telles que l'adresse de messagerie de l'administrateur de la zone, la durée de vie des enregistrements (TTL), le numéro de série de la zone, etc.
            
        8. **PTR (Pointer) Record** : Utilisé dans la résolution inverse (pour les adresses IP) pour mapper une adresse IP à un nom de domaine. Il est principalement utilisé dans le DNS inverse.
            
        9. **SRV (Service) Record** : Permet de spécifier les serveurs offrant un service particulier (par exemple, un serveur de messagerie, de chat, etc.) pour un domaine. Il inclut des informations sur le port et la priorité du serveur.
            
        10. **CAA (Certification Authority Authorization) Record** : Utilisé pour définir quelles autorités de certification (CAs) sont autorisées à émettre des certificats SSL/TLS pour un domaine spécifique.
            
        11. **NAPTR (Naming Authority Pointer) Record** : Utilisé pour définir des règles de réécriture des noms de domaine, souvent associé à la normalisation des numéros de téléphone VoIP.
            
        12. **HINFO (Host Information) Record** : Contient des informations sur le matériel et le système d'exploitation utilisés par un hôte.
            
        13. **LOC (Location) Record** : Stocke des informations de géolocalisation d'un hôte ou d'une ressource.
            
        14. **DNSKEY (DNS Key) Record** : Contient des clés publiques pour sécuriser les communications DNS à l'aide de DNSSEC (Domain Name System Security Extensions).
            
        15. **DS (Delegation Signer) Record** : Utilisé dans le DNSSEC pour référencer la clé publique d'une zone parente.
            
- **Authoritative NameServer :**
    
    - C'est le server qui stocke toute les RR d'un domaine. Y'en a un par domaine ou sous-domaine. Il sert à renvoyer les données demandées quand le recursive server ne les possèdent pas.
        
    - Processus quand le recursive server n'a pas les données demandées dans son cache :
        
        1. Il demande au root server (server qui contient les adresses ip des TLD server) le TLD server du domaine spécifié. Le root server lui renvoie alors.
            
        2. Ensuite, le recursive server envoie une requête avec le nom du SLD ([monsite.com](http://monsite.com "http://monsite.com") par exemple) au TLD server. Le TLD server va donc renvoyer l'adresse ip du SLD server (authoritative nameserver du domaine demandé).
            
        3. Le recursive server envoie une nouvelle requête avec le nom complet du domaine recherché à l'authoritative nameserver. Si on cherche un sous-domaine, l'ANS va renvoyer l'adresse ip de l'ANS du sous-domaine. Sinon, il renvoie l'adresse ip du domaine recherché. Le recursive server va donc stocker cette combinaison adresse ip/domain name dans son cache pendant un certain temps (TTL spécifié dans les RR du ANS)
            
- Whois service et commande :
    
    - Service extrémement important dans le pentest pour la recon. Ce service est une database qui stocke les infos des domaines et ce qu'il y a autour. Ca peut etre des adresses ip, des numéros, des mails, et même des adresses. La commande importante c'est juste whois exemple.com mais y'a aussi le site [whois](https://www.whois.com/whois/ "https://www.whois.com/whois/").


- **Transfert de zone :**
	- Premièrement on a un serveur qui contient toute les informations DNS originales dans un fichier. Donc quand y'a des changements dns qui se font, c'est sur ce serveur qu'ils se produisent. Ensuite, on a les serveurs secondaires qui contiennent des copies des zones principales du serveur DNS "Maitre". On les appelles les slaves. Quand y'a des changements, le maitre envoie une notification aux slaves et eux, ils demandent une copie des infos.
	- Si on arrive à effectuer un zone transfert vers notre propre machine, on récupère toute les informations DNS du serveur.
	- Pour le faire, on peut utiliser dig :
		- `dig challenge01.root-me.org`  Pour chopper l'adresse ip du domaine responsable de celui qui est vulnérable.
		- `dig @ip_address_quon_a ch11.challenge01.root-me.org -p 53 -t any AXFR` Pour effectuer le zone transfert.

- **DNSDumpster**
	- Pour mapper le contexte DNS d'une cible, tu peux utiliser DNSDumpster sur internet. Il donne un bon paquet de RR et propose une map des server/adresse.