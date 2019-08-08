//Daten zum Sotieren in Arrays gespeichert:
var people=[
    {name: "Kirill", rate: 70, active: true},
    {name: "Arnold", rate: 80, active: false}
]
people[0].name;
//Methoden des Arrays:
//push()
//unshift() //hinzufügen
//pop()
//shift() //entfernen
//forEach()
//some()
//every() //Druchlaufen
//concat() //erstellt neues Arrays aus vorliegendem
//filter() //erstellt neues Arrays aus 
//sort() //sortiert anhand einer Funktion
//reverse()
//map() ruft Funktion für jedes Array und erstellt aus Ergebnissen neues Array
    //jQuery-Methoden
//.add()
//.not() //Entfernt Element
//.each() //Durchläuft
//.filter()
//.toArray() //wandelt jQuery-Auswahl zum Array 

//Objekte als Eigenschaft
var people2={
    Arnold={ rate: 70, active: true},
    Kirill={ rate: 80, active: false}
}
people2.Arnold.rate;
//Objekt aus Objekt zu entfernen delete
delete people2.Arnold;
//KindObjekte durchlaufen:
Object.keys; //???

//Filterung = Gruppe von Werten verkleinern:
    //Bsp 1:
    //Array-Obj hat Methoden zum Sortieren, Methode gibt neues Array zurück
    $(function(){
        people = [
            {
                name: "Casey",
                rate: 60
            },
            {
                name: "Casey2",
                rate: 80
            },
            {
                name: "Casey3",
                rate: 120
            }
        ]
        //Bsp1
        var results=[];
        people.forEach(function(person){
            if(person.rate >= 65 && person.rate <=90){
                results.push(person);
            }
        });

        //Bsp2:
        function priceRange(person){
            return (person.rate>=65) && (person.rate<=90);
        }
        var results=[];
        results=people.filter(priceRange);

        var $tableBody=$('<tbody></body>');
        for( var i=0; i<results.length; i++){
            var person=results[i];
            var $row=$('<tr></tr>');
            $row.append($('<td></td>').text(person.name));
            $row.append($('<td></td>').text(person.rate));
            $tableBody.append($row);
        }
        $('thread').aflter($tableBody);
    });

//Dynamische Filterung = Elemente erstellen + je nach Action Elemente ein/ausblenden:
    (function(){
        var rows=[];
        var $min=$('#value-min');
        var $max=$('#value-max');
        var $table=$('#rates');
        function makeRows(){
            people.forEach(function(person){
                var $row = $('<tr></tr>');
                $row.append($('<td></td>').text(person.name));
                $row.append($('<td></td>').text(person.naem));
                rows.push({
                    person:person,
                    $element: $row
                });
            });
        }

        function appendRows(){
            var $tbody=$('<tbody></tbody>');
            rows.forEach(function(row){
                $tbody.append(row.$element);
            })
            $table.append($tbody);
        }
        function update(min, max){
            rows.forEach(function(row){
                if(row.person.rate>=min && row.person.rate <=max){
                    row.$element.show();
                }
                else{
                    row.$element.hide();
                }
            });
        }
        function init(){
            $('#slider').noUiSlider({
                range: [0,150], start:[65,90], handles: 2, margin: 20, connect: true, serialization: {to: [$min, $max], resolution: 1}
            }).change(function(){update($min.val(), $max.val()); });    
            makeRows();
            appendRows();
            update($min.val(), $max.val());   
        }
        $(init);
    }());

