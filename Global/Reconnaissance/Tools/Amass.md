**Amass**  
FAIRE LES API KEYS AVEC LES SITES SUIVANTS :

`AlienVault, BinaryEdge, BufferOver, BuiltWith, C99, Censys, Chaos, CIRCL, DNSDB, DNSTable, FacebookCT, GitHub, HackerOne, HackerTarget, NetworksDB, PassiveTotal, RapidDNS, Riddler, SecurityTrails, Shodan, SiteDossier, Spyse, Twitter, Umbrella, URLScan, VirusTotal, WhoisXML, ZETAlytics, Cloudflare`

Pourquoi l'utiliser ? Il est plus polyvalent et complet de Anubis.

**Flag :**

Y'a beaucoup trop de truc donc cherche là dedans pour une vue complète. [https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md](https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md "https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md")

**Commandes coolos :**

Y'a deux modes :

_intel_ pour la première étape de la recon. C'est là où on collecte toutes les infos général.

_enum_ pour la deuxième étape de la recon. C'est là où on affine un peu nos recherche avec les infos qu'on a eu avec l'intel. On cherche une surface d'attaque potentiel pour énumérer les infos qu'on aurait besoin.

Intel :

Enum :

`amass enum -d example.com`

Cette commande donne tout les sous domaines qu'il trouve avec pas mal de ressource records intéressantes. Mais par contre ne pas l'utiliser sur des grosses app car tu te doutes bien que quand y'a des milliers de sous-domaines ton pc il a chaud.