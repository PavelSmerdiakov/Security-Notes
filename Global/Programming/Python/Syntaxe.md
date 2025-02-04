---
share_link: https://share.note.sx/o61e0399#+ukd+BpK050umRuASHqAEIabzFHvOuhfsQh/3vFd9Qs
share_updated: 2024-11-25T22:05:23+01:00
---
## Structure du code

#### Structure du main
 Afin d'éviter que les importations du script dans d'autre programme ne lance le code, on utilise la fonction main comme ceci :
 ```python
import sys  
import itertools  
 
def my_function():  
    """Do that thing"""  
    print("Hello world!")  
  
def my_main_function():  
    """My main function"""  
    print("Calling my function")  
    my_function()  
    print("Ending the script")  
  
if __name__ == "__main__":  
    my_main_function()
 ```

#### Structures de boucles

- Exemple de boucle for en une unique ligne :
```python
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
```
- Retourne une liste qui indique si un nombre entre 1 et 10 est premier ou non
```python
z = [all(x % i != 0 for i in range(2, x)) if x > 1 else False for x in range(1, 11)]
```

## Type de données

##### Tips je ne sais pas où les foutres
- Pour transformer un élément en tuple :
```python
a = (42)
b = (42,)
print(type(a)) # int
print(type(b)) # tuple
```
- **Unpacking** : C'est pour simplifier l'utilisation de plusieurs valeurs.
- Pour assigner chacun des éléments d'un tuple à une variable (avec utilisation du symbole splat "*") :
```python
a = (1, 2, 3, 4, 5)
x, *y, z = a
-> x = 1
-> y = [2,3,4]
-> z = 5

```

## Fonctions

##### Gestion du surplus d'arguments
On peut utiliser `*args` (args est une convention, tu peux mettre n'importe quel nom) pour les valeurs en trop et `**kwargs` pour les arguments nommés en trop.
Exemple :
```python
def ma_fonction(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

ma_fonction(1, 2, 3, 4, 5, name="Alice", age=30)

# Résultat :
# a: 1
# b: 2
# args: (3, 4, 5)
# kwargs: {'name': 'Alice', 'age': 30}

```

##### Utilisation format de nombres

```python
for i in range(1, 5):
    print(f"Fichier_{i:02}.txt")
```
##### Fonction format pour les strings
C'est pour insérer des éléments dans des placeholders.

##### Listes petites fonctions

**all()**
Retourne True si toute les valeurs d'un tableau sont True
Exemple :
```python
mylist = [True, True, True]  
x = all(mylist) // x = True
```

##### Fonction lambda
Elle permet de créer des minis fonctions qui effectuent une tâches simples sans la complexité d'une vraie fonction.

Syntaxe :
`lambda arguments: expression`

Exemple : 
```python
add = lambda x, y : x + y
```

```python
def move_zeros(array):
	return sorted(array, key=lambda x: not x)
# Pour renvoyer la même liste avec tout les 0 présents à la fin de celle ci
```
