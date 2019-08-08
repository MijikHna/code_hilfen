//Hilfsfunktion IE8
//callback = Name der Funktion
function addEvent(el, event, callback){
    if('addEventListener' in el ){
        el.addEventListener(event, callback, false) 
    }
    else{
        el['e'+event+callback]=callback;
        el[event+callback]=function(){
            el['e'+event+callback](window.event);
        };
        el.attachEvent('on'+event, el[event+callback]);
    }
}

/* <form>
Eigenschaften: action, method, name, elements
Methoden: submit(); reset();
Ereignisse: submit, reset
*/
document.forms[i];
document.forms.formName; //bestimmte <form> ansprechen
document.forms.forms[i].elements[i]; 
document.forms.forms[i].elements.password; //bestimmtes Element der Form ansprechen
document.forms.forms[i].elements.password.value; //Werts des Formelements ansprechen

//Formular abschicken:
(function(){
    var form=document.getElementById("login"); //<form>
    addEvent(form, "submit", function(e){
        e.preventDefault();
        var elements=this.elements;
        var username=elements.username.value;
        var msg="Willkommen "+username;
        document.getElementById("main").textContent=msg; 
    });
});

//Eingabetyp ändern = type="password" in type="text"
(function(){

    var pwd=document.getElementById("pwd");
    var chk=document.getElementById("showPW"); //checkbox

    addEvent(chk, "change", function(e){
        var target=e.target || e.srcElement;
        try{ //try, da bei IE8 kann Error verursachen
            if(target.checked){
                pwd.type="text";
            }
            else{
                pwd.type="password";
            }
        }
        catch(error){
            alert("Browser unterstützt diesen Typ nicht");
        }
    });
}());

//Abschickenschaltfläche deaktivieren:
(function(){
    var form=document.getElementById("newPwd"); //<form>
    var password=document.getElementById("pws"); //type="password"
    var submit=document.getElementById("submit");

    var submitted=false; //Wurde form shcon verschickt?
 
    submit.disabled=true; //deaktivieren "Abschicken"
    submit.className="disabled"; //formatiert "Abschicken"

    addEvent(password, "input", function(e){ //Bei Passwordeingabe
        var target=e.target || e.srcElement; //Ereignisziel
        submit.disabled=submitted || !target.value; //legt disabled fest
        //WEnn form schon verschickt oder Pwd keinen Wert: disabled
        submit.className=(!target.value || submitted) ? "disabled" : "enabled";
    });
    //WEnn Abschicken: Deaktivieren form, um erneutes verschicken verhindern
    addEvent(form, "submit", function(e){ //beim abschicken
        if(submit.disabled || submitted){ //wenn deaktiviert oder gesendet
            e.preventDefault();
            return;
        }
        submit.disabled=true; //deaktiviert abschicken
        submitted=true; //aktualisiert submitted
        submit.className="disabled"; //ändert Stil

        e.preventDefault();
        alert("Passwort ist "+ password.value);
    });
});

//S 593 = Polyfill-Skript= wenn Broswer bestimmte Features nicht unterstützt => wird Ausweichskript ausgeführt
//<- z.B oft Verwendet: Modernizer + Yepnope