document.write() : En gros pour écrire sur la page ce qu'on met dans les parenthèses. ATTENTION : si on le met après que toute la page est chargé (quand on appuie sur un bounton par exemple), cela écrasera tout puis affichera ce qu'il y a en paramètre.

eval() : Tous ce qu'il y a en paramètre sera exécuter en javascript. Par exemple eval( 1 + 1 ) ca renverra 2

replace() : Remplace l'argument 1 par l'argument 2. Exemple d'utilisation : text.replace("fdp", "beaugosse") Par défaut, si dans la chaine de caractère y'a deux fois ou plus la même string, ça remplace que la première. Si on veut remplacer toute les occurences, on fait /fdp/g

throw : C'est pour lancer une erreur. On peut faire throw 111 pour lancer un argument d'erreur ce qui nous renverra dans la console juste 111. On peut aussi mettre plusieurs arguments mais seulement le DERNIER sera retourné. Si on fait throw 111, 112, 113 on verra juste 113. On peut aussi faire : var prout = 10; throw prout = 11; prout et ca nous renverra 11