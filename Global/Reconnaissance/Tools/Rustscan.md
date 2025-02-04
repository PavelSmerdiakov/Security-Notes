Description :  
Scan comme nmap mais plus rapide/adaptatif/simple.

Commandes :

alias rustscan='docker run -it --rm --name rustscan rustscan/rustscan:latest'

-a : Spécifier la ou les adresses ip ou hôtes (www.google.com) séparées par une virgule sans espaces ou encore des fichiers txt avec hôte ou adresse dedans.

-p : Spécifier le ports spécifique qu'on veut scanner.

--range : Spécifier la range de port à scanné. Exemple : --range 1-1000

-- : Permet d'exécuter les commandes suivantes dans nmap. Exemple : rustscan -a [127.0.0.1](http://127.0.0.1 "http://127.0.0.1") -- -A -sC va scanner tous les ports de la cible puis exécuter les commandes -A et -sC dans nmap (-A pour détection d'OS, scripts et autres, -sC pour l'exécution de script de base).

--scan-order "Random" : Scan les ports dans un ordre aléatoire (pour échapper au firewall). Y'a random ou sequential mais seq c'est par défaut (du plus petit au plus haut).