#### **Pointeurs**

- C'est une variable qui contient l'adresse mémoire d'une autre variable

**Utilisation :**

- Spécificateur de format d'un pointeur :
	- `%p`
- Déclarer un pointeur qui pointe vers une valeur int
	- `int *ptr`
- Initialisation d'un pointeur
	- `int num = 10;`
	- `int *ptr = &num;`
- Accéder à la valeur d'un pointeur
	- `int value = *ptr;`
- Modifier la valeur POINTÉE
	- `*ptr = 20;`
- Avoir un pointeur qui ne pointe vers rien
	- `int *ptr = NULL;`
- Déplacer le pointeur dans la mémoire
	- `ptr++`
- `char* name ou char *name` c'est pareil, le premier est cependant plus intuitif (askip)
- `char const * const path_name ;` "`char const*`" indique que `path_name` pointe vers un caractère constant. "`const`" indique que le pointeur lui-même (path_name) est constant.
```C
struch Person {
	char name[20];
	int age;
};

int main(){
	struct Perso Person1;
	struct Person* ptrPerson = &person1;
	ptrPerson->age = 30; // On modifie l'age de Person1 grâce au pointeur.
	person1.age = 30; // C'est un équivalent mais sans le pointeur.
}

```

##### **Switch**

- Alternative de if-else pour les conditions complexes.

**Utilisation :**

```C
 int jour = 1;
 switch (jour) {
 case 1:
	 printf("C'est lundi");
	 break;
 case 2:
	 printf("C'est mardi");
	 break;
 ETC...
 default:
	 printf("Jour Invalide");
 }
```


##### **Type Value**

**size_t**
Représente des valeurs comprises entre 0 (seulement positive) et SIZE_MAX où SIZE_MAX peut prendre :
	2¹⁶-1
	2³²-1
	2⁶⁴-1

**char** ^34615d
- Représente des caractères en valeur ASCII.
- Un caractère vaut 1 byte
- Spécificateur de format : %c

**int**
- Représente un nombre.
- Un int vaut 32 bits
- Spécificateur de format : %d

**long**
- Représente un nombre plus grand que int.
- Un long vaut 64 bits
- Spécificateur de format : %ld

**float**
- Représente un nombre float
- Un float vaut 4 bytes
- Spécificateur de format : %f
- Spécificateur de format avec 2 chiffres après la virgule : %.2f

**double**
- Représente un nombre float plus grand que float.
- Un double vaut 8 bytes
- Spécificateur de format : %lf

**bool**
- Représente un booléen
- Un bool vaut 1 byte
- Exemple d'utilisation des booléens (vulnérabilité) :
	- `bVar1 = std::operator==(local_38,"do_not_hardcode");` 
		- Si local_38 à une valeur "do_not_hardcode", alors bVar1 contiendra >True

**Spécificateur de format**
- Si on veut prendre le troisième arguments passé en hexa: 
	- `printf("%3\$x", a, b, c)` le \ sert à include le $ dans la syntaxe
- Pour récupérer le nombre de caractère écrit jusqu'à là :
	- `printf("blah %n blah", &var)` var contiendra 5 ^4df320
	- Y'a aussi hn pour écrire un nombre de 2 octets, ln pour 4 octets, lln pour 8octets

![Pasted image 20240213213117.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240213213117.png)
![Pasted image 20240213213226.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240213213226.png)
```C
int x = 42;
// Following statements are equivalent:
printf("x is %d, which is boolean %d.\n", x, !!x);
printf("x is %d, which is boolean %d.\n", x, (x == 0 ? 0 : 1));
printf("x is %d, which is boolean %d.\n", x, x != 0);
// Output: "x is 42, which is boolean 1."
  
x = 0;
// Following statements are equivalent:
printf("x is %d, which is boolean %d.\n", x, !!x);
printf("x is %d, which is boolean %d.\n", x, (x == 0 ? 0 : 1));
printf("x is %d, which is boolean %d.\n", x, x != 0);
//Output: "x is 0, which is boolean 0."
```
![Pasted image 20240215205646.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240215205646.png)

**Buffer**
- Un buffer c'est un endroit de mémoire avec une taille prédéfinie qui sert à stocker des valeurs dedans. Ça peut par exemple être une array ou une variable (char buffer[100])

