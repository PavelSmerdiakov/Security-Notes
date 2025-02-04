De notation IND-CPA.  
IND = Indistanguable

CPA = Chosen plain-text attackers c'est quand l'off peut choisir d'encrypter n'importe quelle plaintext.

Dans l'IND-CPA, chaque cipher doit être différent même sur le même plaintext.  
One time pad : Utilisation d'une seule clé qui eat donc secrete. A COMPLETER  
Exemple de construction de base de IND-CPA (one time pad) :  
C = E(K, R, P)  
C = cipher  
E= Juste pour dire qu'on encrypte  
K = Cle de chiffrement  
R = nombre random  
P = plaintext

Construction 1 :  
E(K,R,P) = (DRBG(K,R) xor P,R)

La partie de droite c'est juste pour dire que c'est une encryption sémantique. A gauche, on utilise DRBG. C'est un générateur de bit aléatoire qui utilise une entropie. En gros, pour générer ses seeds, il utilise par exemple des mouvement de souris, de clavier...

On met K et R en parametre pour etre sur que le rendue est random. K c'est la cle de chiffrement et R c'est un nombre random. Donc c'est ca qui permet d'avoir un cipher different pour chaque encryption mm si c'est le même.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/f847acdda15b7ade1417b8cb6d64ac5b.png)![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/359fecd3cf3fb019bbbc6ddd06d43be6.png)![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/398737fb4e043bc629db90edb970b7ed.png)![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/48842dbbcec6f013134b1c18017a6a6d.png)