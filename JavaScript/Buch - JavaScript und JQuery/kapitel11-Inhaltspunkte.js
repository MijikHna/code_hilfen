//= mit Inhaltsfelder zusätzliche Info anzeigen: Ziehharmonika, Registerkarte, modale Fenster, Bildanzeigen, Diashows
<html class="no-js"></html> //Klass no-js, falls JS deaktiviert ist

var elDoc=document.documentElement;
elDoc.className=elDoc.className.replace(/(^|\s)no-js(\s|$)/, "$1"); //Funktion, die die Klasse no-js löscht, falls JS aktiviert ist.

//1) Zieharmonika
//Grundlage ist <ul> -> <li> -> in html5 <details> und <summary>
$('.accordion-panel').animate({
    height: 'show',
    paddingTop: 'show',
    paddingBottom: 'show',
    marginTop: 'show',
    marginBottom: 'show'
})
//Bsp:
//CSS:
//.accordion-panel{ display: none}
$('.accordion').on('click', '.accordion-control', function(e){
    e.preventDefault(); //da Button ist => preventDefault()
    $(this)
        .next('.accordion-panel');
        .not(':animated'); //prüft, ob Element gerade nicht animiert wird
        .slideToggle();
});

//2)-Registerkarte = Reiter
//Registerkarten mit <li> erstellt -> Felder mit <div>; Verknüpfung Reiter und Feld über href, Feld hat id-Att. Beide Att. müssen den selben Wert haben
//Bsp: 
//.tab-panel{ display: none;}
//.tab-pnale.active {display: block;}
$(".tab-list").each(function(){
    var $this = $(this);
    var $tab = $this.find("li.active");
    var $link = $tab.find('a');
    var $panel = $($link.attr("href"));

    $this.on('click', '.tab-control', function(e){
        e.preventDefault();
        var $link = $(this);
        var id = this.hash; //ruft href des angeklickten Reiters ab

        if(id && !$link.is('.active')){
            $panel.removeClass('.active');
            $tab.removeClass('active');
            
            $panel=$(id).addClass('active');
            $tab =$link.parent().addClass("active");
        }
    });
});

//3) - Modale Fenster = Fenster, das vor der Seite erscheint
//Bsp:
//<div class="modal">
    //<div class="modal-content"> ... </div>
//</div>
//<button role="button" class="modal-close>"close </button>
//Script als Design-Muster = Modul-Muster einfügen modal-init.js
(function(){
    var $content=$('#share-options').detach();
    $('#share').on("click", function(){
        modal.open({content: $constent, width: 340, height: 300});
    });
});
//.modal{positon: absolute; z-index: 1000;}
//modal-window.js

//Modul heißt modal = ist eine Funktion, die drei Funktionen enthält
var modal=(function(){
    var $window=$(window);
    var $modal=$('<div class="modal"/>');
    var $content=$('<div class="modal-content" />');
    var $close=$('<button role="button" class="modal-close">Schließen</button>');

    $modal.append($content, $close);

    $close.on("click", function(e){
        e.preventDefault();
        modal.close();
    });

    return {
        center: function() {
            var top=Math.max($window.height()-$modal.outerHeight(), 0)/2;
            var left=Math.max($window.width() - $modal.outerWidth(), 0)/2;
            $modal.css({
                top: top+$window.schrollTop(),
                left: left+$window.scrollLeft()
            });
        },

        open: function(settings){
            $content.empty().append(settings.contetn);
            $modal.css({
                width: settings.width || "auto",
                height: settings.height || "auto",
            }).append("body");
            
            modal.center();
            $(window).on("resize", modal.center);
        },

        close: function(){
            $content.empty();
            $modal.detach();
            $(window).off("resize", modal.center);
        }
    };   
}());

//4) - Bildanzeige:
//Klick auf Vorschaubild => Bild im Zentrum angezeigt
//<div id="photo-viewer"> </div>
//<div id="thumbnails>" <a href=".../thumb-1" class="thumb active" ...> ... </div>
//Beim Laden der Bild class="is-loading", Ladevorgang abgeschlossen => is-loading wird gelöscht
//Bsp:
var request;
var $current;
var cache={};
var $frame = $("#phote-viewer");
var $thumbs = $(".thumb");

function crossfade($img){
    $current.stop().fadeOut("slow");
}

$img.css({
    marginLeft: -$img.width() / 2,
    marginTop: -$img.height()/2
});

