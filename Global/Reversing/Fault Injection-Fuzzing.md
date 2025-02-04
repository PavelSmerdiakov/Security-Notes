


# Ça consiste en quoi ?

- Le fault injection consiste à introduire des input qui vont potentiellement rendre des erreurs ou des comportements innattendus. Le fuzzing c'est du fault injection mais pour la rechercher de vulnérabilités.


# Où introduire nos input ?

- Plus où moins partout où on peut :
	- Le filesystem
	- registres
	- variables d'environnement
	- Windows messages
	- LPC port
	- RPC
	- shared memory
	- command-line arguments
	- network input
	- API
	- GUI
	- System entry

# Comment créer son programme de fault-injection ?

- C'est fastidieux mais c'est possible et interéssant. On a beaucoup de facteurs à prendre en compte.


#### Heuristiques :
- L'heuristiques c'est la science de communiquer et de regarder les réponses afin d'éduquer le communicator (le programme en gros). Ça relève plus ou moins de l'intelligence artificielle mais y'a des moyens un peu plus simples de l'implémenter.
	- On peut par exemple analyser les réponses et dès qu'on obtient une erreur, on change le comportement du programme. Imaginons qu'on reçoit un "Internal server error", quand notre programme reçoit cette erreur, il devient plus aggressif et augmente la fréquence d'injection. Dès qu'on reçoit une réponse différente ou que la situation change, on reprend notre mode soft.
#### Stateless / State-based Protocols :
- Ça à l'air un peu dur donc à approfondir. En gros quand on audit un stateless protocol, c'est simple car on a juste à analyser le comportant fixe de la cible. Quand on a affaire à un state-based protocol, c'est plus compliqué car la réponse de dépent pas seulement de l'input de l'user.


