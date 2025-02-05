**Format d'écriture :**

- Les registres c'est simple, c'est juste EAX, RIP...
- Pour faire la différence entre un nombre et une adresse, les adresses sont entre [].
- **Format Intel :** mov destination, source donc _mov eax, 42_
- **Format AT&T :** movl source, destination donc *movl $42, %eax *Les $ c'est pour valeur immédiate. Les % c'est pour les registres.
### **Intel format**

#### Opcode
https://www.felixcloutier.com/x86/

- Des fois, tu pourras rencontrer des opcodes avec des q à la fin, c'est juste pour dire que c'est un quad word (64bits)
- `PUSH` : Syntaxe : PUSH Operand. On ajoute un élément à la pile donc tout en haut (dans les adresses basses)
- `POP` : Syntaxe : POP Operand. En fait, c'est ultra intelligent comme principe. Dans tous les cas, POP va retirer le dernier élément (adresse la plus basse) de la stack. Il va ensuite placer l'élément retiré dans l'opérande donc l'opérande c'est souvent un registre.
- `ADD` : Syntaxe : ADD Operand1, Operand2. Somme de 2 nombre. Résultat stocké dans Operand1
- `SUB` : Syntaxe : SUB Operand1, Operand2. Soustraction. 1-2 résultat stocké dans Operand1
- `MUL` : Syntaxe : MUL Operand. On multiplie l'operand par EAX et on stocke le résultat dans EDX:EAX. Les MSB (les gros chiffres) seront dans EDX et les LSB (les petits chiffres comme les dizaines) seront dans EAX.
- `DIV` : Syntaxe : DIV Operand. On divise cette fois ci EAX par l'operand. Quotient est stocké dans EAX et reste dans l'operand. L'operand c'est souvent un registre puisqu'on stocke le reste dedans.
- `IMUL` : Syntaxe : IMUL Operand1, Operand2. Pareil que MUL sauf qu'on peut faire avec entier signé (nombres négatifs) On peut aussi faire simplement IMUL operand pour le multiplier par lui meme
- `IDIV` : Syntaxe : IDIV Operand. Pareil que DIV sauf qu'on peut faire avec entier signé
- `CMP` : Syntaxe : CMP Operand1, Operand2. On soustrait operand2 à operand1. En fonction du résultat de la soustraction (qui n'est pas stockée), on change les flags. Exemple : EAX = 10, CMP EAX, 10 la soustraction donnera zéro donc le flag ZF sera sur 1. On se servira donc de ce résultat de flag pour une action comme un jump par exemple.
- `CALL` : Syntaxe : CALL FunctionAddress. On remplace l'operand par l'adresse de la fonction.
- `RET` : Syntaxe : RET. Le processus est simple. On pop tout le haut de la pile (les var locales, adresses plus basses que ebp). Quand on arrive à l'adresse de retour, on pop avec comme opérande EIP/RIP. On va donc retourner à l'instruction qu'elle pointé puisqu'EIP le contient. On peut ajouter un operand en byte pour liberer le nombre de byte qu'on veut à la place des paramètres car ils n'ont pas été pop (ils ont une adresse plus haute que EBP).
- `LEA` : Syntaxe : lea rax,[rbp-0x20]. Elle charge l'adresse absolue d'une adresse relative (rbp-0x20 dans cet exemple) dans rax.
- `JE/JZ` : Jump if Equal / Jump if Zero
- `JNE/JNZ `: Jump if Not Equal / Jump if Not Zero
- `JLE` : Jump if less or equal
- `SHR` :Syntaxe : shr edx, 0x1f Décale les bits (en binaire) de edx vers la droite de 0x1f bits. En fait c'est pour diviser edx par 2^n ou n est le 0x1f.
- `SHL` : Syntaxe : shl edx, 0x0a Pareil que SHR mais c'est pour la multiplication par 2^n.
- `SAL/SAR` : Syntaxe : sar dl, 1, ils sont respectivement comme SHL et SHR mais fonctionnent pour les nombres négatifs.
- `XCHG` : Syntaxe : xchg %eax, %ebx, Échange le contenu des deux registres
- `HLT` : Syntaxe : hlt, Met en état d'arrêt le processus
- `NEG` : Syntaxe : neg %eax, Prend l'inverse algèbrique d'un nombre (10 -> -10)
- `SYSCALL` : Syntaxe : syscall, Provoque un appel système avec en arguments les registres tel que rax, rbx, ...Dans les registres, c'est le numéro d'appel système qui sont définit ici pour Linux : https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/ ou https://thevivekpandey.github.io/posts/2017-09-25-linux-system-calls.html ^4db004
- `Db` : Syntaxe : Db /bin/sh, c'est une "instruction" qui définit des octet de la pile avec l'argument lui est passé. ^51ff06
- `AND` : Syntaxe : and ecx, 3, c'est pour faire une opération "et logique". 
- `REPE` : Syntaxe : repe movsb, repète l'instruction en fonction de la valeur d'ECX.
- `MOVSD` : Syntaxe : movsd eax, ebx, copie un double mot de données vers la destination
- `MOVABS` : Syntaxe : movabs eax, 0x6361726379736165, pour copier des valeurs sur 64bits.
- `LES` : Syntaxe : les dest, src, `???`
- `TEST` : Syntaxe : test eax, eax, fait un ET logique mais ne stocke pas le résultat, il se contente de changer les flag ZF en 0 si eax vaut 0, change SF si le MSB est assigné dans le résultat.
- `CLD` : Syntaxe : cld, s'assure que le flag [[Opcode-Register#^7c5da8|DF]] est mit sur 0.
- `STD` : Syntaxe : std, s'assure que le flag [[Opcode-Register#^7c5da8|DF]] est mit sur 1
- `JO` : Jump if Overflow avec le flag [[Opcode-Register#^539131|OF]]
- `JNO` : Jump if no overflow
- `CLC` : Syntaxe : clc, positionne le [[Opcode-Register#^cb0873|CF]] à zéro
- `STC` : Syntaxe : stc, positionne le [[Opcode-Register#^cb0873|CF]] à 1
- `CMC` : Syntaxe : cmc, inverse le [[Opcode-Register#^cb0873|CF]] 
- `ADC` : Syntaxe : adc dest, src, additionne la dest, la src, [[Opcode-Register#^cb0873|CF]] et stocke le résultat dans dest.
- `SBB` : Syntaxe : sbb dest, src soustrait la valeur de [[Opcode-Register#^cb0873|CF]] à la différence des 2 opérandes.
- `CLI` : Syntaxe : cli, positionne [[Opcode-Register#^6e867d|IF]] sur 0
- `STI` : Syntaxe : sti, positionne [[Opcode-Register#^6e867d|IF]] sur 1
- `INT` : Syntaxe : int num, fait une interruption avec exécute le code associer au numéro. ^fbddbe
- `INT3` : Syntaxe : int3, fait proc un breakpoint



---
#### **Registre :**

- **Spécifique Architectures x64 :**
    
- **Spécifique Architectures x32 :**
    
- **Général :**
    
    - `RSP/ESP` : Stack pointer, il pointe vers le dernier élément ajouté sur le stack. ^0ac733
    - `RBP/EBP` : Base pointer, il pointe vers la base du stack. Donc en dessous de l'adresse de retour
    - `RAX/EAX` : Tel que les registres RBX/EBX/ECX/RCX etc, ce sont des registres temporaires pour stocker des valeurs qu'on ne sait pas où foutre mais qu'on a besoin. ^bd4e75
    - ![[Pasted image 20240227225614.png]]
    - Ce schéma fonctionne aussi pour ebx, ecx ...
    - `RIP/EIP` : Instruction pointer, il stocke l'adresse de l'instruction en cours.
    - `ESI/EDI` : Source Index, Destination Index, Utilisés dans les opérations de copie de données et de transport de variables. ^d5727a

**Flag :** Les flags c'est tous les indicateurs qui reflètent l'état du proco. Ils fournissent également les résultat d'instruction. Ils sont tous défini par EFLAGS. Liste des flags :

- `ZF` : Zero Flag se met à 1 si le résultat d'une opération est zéro.
- `SF` : Sign Flag indique le signe du résultat d'une opération. Il est à 1 si le signe est négatif.
- `CF` : Carry Flag indique si le résultat d'une opération arithmétique contient une retenue.  ^cb0873
- `OF` : Overflow Flag indique un dépassement de capacité, par exemple quand une addition de 2 nombre positif met le MSB sur 1 (qui devrait indiquer un nombre négatif), OF est sur 1 pour indiquer cet overflow ^539131
- `PF` : Parity Flag indique si le nombre de bits sur 1 est pair ou non. Si oui, alors il est mit à 1.
- `DF` : Direction Flag  indique la direction de copie de donnée. S'il est sur 1, alors on copie les données de façon ascendante en commençant par l'adresse la plus basse. Sinon c'est le contraire. ^7c5da8
- `AF` Auxiliary carry Flag est à 1 si la dernière opération a généré une retenue du 3ème bit vers le 4ème.
- `IF` interrupt Flag est à 1 si les interruptions sont autorisée  ^6e867d
- `TF` Trap Flag est à 1 quand on exécute les instructions pas à pas. Il appelle [[Opcode-Register#^fbddbe|int 1]] avant chaque instructions
- 


------------------

#### Construction/logique de code en assembleur

##### Petites notes

L'adresse de retour d'un appel de fonction est dans le registres EAX

Les instructions JL et JG sont utilisés pour la comparaison d'entier signés

Les instructions JB et JA sont utilisés pour la comparaison d'entier non signés

MOVSX prend en compte le signe quand on copie une valeur plus petite vers un registre alors que MOVZX s'en branle et met juste des zéro aux bits msb


###### Prologue d'une fonction 

- C'est les fonctions assembleur de base qui sont exécuté dès qu'une fonction est appelé.
- **push ebp** // On initialise EBP
- **mov ebp, esp** // On met la valeur d'ESP dans EBP pour qu'il pointe au sommet de la fonction à ce moment. Il va donc être la référence (la base) de la fonction avec laquelle on va pouvoir référencer tout les éléments de la stack.
- **sub esp, 10** // On soustrait 10 bytes (en hex donc 16bytes en vrai) ce qui alloue de l'espace vide pour pouvoir placer des variables locales (soustrait car local var ont addr moins élevées que EBP)


###### memcpy-like 

```
mov esi, source_address 
mov ebx, ecx
shr ecx, 2             // divise la taille d'ecx par 4
mov edi, eax           // adresse de destination
repe movsd             // répéte ecx fois la copie de 4 octet vers esi
mov ecx, ebx
and ecx, 3
repe movsb             // = movsd mais 1 par 1 avec ce qui reste dans esi
```
- Ça sert à copier esi vers edi de façon rapide en commençant avec des copies de 4 octets (d'où la division de ecx par quatre car c'est comme un compteur) et quand ecx vaut zéro, il reprend sa valeur initiale puis on fait un ET logique. On récupère donc le reste à copier et on le refout dans edi avec la dernière répétition.


###### strlen-like

```
mov edi, string       
or ecx, 0xffffffff     // OU logique donc met ecx au maximum
xor eax, eax           // met eax à zero
repne scasb            // repète la comparaison de eax avec edi
not ecx                // inverse ecx afin de chopper la taille de string
dec ecx                // décrémente de 1 car complément à deux
```
- Ça sert à trouver la taille de la chaine string. scasb compare le caractère avec eax donc temps qu'on a pas de caractère égale à zéro (repne), ça veut dire qu'on touche pas encore l'octet null de la fin de string. ecx va servir à compter le nombre de caractère dans string. En fait, on l'initialise au maximum car scasb va retirer 1 à chaque caractère. Donc après la répétition, ecx contiendra le nombre d'octet après l'octet null. Mais nous on veut savoir combien il y en a avant donc on l'inverse et on décrémente de 1 car y'a le complément à deux de merde.


