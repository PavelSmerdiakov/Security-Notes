---
share_link: https://share.note.sx/rlmmahs2#dEJf8mXyFkoh6vJ8kzRvVHi56LDfX7wMckXidtOEf3k
share_updated: 2024-11-25T22:05:38+01:00
---
### threading

- Créer un thread
	- `t1 = threading.Thread(target, args)`
	- avec target ce qu'on veut exécuter et args les arguments qu'on lui passe
	- Exemple :
		- `t1 = threading.Thread(target=print, args=("bonjour",))
- Démarrer un thread
	- `t1.start()`
- Fermer un thread lorsqu'il a terminé sa tâche
	- `t1.join()`
- Voir l'id du thread principal
	- `threading.main.thread()`
- Voir l'id du thread actuel
	- `threading.current.thread()`

### logging


### unittest
![[Pasted image 20241116213547.png]]
Exemple :
```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

import unittest
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius  

class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)  
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(-40), -40)

if __name__ == "__main__":
    unittest.main()
```
### concurrent.futures
Module pour les thread pools
```python
import concurrent.futures

def worker():
    print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
```
### requests
Faire une requête GET et voir le status code :
```python
headers = {'User-Agent': 'my-app/0.0.1'}
params = {'userId':1}
response = requests.get("https://www.w3schools.com/python/ref_func_all.asp", params=params, headers=headers)
print(f"Status Code : {response.status_code}")
```

Faire une requête POST et voir le status code :
```python
data = {'title': "foo", 'body': 'bar', 'userId':1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(f"Status Code: {response.status_code}")
```

Chopper par les bretelles les données json si le site en renvoie :
```python
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json() #A noter de data est un tableau rempli de dictionnaire
```

Mettre un timeout :
```python
try:
	response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5)
	print(response.json())
except requests.exceptions.Timeout:
	print("La requête a expiré)
```

Utilisation d'authentification :
```python
from requests.auth import HTTPBasicAuth
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
```

Télécharger un fichier via HTTP :
```python
response = requests.get("https.www.example.com/image.jpg")
with open("image.jpg", "wb") as file:
	file.write(response.content)
```

Créer une session de requête pour conserver la même connexion TCP :
```python
with requests.Session() as session:
    response = session.get('https://jsonplaceholder.typicode.com/posts')
    print(response.json())
```
### json
Pour convertir des chaînes JSON (reçues par exemple d'une API) :
```python
json_str ='{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_str)
print(data)
print(type(data))
```
Et l'output sera :
```python
{'name': 'John', 'age': 30, 'city': 'New York'}
<class 'dict'>
```

Pour convertir un dictionnaire python en chaîne JSON :
```python
data ={"name": "John", "age": 30, "city": "New York"}
json_str = json_dumps(data)
json_str = json_dumps(data, indent=4, sort_keys=True) # Pour un bon formatage (ne pas confondre avec fromage), indent c'est bon j'explique pas ça ntm et sort_keys=True c'est pour trier par ordre alphabétique.
```


### socket
Programme simple de création de connexion :
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",12345))
s.listen(5) #liste d'attente de 5 personne au max
print("Serveur prêt")
conn, addr = s.accept() #conn c'est le socket qui gère à présent la connexion pour que s puisse continuer de recevoir les demandes. addr contient des infos sur cette connexion.
print(f"Connexion établie avec {addr}")
conn.sendall(b"salut pedale")
data = conn.recv(1024) # Le programme est mis en pause temps qu'aucune donnée n'est reçue
print(f"Message reçu : {data.decode()}")
conn.close()
```