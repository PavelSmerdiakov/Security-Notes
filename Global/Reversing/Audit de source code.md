

Quand on fait de l'audit, on essaye d'abord de comprendre le sens global de ce qu'on observe. Dans les gros programmes, on ne regarde pas tous mais souvent simplement un bout de code. On essaye donc de comprendre exactement ce qui se passe, comment les inputs sont gérées, comment les fonctions sont appelé, les paramètres... Après avoir fait ça, on cherche des vulnérabilités possibles.

### Les facteurs de vulnérabilités

###### Les basiques presque introuvables

- On a par exemple les mauvaises utilisations des fonctions tel que Printf, strcpy ou encore strcat (liste à agrandir).

###### Les formats string

- Les Format String Bug sont en général simples à trouver mais faut bien comprendre le contexte d'utilisation car elles sont souvent bien utilisées.

###### Les faux bound-checking

- Parfois, les développeur font un petit effort pour la sécurité mais ne servent en réalité à rien. Donc c'est pas parce qu'il y a une petite protection qu'on ne peut pas la bypass. C'est pas parce que le programme essaye de limiter la taille d'une input dans un buffer qu'il va réussir.

###### Loops

- Les boucles sont aussi interéssante dans l'audit étant donné qu'elles sont plus compliqués à manipuler et à mettre en place correctement.
- 
[HES2015-10-29 Cracking Sendmail crackaddr.pdf](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/HES2015-10-29%20Cracking%20Sendmail%20crackaddr.pdf)


###### Off-by-one

- Les vulnérabilités Off-by-one sont les vulnérabilités qui occurent quand le programmeur fait une faute d'incrémentation. Ça peut être dans les boucles, les copies de données dans lesquelles on essaye de mettre un null bytes à la fin.

###### Non-null termination issues

- Quand les string ne contiennent pas de null byte à la fin, ce qui se trouve derrière peut donc être compris comme faisant partie du buffer. Si en plus l'user controlle le buffer, on a presque les clé du royaume.
```
char dest_buf[256];
char not_term_buf[256];
strncpy(not_term_buf,input,sizeof(non_term_buf));
strcpy(dest_buf,not_term_buf);
```
- Dans ce programme, les deux buffer font la même taille et le dest_buf n'est pas terminé avec un null bytes donc le deuxième buffer est en fait à nous.

###### Mauvaise gestion du null bytes

- Si quand on écrit un buffer, on le fait dans une boucle et avec un groupe de caractères à chaque tour, on peut alors skip le null byte et donc pouvoir l'exploiter. Si des conditions d'une boucle ne sont pas respecté non plus, les null bytes peuvent être également skip.

###### Vulnérabilité de comparaison de nombre signés

- Certaine fois, les programmeurs comparent des nombres signés avec des nombres unsigned ce qui est pas toujours très clair. Des fois, les nombres unsigned sont invalides mais le programme regarde seulement le MSB qui indique que c'est un signed donc il va directement dire que le nombre signé est supérieur au nombre unsigned. **(à revoir)**

```
void verifier_index(int index) {
    if ((unsigned)index < TAILLE_TABLEAU) {
        printf("L'index %d est valide.\n", index);
    } else {
        printf("L'index %d est hors limites.\n", index);
    }
}

```
- Dans cet exemple, si index = (-1), alors il va dire que la condition est vrai sans même regarder le nombre. Il ne va donc pas proc le else alors que index est hors des limites.
- De plus, quand une valeur unsigned est impliquée dans une comparaison, la valeur d'output sera toujours unsigned


###### Interger-related vulnerabilities

- Ce sont des vulnérabilité ou des bugs qui occurent quand la valeur d'un nombre dépasse celle autorisé (minimum de -0x8000 et maximum de 0x7fff pour les nombres signés sur 16bits). 
```
char *buf;
int allocation_size = attacker_defined_size + 16;
buf = malloc(allocation_size);
memcpy(buf,input,attacker_defined_size);
```
- Dans cet exemple, si la taille indiqué par l'attaquant est trop petite, alors on aura pas la place pour placer les données contenues dans input.
```
#define HEADER_SIZE 16
char data[1024],*dest;
int n;
n = read(sock,data,sizeof(data));
dest = malloc(n);
memcpy(dest,data+HEADER_SIZE,n – HEADER_SIZE);
```
- Plus ou moins pareil pour celui-là.
```
nresp = packet_get_int();
if (nresp > 0) {
response = xmalloc(nresp * sizeof(char*));
for (i = 0; i < nresp; i++)
response[i] = packet_get_string(NULL);
}
```
- Dans ce cas, la valeur peut très bien dépassé le maximum autorisé étant donnée qu'elle est multipliée et donc produire une erreur.
https://learn.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-007


###### Conversion d'entier de différentes tailles

- Ces conversions peuvent être troublantes mais sont des bugs auquels il faut penser. Quand on converti des nombres unsigned vers des nombres signed de différente taille ou l'inverse, les résultat ne sont pas forcément ceux attendus. 
- La table des conversions :
  
 ![Pasted image 20240306212051.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240306212051.png)

![Pasted image 20240306212104.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240306212104.png)

###### Double free vulnérabilité

**CVE-2018-17182**
**CVE-2009-3555**

- Elles occurent quand on lance la fonction free() 2 fois pour un seul chunk. Quand on libère de la mémoire, on place le pointer vers null afin d'éviter qu'il ne soit réutilisé. S'il fait autre chose, y'a peut être une vulnérabilité.


###### Usage de mémoire Out-of-Scope 

