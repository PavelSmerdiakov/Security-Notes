- AJAX sert à changer un élément d'une page sans la recharger entierement. Il sert de communication entre le server web et le document. Exemple concret :

Change Content            //création d'un bouton qui appelle la fonction loadDoc() quand on clique

Les fonctions d'object pour ajax :                                                    Les propriétés pour ajax :

|Property|Description|Method|Description|
|---|---|---|---|
|onload|Defines a function to be called when the request is received (loaded)|new XMLHttpRequest()|Creates a new XMLHttpRequest object|
|onreadystatechange|Defines a function to be called when the readyState property changes|abort()|Cancels the current request|
|readyState|Holds the status of the XMLHttpRequest.  <br>0: request not initialized  <br>1: server connection established  <br>2: request received  <br>3: processing request  <br>4: request finished and response is ready|getAllResponseHeaders()|Returns header information|
|responseText|Returns the response data as a string|getResponseHeader()|Returns specific header information|
|responseXML|Returns the response data as XML data|open(_method, url, async, user, psw_)|Specifies the request  <br>_method_: the request type GET or POST. Prendre post si information sensible de l'user, ou besoin de beaucoup de place. Sinon c'est get  <br>_url_: the file location  <br>_async_: true (asynchronous) or false (synchronous) DOIT ETRE SUR TRUE (DEJA PAR DÉFAUT)  <br>_user_: optional user name  <br>_psw_: optional password|
|status|Returns the status-number of a request  <br>200: "OK"  <br>403: "Forbidden"  <br>404: "Not Found"  <br>For a complete list go to the [Http Messages Reference](https://www.w3schools.com/tags/ref_httpmessages.asp "https://www.w3schools.com/tags/ref_httpmessages.asp")|send()|Sends the request to the server  <br>Used for GET requests|
|statusText|Returns the status-text (e.g. "OK" or "Not Found")|send(_string_)|Sends the request to the server.  <br>Used for POST requests|
|||setRequestHeader()|Adds a label/value pair to the header to be sent|