### Sommaire (chat GPT)
```
Chiffrement
├── Techniques de Base
│   ├── Substitution
│   └── Transposition
│
├── Types de Chiffrement
│   ├── Symmetric Key
│   │   ├── Block Cipher
│   │   │   ├── Utilise Substitution et Transposition
│   │   │   └── Modes de Fonctionnement
│   │   │       ├── ECB
│   │   │       ├── CBC
│   │   │       ├── CFB
│   │   │       ├── OFB
│   │   │       └── CTR
│   │   └── Stream Cipher
│   └── Asymmetric Key
│       └── Diffie-Hellman Algorithm
│       └── RSA, ECC, etc.
│
├── Hachage Cryptographique
│   ├── MD5
│   ├── SHA-1
│   ├── SHA-256
│   └── SHA-3
│
├── Cryptographie Homomorphe
│   ├── Paillier
│   └── Fully Homomorphic Encryption (FHE)
│
├── Cryptographie Quantique
│   └── QKD (Quantum Key Distribution)
│       └── BB84
│
├── Cryptographie Basée sur l'Identité
│   └── IBE (Identity-Based Encryption)
│       └── Boneh-Franklin IBE Scheme
│
├── Chiffrement à Diffusion Secrète
│   └── Schéma de Shamir
│
├── Signatures Numériques
│   ├── DSA (Digital Signature Algorithm)
│   └── ECDSA (Elliptic Curve Digital Signature Algorithm)
│
└── Cryptographie Post-Quantique
    ├── Lattice-Based Cryptography
    └── Code-Based Cryptography
```
![Pasted image 20240520172616.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240520172616.png)

### Définition
On a 2 type de systèmes de chiffrement (y'en a d'autre aussi, check la fin.)
déchiffrement = quand on a la clé
décryption = quand on a pas la clé
chiffrer = encoder un message avec une clé
crypter = encoder un message sans connaître la clé (impossible donc terme débile)

###### Indice de coïncidence
L'indice de coïncidence c'est la probabilité que 2 lettres choisies aléatoirement dans un texte/cipher soient identiques. C'est made by Friedman.
$n$ = nombre de lettres dans le texte
$n_{1}$ = nombre de A dans le texte
$n_{26}$ = nombre de Z dans le texte ^09e1f0

$$P(2\ fois\ A) = \frac{C^{n_{i}}_{2}}{C^{n}_{2}} = \frac{\frac{n_{1}(n_{1}-1)}{2}}{\frac{n(n-1)}{2}} = \frac{n_{1}(n_{1}-1)}{n(n-1)}$$
Donc pour calculer la probabilité d'avoir 2 lettres identiques, on fait la somme de chaque proba :
$$IC = \sum_{i=1}^{26} \frac{n_{i}(n_{i}-1)}{n(n-1)}$$
En France, il vaut 0,074
Programme pour le calculer : 
```
def indice_coincidence(text):
    text = text.replace(" ", "").upper()

    n = len(text)
    frequence = {}
    for lettre in text:
        if lettre in frequence:
            frequence[lettre] += 1
        else :
            frequence[lettre] = 1
    ic = 0
    for fi in frequence.values():
        ic += fi * (fi - 1)

    if n > 1:
        ic /= n * (n - 1)
    else:
        ic = 0

    return ic

texte = ""
ic = indice_coincidence(texte)
print(f"Le voilà ton putain d'indice de clochard espèce de bouffon va\n{ic : .6f}")
```