- Si un programme définit des espaces mémoires qui ont une durée de vie ou un scope, si on peut les utiliser avant ou après, y'a un bug et c'est peut-être une vulnérabilité.


###### Variable non initialisées
https://vulncat.fortify.com/en/detail?id=desc.controlflow.cpp.uninitialized_variable
https://cqr.company/web-vulnerabilities/uninitialized-memory-vulnerabilities/
- Si des variables sont inutilisées et non initialisées, ça veut dire que dans la mémoire, elles ne contiennent rien. On pourrait par exemple passer par dessus des variables non initialisée pour permettre de faire des buffer overflows.
```
int vuln_fn(char *data,int some_int) {
	char *test;
	if(data) {
		test = malloc(strlen(data) + 1);
		strcpy(test,data);
		some_function(test);
	}
	if(some_int < 0) {
		free(test);
		return -1;
	}
	free(test);
	return 0;
}
```
- Si data est null, alors test n'est pas initialisé.


###### User After Free
https://cwe.mitre.org/data/definitions/416.html
https://beta.hackndo.com/use-after-free/
https://owasp.org/www-community/vulnerabilities/Using_freed_memory
- Quand un programme libère une mémoire, plus rien ne doit pointer vers celle-ci. Si c'est le cas, on pourrai avoir des problèmes en accédant à une mémoire libres car ce n'est pas la même structure.

```
    #include <stdio.h>
    #include <unistd.h>

    #define BUFSIZER1   512
    #define BUFSIZER2   ((BUFSIZER1/2) - 8)

    int main(int argc, char **argv) {
        char *buf1R1;
        char *buf2R1;
        char *buf2R2;
        char *buf3R2;

        buf1R1 = (char *) malloc(BUFSIZER1);
        buf2R1 = (char *) malloc(BUFSIZER1);

        free(buf2R1);

        buf2R2 = (char *) malloc(BUFSIZER2);
        buf3R2 = (char *) malloc(BUFSIZER2);

        strncpy(buf2R1, argv[1], BUFSIZER1-1);
        free(buf1R1);
        free(buf2R2);
        free(buf3R2);
    
```
- Dans ce cas, la mémoire à l'emplacement buf2R1 est pointé alors qu'il "n'existe plus".


###### Multithreaded Issues and Re-Entrant safe code

- Dans les programmes qui utilisent le multithreading, on doit bien faire attention aux variables qui sont utilisé car si une variable est utilisée par plusieurs thread en même temps, elle a un status "non défini" car on ne sait pas quel thread va y accéder en premier. On pourrait donc par exemple faire des races conditions. C'est un peu le problème des prédictions dans le pipeline.


###### Mauvaise utilisation d'Authentication et d'Authorization
http://www.omnigroup.com/mailman/archive/macosx-admin/2001-June/020678.html

- L'authentication c'est le fait de vérifier l'identité d'une personne alors que l'authorization c'est vérifier si cette personne a accès à une donnée.
- Dans certain cas, les deux ne sont pas liées et donc peuvent comporter des vulnérabilités.


###### Des grandes vulnérabilité peuvent apparaître dans des endroits tous bêtes
cve.mitre.org/cgi-bin/cvename.cgi?name=CAN-2002-0891
otn.oracle.com/deploy/security/pdf/2003Alert58.pdf
www.kb.cert.org/vuls/id/322540
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CAN-2002-1123

- Ça pourrait par exemple être dans des login input ou authentication.



### Trouver des failles manuellement

- En premier lieu, il faut essayer de comprendre comment fonctionne le système sans même regarder la documentation et le source code.
- Ensuite, on regarde les zones de faiblesse en trouvant des comportements étrange pendant l'utilisation du système avec des tracing tools par exemple.
- Ensuite, tu peux tester des attaques courante pour voir comment elles réagissent. Tu ne va pas forcément trouver un truc interéssant mais si t'en trouve, t'as une faille facile à faire alors.
- Tu peux te poser des question du genres "Qu'est ce qui parse cette input ?", "Quelle est sa portée ?"...


### Bypass les détecteurs d'attaques

###### Utilisation de techniques similaires aux XSS, SQL injection ou autre

- Imaginons qu'on ait un programme qui bloque certains mot, on pourrait par exemple les doubler comme par exemple mettre uniunionon à la place de union.

###### Encodage différent

- On pourrait encoder les inputs en base64, unicode...


### Indicateur de bug/vulnérabilités

![Wiley.The.Shellcoders.Handbook.2nd.Edition.Aug.2007.pdf](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Wiley.The.Shellcoders.Handbook.2nd.Edition.Aug.2007.pdf)

A variable indexed write into a character array:
- `mov [ecx+edx], al`

A variable indexed write to a local stack buffer:
- `mov [ebp+ecx-100h], al`

A write to a pointer, followed by an increment of that pointer:
```
mov [edx], ax
inc edx
inc edx
```

A sign extended copy from an attacker-controlled buffer:
```
mov cl, [edx]
movsx eax, cl
```

An addition to or subtraction from a register containing attacker-controlled
data (leading to an integer overflow):
```
mov eax, [edi]
add eax, 2
cp eax, 256
jae error
```

Value truncation as a result of being stored as a 16- or 8-bit integer:
```
push edi
call strlen
add esp, 4
mov word ptr [ebp-4], ax
```
### Tips and tricks

###### Graph view

- Afin de comprendre plus facilement l'utilisation d'une fonction, les graphiques sont souvent utiles. À approfondir quand tu aura utiliser.


