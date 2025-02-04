En gros c'est parce que ca a créer une petite partition donc faut le retirer et la remplacer :
- `sudo fdisk -l`
- `sudo fdisk /dev/sdc1`
- `d`
- `n` et tu suis le truc par défaut.
- `w`
- `mkfs.ntfs /dev/sdc1`
