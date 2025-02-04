[hacktrick](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/dll-hijacking "https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/dll-hijacking")

[pentestlab](https://pentestlab.blog/2017/03/27/dll-hijacking/ "https://pentestlab.blog/2017/03/27/dll-hijacking/")  
Ordre de recherche des dll dans système 32 bits :

1. The directory from which the application is loaded. C'est l'emplacement de base du fichier oú il est installé. ≠ current directory.
    
2. C:\Windows\System32
    
3. C:\Windows\System
    
4. C:\Windows
    
5. The current working directory. Exemple : si dans un shell on est dans C:\Windows\Program mais que l'app est dans Document, bah le current dir c'est le program.
    
6. Directories in the system PATH environment variable
    
7. Directories in the user PATH environment variable
    

Tools :

Procmon from sysinternals :  
Pour rechercher les dll qui manque sur le system