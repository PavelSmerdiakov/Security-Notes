
Dans un système de chiffrement, le chiffrement peut représenter sous la forme 
$$Y = E(K,X)$$
avec $Y$ le cipher, $E$ le système de chiffrement symétrique, $K$ la clé et $X$ le plaintext.
Le déchiffrement peut présente alors sous la forme 
$$X = D(K,Y)$$
![Pasted image 20240523220432.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240523220432.png)

$\hat{K}$ C'est l'estimation de la clé par le cryptanalyste
$\hat{X}$ C'est l'estimation du plaintext par le cryptanalyste ^6c1ace

# Block Cipher
Dans un chiffrement en Block Cipher, on coupe le plaintext en bloc (64,128,...bits) puis on les traite indépendament (parfois, ils ont des liens entre eux). Y'a souvent besoin de padding pour combler. On utilise la substitution et la transposition.
Exemple d'algorithme de Block Cipher :
- **AES**
- **DES**

Exemple de mode de fonctionnement de Block Cipher :
- **ECB**
- **CBC**
- **CFB**
- **OFB**
- **CTR**

## -Principes fondamentaux
Pour contrer la cryptanalyse de Block Cipher, on utilise 2 principes fondamentaux.
### --Diffusion

#### ---Fonctionnement
Le principe cryptanalystique de la diffusion c'est de voir, quand on change un seul bit du plaintext, la mesure dans laquelle le cipher change. Le but de la diffusion c'est de faire en sorte que quand on change un bit du plaintext, une grande partie du cipher change (idéalement tout le cipher). On veut donc **détruire toutes traces de lien entre le plaintext et le ciphertext afin que le cryptanalyste ne déduise pas la clé.**
Il faut faire en sorte que les fréquences des lettres et des digrammes (paires de lettres) dans le texte chiffré soient aussi proches que possible d'une distribution uniforme.

---
*Exemple de chiffrement utilisant la diffusion :*
$$y_{n} = (\sum_{i=1}^{k}m_{n+i}) \pmod{26}$$
$y_{n}$ c'est la lettre du cipher qui résultera d'un chiffrement d'un bloc. Là faut bien comprendre qu'un bloc de plusieurs lettres dans le plaintext donnera une seule lettre dans le cipher.
$k$ c'est le nombre de lettre du plaintext que va contenir chaque bloc.
$m_{n+i}$ c'est le nombre dans l'alphabet de la lettre de base + i. Avec i qui est incrémenté évidemment.
*Utilisation :*
On cherche à chiffrer "HELLO", on prend des blocs de 3 lettres et on permet le chevauchement de bloc :
$y_{1} = (H + E + L) \pmod{26}$
$y_{2} = (E + L + L) \pmod{26}$
$y_{3} = (L + L + O) \pmod{26}$
- H = 7
- E = 4
- L = 11
- L = 11
- O = 14
$y_{1}=22 \pmod{26} = W$
$y_{2} = 26 \pmod{26} = A$
$y_{3} = 36 \pmod{26} = K$
Donc le cipher donnerai WAK.
En revanche, pendant le déchiffrement, faudra bien prendre en compte que les blocs se sont chevauchés car sinon on aurait $\hat X = HELELLLLO$.
On pourrai retirer le chevauchement mais ça voudrais dire que les dernières lettres auront un padding rempli de 0, ce qui les rendra peut-être vulnérable. A approfondir ? BRANCH NUMBER

---
#### ---Cryptanalyse
Pour analyser la quantité de diffusion d'un cipher, on a quelque méthode.
**Branch Number**
C'est une technique de cryptanalyse (également utiliser durant la conception de système de chiffrement) qui mesure la diffusion d'une fonction. 
$$B = min_{a\neq 0} (W(a)+W(F(a)))$$
$B$ le Branch Number
$a$ un vecteur, différence entre 2 vecteurs d'entrés
$W(a)$ le Hamming Weight
$F(a)$ la fonction de chiffrement par exemple MixColumns dans AES

