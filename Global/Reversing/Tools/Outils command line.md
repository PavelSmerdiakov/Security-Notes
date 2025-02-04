#  GDB

Lancer le débuggueur gdb sur un programme (pense à compiler le script avec l'option -g pour le déboguage) :
- `gdb myscript`


##### Affichage

Exécuter des commandes d'un shell (un clear par exemple):
- `shell clear`

Voir l'assembleur d'une fonction (main dans mon cas) :
- `disass main`

Voir l'assembleur quand y'a pas de main :
- `info file` puis regarder l'adresse de l'entry point. Tu met un breakpoint dessus. Tu peux pas faire disassemble parce que gdb ne sait pas où s'arrêter mais tu peux regarder les valeurs de `rip` avec la commande x `x/15i $rip`. Ça c'est pas encore main mais après tu cherche dans les instructions des appels à des fonctions du genre `__libc_start_main@plt`

Mettre l'affichage de l'assembleur en intel :
- `set disassembly-flavor intel`

Afficher le code source autour de la déclaration d'une fonction ou d'une ligne :
- `list main`
- `list 10`


##### Text-user Interface mode (TUI)

Activer/désactiver le mode TUI :
- `tui enable`
- `tui disable`

Afficher la fenêtre avec le code source du programme :
- `layout src`

Afficher la fenêtre avec le code assembleur :
- `layout asm`

Afficher la fenêtre avec les registres :
- `layout regs`

Afficher deux fenêtres et les changer :
- `layout split`
- `layout next`
- `layout prev`



##### Execution

Dans gdb, pour lancer le script :
- `run`
- `r`

Lancer le script avec des arguments :
- `run para1 para2`

Arrêter le programme en cours :
- `kill`
- `k`

Mettre un breakpoint :
- Tu peux remplacer le break par `b`
- `break main`
- `break *0x0000555555555148` le * indique qu'on parle d'une adresse.
- `break ./myscript.c:linenumber`
- `break 4` où 4 est le numéro de ligne dans le fichier C.

Voir tes breakpoints :
- `info breakpoints`
- `info b`
- `i b`

Supprimer des breakpoints :
- `delete breakpoint 1`
- `delete`

Désactiver un breakpoint :
- `disable 2`

Lancer en s'arrêtant automatiquement à la fonction main() :
- `start`

Continuer l'exécution après un breakpoint jusqu'à la fin ou au prochain breakpoint :
- `continue`
- `c`

Avancer à la prochaine ligne du code source en passant l'exécution des fonctions (si la prochaine instruction c'est l'appel d'une fonction, elle est exécutée dans son intégralité) :
- `next`
- `n`

Avancer à la prochaine ligne du code source en entrant dans la fonction appelée :
- `step`
- `s`

Avancer pas à pas dans les instructions en assembleur :
- `stepi`
- `si`

Afficher la backtrace :
- `backtrace`
- `bt`
- #0 est la dernière fonction appelée. Quand on appelle une fonction, on l'ajoute en haut de la pile. Quand elle se termine, on la retire et on revient à la fonction parent #1 et ainsi de suite. 

- Afficher le PID : ^7f5428
	- `info proc`
	- `info inferior`

Continuer jusqu'à ce que la fonction actuelle se termine :
- `finish`


##### Watchpoint

Mettre un watchpoint (surveiller les changements de valeur d'une variable ou d'une adresse mémoire) :
- `watch var1` Sachant qu'il faut que le programme soit en cours d'exécution.
- `watch *0x7fffffffda8c`


##### Variable

Afficher la valeur d'une variable / adresse mémoire :
- `print var`
- `p var`
- `p 0x7fffffffda8c`

Afficher l'adresse mémoire d'une variable :
- `p &var`

Afficher le type de la variable / adresse mémoire :
- `ptype var`
- `ptype *0x7fffffffda8c`

Afficher toute les variables disponibles localement que tu as défini :
- `info locals`
- `i locals`

