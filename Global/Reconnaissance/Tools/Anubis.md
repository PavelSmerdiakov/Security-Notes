**Anubis **

Pourquoi l'utiliser ? Il est sympatoche et rapide à prendre en main. Pas forcément très complexe mais sympa en cas de besoin rapide.

**Flag :**

```
  -h --help                       show this help message and exit

  -t --target                     set target (comma separated, no spaces, if multiple)

  -f --file                       set target (reads from file, one domain per line)

  -n --with-nmap                  perform an nmap service/script scan (bug ?)
  -o --output                     save to filename

  -i --additional-info            show additional information about the host from Shodan (requires API key (non))

  -p --ip                         outputs the resolved IPs for each subdomain, and a full list of unique ips

  -a --dont-send-to-anubis-db     don't send results to Anubis-DB
  -r --recursive                  recursively search over all subdomains

  -s --ssl                        run an ssl scan and output cipher + chain info

  -S --silent                     only out put subdomains, one per line

  -w --overwrite-nmap-scan SCAN   overwrite default nmap scan (default -nPn -sV -sC)

  -v --verbose                    print debug info and full request output

  -q --queue-workers NUM          override number of queue workers (default: 10, max: 100)

  -V --version                       show version and exit
```

Commande coolos :

```
anubis -t target.com -piv

anubis -t target.com --with-nmap -o temp.txt -i --overwrite-nmap-scan "-F -T5" -vp
```

La commande simple --with-nmap bug donc utilise --overwrite-nmap-scan à chaque fois.