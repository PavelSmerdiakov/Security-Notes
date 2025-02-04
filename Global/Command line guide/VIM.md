Dans le tool :

- Voir la page d'aide : :h
- Quitter et enregistrer : :qw ou :x
- Quitter sans enregistrer : :q!
- Mettre en suspend une session vim : Ctrl + Z, pour revenir dedans à partir du shell, tu peux faire fg.
- Insérer : i
- Insérer en fin de ligne : A
- Insérer une nouvelle ligne : o
- Retour en arrière : u
- Supprimer le caractère en dessous du curseur : x
- Supprimer une ligne : dd
- Séléctionner texte en mode visuel : v puis se déplacer avec curseur ou h,j,k,l
- Mouvement :
    - Début de ligne : ^ (appuie 2 fois)
    - Fin de ligne : $
    - Début du prochain mot : w
    - Fin du prochain mot : e
    - Répéter une action plusieurs fois : 3w pour aller 3 fois au début du prochain mot

Dans le shell :

- Substituer toute les occurences d'un mot avec un autre : vim +%s/ancien/new/g prout.txt
- On peut aussi mettre : vim -c %s/ancien/new/g prout.txt
- Ouvrir n fenêtre en horizontale (changer le o en 0 pour verticale) : vim -on file1.txt file2.txt