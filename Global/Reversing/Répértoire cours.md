https://github.com/onethawt/reverseengineering-reading-list

**Compiler :**  
Le fonctionnement du compiler est sympa. Il est divisé en trois phases :

0. **Préprocesseur :** C'est la phrase de traitement des directives de préprocesseur qui va donc faire les instructions qui lui sont indiquées dans le programme source.

- ![[Pasted image 20240216213308.png]]![[Pasted image 20240216215408.png]]
1. **Le front-end :** D'abord, la lexical analysis converti les instructions en "lexemes" qui est une unité qui représentes les trucs du genre if, else, les variables, les opérateurs enfin tout quoi. Chaque lexeme est ensuite converti en "token" qui est sous la forme (token-name, attribute-value) où token-name c'est juste un nom utilisé pendant l'analyse syntaxique et l'attribute-value pointe vers une entrée de la **symbol table**. *La symbol table contient des éléments tels que les variables, les fonctions, les constantes mais pas les opérateurs ni les instructions de contrôle de flux (while, for...) par exemple car ils n'ont pas de valeurs.* Ensuite, la syntax analysis créer un syntax tree. Le semantic Analyzer va reprendre cet arbre puis va en gros check le bon fonctionnement des types de données. 
    
2. **L'optimiseur :** Ensuite, on converti l'arbre en code facile et rapide à faire puis il est passé dans l'optimizer.
	- **Type checking :** Il check le bon fonctionnement des opérations sur les types de données. Il regarde aussi si y'a des problèmes de sécurité par exemple si une string n'est pas vérifiée et qu'elle a un impact sur le control-flow, il le voit.
	- **Bound checking :** C'est la détection des buffer over-flow dans les programmes, qui n'a pas toujours un bon success rate.
	- **Memory-Management Tools :** Résout pas mal de problème tel que les memory leak, l'optimisation des accès à la mémoire, l'optimisation de l'allocation de mémoire etc...

4. **Le back-end :** Il s'occupe de générer le code machine (pas en assembleur) grâce au code optimisé. Cette partie est décomposé en plusieurs étapes dont 3 très importante pour nous, reverser :
    
    - Instruction Selection : C'est à ce moment que le compiler choisit les instructions à utiliser à partir du code optimisé.
    - Register Allocation : Là, on associe des registres aux variables locales. Sachant qu'il y a une infinité de registres possible mais que le proco n'a pas une place infini, c'est là que le register allocation entre en scène.
    - Instruction Scheduling : C'est pour pouvoir avoir un interleaved code. Ca signifie que des instruction qui parle de choses différentes vont au final créer une séquence d'instructions. On essaye d'avoir un parallèlisme le mieux possible pour être rapide.

**Object Code :** C'est le code qu'utilise les langages comme le C ou C++. C'est un code qui est directement utilisé et lu par le cpu.

**ByteCode :** C'est le code qu'utilisent les langages comme Java, Python ou C#. Il nécessite une VM application pour être executé.

- Il existe deux type de virtual machines :
    - **Virtual Machine Système :** Tout un système physique est émulé et permet donc d'executer un os.
    - **Virtual Machine Application :** C'est conçu pour executer seulement des programmes. Un peu de lecture si tu te fais chier : [https://www.jmdoudoux.fr/java/dej/chap-jvm.htm](https://www.jmdoudoux.fr/java/dej/chap-jvm.htm "https://www.jmdoudoux.fr/java/dej/chap-jvm.htm")
- Processus utilisé avec le ByteCode :
    - On utilise un compiler pour générer le bytecode à partir du code high-level.
    - Avec le fichier, on appelle la VM application pour interpréter et exécuter le programme.
- ![[Pasted image 20240216210638.png]]

**System-level Reversing :** Analyse d'un système ou programme en examinant toute les input et output. Il faut bien comprendre comment fonctionne les os pour comprendre correctement comment les inputs et outputs du programme fonctionne.

**Code-level Reversing :** Analyse en profondeur du code low-level pour bien comprendre comment ca fonctionne. On en fait généralement après le System-level reversing.

**Tailles des type de données en byte (langage C) :**

1. **char :** 1 octet
    
2. **int :** 4 octets
    
3. **float :** 4 octets
    
4. **double :** 8 octets
    
5. **short :** 2 octets
    
6. **long :** 4 octets
    
7. **long long :** 8 octets
    
8. **pointer (pointeur) :** 4 octets (sur une architecture 32 bits) ou 8 octets (sur une architecture 64 bits)


