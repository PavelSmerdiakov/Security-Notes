## **STP** : Spanning Tree Protocol

- Protocole qui gère les chemins du trafic pour ne pas avoir de boucles ou de conflits.
- Quand y'a plusieurs switch sur un réseau (quand le STP est présent quoi), un root switch est désigné et c'est lui qui va gérer tous ça.
- Pour que les switch se mettent d'accord sur qui est le root, on utilise leur BID (Bridge Identifier) qui est composé de l'adresse MAC et du Switch priority (nombre sur 12bits, par défaut égale à 0x8000). Par défaut, c'est le switch avec le BID le plus bas qui est élu Root Bridge. En cas d'égalité, c'est l'adresse MAC la plus basse qui est élue.
- [https://openspacecourse.com/le-protocole-stp/](https://openspacecourse.com/le-protocole-stp/ "https://openspacecourse.com/le-protocole-stp/")

## **NDP** : Neighbor Discovery Protocol

- Protocole équivalent de l'ARP mais pour les réseau IPv6.
- La machine envoie un Neighbor solicitation au switch donc en multicast et le routeur renvoie un Neighbor Advertisement.


## **HTTP** : Hyper Text Transfer Protocol
RFC utilisée : RFC 2616, RFC 1864, RFC 2818
- Protocol au niveau de la couche application qui permet de partager tout type d'informations.
- *URI* : Uniform Ressource Identifier, c'est des chaines de caractères normalisées qui permettent d'identifier des ressources sur internet. Par exemple, un *URL* (http://test.com) permet d'identifier l'adresse d'une ressource. C'est donc un URI. 
- Pour rappel, un **scheme** c'est un mot pour désigner le protocole utilisé. Il est utilisé dans les URL par exemple.
- Pour la version HTTP (1.0, 1.1), le premier chiffre c'est le *major* et le deuxième c'est le *minor* . C'est un peu pareil pour tout les protocoles.
- Un **token** c'est un mot/entité d'une ligne.
	- Par exemple, dans la **Request-Line** `GET /ssdp/device-desc.xml HTTP/1.1\r\n`, GET c'est un token.
- **MIME (Multipurpose Internet Mail Extensions)** c'est un mécanisme standard utilisé pour indiquer le type de média et le format de données d'une ressource sur Internet. Cela permet aux navigateurs web et aux autres agents utilisateur de comprendre comment interpréter et traiter les données reçues d'un serveur. Il est spécifié dans l'header Content-Type d'une réponse HTTP. 
- La compression de données possible d'un paquet que supporte le client est spécifié dans la requête HTTP 1.1 avec le token *Accept-encoding*. On a gzip ou x-gzip par exemple.
- *transfer-coding* (fais gaffe y'a pas de majuscule et c'est case-sensitive) c'est la méthode de transformation du corps du message pour le transport sur le réseau. On peut avoir une valeur comme chunked ou transfer-extension.
- *User-Agent* est un header qui spécifie l'user-agent du client.
	- Exemple :
		- `User-Agent: CERN-LineMode/2.15 libwww/2.17b3`
- *Trailer* c'est un header qui inclut des champs additionnel de données header qui peuvent être dynamiques.
	- Exemples :
```
HTTP/1.1 200 OK
Content-Type: text/plain
Transfer-Encoding: chunked
Trailer: Expires

7\r\n
Mozilla\r\n
9\r\n
Developer\r\n
7\r\n
Network\r\n
0\r\n
Expires: Wed, 21 Oct 2015 07:28:00 GMT\r\n
\r\n

```
- *ETag* est un header qui permet de s'assurer que les ressources demandés n'ont pas été changées. Un serveur envoie un ETag au client qui lui va le mettre dans son cache donc quand il redemande la page, il va renvoyer le ETag et le serveur va lui dire si il a été changé (à cause de modifications de ressources) ou pas. 
- *Last-Modified* et *ETag* permettent entre autre au client de conaitre quelle version de la ressource on demande. Last-Modified est envoyé uniquement par le serveur alors que le ETag peut être utilisé par le client également.
- *Referer* est un header qui indique l'URI à laquelle se trouver le client avant d'aller à la ressource demandée.
- *Content-MD5* ([RFC 1864](https://repository.root-me.org/RFC/EN%20-%20rfc1864.txt))est un header VULNERABLE étant donnée que MD5 est vulnérable au attaque par collision (2 input peuvent produire le même hash donc vulnérable quand on parle de signature), au reversing et au brute force (dû à sa rapidité de génération) . C'est utilisé comme un MIC (Message Integrity Check, c'est-à-dire un petit token qui sert à s'assurer que le message n'a pas été altéré pendant la transmission). Le token n'est généré qu'à partir d'un user agent et évidemment du message. Puis, quand le serveur a reçu la requête, il vérifie à son tour si le hash est correct. La sortie de l'algorithme MD5 est un 128bits digest. Quand on capture un paquet, on le voit encodé en plus en Base64. On pourrai voir ce header sous la forme :
	- `Content-MD5:  Q2hlY2sgSW50ZWdyaXR5IQ==`
- *Content-Range* est un header qui spécifie la taille des données dans le paquet quand on est en présence d'un message partiel (en morceaux). 
	- Exemple :
	       HTTP/1.1 206 Partial content
	       Date: Wed, 15 Nov 1995 06:25:24 GMT
	       Last-Modified: Wed, 15 Nov 1995 04:58:08 GMT
	       Content-Range: bytes 21010-47021/47022
	       Content-Length: 26012
	       Content-Type: image/gif
- *Location*  
- *Content-Location* est un header qui indique l'URL de la ressource renvoyée dans la réponse. C'est différent de Location dans le sens où là, on parle de la donnée qui est envoyé alors qu'avec Location, on parle de la donnée où l'on est redirigée. C'est un peu abstrait comme différence ceci-dit.
	- Syntaxe : 
		- `Content-Location: /my-first-blog-post`
- *Accept-Ranges* est un header qui est utilisé par le client pour préciser s'il accepte le téléchargement partielle (reçoit la ressource en plusieurs morceaux/paquets). Si c'est avec une valeur en bytes, cette valeur sera la taille des paquets. Si c'est sur *None*, le client ne l'autorise pas et donc toute la ressource sera envoyé dans un seul paquet (énorme).
- *Accept-Encoding* est un header qui indique les type d'encodage que l'émetteur accepte. 
	- Syntaxe :
		- `Accept-Encoding: gzip;q=1.0, identity; q=0.5, *;q=0`
- *Accept-Charset* est un header qui indique les types de caractère encoding que l'émetteur accepte
	- Syntaxe : 
		- `Accept-Charset: iso-8859-5, unicode-1-1;q=0.8`
- *Allow* est un header qui liste les méthodes supportées par une ressource. Il doit être envoyé si le serveur répond avec un 405 Method Not Allowed.
	- Syntaxe :
		- `Allow: GET, HEAD, PUT`
- *Connection* est un header qui contrôle la façon dont la connexion reste ouverte ou non après que la transaction courante soit terminée. `keep-alive` veut dire que la connexion persiste. Sinon c'est `close`
- *Cache-Control* c'est un header qui contient des directives (instructions) dans les requêtes et dans les réponses pour contrôler la mise en cache dans les browsers. Les directives sont non sensitive case, séparées par des virgules et certaines d'entres elles ont des arguments optionnels.
	- <table>
  <thead>
    <tr>
      <th>Requête</th>
      <th>Réponse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>max-age</code></td>
      <td><code>max-age</code></td>
    </tr>
    <tr>
      <td><code>max-stale</code></td>
      <td>-</td>
    </tr>
    <tr>
      <td><code>min-fresh</code></td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>s-maxage</code></td>
    </tr>
    <tr>
      <td><code>no-cache</code></td>
      <td><code>no-cache</code></td>
    </tr>
    <tr>
      <td><code>no-store</code></td>
      <td><code>no-store</code></td>
    </tr>
    <tr>
      <td><code>no-transform</code></td>
      <td><code>no-transform</code></td>
    </tr>
    <tr>
      <td><code>only-if-cached</code></td>
      <td>-</td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>must-revalidate</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>proxy-revalidate</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>must-understand</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>private</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>public</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>immutable</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td><code>stale-while-revalidate</code></td>
    </tr>
    <tr>
      <td><code>stale-if-error</code></td>
      <td><code>stale-if-error</code></td>
    </tr>
  </tbody>
</table>

- *Content-Type* indique le type MIME de la ressource envoyée. Des fois, le browser veut détecter lui-même le type MIME de la ressource en l'inspectant. Pour l'en empêcher, on peut utiliser l'header **X-Content-Type-Options**. Les valeurs de Content-Type possibles sont : 
	- *text/plain* : Texte brut
	- *text/html* : Document HTML
	- *application/json* : Objet JavaScript en notation JSON
	- *image/jpeg* : Image JPEG
	- *audio/mpeg* : Fichier audio MPEG
	- *video/mp4* : Fichier vidéo MP4
	- *application/pdf* : Document PDF
	- *application/xml* : Document XML
- *WWW-Authenticate* 
	- Il définit la méthode d'authentification qui doit être utilisé pour avoir l'accès à une ressource. Syntaxe :
		- `WWW-Authenticate: <type> realm=<realm>` 
	- Exemple : 
		- `WWW-Authenticate: Basic realm="Accès Restreint"`
	- Realm en gros c'est utilisé pour dire qui y a accès et type c'est le type de connexion, souvent en basic ou parfois en digest. Ces types sont apparentés à des challenges/credentials.
- *Expect* est un header qui indique ce que le client s'attend à recevoir si tout se passe bien.
	- Exemple :
		PUT /somewhere/fun HTTP/1.1
		Host: origin.example.com
		Content-Type: video/h264
		Content-Length: 1234567890987
		Expect: 100-continue
	- Ici, le client s'attend à recevoir un 100 Continue.
	- Si le serveur ne comprend pas ou ne peut pas répondre correctement à la requête comme le client le veux, il renvoie un 417 Expectation Failed.
- *Expires* est un header qui indique la date ou la durée maximum de validité d'un cache.
	- Exemple :
		- `Expires: Thu, 01 Dec 1994 16:00:00 GMT`
- *From* est un header qui spécifie l'e-mail de l'émétteur.
	- Exemple :
		- `From: webmaster@w3.org`
- *Accept* indique les types de contenu exprimé sous la forme de MIME que le client est capable d'interpréter. 
	- Syntaxe :
		- `Accept: <MIME_type>/<MIME_subtype>`
		- `Accept: <MIME_type>/*`
		- `Accept: */*`
		- Toute les valeurs sont placées selon un ordre de préférence exprimé par une *quality value* `;q=` qui a pour valeur max 1.
		- `Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8`
		- où les 2 premiers sont à 1 (sont les préférés) et les 2 derniers sont spécifiés.
- **Les requêtes conditionnelles** :
	- Elles sont utilisées pour comparer les ressources demandées avec celles que le serveur possède. Dans ces requêtes, on a soit :
		- *Une validation forte* où l'on demande une validation/comparaison de la ressource octet par octet. On le fait souvent en employant une ETag avec le hashage MD5 de la ressource (ou un dérivé).
		- *Une validation faible* qui considère deux ressources identiques si le contenu est équivalent. Mais ça peut être basé simplement sur la date ou sur un autre paramètre du même délire. Ça  dépend du contexte.
	- Pour conditionner les requêtes, on utilise plusieurs headers HTTP :
		- *If-Match* : Réussit si la ETag de la ressource demandée est égal à un de ceux listés dans l'header de la requête. Par défaut, sauf si l'ETag est préfixé par `/W`, c'est une validation forte.
		- *If-None-Match :* : Réussit si la ETag de la ressource demandée est différent de tout ceux listés dans l'header de la requête. Par défaut, sauf si l'ETag est préfixé par `/W`, c'est une validation forte.
		- *If-Modified-Since* : Réussit si la date `Last-Modified` de la ressource distante est plus récente que celle de l'header de la requête.
		- *If-Unmodified-Since* : Réussit si la date `Last-Modified` de la ressource distante est plus vieille que celle de l'header de la requête.
		- *If-Range* : Comme If-Match et If-Unmodified-Since mais avec un seul ETag ou une seul date. Si ça ne correspond pas, la requête est rejetée. Sinon, c'est un 200 OK qui est envoyé avec la totalité de la ressource.
	- Ces requêtes on les utilisent pour le cache notamment. Si le cache est obsolète (pour le savoir, on utilise l'header Expires et Cache-Control qui donne des informations sur la durée de vie avec max-age ou comment il doit être validé avec must-revalidate ou no-cache),  le client envoie une requête avec peut-être le If-Modified-Since ou If-None-Match. Le serveur va envoyé, si la ressource n'a pas changée, un 304 Not Modified ou alors un 200 OK si la ressource a bel et bien changée.
- 
- La **Request-URI** c'est la ligne qui spécifie la ressource qu'on chercher à acquérir.
	- Exemple 1 :
		- `GET http://www.w3.org/pub/WWW/TheProject.html HTTP/1.1`
	- Exemple 2 :
		- `GET /pub/WWW/TheProject.html HTTP/1.1`
		- `Host: www.w3.org` w3.org c'est l'hôte et du coup /pub/www/TheProject.html c'est un relative URI (dépendant de son contexte) et pas un absolute URI (indépendant de son contexte). L'header Host est donc nécessaire.
- **Code HTTP**
	- *100* : Continue. Autorise au client d'envoyer les données qu'il souhaite. C'est utile dans les cas où les données sont volumineuses car ça servirait à rien d'envoyer 3 kg de données alors que le serveur ne le regarde même pas. Si le serveur refuse, il envoie un 417 à la place. Pour demander un 100 continue, le client met le header expectation 100 continue 
	- *200* : OK. Indique que la requête a bien été effectuée. Cependant, la signification exacte dépend de la méthode de la requête : 
		- *GET* : La ressource est cherchée et transmise dans le message body de la réponse.
		- *HEAD* : La réponse avec les headers est bien envoyée
		- *POST* : La ressource qui décrit le résultat de l'action est transmise dans le message body
		- *TRACE* : Le message body contient le message de la requête tel qu'il est reçu par le serveur.
	- *201* : Created. Indique que la ressource a bien été créée. Le 201 est envoyée après la création avec la ressource dans le body. 
	- *202* : Accepted. La requête est accepté mais pas encore effectuée. 
	- *204* : No Content. La requête est effectué mais n'a rien à renvoyer. 
	- Les *3xx* indiquent que l'utilisateur doit effectuer une action pour que la requête se fasse correctement.
	- *300* : Multiple Choices. Indique que le client doit faire un choix pour continuer la requête. 
	- *301* : Moved Permanently. Indique que la ressource a été bougée à un nouvel URI. Ce nouvel emplacement doit être contenu dans l'header *Location*. Les browsers redirigeront l'utilisateur vers cette nouvel page seulement si c'est une requête HEAD ou GET puis les moteurs de recherche mettront à jour leurs liens vers la ressource.
	- *302* : Found. Indique que la ressource a été bougée à un nouvel URI. Ce nouvel emplacement doit être contenu dans l'header *Location*. Les browsers redirigeront l'utilisateur vers cette nouvel page seulement si c'est une requête HEAD ou GET. Cependant, les moteurs de recherche ne mettront pas à jour leurs liens vers la ressource.
	- Les *4xx* sont des erreurs de la part du client.
	- *400* : Bad Request. La requête n'est pas comprise le serveur à cause de la syntaxe. Le client ne doit pas répéter la requête sans modifications.
	- *401* : Unauthorized. Le client n'est pas autorisé car il manque des informations valides. La réponse doit être envoyée avec l'header WWW-Authenticate qui indique le type d'authentification. ^a09ef8
	- *402* : Payment Required. Le nom va de soi
	- *403* : Forbidden. Le serveur comprend la requête mais ne l'autorise pas. C'est comme 401 Unauthorized mais l'accès est définitivement bloqué.
	- *404* : Not Found. Le serveur n'a pas trouvé l'URI de la requête et n'a aucune informations dessus.
	- *405* : Method Not Allowed. Le nom va de soi 
	- *408* : Request Timeout. Le client n'a pas répondu assez rapidemment au serveur. Le client peut tout de même répéter la requête.
	- *417* : Expectation Failed. Le nom va de soi. 
	- Les *5xx* sont des erreurs de la part du serveur.
	- *500* : Internal Server Error. Le serveur a rencontré une situation inattendue ce qui l'empêche de fonctionner correctement.
	- *501* : Not Implemented. Le serveur ne supporte pas la fonctionnalité pour réaliser la requête. Ça peut être une méthode par exemple. Cependant, les méthodes qui ne peuvent jamais renvoyer un 501 sont les GET et HEAD.
	- *502* : Bad Gateway. Le serveur qui agit comme gateway ou proxy a reçu une réponse invalide de la part du serveur en amont.
	- *503* : Service Unavailable. Le serveur est injoignable dû à une maintenance, une demande trop élevée de requêtes ou simplement que le serveur n'accepte pas de requêtes.
	- *504* : Gateway Timeout. Le serveur qui agit comme gateway ou proxy n'a pas reçu de réponse de la part du serveur en amont spécifié par l'URI dans le temps impartis.
- **Méthode HTTP**
	- Safe Method :
		- *GET*
			- C'est pour demander une ressource. La requête ne doit pas contenir de données.
		- *OPTIONS*
		- *HEAD* :
			- C'est comme le GET sauf que dans la réponse, y'a pas de message body, seulement des headers. Donc quand le client envoie une requête HEAD, il demande simplement les metadata associées à une ressource du serveur. Le serveur va donc envoyées les headers. C'est utile quand le client demande juste des informations avant de télécharger une ressource complète.
		- *POST*
			- C'est pour envoyer des données au serveur. Le type du corps (Le MIME) de la requête est indiqué par l'header Content-Type.
			- Si le Content-Type a une valeur *application/x-www-form-urlencoded*, la donnée est formaté avec des & et des +. Par exemple : `nom=John&age=30`. Les caractères spéciaux sont encodés en urlencode donc "+" va donner %20 et "&" va donner %26. Y'a d'autre type de format comme *multipart/form-data* pour les données binaires ou *text/plain* pour du raw text.
			- Si la ressource fut bien créée sur le serveur, un 201 Created est envoyé au client. 
			- Exemple de requête POST :``
				- POST / HTTP/1.1
				- Host: foo.com
				- Content-Type: application/x-www-form-urlencoded ^844b0b
				- Content-Length: 13
				- say=Hi&to=Mom
		- *DELETE* 
			- C'est pour supprimer une ressource du serveur. Elle peut être cependant annulé par une intervention humaine donc le client n'a aucun moyen de savoir si la donnée est toujours présente, même s'il reçoit une réponse qui lui dit qu'elle est supprimée (un 200 OK, un 202 Accepted ou encore un 204 No Content)
		- *TRACE*
			- C'est pour voir la requête exacte envoyé par le client au serveur. Son fonctionnement est le suivant :
				- Le client envoie une TRACE request vers une ressource d'un serveur.
				- Le serveur renvoie exactement la même requête que le client a envoyé sans body.
				- Le client reçoit alors les headers qui peuvent inclure des cookies, des headers d'authentification, etc...
			- C'est utilisé pour le déboguage ou pour obtenir des informations sur le fonctionnement interne du serveur (tiens tiens tiens). Avec des TRACE request, on peut faire par exemple des XST (Cross-Site Tracing) qui peuvent mener à des hijacking, des XSS ou des information disclosure. Voir https://owasp.org/www-community/attacks/Cross_Site_Tracing.
		- *CONNECT* 
			- C'est pour créer uen communication bidirectionnelle avec la ressource demandée. Ça peut être utilisé pour ouvrir un tunnel SSL par exemple.

	- Unsafe Method :
		- *PUT* 
			- C'est presque comme POST. La différence entre POST et PUT c'est que PUT est une méthode *idempotente* (si la même donnée est envoyée plusieurs fois avec succès, elle aura toujours le même effet) alors que POST peut causer des effets secondaires (addition d'action, passer plusieurs fois une commande...) 
			- C'est une méthode considérée comme unsafe car elle peut upload des fichiers directement sur le serveur sans validations. Il faut cependant des credentials en général pour pouvoir se connecter au service évidemment.
- Le **Content Negotiation** c'est le mécanisme qui permet au client et au serveur de déterminer entre eux le meilleur format à utiliser dans la communication.
	- Y'a la *User Agent-driven Content Negotiation* où le server envoie une page avec toute les représentations qu'il comporte. L'user/agent reçoit donc un 300 Multiple Choices avec les formats et en choisit un.
 - 
![Pasted image 20240514181058.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240514181058.png)

	- Puis y'a le *Server-driven Content Negotiation* où cette fois-ci l'user envoie avec les headers Accept, Accept-Encoding ou encore Accept-Language (nan y'a pas de définition pour ça sale con). Le serveur va donc choisir le format qui convient le mieux.
	- ![Pasted image 20240514182101.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240514182101.png)

## **TLS** : Transport Layer Security
RFC utilisées : [RFC 5246](https://www.rfc-editor.org/rfc/rfc5246.txt), [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.txt), [RFC 4346](https://www.rfc-editor.org/rfc/rfc4346.txt), [RFC 2818](https://www.rfc-editor.org/rfc/rfc2818.txt), [RFC 8740](https://www.rfc-editor.org/rfc/rfc8740.txt),  [RFC 2246](https://repository.root-me.org/RFC/EN%20-%20rfc2246.txt)
Autre : 
https://repository.root-me.org/Cryptographie/Asym%C3%A9trique/EN%20-%20DROWN:%20Breaking%20TLS%20using%20SSLv2.pdf
https://repository.root-me.org/R%C3%A9seau/EN%20-%20BlackHat%20USA%2009%20Zusman%20AttackExtSSL%20paper.pdf
https://repository.root-me.org/R%C3%A9seau/EN%20-%20BlackHat%20USA%2009%20Marlin%20Spike%20DefeatSSL%20slides.pdf
https://repository.root-me.org/R%C3%A9seau/EN%20-%20BlackHat%20USA%2009%20Zusman%20AttackExtSSL%20slides.pdf
https://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20HTTPS%20Cookie%20Stealing.pdf
https://www.wireshark.org/docs/dfref/t/tls.html
https://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file


**TLS** c'est un protocole utilisé dans HTTPS qui permet de s'assurer du chiffrement de la communication. Sans TLS, tout le trafic HTTP serait en plain text.
Avant TLS, on avait droit à **SSL** mais il est plus du tout utilisé, tout comme TLS 1.0/1.1 et peut-être bientôt 1.2. Pour pas me faire chier, je vais seulement décrire le fonctionnement de TLS 1.3 (et 1.2 si j'ai pas la flemme) ainsi que les vulnérabilité de toute les versions.
#### TLS 1.0

#### TLS 1.1

#### TLS 1.2

![Pasted image 20240519175321.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240519175321.png)

https://www.thesslstore.com/blog/cipher-suites-algorithms-security-settings/
*Étape 1* D'abord on a le TCP 3 way handshake pour initier la connexion.
*Étape 2* Ensuite le client envoie un **ClientHello**. Dans ce message, le client donne plusieurs informations :
- Versions max de TLS qu'il supporte
- Un nombre random
- Une liste de ciphersuite
Un **ciphersuite** c'est un ensemble de protocole cryptographique qui définissent comment les communications sécurisées seront réalisées.
**Contenu d'un ciphersuite** :
- *Key Exchange Algorithm* : c'est pour établir une clé de session qui sera utilisé entre le client et le serveur. Y'a par exemple RSA, Diffie-Hellman (DH), Elliptic Curve Diffie-Hellman (ECDH) ou encore Pre-Shared Key (PSK).
- *Bulk Encryption Algorithm* : c'est pour chiffrer les données qui seront transmisses durant la communication. Y'a par exemple AES, 3DES ou encore RC4 (vulnérable).
- *Authentication Algorithm* : c'est pour s'assurer que les deux communicants de la discussion sont bien ceux qu'ils prétendent être. On a notamment RSA et ECDSA.
- *Hashing Algorithm* : c'est pour s'assurer de l'intégrité des messages et de l'authentication en utilisant HMAC. On a par exemple SHA-1, SHA-256, SHA-384...
Exemple de ciphersuite :
- `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
*Étape 3* Après ça, le serveur va envoyer au client le certificat. Mais avant, le serveur doit le créer :
- **Etapo uno** : Le serveur envoie à un CA (Certificate Authority, c'est une organisation qui valide et créer les certificats (au format X.509 par exemple). Y'en a une douzaine dans le monde) sa clé publique (on est dans le cas d'une encryption asymétrique). 
- **Etapo dos** : Le CA créer un certificat composé d'information sur le CA et sur le serveur ainsi que la clé publique du serveur en plaintext et enfin l'**encrypted server public key** qui est simplement le digest (l'output de la hash function) entre la clé publique du serveur encryptée avec le clé privée du CA. L'output c'est ce qu'on appelle la **Signature**.
- **Etapo tres** : Le serveur renvoie ce certificat au client.
*Étape 4* Ensuite, le client doit s'assurer que le serveur ne lui met pas à l'envers avec son certificat pourri. Il va donc demander au CA (qu'il connait grâce aux informations dans le certificat) sa clé publique. Le client va donc "encrypter" l'encrypted server public key avec la public key du CA (en gros c'est comme s'il le déchiffrer) et va comparer l'output avec la server public key qui se trouve elle aussi dans le certificat. Si c'est la même chose, y'a pas de lézards.
*Étape 5* Maintenant, on entame le **Key Exchange**. Le client va générer une session key et va l'encrypter avec la public key du serveur. Y'aura donc seulement le serveur qui pourra découvrir c'est quoi la session key.
*Étape 6* Enfin, le serveur décrypte cette session key et en informe le client. Maintenant, ils peuvent tous les deux échanger leurs petits secrets en toute intimité.

Un **certificat** peut être contenu dans un fichier *PEM* (Privacy Enhanced Mail). Ce format de fichier est utilisé pour contenir des Certificats X.509, des clés public/private RSA, DSA ou encore des chaînes de certificats.
Pour configurer un serveur Apache avec SSL/TLS, on peut faire :
```
SSLCertificateFile /path/to/your_domain_name.crt
SSLCertificateKeyFile /path/to/your_private.key
SSLCertificateChainFile /path/to/your_chain.pem
```
Dans le cas où on a des paquest intercepté dans wireshark et qu'on a un fichier PEM qui contient une clé private RSA (avec optionnellement des certificats, des publics key...), on peut déchiffrer le trafic avec allant dans Edit->Preference->RSA KEY.
**Composition des paquets**
- On parle d'abord de **Record** pour désigner toute les informations relatives à une **layer**. Une layer c'est par exemple ServerHello, Handshake Protocol: Certificate... Donc quand le serveur envoie son certificat avec son ServerHello et son HelloDone, on a 3 Record.
- 
#### REGARDE RFC 2246 AVEC SOMMAIRE PAR EXEMPLE CBC
#### TLS 1.3

![Pasted image 20240519175321.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240519175321.png)

D'abord on a le TCP 3 way handshake pour initier la connexion.
![Pasted image 20240519184249.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240519184249.png)
Ensuite le client envoie un **ClientHello**. Dans ce message, le client donne plusieurs informations :
- Les versions TLS que le client supporte
- 

## **SSL** : Secure Socket Layer
RFC utilisées : [RFC 6101](https://www.rfc-editor.org/rfc/rfc6101.txt), 
