
##### join
C'est pour concaténer des strings.
Exemple :
```python
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) # va afficher John#Peter#Vicky
```

```python
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
### Pour dégager toute les voyelles (sans compter le y parce que codewars sont teubés)
```

##### sorted
Pour trier les listes, tuples ou dictionnaires

Syntaxe :
`sorted(iterable, key=key, reverse=reverse)`
Pour key, on peut mettre une fonction et par conséquent, l'ordre dépendra de la valeur retourné par la fonction. On pourrait mettre `key=len` par exemple.