**Intel NetBurst (ancêtre de Core) :** Microarchitecture qui est l'environnement d'exécution de programme.

**Micro-Ops (µop ou uop) :** Instructions, défini par microcode (ensemble d'instructions pour générer des µops de bas-niveau stocké dans une mémoire ROM) et généré par le front-end du pipeline, pouvant être exécuté plus rapidement en utilisant un execution trace cache ([http://www.eecs.harvard.edu/cs146-246/micro.trace-cache.pdf](http://www.eecs.harvard.edu/cs146-246/micro.trace-cache.pdf "http://www.eecs.harvard.edu/cs146-246/micro.trace-cache.pdf")) qui stocke les instructions souvent utilisé. Ca évite d'aller les chercher dans le ROM à chaque fois. Une µops c'est une opérations coté hardware donc c'est même plus en machine code, c'est encore après.

**Microcode :** Ensemble d'instructions interne au processeurs qui définissent comment les instructions du programme doivent être effectué. Le microcode aide le front-end à générer le µops. Le microcode c'est une couche de la micro-architecture d'un proco donc il ne change jamais peu importe le programme exécuté.

**CPU Pipelines :** [https://passlab.github.io/CSE564/notes/lecture05_Pipelining.pdf](https://passlab.github.io/CSE564/notes/lecture05_Pipelining.pdf "https://passlab.github.io/CSE564/notes/lecture05_Pipelining.pdf") Technique utilisé dans la conception des processeurs pour effectuer rapidement des instructions. Dans NetBurst, trois étapes principales sont utilisées :

- **Front-end :** Il décode chaque instruction et produit des sequences de micro-ops qui représente chaque instructions à l'aide du microcode qui lui dit comment faire.
    - **Analyse des dépendances :** Il check les dépendances entre chaque instructions/µops. Cela l'aide pour définir un ordre d'execution probable.
    - **Analyse des ressources nécessaires à l'instruction :** Il regarde ce que l'instruction a besoin comme ressource pour pouvoir être exécuté. Il peut avoir besoin de registres ou d'unités d'exécutions ou encore des ports mémoires.
    - **Analyse des ressources disponible :** Il regarde quelles sont les ressources disponible ou utilisées. Si une ressources est déjà utilisé par une autre instruction, y'aura peut-être un conflit donc le scheduler doit trouver une solution (à développer mais complexe je crois).
    - Ces micro-ops sont ensuite envoyés dans le Out of Order Core.
- **Out of Order Core :** Il reçoit les micro-ops du front-end. Il doit d'abord stocké l'ordre des µops dans le ROB. On a ensuite
    - **Allocation des ressources à des instructions :** Suite aux analyses, le scheduler va donc attribuer aux ressources libres des instructions. Ca peut être des ports d'exécution, des réservations de registres etc...
    - **Register Renaming :** Y'a parfois des dépendances de données entre les instructions [https://en.wikipedia.org/wiki/Data_dependency](https://en.wikipedia.org/wiki/Data_dependency "https://en.wikipedia.org/wiki/Data_dependency") :
        - **True dependency RAW (Read after write) :** Quand une instruction dépend du résultat d'une autre instruction. Exemple : A = 3; B = A; B est dépendant de A en True dependency. Les deux instructions ne peuvent donc pas être exécuté en meme temps.
        - **Anti-dependency WAR (Write after read) :** C'est un peu bizarre celle-ci. En gros, c'est quand une données est utilisé alors qu'elle sera changé apres. Exemple pour simplifier : B = 3; A = B+; B=7; l'instruction 2 est anti-dependente de la 3 car on ne peut pas les executer en meme temps. Si on les execute en meme temps, B pourrai d'abord prendre la valeur 7 et donc changer ce qu'aurai du contenir A. Autre exemple : MUL R3,R1,R2;     ADD R2,R5,R6;   on multiplie r1 par r2, on stocke dans r3
        - **Output dependency WAW (Write after write) :** Quand deux instructions successive stocke le résultat dans le même endroit. Exemple : ADD r1,r2,r3;     SUB r1, r4,r5;     Si on execute en meme temps, le résultat ne sera pas le meme en fonction duquel sera fini en premier.
        - Le scheduler analyse alors ces dépendences et créer des registres virtuels (des copies de registres) qui pourrais causer des conflits de dépendences.
    - **Dispatchement des instructions dans les ports d'exécution :** Grâce aux types d'opérations de l'instruction, le scheduler va savoir vers quel port envoyer chaque instructions.
    - Ensuite, les µops sont envoyées dans les ports d'exécution grâce au scheduleur. Le but est d'utiliser les ressources du proco le plus aggressivement possible pour avoir un bon parallèlisme. Quand le code est bien optimisé, le proco peut émettre plusieurs micro-ops par clock-cycle.
- **Retirement section :** Il s'assure que l'ordre final dans lequel les instructions sont rendus est correct. Il se sert du ROB (Reorder Buffer) pour remettre en ordre les résultats données par les ports d'exécutions. Il va ensuite les renvoyer dans l'architecture externe du processeur. C'est donc la toute dernière étapes dans ce pipeline.

**ROB (Reorder Buffer) :** Cache externe du pipeline (comme le ROM) qui stocke l'ordre des µops qu'ils reçoit du Front-end. L'ordre des µops sont donc toujours dans l'ordre du machine code. Cela permet au retirement section de ranger (comiter) grâce au ROB les résultats des µops rendus par les ports d'exécution dans l'ordre du machine code. L'architecture externe (juste après le retirement section) n'a donc pas besoin de s'occuper de l'ordre des résultats.

**Scheduler :** Composant entre les ports d'execution et le stockage de µops dans le ROB. Il se charge de dispatcher les µops dans les ports d'executions correspondants.

Les 4 ports de NetBurst :  
![[Pasted image 20250120214831.png]]

Port 0 et 1 ont tout les deux ALU (arithmetic logical units) ce qui permet d'effectuer 4 opérations par clock cycle (2 par ALU)

Y'a également un problème avec ce système. Quand on est dans des boucles et qu'on ne sait pas si une condition est respecté ou alors pas à temps, ca réduit les performences. On utilise donc des stratégie de prédictions pour essayer de prédire des conditions : (chat gpt) ^bfdc75

1. **Prédiction statique :** La prédiction est basée sur des informations statiques, telles que la disposition du code ou des modèles simples. Par exemple, on pourrait toujours prédire que les branches sont prises ou non prises en fonction de la tendance historique.
    
2. **Prédiction dynamique :** La prédiction est basée sur des informations en temps réel et peut être ajustée au fil du temps. Les processeurs utilisent souvent des compteurs de branchement (branch counters) pour suivre l'historique récent des branches et ajuster leur prédiction en conséquence.
    
3. **Prédiction par saut indirect :** Certains sauts sont indirects, ce qui signifie que la cible du saut n'est pas immédiatement évidente. Les stratégies de prédiction pour les sauts indirects peuvent utiliser des tables de correspondance (tables de branchement indirect) pour prédire la cible probable.
    
4. **Prédiction basée sur le contenu (Content-Based Prediction) :** La prédiction est basée sur le contenu des registres ou de la mémoire. Par exemple, si une variable indique la direction probable d'un saut, la prédiction peut en être basée.
    
5. **Prédiction par extrapolation :** Certains processeurs utilisent des modèles complexes qui tentent d'extrapoler le comportement futur des branches en fonction de l'historique passé.
    

**Virtual Memory** : C'est un concept très important dans les os pour acceder au données en mémoire. Il utilise une (ou plusieurs pour avoir différent niveau, à clarifié) page table pour faire la liaison entre la mémoire physique et le programme. Le programme va se servir d'adresse virtuelles pour acceder à des données physiques. En fait, les adresses virtuel contiennent rien, c'est juste une sorte de pointeurs vers une adresse physique (qui peut etre sur la ram ou sur le disque). Chaque programme sera indépendant puisqu'ils auront tous leur propre table de page qui vont toute commencé à la même adresse puisque c'est juste une template en fait. Les programmes n'ont donc pas à se soucier des adresses physique qui sont libre ou non, ca sera le rôle du virtual memory.

[https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/9_VirtualMemory.html](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/9_VirtualMemory.html "https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/9_VirtualMemory.html")  

Il utilise à la fois la ram (pour stocker les pages actives) et la partition swap (pour stocker les pages inactives).

On a + de place (page) virtuelles que de place physique. Ca s'explique par le fait que la mémoire virtuel c'est vu du coté du programme. Le programme ne fait pas la différence entre le swap et la ram, il s'en fout. Donc la mémoire virtuel contient sans distinction les pages qui sont dans le swap et dans la ram. Alors que par "places physique", on veut dire les places dans la ram (même si le swap c'est quand même physique aussi).

**Mémoire swap :** C'est une partition dans le disque qui contient les pages inactives quand elles étaient dans la ram. En fait, la ram manque parfois de place donc on va dégager la page la plus vieille (grâce à une info de la page, [https://people.kth.se/~johanmon/courses/id2206/lectures/swapping-handout.pdf](https://people.kth.se/~johanmon/courses/id2206/lectures/swapping-handout.pdf "https://people.kth.se/~johanmon/courses/id2206/lectures/swapping-handout.pdf")) dans la partition de disque swap. On va donc la remplacer dans la ram par la nouvelle page. L'adresse virtuelle de la page envoyé dans le swap va donc changer car la page aura bougée.

**Page table :** C'est un tableau qui va lier une page de la mémoire virtuel (que le programme va demander) à une page de la mémoire physique (RAM). Pour chaque page, y'a d'autre informations optionnels :

- **Bits de présence :** Si bit à 1, la page est présente en mémoire physique. Si 0, la page est dans le swap
- **Bits de protection :** Y'a 3 bits : la lecture, l'écriture et l'exécution. Quand ils sont à 1, les permissions sont accordées.
- **Dirty bit (à pas confondre avec dirty grosse bite ou dirty tomy) :** Quand la page est chargé en mémoire, il est à 0 car pas modifié. Si il est modifié (suite à une écriture dans la page par exemple), il est mit à 1. C'est utile dans le cas où y'a plus de place donc on swap en priorité les pages avec le dirty bit à 1 car y'a peut-être des données importante qui ont été modifié. On l'écrit donc dans le swap pour un peu plus de permanence.
- **Caching (à développer) :**
- **Bits de référence (à développer) :**

**Page :** C'est l'ensemble des adresses dans une intervalle. En général, une page contient une suite de 4096 adresses. Une page virtuelle correspond à une page mémoire (dans la ram ou dans le swap) mais qui n'est pas forcément à la meme adresse. Par exemple, une page virtuelle à l'adresse virtuelle 0x00000000 peut faire référence à l'adresse physique en ram 0x10000000. C'est tout le principe du virtual memory.

**Composition d'une adresse virtuel :**

- **Virtual page number :** Numéro de la page virtuel que l'on veut acceder pour recuperer la page physique.
- **Offset :** C'est l'endroit exacte qui est relatif à la page que l'on veut toucher. C'est pour se reperer dans la page virtuelle et physique : il ne change pas dans le processus virtuel->physique donc il ne passe pas par le page table.
![[maxresdefault.jpg]]


**Page fault :** C'est le truc qui ne doit jamais arriver car ça cause un retard de fils de pute. Quand une page physique n'est pas dans la ram, ça veut dire qu'elle est dans le swap. On déclenche donc un page fault. On va donc chercher la page dans le swap, la remettre dans la ram puis redemander si la page est dans la ram. C'est ce processus qui est très long.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/0f4d81bb2c21fc1ceba8aece1324f8d1.png)

