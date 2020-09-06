1. Loops
    1. `for(int i=0; i<x; i++)`

        ```java
        for(int i=0; i<intArray.length; i++){
            System.out.print(intArray[i]);
        }
        ```

    2. for-each

        ```java
        for(int i: intArray){
            System.out.print(i);
        }
        ```

2. `Arrays.toString()`
    * `Arrays.toString(intArray);`
      * wenn man eigene Klassen erstellt, muss man schauen, dass an `toString()` für eigene Klasse überschreibt
      * nicht für Mehr-Dim Arrays geeignet

3. `Arrays.deepToString()`
    * das gleiche wie 2 für Mehr-DiM arrays: `Array.deepToString(multiDimArr);`
    * `toString()` muss überschrieben werden wenn Obj in Array eigene Klassen sind

4. `Arrays.asList()`
    * `Array.asList(intArray)`;
    * Array muss aber kein Prim-Typ sein, also hier muss es Array von `Ingteger` sein
    * nur für Ein-Dim Arrays

5. Iterator
    * mittels Iterator-Obj Array durchlaufen und printen

        ```java
        Iterator<Integer> it = intList.iterator();
        while(it.hasNext()){
            it.next();
        }
        ```

6. Java Stream API
    * um Collection von Obj zu behandeln.
    * String = Sequence von Obj.
    * hier wird die `forEach()` des Stream-Obj. verwendet

        ```java
        Arrays.stream(intArray).forEach(System.out::print);
        ```
