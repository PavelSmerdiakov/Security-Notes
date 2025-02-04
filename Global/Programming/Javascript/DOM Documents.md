document.getElementById("monBouton").onclick = () => {  
    alert("Le bouton a été cliqué !");  
}; pour executé du code après un évènement.

---

evenement : more here : [https://www.w3schools.com/jsref/dom_obj_event.asp](https://www.w3schools.com/jsref/dom_obj_event.asp "https://www.w3schools.com/jsref/dom_obj_event.asp")  
![Screenshot_2023-08-23_18_09_24.png](file:///home/wpkaliuser/.config/joplin-desktop/resources/afd3c729bb5a200a2a5e12523e023c43.png)

---

Modifier un element html :

|Property|Description|
|---|---|
|_element_.innerHTML =  _new html content_|Change the inner HTML of an element|
|_element_._attribute = new value_|Change the attribute value of an HTML element|
|_[element](http://element.style.property "http://element.style.property")_[.style.](http://element.style.property "http://element.style.property")_[property](http://element.style.property "http://element.style.property") = new style_|Change the style of an HTML element|
|Method|Description|
|_element_.setAttribute*(attribute, value)*|Change the attribute value of an HTML element|

setattribute fait comme _element_.*attribute = new value. *Je trouve juste la methode un peu plus rapide.

innerHTML c'est le contenu d'un élément.

---

Ajouter ou dégager un élément html :

|Method|Description|
|---|---|
|document.createElement(_element_)|Create an HTML element|
|document.removeChild(_element_)|Remove an HTML element|
|document.appendChild(_element_)|Add an HTML element|
|document.replaceChild(_new, old_)|Replace an HTML element|
|document.write(_text_)|Write into the HTML output stream|

---

désigner les éléments html grace au dom :

|Property|Description|DOM|
|---|---|---|
|document.anchors|Returns all [elements that have a name attribute](#)|1|
|document.applets|Deprecated|1|
|document.baseURI|Returns the absolute base URI of the document|3|
|document.body|Returns theelement|1|
|document.cookie|Returns the document's cookie|1|
|document.doctype|Returns the document's doctype|3|
|document.documentElement|Returns theelement|3|
|document.documentMode|Returns the mode used by the browser|3|
|document.documentURI|Returns the URI of the document|3|
|document.domain|Returns the domain name of the document server|1|
|document.domConfig|Obsolete.|3|
|document.embeds|Returns all elements|3|
|document.forms|Returns all elements|1|
|document.head|Returns theelement|3|
|document.images|Returns all  elements|1|
|document.implementation|Returns the DOM implementation|3|
|document.inputEncoding|Returns the document's encoding (character set)|3|
|document.lastModified|Returns the date and time the document was updated|3|
|document.links|Returns all and [elements that have a href attribute](#)|1|
|document.readyState|Returns the (loading) status of the document|3|
|document.referrer|Returns the URI of the referrer (the linking document)|1|
|document.scripts|Returns all elements|3|
|document.strictErrorChecking|Returns if error checking is enforced|3|
|document.title|Returns the|