Afficher toute les variables disponibles localement, y compris celles que tu n'as pas défini :
- `i variables`

Afficher la taille d'une variable :
- `p sizeof(var)`

Afficher les infos des arguments de la fonction :
- `i args` 

Trouver la taille d'un buffer qui est dans le tas/heap :
- `x/gx buf-8` où buf est le nom de la variable


##### Commande x 

La commande x c'est pour examiner une adresse mémoire. C'est assez important dans le déboguage.
Syntaxe général :
- `x/nfu addr` où n est le nombre d'éléments à afficher.
- f est le format de l'affichage :
	- x pour hexadécimal
	- d pour décimal
	- o pour octal
	- t pour binaire
	- u pour unsigned decimal
	- f pour floating point
	- a pour adresse
	- c pour caractère
	- s pour string
	- i pour instruction
- u est l'unité d'affichage 
	- b pour octet
	- w pour word
	- g pour long
- addr est l'adresse à inspecter.


##### Registres 

Afficher les valeurs des registres ;
- `info registers`
- `i r`
- `i r rip`
- `p $rip`

Modifier la valeur d'un registre :
- `set $rax = value`

Afficher la valeur du registre à chaque fois qu'elle change :
- `display $rip`
- `delete display $rip` pour le désactiver


---
# objdump

^fcb9c4

C'est pour générer le code assembleur à partir d'un code binaire

Utilisation de base pour voir les vingt lignes de main en format intel:
- `objdump -M intel -D myscript | grep -A20 main`





# LDD

C'est un outil qui permet de lister les bibliothèque partagées qui sont utilisées par le programme. Il permet aussi de voir les adresses des lib.

Pour voir les dynamic lib et leur adresses (à faire sur le fichier binaire comme par exemple /usr/bin/ls):
- `ldd proutfile`



# ROPgadget


Utilisé pour faire des attaques ROP.
# NASM



# ld
# Strace

^935de7
Permet de voir les appels systèmes d'un programme tel que les ouvertures de fichier, les écritures, les appels réseaux...
# Ltrace

C'est un outil pour voir les appels aux librairies d'un programme. Ça permet aussi de voir les paramètres données ou les fonctions en plein exécution.

Exemple d'utilisation :
- Y'a un moment où je ne voyais pas le paramètre qui était passé à une fonction dans Ghidra :![[Pasted image 20240309163532.png]]
- Là y'a `__s2` qui prend la valeur de retour de la fonction FUNblabla avec les paramètres `local_1a8` `0x20` et 3. En gros on comprend que c'est une fonction qui passe une string, qui l'encrypt (c'est probable rien qu'en voyant ce bout de code) puis le ressort dans `iVar1`.
- Ensuite `__s2` est comparé avec notre input et s'ils sont identiques, alors le if proc.
- Donc pour voir ce que contient `__s2`, on va regarder les paramètres avec ltrace (car on n'arrive pas à trouver le contenu de `__s2` dans ghidra). 
- On a simplement à faire `ltrace ./crackme`, on regarde qu'est ce qui est comparé avec la fonction `strcmp` et on voit notre input ainsi que `bd4c217637bc828982c090b2de41b84d`. 
- Bon là c'est bizarre mais on doit donner l'input encrypté et pas le hash décrypté (pass1785).

# GCC

^676e59


- C'est un compiler abruti.
https://medium.com/@ofriouzan/part-2-compiler-level-security-mechanisms-gcc-d01246b8d157

Pour lier statiquement les bibliothèques (les intégrer directement dans le fichier binaire) plutôt que de les lier dynamiquement :
- `-static`

Pour lier les bibliothèques au programme seulement quand c'est vraiment nécessaire :
- `-z lazy`

Pour rendre l'exécution de code dans la stack possible :
- `-z execstack`

Pour désactiver la relocalisation (changement d'adresse d'éléments pendant l'exécution) :
- `-z norelrol`

Désactiver les protections de la pile tel que les canary.
- `fno-stack-protector`



# UPX

^ab7a42