###### Strict Avalanche Criterion (SAC)
Le critère d'avalanche est une méthode pour mesurer la robustesse d'un [[Symmetric Encryption#^6c1ace|symmetric cipher system]] ou d'une fonction de hashage.
Dans le SAC, on a aussi le **SPAC** (Strict Plaintext Avalanche Criterion) qui définit le plaintext avalanche effect. Quand tu fais un changement d'un bit dans le plaintext, ça doit faire un grand changement dans le cipher. Pour qu'un block cipher satisfasse le SPAC, il doit, pour chaque changement de bits dans le plaintext, avoir la moitié des bits du cipher qui change (chaque bits du cipher a 50% de chance de changer).
On parle aussi de **SKAC** (Strick Key Avalanche Criterion) pour désigner tout les changements effectué sur le cipher quand on change un bit sur la clé. ^30c5cb

###### Hamming Weight

^78265f

Le Hamming Weight c'est un nombre qui permet de quantifier le total de bits différents de 0 dans un nombre.
*Exemple :*
11011001 -> Hamming Weight = 5
850460807 -> Hamming Weight = 6

###### Parité

^6a1a28

La parité sert à vérifier l'intégrité du plaintext. Ça consiste à utiliser un bit d'un bloc dans le but de s'assurer que les données n'ont pas été changées. Le bit qu'on change c'est le MSB pour assurer une meilleurs implémentation. 
On a 2 types :
**Even Parity** : Le bit utilisé s'assure que le bytes rende un nombre pairs.
**Odd Parity** : Le bit utilisé s'assure que le bytes rende un nombre impairs.






 Kerckhoffs's principle










https://en.wikipedia.org/wiki/Category:Cryptographic_attacks
CHAT GPT:
### Méthodes de Cryptanalyse de Base

1. **Analyse de Fréquence** : Compter les fréquences des lettres ou des blocs dans le texte chiffré pour trouver des motifs récurrents.
2. **Brute Force** : Essayer toutes les clés possibles jusqu'à trouver la bonne. Cela devient impraticable pour des clés suffisamment longues.
3. **Known Plaintext Attack (KPA)** : Disposer d'échantillons de texte clair et de texte chiffré correspondants pour déduire la clé.
4. **Chosen Plaintext Attack (CPA)** : Choisir des textes clairs et obtenir les textes chiffrés correspondants, permettant ainsi d'analyser le chiffrement.
5. **Chosen Ciphertext Attack (CCA)** : Choisir des textes chiffrés et obtenir les textes clairs correspondants, souvent utilisé pour analyser les décryptages.

### Méthodes de Cryptanalyse Classiques

6. **Differential Cryptanalysis** : Analyser les différences entre paires de textes clairs et leurs textes chiffrés correspondants pour trouver des patterns et déduire la clé.
7. **Linear Cryptanalysis** : Utiliser des approximations linéaires des transformations non linéaires du chiffrement pour trouver des corrélations exploitables. page 364 encyclopedia
8. **Integral Cryptanalysis** : Étudier la propagation des bits fixes, variables et constants à travers plusieurs tours de chiffrement.
9. **Biclique Attack** : Technique améliorée de brute force qui réduit la complexité temporelle en utilisant des bicliques pour diviser le problème en sous-problèmes plus petits.

### Méthodes de Cryptanalyse Avancées

10. **Slide Attack** : Exploiter la symétrie dans les clés de chiffrement pour trouver des faiblesses en analysant des paires de texte clair et de texte chiffré.
11. **XSL Attack** : Attaque algébrique qui transforme le chiffrement en un système d'équations polynomiales et les résout.
12. **Boomerang Attack** : Combinaison de deux differential cryptanalyses pour attaquer des schémas de chiffrement avec une complexité plus faible.
13. **Meet-in-the-Middle Attack** : Utiliser deux étapes de chiffrement ou de déchiffrement pour réduire le nombre de clés à tester.

### Méthodes de Cryptanalyse Très Avancées

14. **Algebraic Attacks** : Utiliser des équations algébriques pour décrire les transformations du chiffrement et les résoudre pour trouver la clé.
15. **Interpolation Attack** : Utiliser des polynômes d'interpolation pour décrire la relation entre les textes clairs et chiffrés.
16. **Side-Channel Attacks** : Exploiter des informations physiques (temps d'exécution, consommation d'énergie, rayonnement électromagnétique) pour déduire des informations sur la clé.
    - **Timing Attack**
    - **Power Analysis Attack**
    - **Electromagnetic Analysis Attack**
17. **Differential Power Analysis (DPA)** : Analyser les variations de consommation de puissance pour extraire des informations sur la clé.
18. **Template Attack** : Utiliser un modèle préétabli de la consommation de puissance pour prédire les opérations internes et déduire la clé.
19. **Fault Injection Attack** : Induire des fautes dans le chiffrement (par exemple en perturbant l'alimentation) et analyser les résultats pour trouver la clé.
20. **Quantum Cryptanalysis** : Utiliser des algorithmes quantiques (comme l'algorithme de Grover) pour attaquer des chiffrements classiques plus efficacement que les méthodes traditionnelles.

### Méthodes de Cryptanalyse Spécialisées

21. **Impossible Differential Cryptanalysis** : Utiliser des différentiels qui ne peuvent pas se produire dans le chiffrement pour éliminer des clés candidates.
22. **Higher-Order Differential Cryptanalysis** : Étendre la differential cryptanalysis en utilisant des dérivées de plus haut ordre des différences de texte clair.
23. **Integral Attack (Square Attack)** : Analyser des ensembles complets de textes clairs avec certaines propriétés invariantes sous la transformation de chiffrement.
24. **Multiset Attack** : Extension de l'attaque intégrale utilisant des multiensembles de valeurs pour trouver des faiblesses dans le chiffrement.




### 3. **Autres Types de Chiffrement** (hors symétric asymétric)

En plus des méthodes symétriques et asymétriques, il existe d'autres types et techniques de chiffrement :

- **Chiffrement par Flot** :
    
    - Utilise un flot de clés pour chiffrer des données de manière bit par bit ou byte par byte. Par exemple, le RC4, mentionné précédemment, est un algorithme de chiffrement par flot.
- **Chiffrement de Bloc** :
    
    - Les données sont divisées en blocs de taille fixe et chaque bloc est chiffré séparément. AES et DES sont des exemples de chiffrements de bloc.
- **Chiffrement Homomorphique** :
    
    - Permet de réaliser des opérations sur des données chiffrées sans les déchiffrer. Cela est particulièrement utile pour le traitement de données sécurisées dans le cloud.
- **Chiffrement Post-Quantique** :
    
    - Algorithmes en développement pour résister aux attaques potentielles des futurs ordinateurs quantiques. Exemples incluent le **Lattice-based Cryptography** et **Hash-based Cryptography**.
- **Chiffrement de Code Correcteur d'Erreurs** :
    
    - Utilisé dans certaines communications pour permettre la détection et la correction des erreurs dans les données transmises.




La cryptographie quantique et la cryptographie post-quantique sont deux domaines distincts qui traitent des défis posés par les technologies quantiques, mais elles le font de manières différentes.

### Cryptographie Quantique

La cryptographie quantique utilise les principes de la mécanique quantique pour développer des systèmes de communication sécurisés. Voici quelques caractéristiques et exemples :

- **Principes Fondamentaux** : Exploite les propriétés de la physique quantique, telles que la superposition et l'intrication, pour sécuriser les communications.
- **Exemple Principal** : **Quantum Key Distribution (QKD)**
    - **BB84** : Le premier et le plus connu des protocoles QKD, développé par Charles Bennett et Gilles Brassard en 1984. Il permet deux parties de partager une clé secrète en utilisant des bits quantiques (qubits) de manière à ce que toute tentative d'écoute soit détectée.
    - **Principe** : Si un espion tente de mesurer les qubits en transit, il introduit des perturbations détectables, assurant ainsi la sécurité du canal de communication.

La cryptographie quantique vise à fournir une sécurité inconditionnelle basée sur les lois de la physique quantique, plutôt que sur la difficulté computationnelle de certains problèmes mathématiques.

### Cryptographie Post-Quantique

La cryptographie post-quantique, en revanche, se concentre sur la création d'algorithmes cryptographiques résistants aux attaques par des ordinateurs quantiques. Ces algorithmes sont conçus pour fonctionner sur des ordinateurs classiques, mais sont sécurisés contre les capacités de calcul des futurs ordinateurs quantiques. Voici quelques caractéristiques et exemples :

- **Objectif** : Assurer que les algorithmes cryptographiques actuels restent sécurisés face aux ordinateurs quantiques, qui peuvent potentiellement casser les algorithmes utilisés aujourd'hui (comme RSA, DSA, et ECC) en utilisant des algorithmes quantiques (comme l'algorithme de Shor).
- **Types de Cryptographie Post-Quantique** :
    - **Cryptographie Basée sur les Réseaux (Lattice-Based Cryptography)** : Utilise des problèmes mathématiques liés aux réseaux euclidiens, tels que le problème de la courte base (Shortest Vector Problem, SVP).
        - **Exemple** : Algorithmes de chiffrage comme NTRU.
    - **Cryptographie Basée sur les Codes (Code-Based Cryptography)** : Basée sur la difficulté de décoder certains types de codes correcteurs d'erreurs.
        - **Exemple** : Schéma de McEliece.
    - **Cryptographie Multivariée (Multivariate Polynomial Cryptography)** : Utilise des systèmes d'équations polynomiales multivariées.
        - **Exemple** : HFE (Hidden Field Equations).
    - **Cryptographie Basée sur les Fonctions de Hachage (Hash-Based Cryptography)** : Utilise des fonctions de hachage pour créer des signatures numériques.
        - **Exemple** : Schéma de signature XMSS (eXtended Merkle Signature Scheme).

### Résumé des Différences

1. **Approche** :
    
    - **Cryptographie Quantique** : Utilise des phénomènes de la mécanique quantique pour sécuriser les communications (ex. QKD).
    - **Cryptographie Post-Quantique** : Développe des algorithmes sécurisés contre les attaques par des ordinateurs quantiques, mais qui fonctionnent sur des ordinateurs classiques.
2. **Technologie** :
    
    - **Cryptographie Quantique** : Requiert des technologies quantiques comme les qubits et les réseaux de communication quantiques.
    - **Cryptographie Post-Quantique** : Utilise des mathématiques avancées pour créer des algorithmes résistants aux capacités de calcul des futurs ordinateurs quantiques.
3. **Sécurité** :
    
    - **Cryptographie Quantique** : Offre une sécurité basée sur les principes physiques de la mécanique quantique, assurant que toute tentative d'espionnage sera détectée.
    - **Cryptographie Post-Quantique** : Offre une sécurité basée sur des problèmes mathématiques difficiles à résoudre, même pour des ordinateurs quantiques.

En conclusion, la cryptographie quantique et post-quantique répondent à des besoins différents mais complémentaires dans le domaine de la sécurité de l'information à l'ère des technologies quantiques.