//Gefilterte Bilderanzeige: = Klick auf Filternamen => entsprechende Bilder werden angezeigt 
//! <img> bekommt data-tags="..., ..." = Filternamen
//<img src="..." data-tags="..., ..." /> + Array tagged={ tag1: [p1.jpg, p6.jpg], tag2: [p4.jpg, p6.jpg], usw.}
    //Bsp:
    //1 tagged-Obj vorbereiten
    (function(){
        var $imgs=$('#gallery img'); //ist div
        var $buttons=$('#buttons'); //ist div
        var tagged={}; //leeres Objekt
        $imgs.each(function(){
            var img=this;
            var tags=$(this).data('tags');
            if(tags){
                tags.split(',').forEach(function(tagName){
                    if(tagged[tagName]==null){
                        tagged[tagName]=[];
                    }
                    tagged[tagName].push(img);
                });
            }
        });
    }());
    //Button-Klick:
    (function(){
        $('<button/>', {
            text: "Alle",
            class: "active",
            click: function(){
                $(this)
                    .addClass('activae')
                    .siblings()
                    .removeClass('active')
                $imgs.show();
            }
        }).appendTo($buttons);
        $.each(tagged, function(tagName){
            $('<button/>', {
                text: tagName+' ('+tagged[tagName].length+')',
                click: function(){
                    $(this)
                        .addClass('active')
                        .siblings()
                        .removeClass('active')
                }
            }).appendTo($buttons);
        });
    }());

//Suche:
//Bsp: = Suche der Bilder anhand des alt-Attr von <img> + cache-Obj verwendet
cache=[
    {element: img, text: 'lala1'},
    {element: img, text: 'lala2'}
]
    //Bsp:
    (function(){
        var $img=$('#gallery img');
        var $search=$('#filter-search');
        var cache=[];

        //Cache einrichten
        $img.each(function(){
            cache.push({
                element: this,
                text: this.alt.trim().toLowerCase()
            });
        });
        function filter(){
            var query=this.value.trim().toLowerCase(); //trim() = Entfernt Weißraum vonm Anfang und Ende des Strings
            cache.forEach(function(img){
                var index=0;
                if(query){
                    index=img.text.indexOf(query);
                }

                img.element.style.display=index===-1?'none':'';
            });
        }
        if('oninput' in $search[0]){
            $search.on('input', filter);
        }
        else{
            $search.on('keyup', filter);
        }
    }());

    //sort() = sortiert lexikografische => wenn man anders will => eigene Vergleichsfunktion schreiben = als Param sort() mitgeben. Vergleichsfunktion sollte <0, 0, >0 liefern
    //sort() vergleicht immer 2 Werte
    var prices=[1,2,125, 2, 19, 14];
    prices.sort(function(a,b){
        return a-b;
    });

    //Tabelle sortieren = nach Klick auf eine Spalte nach dieser Spalte sortieren
    //<tabel class="sortable"> ... //table muss class="sortable" haben
    //<tr> <td data-sort="name">.. </td> <td data-sort="duration">...</td> <td data-sort="date">..</td> <- SpaltenKöpfe soltlen data-sort-Attr haben
    var compare={
        name: function(a,b){
            a=a.replace(/^the /i, ''); //alle the durch '' ersetzen am Anfang
            b=b.replace(/^the /i, '');
            if(a<b){
                return -1;
            }
            else{
                return a>b?1:0;
            }
        },
        duration: function(a,b){
            a=a.split(":");
            b=b.split(":");

            a=Number(a[0])*60+Number(a[1]);
            b=Number(b[0])*60+Number(a[1]);
            return a-b;
        },
        date:function(a,b){
            a=new Date(a);
            b=new Date(b);
            return a-b;
        }
    };

    $('.sortable').each(function(){
        var $table=$(this);
        var $tbody=$table.find("tbody");
        var $contrls=$table.find("th");
        var rows=$tbody.find("tr").toArray();

        $contrls.on("click", function(){
            var $header=$(this);
            var order=$header.data("sort");
            var column;
            if($header.is("ascending") || $header.is(".descending")){
                $header.toggleClass("ascending descending");
                $tbody.append(rows.reverse());
            }
            else{
                $header.addClass("ascending");
                $header.siblings().removeClass("ascending descending");
                if(compare.hasOwnProperty(order)){
                    column=$controls.index(this);
                    rows.sort(function(a,b){
                        a=$(a).find("td").eq(column).text();
                        b=$(b).find("td").eq(column).text();
                        return compare[order](a,b);
                    });
                    $tbody.append(rows);
                }
            }
        });
    });