$img.stop().fadeTo("slow", 1);
$current = $img;

//Cache-Obj
var cache={
    "c11/img/photo1-jpg" : {
        "$img": jQuery-Objekt, "isLoading": false
    },
    "c11/img/photo2.jpg" : {
        "$img": jQuery-Objekt, "isLoading": false
    }
}

//Bsp2:
$(document).on('click', '.thumb', function(e){
    var $img;
    var src=this.href;
    request = src;
    
    e.preventDefault();

    $thumbs.removeClass('active');
    $(this).addClass('active');

    if(cache.hasOwnClass(src)){
        if(cache[src].isLoading===false){
            crossfade(cache[src].$img);
        }
    }
    else{
        $img=$('<img/>');
        cache[src]={
            $img: $img,
            isLoading: true
        };

        $img.on('load', function(){
            $img.hide();
            $frame.removeClass('is-loading').append($img);
            cache[src].isLoading=false;
            if(request===src){
                crossfade($img);
            }
        });
        $frame.addClass('is-loading');

        $img.attr({
            'src':src,
            'alt':this.title || ''
        });
    }
});
$('.thumb').eq(0).click();

//5) - Diashow
//<div class="slide-viewer">
    //<div class="slide-group">
        //<div class= slide slide-1">...</div>
        //...
    //</div>
//</div>
//slide-viewer {position : relative; overflow: hidden; height: 300px;}
//slide-group {width: 100%; height: 100%; position: relative;}
//.slide{width: 100% height: 100%, display: none; position: absolute;}
//.slide:first-child{display: block;}
$('.slider').each(function(){
    var $this=$(this),
    var $group=$this.find('.slide-group'),
    var $slide=$this.find('.slide'),
    var buttonArray=[],
    var currentIndex=0,
    var timeout;

    function advance(){
        clearTimeout(timeout);
        timeout=setTimeout(function(){
            if(currentIndex < ($slides.length-1)){
                move(currentIndex+1);  
            }
            else{
                move(0);
            }
        }, 4000);
    }
    $.each($slides, function(index){
        var $button=$('<button type="button" class="slide-btn">&bull; </button>');
        if(index===currentIndex){
            $button.addClass('active');
        }
        $button.on('click', function(){
            move(index);
        }).appendTo('.slide-button');
        buttonArray.push($button);
    });

    advance(); //löscht Timer bevor sie ihn neustartet

    function move(newIndex){
        var animateLeft, slideLeft;
        advance();
        if($group.is(':animated')|| currentIndex === newIndex){
            return;
        }
        buttonArray[currentIndex].removeClass('active');
        buttonArray[newIndex].addClass('active');

        if(newIndex > currentIndex){
            slideLeft='100%';
            animateLeft='-100%';
        }
        else{
            slideLeft='-100%';
            animateLeft='100%';
        }
        $slides.eq(newIndex).css({left:slideLeft, display:'block'});
        $group.animate({left: animateLeft}, function(){
            $slides.eq(currentIndex).css({display: 'none'});
            $slides.eq(newIndex).css({left: 0});
            $group.css({left: 0});
            currentIndex=newIndex;
        });
    }
});
//6) jQuery-PlugIn erstellen = jQuery-Methoden ohne Biblothek hinzufügen
//PlugIN funtioniert so: Satz von DOM-Elementen in Form einer jQ-Auswahl übergeben. DOM mit jQuery-Plugin bearbeiten, jQuery-Objekt zurückgeben
(function($){
    $.fn.accordion=function(speed){//jQuery hat Objekt .fn, mit dem Funktionsumfang erwetiern kann. Plugins werden als Methoden geschrieben, die zum Ojb .fn hinzugefügt werden
    return this; //jQuery-Obj zurückgeben: = mit return this.
    }
})(jQuery); //  Namespace schützen = Plugin-Code steht in IIFE

//Plug-In - Zieharmonika:
(function($){
    $.fn.accordion=function(speed){
        this.on('click', '.accordion-control', function(e){
            e.preventDefault();
            $(this)
                .next('.accordion-panel')
                .not(':animated')
                .slideToggle(speed);
        });
        return this;
    }
})(jQuery);

<ul class="menu">
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
    <li>
        <a href="#" class="accordion-control"> ...</a>
        <div class="accordion-panel"> ....</div>
    </li>
</ul>