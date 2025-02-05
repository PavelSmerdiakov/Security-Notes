

- **Bus error vs segmentation fault**
	- Quand tu reçois un bus error, c'est qu'on tente d'accéder à une adresse non valide.
	- Quand tu reçois un segmentation fault, c'est qu'on tente d'accéder à une adresse où on a pas accés.
- **Désactiver la randomisation de la stack**
	- `echo 0 > /proc/sys/kernel/randomize_va_space`
- **La réactiver**
	- `echo 2 > /proc/sys/kernel/randomize_va_space`
- **Voir les emplacement mémoire writable d'un processus**
	- `cat  /proc/[pid]/maps` Pour trouver le pid d'un programme qu'on débugue [[Outils command line#^7f5428|clique ici]]

- **Endroit cible à remplacer dans un exploit**
	- The saved return address (a straight stack overflow; use information
		disclosure techniques to determine the location of the return address)
	- The Global Offset Table (GOT) (dynamic relocations for functions; great
		if someone is using the same binary as you are; for example, rpm)
	- The destructors (DTORS) table (destructors get called just before exit)
	- C library hooks such as malloc_hook, realloc_hook and free_hook
	- The atexit structure (see the man atexit)
	- Any other function pointer, such as C++ vtables, callbacks, and so on
	- In Windows, the default unhandled exception handler, which is
		(nearly) always at the same address
- **Débuguer un programme avec un fichier core**
	- Si tu reçois une erreur du genre segmentation fault durant l'exécution d'un programme, tu peux l'analyser en créant un core dump qui enregistre la mémoire et l'exécution du programme au moment de l'erreur. Pour activer ça :
		- `ulimit -c unlimited` Attention, ça peut prendre un peu de place donc active-le seulement quand tu en as besoin.
	- Pour le désactiver :
		- `ulimit -c`
- **Taille des buffer**
	- En général, les buffer sont implémenté avec une taille de multiple de 2. De temps en en de 10. Le reste a souvent une taille basé sur le même schéma mais avec une soustraction ou une addition de 1 à 20 bytes. Tu peux te servir de ces probabilités pour créer ton fault injection program. Si on teste avec un grand nombre de taille de buffer, à la base on aurait 70 000 teste possibles par exemple contre environ 800 avec nos statistiques.

- **Voir toutes les strings d'un programme**
	- `strings ./prout
## Liens sympa pour apprendre 

- https://github.com/ir0nstone/pwn-notes/tree/master/types
- https://github.com/rosehgal/BinExp
- https://github.com/alanvivona/pwnshop
- https://sumit-ghosh.com/posts/hijacking-library-functions-code-injection-ld-preload/