---
Exemple simplifié :
Une fonction simple sur des vecteurs binaires de 3 bits :
$F(010) = 001$
$F(001) = 010$
$F(011) = 111$

Pour calculer le Branch Number de cette fonction :
I ) On pose $a = 010$, $W(a) = 1$ et $W(F(010))=1$. ∴ 
$$B = W(010) + W(F(010)) = 1+1=2$$
II ) On pose $a = 001$, $W(a) = 1$ et $W(F(001))=1$. ∴ 
$$B = W(001) + W(F(001)) = 1+1=2$$
III ) On pose $a = 011$, $W(a) = 2$ et $W(F(011))=3$. ∴ 
$$B = W(011) + W(F(011)) = 2+3=5$$
Avec la plus petite valeur = 2 donc le Branch Number = 2.

---



### --Confusion
#### ---Fonctionnement
Pour ce qui est de la confusion d'un système de chiffrement, on veut **détruire toutes les traces de lien entre le ciphertext et la clé afin que le cryptanalyste ne déduise pas la clé** pour ensuite trouver le plaintext.

## -Système de chiffrement
### --Substitution Permutation Network (SPN)
Ce type de Block Cipher est basé sur les substitution, sur les permutations ainsi que sur les XOR operations. AES c'est un SPN. Les SPN offre de bonnes diffusion et confusion (terme inventé par Claude Shannon). 
#### ---S-Boxes
Une **S-Box** est la partie qui s'occupe de la substitution du chiffrement. Il prend en input un block de n bits et en sort un block de m bits. On va appeler cette box : n x m S-box
Une S-Box doit remplir des conditions pour qu'elle soit efficace :
- Chaque bit de l'output doit dépendre de tout les input bits
- En moyenne, le changement d'un input bit doit changer la moitié des output bits. Il rempli donc le SPAC.
- Il doit être non-linéaire, c'est-à-dire qu'on ne peut pas poser d'équation linéaire ou affine dessus, sinon elle pourrait être analysé facilement.
- Même si on connait une partie de l'input bits, on ne peut pas retrouver l'output bits.
![Pasted image 20240528164011.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240528164011.png)



#### ---P-Boxes
Par conséquent, une **P-Box** est la partie qui s'occupe de la permutation. Elle prend en input un block de n bits et sort un block de m bits. Les bits sont mélangés de sorte à ce que la relation entre le plaintext et le ciphertext soit compliqué à comprendre.

![Pasted image 20240528165608.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240528165608.png)
On a plusieurs type de P-Box, notamment les **compressions** qui sort en output un nombre de bits inférieur à l'input. L'**expansion** qui sort une output plus grande que l'input. Et enfin les **straight** qui sortent une output de même taille que l'input. Seulement les P-Boxes straight sont inversible, ce qui veut dire qu'on peut faire le chemin inverse pour trouver le plaintext à partir d'un ciphertext.
#### ---Rounds
Les rounds sont les concaténations de P-Boxes, S-Boxes et XOR. 
![Pasted image 20240528170624.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240528170624.png)
Les SPN utilisent pour chaque round **une clé différente**. Ces round keys proviennent d'une secret main key. Le dernier round du schéma n'est pas nécessaire puisqu'il est cryptographiquement inutile. 
Pour le déchiffrer, inverse l'ordre des rounds ainsi que les round keys.
#### ---Feistel Algorithm
C'est une forme de SPN.
![Pasted image 20240529212020.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240529212020.png)
Le fonctionnement n'est pas hyper compliqué.
**Chiffrement**
On va couper le plaintext en deux partie. La partie de droite va être introduite avec la round key dans une fonction qui varie selon l'algorithme. Ensuite, l'output va être XORé avec la partie gauche du plaintext. Cette portion est alors mise à droite. À gauche, on met l'ancienne partie à droite. On fait ça pour chaque ronde. 
A la fin, on inverse la gauche et la droite afin de faciliter le déchiffrement.
**Déchiffrement**
C'est simplement le processus inverse. La seule chose qui change, c'est qu'on inverse l'ordre des round keys.
$$(L,R) \rightarrow (R,L\ \oplus\ F(R,k))$$

