

## Qu'est ce que c'est ?

- C'est un outil très puissant pour le reversing de fichier non open-source. Il permet de désassembler plusieurs type de fichier tel que les fichiers .bin, .elf, .dll, .so ou encore les fichiers de micrologiciels, fichiers de firmware utiles pour le IoT ou d'autre type comme pour les jeux vidéos.
- Il permet aussi de décompiler le fichier vers une représentation high-level plus ou moins fidèle.

## Choses à penser dans Ghidra

###### XREF

- XREF fait référence aux endroits où l'élément est utilisé. Tu verras souvent la notation `XREF[2] : 00101154(W)` après la déclaration d'un élément ou un truc du genre. Le `[2]` signifie qu'il y a 2 référence à l'élément dans le set d'instruction. `00101154` c'est une adresse d'instruction où l'élément est utilisé, c'est pour donner un exemple en fait. Le `(W)` c'est pour dire qu'il peut être réécrit.

##### Notation des éléments

Par soucis de simplicité et de lecture, Ghidra utilise des conventions de nommage.

**Fonction***

- Elles ont parfois un préfixe `FUN_` suivi d'un nombre unique dans le cas où il ne retrouve pas le nom.

**Variables locales**

- Elles ont souvent des noms du genre `local_10` ou parfois avec une lettre pour spécifier le type de données

**Variables globales**

- Elles ont parfois un préfixe tel que `DAT_` ou `g_`

**Constantes**

- Elles ont parfois des préfixes comme `const_`, `k_`, `c_` 

**Tableaux**

- Ils ont parfois des préfixes `array_`

**Structures de données**

- Des fois elles ont des préfixes `struct_`

**Pointeurs**

- Ils ont parfois des préfixes tel que `ptr_` ou `p_`


