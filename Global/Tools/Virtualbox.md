**Pour connecter une vm à Metasploitable 2 en Host-only : **

Pour connecter Metasploitable 2 et Kali Linux en utilisant VirtualBox avec un adaptateur réseau en mode "host-only", suivez ces étapes :

1. **Créer un réseau "Host-Only"** : Assurez-vous d'abord que vous avez créé un réseau "Host-Only" dans VirtualBox. Pour ce faire, suivez ces étapes :
    
    - Ouvrez VirtualBox.
    - Allez dans "Fichier" (File) > "Préférences" (Preferences).
    - Dans la fenêtre des préférences, cliquez sur "Réseau" (Network) dans le volet de gauche.
    - Sous l'onglet "Hôtes uniquement" (Host-Only), cliquez sur le bouton "+" pour ajouter un nouvel adaptateur.
    - Cela créera un nouvel adaptateur réseau "VirtualBox Host-Only Ethernet Adapter".
2. **Configurer les adaptateurs réseau des machines virtuelles** : Maintenant, configurez les adaptateurs réseau de vos machines virtuelles comme suit :
    
    - Pour Metasploitable 2 :
        - Sélectionnez votre machine virtuelle Metasploitable 2 dans VirtualBox.
        - Cliquez sur "Configuration" (Settings).
        - Allez dans la section "Réseau" (Network).
        - Pour "Adaptateur 1" (Adapter 1), sélectionnez "Attaché à : Adaptateur réseau hôte" (Attached to: Host-only Adapter).
        - Dans le champ "Nom" (Name), choisissez l'adaptateur "VirtualBox Host-Only Ethernet Adapter" que vous avez créé.
    - Pour Kali Linux :
        - Sélectionnez votre machine virtuelle Kali Linux dans VirtualBox.
        - Cliquez sur "Configuration" (Settings).
        - Allez dans la section "Réseau" (Network).
        - Pour "Adaptateur 1" (Adapter 1), sélectionnez "Attaché à : Adaptateur réseau hôte" (Attached to: Host-only Adapter).
        - Dans le champ "Nom" (Name), choisissez le même adaptateur "VirtualBox Host-Only Ethernet Adapter" que pour Metasploitable 2.
3. **Configurer les paramètres IP** : Maintenant, dans les machines virtuelles, vous devrez configurer les paramètres IP manuellement pour qu'elles puissent communiquer entre elles. Voici comment le faire :
    
    - Pour Metasploitable 2 :
        - Ouvrez un terminal sur Metasploitable 2.
        - Éditez le fichier de configuration réseau avec la commande :

5. Assurez-vous que votre configuration ressemble à ceci :
    

- Enregistrez et fermez le fichier.
    

1. Pour Kali Linux :

- Ouvrez un terminal sur Kali Linux.
- Éditez le fichier de configuration réseau avec la commande :

2. ## Assurez-vous que votre configuration ressemble à ceci :
    
    - Enregistrez et fermez le fichier.
3. **Redémarrez les machines virtuelles** : Redémarrez les deux machines virtuelles pour que les nouvelles configurations réseau prennent effet.
    

** Quels type de réseau choisir ? : **

**NAT : **

La vm accède à internet via la même connexion que l'hôte. Donc la vm n'aura pas d'adresse ip et ne sera pas connecté au réseau. Les machines du réseau local ne pourront pas lui parler. Mais par exemple, si tu lance un server http sur la vm au port 443, bah quand on accedera à l'adresse ip de l'hôte avec le port 443, on tombera sur le server lancé par la vm.

**Réseau NAT : **

Un réseau NAT on l'utilise quand on veut connecter plusieurs vm sur un même réseau. Par défaut, le NAT ne permet pas de faire communiquer plusieurs vm donc on va créer un réseau.

Pour créer un réseau NAT sur virtualbox, on va dans File -> Tools -> Network Manager -> Nat Networks et là tu créer un réseau. Pense bête : n'oublie pas d'activer le DHCP hein.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/179d6aabfe6837b78b7d71912fe93d64.png)  
**Bridged :**

Dans ce cas là, la vm sera comptée comme une machine physique sur le réseau donc elle aura adresse mac, ip etc. Elle pourra contacter les autres machines sur le réseau local.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/f6ad84e785cb8995b6f1740d31cb95ee.png)  
**Host-Only :**

Cette fois-ci, elle sera sur son propre réseau coupé d'internet. Donc elle pourra contacter l'hôte physique et les autres vm sur le même réseau mais ne pourra pas parler aux autres machines sur le réseau local physique ni même à internet. Host-Only c'est utiliser généralement quand on fait des tests avec une vm vulnérable comme metasploitable ou quand tu veux tester des malware.

Par contre il faut créer un réseau dans virtualbox mais c'est simple :

Tools-> Host-only Networks -> tu config manuellement ça prend genre 2s tu met juste l'adresse de base [192.168.56.1](http://192.168.56.1 "http://192.168.56.1") ou un truc du genre on s'en fout tfacon e

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/f7ea8453e7748c779f32b4c54e99b878.png)  
**Internal Network :**

C'est un peu comme Host-Only sauf que les communications seront possibles seulement entre les vm qui sont sur le réseau. Le hôte ne pourra pas communiquer avec elles. C'est sympa pour reproduire un vrai réseau sans interferer avec le réseau local. En fait on peut créer un peu ce qu'on veut comme un routeur par exemple (regarde sur internet ca peut etre sympa a savoir faire, ptet une couche d'anonymat possible ?) mais par contre je ne sais pas si c'est possible que le traffic du réseau interne ne passe pas par le réseau local. Je pense pas.

Pour le créer, faut mettre les vm que tu veux sur l'interface internal network. Ensuite, dans un shell (hôte), va dans /usr/lib/virtualbox et execute la commande suivante pour créer un server dhcp avec les infos que tu veux :

- vboxmanage dhcpserver add --network=intnet --server-ip=10.0.2.1 --netmask=255.255.255.0 --lower-ip=10.0.2.2 --upper-ip=10.0.2.10 -enable

Dans le cas où une vm ne se connecte pas, quand j'ai désactivé dans la vm l'interface eth0 (l'interface connectée quoi) puis relancé la vm, ça a marché.

![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/900977a0d9fc0001ded96036b3976fe0.png)![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/4695d239aa8a5341ebb17c10954b6223.png)

**Résumé : **  
![image.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/1033a52056f6dc6e36d5f6759a514eb7.png)