**Translation lookaside buffer (TLB) :** [https://en.wikipedia.org/wiki/Translation_lookaside_buffer](https://en.wikipedia.org/wiki/Translation_lookaside_buffer "https://en.wikipedia.org/wiki/Translation_lookaside_buffer") C'est un cache mémoire qui contient les translations réçentes d'adresse virtuel vers adresse physique. Avant de parcourir le page table, on va d'abord check dans le TLB pour voir si l'adresse virtuelle est dedans. Si elle y est (TLB hit), on gagne du temps à mort car on va direct vers l'adresse physique du coup. Si elle n'y est pas (TLB miss), on va donc parcourir le page table. On va ensuite charger l'adresse physique correspondante dans le TLB cache. Si y'a plus de place dans le TLB, on dégage l'entrée la plus vieille et on met le nouveau à la place. Dans le cache TLB, on a un tag (adresse virtuelle) qui correspond à une adresse physique, comme le page table.

C'est un cache mémoire qui doit être très petit pour être performent.

## **Windows Reversing**

**Working sets :** C'est l'ensemble des pages mémoire physique (ram) qui sont actuellement utilisés par un processus/programme. Ca aide le systeme pour determiner quelles sont les pages à foutre dans le disque.

Kernel Memory : On veut pas que les programmes puissent acceder à la mémoire du systeme ce qui est normal pour des questions de sécurité. On sépare donc la ram en deux partie. La mémoire kernel occupe souvent entre 1 et 4go.

User Memory :

Processus initialisation programme pour reversing :  
Creation grace a l'api win Createprocess  
Check ca [https://renenyffenegger.ch/notes/Windows/development/process/index](https://renenyffenegger.ch/notes/Windows/development/process/index "https://renenyffenegger.ch/notes/Windows/development/process/index")  
Allocation mémoire

On map le fichier NTDLL.DLL qui contient les fonctions du kernel (check ce que c'est psk la peut pas)

Create process utilise le premier thread et fout une stack dedans pour charger les processus

On lance la fonction lrdpinitialize dans ntdll.dll

00


## **Linux Reversing**

#### Intel Architecture 32 bits

**Couche mémoire d'un programme :**
- ![[Pasted image 20240217113519.png]]

**Stack :** 
![stack-memory-architecture-1-768x802.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/2936dd05ba0b4efbde985c4debce2a8c.png) ^01daaf
- La stack est en Last in first out (LIFO)

**Heap ou tas :**
https://gist.github.com/AdamGold/5053eea2ba05867caa55dcc43d9bc560
- C'est un espace mémoire pour les données dynamiques, qui change de taille ou autre. À la différence des valeurs de la stack, les variables sont accessibles globalement, on peut changer leur dimension, on doit gérer la mémoire et l'efficacité n'est pas garantie. Par exemple, si on libère un bloc mémoire entre deux autres blocs, la mémoire sera fragmentée.
- Il est utilisé souvent pour les objets de structure car ils changent, peuvent ne pas avoir certains paramètres, peut prendre beaucoup de place...
- L'allongement de mémoire se fait vers les adresses hautes, vers la stack.
- Le heap est bien défini dans la description de malloc() en C.
- Le heap se compose de chunk divisé en "2" partie et sont différent en fonction de s'ils sont alloués ou libres :
	- **Chunk alloués :**
		- **Les meta-data** dans lesquelles sont stockées plusieurs informations concernant l'espace alloué (dans l'ordre):
			- La taille du précédent chunk dans la mémoire s'il est libre pour permettre de retrouver facilement les chunks libres.
			- La taille du chunk actuel en bytes (meta-data comprises).
		- **Les données stockées.**
```
    chunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		    |             Size of previous chunk, if unallocated (P clear)  |
		    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		    |             Size of chunk, in bytes                     |A|M|P|
      mem-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	  	    |             User data starts here...                          .
	  	    .                                                               .
	  	    .             (malloc_usable_size() bytes)                      .
	  	    .                                                               |
nextchunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		    |             (size of chunk, but used for application data)    |
		    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		    |             Size of next chunk, in bytes                |A|0|1|
		    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
- `
	- **Chunk libres :**
		- C'est pas vraiment divisé en partie étant donné qu'il n'y a pas de données stockées. 
		- On a d'abord la taille du précédent chunk seulement s'il est libre. On sait s'il est libre avec le lowest bit qui l'indique (s'il est sur P, PREV_INUSE, le précédent est libre)
		- La taille du chunk actuel.
		- Un pointeur vers le prochain chunk 
		- Un pointeur vers le précédent chunk
		- L'espace inutilisé qui peut être égal à 0
		- La taille du chunk actuel
		- La taille du prochain chunk.
```
    chunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		    |             Size of previous chunk, if unallocated (P clear)  |
		    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	`head:' |             Size of chunk, in bytes                     |A|0|P|
      mem-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	  	    |             Forward pointer to next chunk in list             |
	  	    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	  	    |             Back pointer to previous chunk in list            |
	  	    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	  	    |             Unused space (may be 0 bytes long)                .
	  	    .                                                               .
	  	    .                                                               |
nextchunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    `foot:' |             Size of chunk, in bytes                           |
    	    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    	    |             Size of next chunk, in bytes                |A|0|0|
    	    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**BSS :**

- C'est comme le segment de données sauf que c'est pour les données non initialisées. Donc par exemple un `int global_var;` hors des fonctions. En fait c'est souvent utile car les données qui sont dedans sont directement initialisées à 0 pas comme dans la stack où elles ont une valeur random. Ça permet aussi d'économiser de la place dans la mémoire.

**Segment de données :**

- C'est un segment de données constants qui stockent justement les  données constantes et initialisées. Ça peut être des variables globales (hors des fonctions) ou statiques (avec le type static). La taille est prédéfinie avant l'exécution du programme étant donné qu'on les change pas.

**Text :**

- C'est là où sont contenu les instructions en langage machine.
- Entre chaque instructions, il se passe ça :
	- 1. Lire l'instruction indiquée par EIP/RIP
	- 2. Additionne la taille en octets de l'instructions à EIP/RIP
	- 3. Exécuter l'instruction lue à l'étape 1
	- 4. Retour à l'étape 1
