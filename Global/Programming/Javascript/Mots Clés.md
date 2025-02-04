Ajouter le contenu d'un autre site : balise

innerHTML : C'est le contenu d'un élément HTML. Exemple :

"Bonjour"

. Si dans jvscript on veut récupérer le contenu : const myelement =  document.getelementbyid("word").innerHTML

déclaration d'un objet : const car = {type:"Fiat", model:"500", color:"white"}; Pour accéder à une valeur, _objectName["propertyName"] ou objectName.propertyName_

Pour déclarer un objet sans mettre de paramètre et en spécifiant le type, x = new String();        // Declares x as a String object

Executer quelque chose après un évènement :   VIEUX : <_element_  _event_=**"_some JavaScript_"**>. Par exemple : The time is?. Ca ajoutera la date en dessous. Si on veut remplacer le "The time is?", on  utilise this : The time is?

Meilleur méthode :

```JS
document.getElementById("monBouton").onclick = () => {
    alert("Le bouton a été cliqué !");
};
```

doit être utilisé dans un bloc javascript (plus pratique que de mettre le code a executé directement dans la balise). On peut remplacer () => par function() mais c'est moins recommendé. Y'A JAMAIS RIEN DANS LES PARENTHESES.

![Screenshot_2023-08-23_18_09_24.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/afd3c729bb5a200a2a5e12523e023c43.png)  
more here : [https://www.w3schools.com/jsref/dom_obj_event.asp](https://www.w3schools.com/jsref/dom_obj_event.asp "https://www.w3schools.com/jsref/dom_obj_event.asp")

Map (tableau avec key-value) : ``const fruits = new Map([["apples", 500],["bananas", 300],["oranges", 200]]); Si je fais fruits.get("apples");`` ca va renvoyer 500

les backstick `` servent comme des "" mais avec plus de fonctionnalité :

```JS
const name = "Alice";
const message = `Hello, ${name}!`;
```

NE PAS CONFONDRE LA SYNTAXE D'UN OBJET JSON AVEC LA SYNTAXE D'UN OBJET JAVASCRIPT

Javascript : name = "value"  
Json : "name" = "value"

![Screenshot_2023-08-23_18_09_24.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/4545e73ac239728e0549fac0d11dfb9f.png)