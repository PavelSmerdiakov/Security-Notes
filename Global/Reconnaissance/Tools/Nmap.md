![nmap_path_scan.jpg](file:///home/wpkaliuser/.config/joplin-desktop/resources/f319bb4717014abe9c0bcf8a8037e5f0.jpg)

Découvrir les hôtes en ligne :

nmap -sp target

Port scan :

- nmap -sS target SYN scan
- nmap -sU UDP scan
- nmap -sT TCP connect scan
- nmap --top-ports 20 target scan les 20 ports les plus populaire

OS scanning :

- nmap -O target

Output file :

- -oN output.txt

Changer d'user-agent :
- C'est pour que 
- --script http-useragent-tester.nse
- Dans le fichier, faut remplacer soit le wget, soit le mechanizc (un truc comme ca)
