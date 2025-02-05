##### **tgmath.h**

- Librairie pour les fonctions mathématiques.


##### **string.h**

- Librairie pour tous ce qui touche aux string
- **Fonctions :**
	- `memcpy(target, source, len)` Utilisée pour copier un bloc mémoire vers un autre endroit.
	```C
	int main(){
		char source[] = "Hello world";
		char destination[20];
		memcpy(destination, source, strlen(source) + 1);
		printf("Source : %s\n", source); // Retournera Hello world
		printf("Destination : %s\n", destination); // Retournera Hello world
		return 0;
	}
	```
	- `memcmp(s0, s1, len)` Utilisé pour comparé deux valeurs de len taille. Retourne 0 si les deux sont égaux, un nombre négatif si le premier argument est inférieur, sinon c'est positif.
	- `memchr(s, c, len)` Utilisée pour renvoyer la première occurence du caractère c dans l'array de char par exemple de taille strlen(s).
	- `memset(array, 0, sizeof(array))` Rempli l'array de taille sizeof(array) avec la valeur 0
	- `strlen(s)` Utilisée pour renvoyer la taille de la string donnée.
	- `strcpy(target, source)` Utilisée pour copier une chaîne de caractère (char source[] par exemple) vers la target. La target doit être assez grande pour pouvoir accueillir la source. 
	- `strcmp(s0, s1)` Utilisée pour comparer deux char. Renvoie un nombre négatif si la première chaine de caractère est inférieur à la seconde, inversement et un 0 si elles sont identiques.
	- `strchr(s, c)`Pareil que memchr mais s doit être 0-terminated
	- `strspn(s0, s1)` retourne le nombre de caractère dans s0 qui apparaissent aussi dans s1.
	- `strcspn(s0, s1)` Retourne le nombre de caractère dans s0 qui n'apparaissent pas dans s1.

##### **assert.h**
##### **complex.h**
##### **ctype.h**
##### **errno.h**
##### **fenv.h**
##### **float.h**
##### **inttype.h**
##### **iso646.h**
##### **limits.h**
##### **locale.h**
##### **math.h**
##### **setjmp.h**
##### **signal.h**
##### **stdalign.h**
##### **stdarg.h**
##### **stdatomic.h**
##### **atdbool.h**
##### **stddef.h**
##### **stdint.h**
##### **stdio.h**
##### **stdlib.h**
##### **stdnoreturn.h**
##### **time.h**
##### **gtmath.h**
##### **threads.h**
##### **uchar.h**
##### **wchar.h**
##### **wctype.h**
##### **Libc**

^06e7f1

- C'est une librairie de base du langage C dans laquelle se trouve toutes les fonctions classiques.

- **Fonctions**
	- 



##### **unistd.h**

- C'est une librairie qui définit les fonctions standard qui sont souvent utilisé dans la gestion de processus, de fichier etc...

- **Fonctions**
	- `fork()` Elle créer un processus qui est une copie exacte du processus parent du programme. 
	- `execve(const char *pathname, char *const _Nullable argv[], char *const _Nullable envp[]);` Cette fonction permet d'exécuter un programme binaire ou qui commence par `#! interpreter [arg]` donné dans le premier paramètre. Ce premier paramètre doit être un pointeur. Ensuite, on donne les paramètres à donner au fichier qu'on va lancer sous forme d'array se terminant par un NULL byte. Enfin,  on fout des variables d'environnement. ^d84b9a
##### **sys/socket.h**

- Utilisé pour toutes les communications réseaux entre plusieurs machine.
- **Fonctions**
	- `int socket(int domain, int type, int protocol)` 
		- Pour créer une socket, aka un point de terminaison
		- La fonction retourne un descripteur de socket.
		- Le domaine c'est le type de d'adresse/domaine à utiliser :
			- AF_INET : Adresse IPv4
			- AF_INET6 : Adresse IPv6
			- AF_UNIX : Processus local, par exemple entre les processus sur le même système
		- Le type c'est le type de communications :
			- SOCK_STREAM : TCP
			- SOCK_DGRAM : UDP
			- SOCK_RAW : Accès direct aux paquets réseaux
			- SOCK_SEQPACKET : Pour paquets de type séquentielle, afin de garantir la livraison séquentielle des paquets
		- Le protocole c'est bah t'es con ou quoi :
			- 0 : Sélectionne automatiquement le bon protocole
			- IPPROTO_TCP : TCP
			- IPPROTO_UDP : UDP
			- IPPROTO_ICMP : ICMP
			- IPPROTO_RAW : Paquets réseaux bruts

	- `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)`
		- Pour lier une adresse à un socket.
		- Le sockfd c'est le descripteur de socket
		- addr c'est pour l'adresse à lier
		- 