#### ---Data Encryption Standard (DES)
DES c'est un algorithme de chiffrement SPN block cipher. À la base, on a IBM qui créé Lucifer en 1974. Puis la NSA reprend le principe pour créé DES en 1976.
C'est un système qui utilise des blocks de 64 bits, dont 8 sont utilisés pour vérifier la parité du block. En effet, 8 bits (1 par bytes) du block sont utilisés de manière à ce que chaque bytes soit impairs. On obtient un block avec des "bits utiles" de 56bits.
**Fonctionnement**
![Pasted image 20240530214849.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240530214849.png)
- On fractionne le plaintext en blocks de 64 bits.
- On fait une permutation initiale![Pasted image 20240530215216.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240530215216.png) puis on le scinde en 2 partie. C'est simple : tout les nombres pairs de 2 à 64 vont dans la partie en haut (partie gauche $L_{0}$) et tout les nombres impairs de 1 à 63 vont dans la partie en bas (partie droite $R_{0}$).
- Maintenant, on entre dans les rounds, dans lesquelles chaque bloc est soumis à un ensemble de transformations.
	- $R_{0}$ est étendu à 48bits grâce à une fonction d'expansion. ![Pasted image 20240530215725.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240530215725.png) Dans cette matrice, les deux premiers bits de chaque ligne sont identiques aux derniers de chaque ligne supérieures. Cette matrice est donnée par $E[D_{0}] = D'_{0}$ 
	- Après ça, on XOR $D'_{0}$ avec la round key ce qui donne $D_0$ (pas le même qu'avant, c'est juste pour la compréhension).
	- Le résultat est scindé en 8 blocs de 6 bits notés $D_{0i}$.
	- Ces blocs sont passés dans des fonctions de sélection : On utilise une matrice de 4 lignes et 16 colones.![Pasted image 20240531161816.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240531161816.png)Le 1er et le dernier bit du bloc sont concaténés et donne la ligne. Les 4 bits restant donne la colonne. Le chiffre résultant est l'output de la fonction. Avec des blocs de 6 bits, on obtient donc des blocs de 4 bits.
	- On regroupe les 8 blocs de 4 bits pour avoir 1 bloc de 32 bits.
	- On refait une permutation avec la matrice suivante ![Pasted image 20240531162050.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240531162050.png)
	- À présent, on refait un XOR avec $L_1$ et $R_0$ pour donner $R_1$ puis on recommence le processus 16 fois.
- À la fin, on regroupe les 2 blocs de 32 bits et on refait la permutation initiale.

**Génération des round keys**
À chaque round de l'algorithme DES, on utilise une round key différente.
La clé de 64bits va servir à les générer. 
- D'abord, on dégage les 8 bits de parité pour avoir 56 bits utiles.
- Ensuite, on les fout dans CP-1 qui a pour matrice ![Pasted image 20240531161131.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240531161131.png) Si tu regarde bien, y'a un pattern en diagonale mais je n'ai pas encore compris.
- On coupe l'output en 2 partie. $L_i$ (en haut) et $R_i$ (en bas) puis on décale tout les bits de 1 cran à gauche.
- On regroupe les 2 parties puis on le fout dans CP-2 qui, lui, va ressortir une matrice de 48 bits qui representera la round key.![Pasted image 20240531161415.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240531161415.png)




# Stream Cipher
Dans un chiffrement en Stream Cipher, on chiffre les bits en même temps, de façon continue. A la place d'avoir plusieurs blocs en output, on en obtient qu'un seul. Y'a pas besoin de padding puisqu'en général, on prend une clé de la longueur du plaintext. 

Exemple de mode de fonctionnement de Stream Cipher :
- **RC4**
- **CHACHA20**
