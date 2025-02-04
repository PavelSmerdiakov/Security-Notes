C'est un outil coolos pour choper des infos sur des gens avec des pseudos sur pas mal de réseaux (plus de 300 sites)

Y'a pas grand chose à faire mais c'est juste que c'est un outil pour des petites utilisation juste pour voir si un utilisateur existe sur un site/réseau.

Les outputs sont faites automatiquements dans un fichier du même dossier donc mieux vaut le lancer dans un dossier fait pour.

**Commandes :**  
Help menu :

```
positional arguments:

  USERNAMES             One or more usernames to check with social networks. Check similar usernames using {%}

                        (replace to '_', '-', '.').

options:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT

                        If using multiple usernames, the output of the results will be saved to this folder.

  --output OUTPUT, -o OUTPUT

                        If using single username, the output of the result will be saved to this file.

  --tor, -t             Make requests over Tor; increases runtime; requires Tor to be installed and in system path.

  --unique-tor, -u      Make requests over Tor with new Tor circuit after each request; increases runtime; requires

                        Tor to be installed and in system path.
  --csv                 Create Comma-Separated Values (CSV) File.

  --xlsx                Create the standard file for the modern Microsoft Excel spreadsheet (xslx).

  --site SITE_NAME      Limit analysis to just the listed sites. Add multiple options to specify more than one

                        site.
  --proxy PROXY_URL, -p PROXY_URL

                        Make requests over a proxy. e.g. socks5://127.0.0.1:1080

  --json JSON_FILE, -j JSON_FILE

                        Load data from a JSON file or an online, valid, JSON file.

  --timeout TIMEOUT     Time (in seconds) to wait for response to requests (Default: 60)

  --print-all           Output sites where the username was not found.

  --print-found         Output sites where the username was found (also if exported as file).

  --no-color            Don't color terminal output
  --browse, -b          Browse to all results on default browser.
  --local, -l           Force the use of the local data.json file.
  --nsfw                Include checking of NSFW sites from default list.
```

Faire des recherches anonymement au travers de Tor : -t ou --tor  
Ouvrir direct les liens : -b ou --browse