1. Google Chrome Extension to Inject the JS-Code installieren
    1. Extension `custom JavaScript for Websites` = erlaubt JS auf Websites automatisch zu laufen und speichert diesen Code für weiter Besuche
2. DOM Elemente laden und Injection Code erstellen
    1. mit Entwickler-Tools Element finden, das den Pop-up aufruft.
    2. Bsp: Element `<iframe id=wallIframe>` (Testseite: The Washington Post)
    3. Code schreiben:
    ```js
    /* DOM Manipulation
    * If you want to update / add single style in DOM Element style attribute you can use this function:
    * inject javascript after page reloads.
    */

    function setCssStyle(el, style, value) {
        var result = el.style.cssText.match(new RegExp("(?:[;\\s]|^)(" +
            style.replace("-", "\\-") + "\\s*:(.*?)(;|$))")),
            idx;
        if (result) {
            idx = result.index + result[0].indexOf(result[1]);
            el.style.cssText = el.style.cssText.substring(0, idx) +
            style + ": " + value + ";" +
            el.style.cssText.substring(idx + result[1].length);
        } else {
            el.style.cssText += " " + style + ": " + value + ";";
        }
    }
    var element = document.getElementById("wallIframe");
    setCssStyle(element, "display","none !important");
    ```
3. Diesen Code mit Enwickler-Tools testen
    1. einfach in Console den Script reinkopieren und ausführen
    2. Links-Klick auf Erweiterung Code reinkopieren und Speichern und Testen
        * hier hat es nicht funktioniert: Mögliches Problem könnten sein, dass `<iframe>`nach X Sekunden geladen wird. (man könnte es im *Network Log* checken)
        * Lösung: man könnte **timeout**-Funktion einfügen (10 Sek warten).
        ```js
        setTimeout(
            function() {
                function setCssStyle(el, style, value) {
                    var result = el.style.cssText.match(new RegExp("(?:[;\\s]|^)(" +
                        style.replace("-", "\\-") + "\\s*:(.*?)(;|$))")),
                    idx;
                    if (result) {
                    idx = result.index + result[0].indexOf(result[1]);
                    el.style.cssText = el.style.cssText.substring(0, idx) +
                        style + ": " + value + ";" +
                        el.style.cssText.substring(idx + result[1].length);
                    } else {
                    el.style.cssText += " " + style + ": " + value + ";";
                    }
                }
            
            var element = document.getElementById("wallIframe");
            setCssStyle(element, "display", "none !important");
            },
            10000
        );
     ```
5. Weitere Gedanken:
    1. man kann statt timeout auch so vorgehen:
    ```js
    document.addEventListener("DOMContentLoaded", function() { 
        // Your function goes here
    }
    ```
    * Empfehlung: aber besser mit Timeout-Funktion zu bleiben
* man kann diese Erweiterung auch benutzen, um Ads zu blocken, Pop-Ups zu blocken, Fonts verändern. 