##### **Directives de Préprocesseur**

C'est des instructions spéciale qui sont déstinées à être traitée par le préprocesseur du compilateur avant la compilation proprement dite du code.

**Macros prédéfinies**

- `__LINE__` indique le numéro de ligne du script
- `__FILE__` indique le nom du fichier
- `__DATE__` indique la date de compilation (chaîne de caractères)
- `__TIME__` indique l'heure de compilation (chaîne de caractères)
- `__cplusplus` elle est définie si le code est compilé en tant que programme C++
- `__STDC__` elle est définie si le code est compilé en tant que programme conforme aux normes C
- `__func__` indique le nom de la fonction actuelle
- `__VA_ARGS__` indique les arguments d'une macro variadic (arguments qui varie en nombre)


**ifdef/ifndef et endif** 

- C'est pour compiler les instructions entre les deux directives seulement si la macro (DEBUG dans mon cas) est défini ou activée.
```C
#include <stdio.h>

int main() {
#ifdef DEBUG
    printf("Mode de débogage activé\n");
#endif

    printf("Hello world !\n");
    
#ifdef DEBUG
    printf("printf effectué\n");
#endif
    return 0;
}

```
- Pour l'activer, on peut faire avec l'option -D de gcc :
	- `gcc -DDEBUG myscript.c -o myscript`
- Pour activer la macro avec une valeur :
	- `gcc -DDEBUG=value myscript.c -o myscript`
- ou alors directement mettre `#define DEBUG` en haut du script.
- C'est la même logique avec `ifndef`

**define**

- C'est pour définir des macros. C'est un peu comme des variables qui seront utilisées pendant tous le programme. Ça peut être des constantes universelle par exemple comme PI.
```C
#include <stdio.h>

#define PROUT

#define PI 3.14

#define PI2 (22/7)

#define SQUARE_AREA(s) (s * s)

#define CONCAT(a, b) a ## b // le ## va concatener les deux paramètres.

# define MINSIZE (X , Y ) ( sizeof ( X ) < sizeof ( Y ) ? sizeof ( X ) : sizeof ( Y ) )

int main(){
	printf("%d", PI);
	
	printf("%d", PI2):
	
	area = SQUARE_AREA(5);
	
	printf("%d", area);
	
	int value1 = 10;
	int value2 = 20;
	int CONCAT(value, 1) = 100; // value1 va donc être à 100
	int CONCAT(value, 2) = 200; // value2 va donc être à 200

#ifdef PROUT
	printf("Hello world");
#endif

}
```

**error**

- C'est pour la gestion d'erreur pendant la compilation. C'est inutile après avoir compilé le programme donc c'est vraiment pour le debug.
```C
#include <stdio.h>

#ifndef DEBUG
	#error "DEBUG is not defined! Please define DEBUG before compiling."
#endif

int main() {
	printf("Programme en cours d'exécution\n");
	return 0;
}
```
- Comme d'habitude, il faut déclarer la macro DEBUG quelque part sinon dans ce cas ci, on va pas pouvoir faire la compilation et on aura l'erreur indiquée.


**if else elif**

- C'est comme les if else elif de base mais pour les expressions qui inclut des macros.
```C
#include <stdio.h>
#define VALUE 10
int main() {
	#if VALUE > 5
	    printf("VALUE est supérieur à 5\n");
	#else
	    printf("VALUE est inférieur ou égal à 5\n");
	#endif
	return 0;
}
```
**import**

- C'est comme la directive `#include` mais c'est pour contrer l'inclusions d'autre fichier en double. Par exemple si le fichier qu'on inclut a lui-même inclut des fichiers qu'on a dejà inclut dans notre script,  bah avec `#import` y'a pas de soucis. Même si en général, on utilise plutôt `#include` pour pas se faire chier et pas habitude.

**line**

- C'est pour définir le numéro de ligne du fichier et facultativement le nom du fichier. C'est utile quand tu génère du code dynamiquement mais en général on s'en branle un peu.
```C
#include <stdio.h>

int main(){
#line 100 myscript.c
	printf("The current line number is %d\n", __LINE__);
#line 200
	printf("The current line number is %d\n", __LINE__);
}
```
- L'output sera donc 
```C
The current line number is 101
The current line number is 201
```

