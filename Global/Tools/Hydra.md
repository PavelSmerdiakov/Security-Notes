Description :

Programme de brute force efficace grâce au nombre de services sur lesquelles on peut l'utiliser.

N.B. : Les flags qu'on utilise dépendent du protocole que l'on vise. Les flags ne seront pas forcément les mêmes pour ssh que pour ftp.

SSH :  
`hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh`  
Flags :  
-l : noms d'utilisateur  
-P : mot de passe a tester. Ca peut être une wordlist ou juste un mot de passe  
-t : Nombre de threads parallèlement utilisés  
-q : mode silencieux, pas d'affichage d'erreurs  
-v : verbose mode  
-c (time) : spécifie le temps de pause après chaque tentatives

-f :  quitte après avoir trouver une combinaison correctes. Utile quand on a plusieurs nom d'utilisateurs mais qu'on en veut juste un de la liste, peu importe lequel.

-o (file) : spécifie le fichier où mettre les combinaisons correctes.  
-b : spécifie le type de fichier de l'option -o (fichier json, txt...)

-C (file) : Utilise a la place de l'option -l et -P, un fichier avec des combinaisons précises de format login:pass.

-s (port) : spécifie le port cible dans le cas où le service est sur un autre port que celui par défaut.

-R : restorer une session précédentes en cas de crash ou autres.  
-x MIN:MAX:CHARSET :  
MIN : minimum de caractère de mot de passe  
MAX : maximum de caractère de mot de passe

CHARSET : spécification de caractère à utiliser dans le mot de passe sachant que dans hydra :

a = mot de passe avec uniquement des minuscule  
A = mot de passe avec uniquement des majuscule  
1 = uniquement des chiffres

et pour les autres, ajouter leur représentation comme le montre les exemples ci-dessous.

Exemples :  
-x 3:5:a  generate passwords from length 3 to 5 with all lowercase letters

-x 5:8:A1 generate passwords from length 5 to 8 with uppercase and numbers

-x 1:3:/  generate passwords from length 1 to 3 containing only slashes

-x 5:5:/%,.-  generate passwords with length 5 which consists only of /%,.-

-x 3:5:aA1 -y generate passwords from length 3 to 5 with a, A and 1 only

`sudo hydra admin passwords.txt 192.168.1.100 http-post-form "/login:username=admin&password=^PASS^:F=incorrect"`

admin : utilisateur à brute force  
http-post-form : Pour indiquer qu'on veut brute force une page web en  post.

/login : **PIÈGE ATTENTION** : ca désigne la page /login (le path) non pas le fait qu'on mette les logins juste derrière.

F=incorrect : met le toujours car je crois que si tu met juste incorrect sans la variable ca fait bugger.