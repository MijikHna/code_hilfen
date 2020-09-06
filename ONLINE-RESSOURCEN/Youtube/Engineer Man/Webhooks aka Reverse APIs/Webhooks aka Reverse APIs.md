* - HTTP-Messages die an einen Event zu third Party-Service gesendet werden, die man benutzt. 
* - PreBuild API, an die man Daten senden kann.
* - Also am Bsp von github.com
    * falls es ein neuen Commit, wird ein Webhook gesendet (deswegen Reverse API, da keine Client-Request)
    * man kann in github.com-Settings einstellen, wohing Webhook gesendet wird.
* also API = pull; Webhook = push
* Webhook müssen auch wie RESTAPI implementiert werden.