**undef**

- C'est pour supprimer une macro précédemment créée avec `#define`

**pragma**

- C'est pour envoyer des instructions au compileur avant même la compilation.
- C'est assez dense et profond comme concept parce que y'a plein de chose à faire avec.
```C
#include <stdio.h>
#pragma GCC poison printf
int main(){
	printf("Cette ligne va retourner une erreur.");
	return 0;
}
```
##### **enum**

- C'est vraiment pour faire une énumération. T'associes des chaîne de caractère par exemple et donc la première occurence va avoir comme valeur 0.
```C
enum corvid { magpie, raven, jay, corvid_num, };
int main(){
	char const *const animal[corvid_num] = {
	[raven] = "raven",
	[magpie] = "magpie",
	[jay] = "jay",
	};
	for (unsigned i = 0; i < corvid_num; i++){
		printf("Blabla %u %s\n", i, animal[i]); // raven aura 0, magpie aura 1 etc...
	}
	return 0;
}
```
- Pour faire des opérations, on ne peut pas les faire sur des objets :
```C
signed const o42 = 42;
enum {
b42 = 42 , // ok , 42 is a literal
c52 = o42 + 10 , // error , o42 is an object
b52 = b42 + 10 , // ok , b42 is not an object
};
```
##### **Array**

- C'est simplement un tableau comme en python, simple ou complexe.
- `int numbers[5] = {1,2,3,4,5};`
- `int x = numbers[2];`
- `numbers[4] = 10;`
- `int size = sizeof(numbers) / sizeof(numbers[0])` C'est pour déterminer la taille du tableau dans la mémoire.
- ````int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
	};
- `double C[M][N];` Déclare un tableau C de M ligne et N colonnes avec des éléments de type double
- `double (D[M])[N];`Déclare un tableau D de M éléments qui pointe chacun vers un tableau de N éléments de type double. Pour accéder à un élément : `D[0][1] = 5,0;`

##### **Structure**

- Les structures en C c'est comme les classes en python. Elle permet de créer des objets du type de la structure donc avec les propriétés et tout.

Copié collé de je ne sais plus où :

```C
struct Personne {
	char nom[50];
	int age;
	float taille;
}
int main(){
	struct Personne p1;
	strcpy(p1.nom, "Alice");
	p1.age = 30;
	p1.taille = 1.75;
}
```

```C
struct animalStruct {
	const char * jay ;
	const char * magpie ;
	const char * raven ;
	const char * chough ;
};
struct animalStruct const animal = {
	.chough = " chough " ,
	.raven = " raven " ,
	.magpie = " magpie " ,
	.jay = " jay " ,
};
```

##### **Fonctions**

- `int main(int argc, char *argv[]){}` argc c'est le nombre d'arguments y compris le nom du programme, argv c'est les arguments passés.
```C
size_t pgcd(size_t a, size_t b){
	assert(a<= b);
	if (!a) return b;
	size_t rem = b % a;
	return pgcd(rem, a);
}
```
- ![Pasted image 20240216163759.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240216163759.png)
- **Fonction de callback**
	- Une fonction de callback c'est une fonction qui est passé en argument à une autre fonction. Ça permet de gérer différement la sortie d'une fonction ou instruction sans même le spécifier dans le main, on a simplement à dire vers quel fonction le flux doit être redirigé et la fonction se charge du reste.
```C
#include <stdio.h>

typedef void (*CallbackFunction)(int);

void add(int a, int b, CallbackFunction callback) {
    int result = a + b; 
    callback(result);    
}


void afficher_resultat(int result) {
    printf("Le résultat du calcul est : %d\n", result);
}

int main() {
    add(10, 5, afficher_resultat);
    return 0;
}

```


- **gets()** 
	- Fonction qui lit l'input stdin entrée par l'utilisateur dans le shell. Très dangereuse car elle ne vérifie pas la taille de l'input donc stack overflow possible.
	- Syntaxe : gets(var)
- **fgets()**
	- Version sécurisée de gets() car elle lit seulement la taille de l'input que la var spécifie
	- Syntaxe : fgets(var)
##### **Threads**

