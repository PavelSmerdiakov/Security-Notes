Description :

Exécute simplement des programmes ou fichiers a des moments précis et avec des intervalles.

![](https://github.com/PavelSmerdiakov/Security-Notes/blob/main/Pasted%20image%2020250204175252.png)

Si tu fait cat /etc/crontab, tu peux voir quelles sont les tâches qui s'exécute. Tu vois aussi le path (PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin dans mon cas) c'est là où il va chercher les programmes. par exemple si il cherche un programme, il va d'abord regarder dans home/user puis /usr/local ...

Vulnérabilité :

Si tu vois une tâche qui exécute un programme dans /usr/local/bin qui s'appelle bonjour par exemple, tu peux créer le même fichier dans /home/user mais avec ce que tu veux dedans car il regardera d'abord dans /home/user et s'il le trouve, il l'exécute.
