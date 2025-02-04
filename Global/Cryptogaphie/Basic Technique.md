Ces techniques sont, pour la plupart, utilisées seulement pour le flex de savoir que ça existe. En réalité c'est plus des systèmes d'actualité mais c'est simplement pour te donner une petite histoire de la cryptologie/cryptanalyse.

### -Substitution
Dans un chiffrement par substitution, chaque élément (lettre, chiffre...) du plaintext est remplacé par un autre.
##### -- Substitution monoalphabétique
Deux lettres distinctes doivent être chiffrées en 2 signes distincts. Dans le cas contraire, y'aurait ambiguïté.
Exemple d'algorithme' :
- **Carré de Polybe**
- **Chiffre de Delastelle**
- **Chiffre des Templiers**
- **Chiffre de PigPen**
- **Code de César**

##### -- Substitution polyalphabétique
Une lettre est changée en fonction d'une clé et non pas de manière fixe. Cette clé indique le nombre de décalage en fonction d'un position.
Exemple d'algorithme :
- **Chiffre de Vigenère**
- **Chiffre de Hill**
- **Enigma**
Exemple :
On chiffre le mot `AAAAAAA` avec la clé `123`, on obtient `BCDBCDB` avec 1,2 et 3 des numéros de décalage en fonction de la position. On peut aussi faire une clé avec des lettres par exemple `cle`. On regarde leur position dans l'alphabet et on chiffre.
### -Transposition
Dans un chiffrement par transposition, on inverse l'ordre des lettres du plaintext. On peut par exemple couper le plaintext en bloc de lettres identiques (avec padding si besoin) pour échanger les places. Le nombre de permutations possibles c'est la factorielle de len(plaintext).
Exemple :
Là on prend par colonne puis on inverse x et y.
![[Pasted image 20240526180835.png]]
L'[[Définitions#^09e1f0|indice de coïncidence]] n'est pas modifier durant un chiffrement par transposition donc ou pourrai, grâce à une analyse de fréquence, déterminer que c'est un chiffrement par transposition.