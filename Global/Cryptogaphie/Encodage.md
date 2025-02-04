## Base64

[RFC 1521](https://www.rfc-editor.org/rfc/rfc1521.txt)

Base64 convertit du binaire en ASCII.
Table ASCII :
![Pasted image 20250110111834.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020250110111834.png)


64 c'est pour le nombre de caractères ASCII qu'on peut utiliser (26,26 pour maj,min/10 pour chiffres/2 pour caractère spécial)
Table base64 :
![[Pasted image 20250110094142.png]]
Fonctionnement :
Le principe est simple :
- Si le nombre de caractère n'est pas un multiple de 3, il ajoute des "=" à la fin
- On encode en ASCII
- On converti le ASCII en binaire de 8 bits
- On divise les chunks en 8 bits en chunks de 6 bits
- On converti le binaire en décimale puis en caractère de la table base64

C'est un algorithme d'encodage faisant partie de MIME.
Pour reconnaître du base64, on peut notamment penser au fait qu'une chaine encodé doit avoir un nombre de caractère multiple de 4.


## BinHex

Plutôt désué à cette heure. C'était utilisé pour les macintosh.
On peut le reconnaitre avec les ":" qu'il contient au début de l'encodage et à la fin.


## MD5
[RFC 1321](https://www.ietf.org/rfc/rfc1321.txt)
C'est une fonction de hashage créée par Ronald Rivest le GOAT. Elle prend en input des multiples de 512 bits pour retourner un 128 bits. MD5 ne travaille qu'avec du 32bits (8hex).

MD5 utilise 6 opérations :
bitwise OR : I
bitwise AND : &
bitwise XOR : ^
bitwise NOT : inverse tout
bit rotation : décale tout les bits de n rang vers la gauche
bitwise ADD : une addition connard t'es débile ? Bon par contre quand y'a un overflow dans l'addition (quand les 32bits ne peuvent plus le contenir), MD5 permet de simplement dégager le 1 de gauche en trop.

Fonctionnement :
https://www.youtube.com/watch?v=5MiMK45gkTY
La vidéo va bien mieux expliquer le fonctionnement que moi.

#### Collisions attacks :

![[EN - Collisions of MD5.pdf]]
