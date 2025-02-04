


# Types de Cryptanalyse

## -Differential Cryptanalysis
C'est une méthode de cryptanalyse qui requiert de tester des plaintext à insérer dans l'algorithme de chiffrement mais pas de n'importe quelle manière.
La technique repose sur les probabilités.
On va utiliser plusieurs paires de plaintext à insérer dans une S-Box.
Ces paires ne sont pas choisies au hasard : on va faire en sorte que chaque plaintext XORé avec son couple donne le même $X$.
À présent, on chiffre les $X$ dans la S-Box puis on XOR à nouveau les deux résultats de façon à avoir $f(P_1)\oplus f(P_2) = Y$
De cette façon, on pourra observer si toute les combinaisons possibles pour donner le premier XOR $X$ donneront ou non $Y$ lors du deuxième XOR avec les outputs de fonction.

Pour l'illustration, imaginons qu'on ait 3 paires de plaintext qui, quand ces paires sont XORé, donne le même $X$. Si, après avoir XORé les paires d'output de fonction, on obtient 2 fois le même $Y$ mais que le troisième donne une autre valeur, on a donc $\frac{2}{3}$ chances d'avoir $Y$. 
Tu verras peut-être $\delta _{in}$ et $\delta _{out}$ mais c'est simplement des petites différences qu'on ajoute respectivement à l'input et qui se produisent donc à l'output.

Dans une opération linéaire, on a
$$\delta _{out} = L(x+\delta_{in}) \oplus L(x) = L(\delta_{in})$$
Avec $x$ une entrée quelconque, $\delta_{in}$ une petite différence qui va être apportée à la fonction.
On obtient donc logiquement
$$\delta_{in} \overset{L}\longrightarrow \delta_{out}$$ Avec une probabilité certaine de 1. Tout ça est dû au fait que $L$ est une fonction linéaire.
**Rappel** le XOR et le AND peuvent s'écrire dans un ensemble $\Bbb F_2$ (corps fini à 2 éléments possibles {0, 1}) :
- Le XOR va s'écrire sous une addition modulo 2 :
	- 0+0=0, 0+1=1, 1+0=1, 1+1=0
- Le AND va s'écrire sous une multiplication modulo 2 :
	- 0⋅0=0, 0⋅1=0, 1⋅0=0, 1⋅1=1
En outre, un nombre binaire peut s'écrire dans l'ensemble $\Bbb F^m_2$ où $m$ est un vecteur qui représente la taille en bits.


$$DDT[\delta_{in}][\delta_{out}] = \\#\{x \in \Bbb F^m_2 : S(x)+S(X+\delta_{in})=\delta_{out} \}$$



# Cryptanalyse sur Algorithmes

## -DES
differential cryptanalysis, linear cryp..., davies attack








# Projet d'analyse de hash

Nombre de bits du hash
