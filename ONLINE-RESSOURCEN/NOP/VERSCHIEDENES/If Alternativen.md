#### unnötiges else
* Bad:
```c#
public void lala(int param){
    if(param > 5){
        //
    }
    else{
        //
    }
}
```
* Good
```java
public void lala(int param){
    if(param > 5){
        //
        return;
    }
    
    //
}
```
#### Zuweisung in if-else
* Bad:
```c#
public void lala(int param){
    string lala = string.Empty;
    if(param == 0){
        lala="male";
    }
    else if(param == 1){
        gender="female";
    }
    else{
        gender="unknown";
    }

    return gender;
}
```
* Good:
```c#
public void lala(int param){
    string lala = string.Empty;
    if(param == 0) return 'male';
    if(param == 1) return "female";

    return "unknown";
}
```
* Better: 
```c#
public string lala(int param){
    if (input < 0) throw new ArgumentException();
    if (input < 1) throw new ArgumentException();

    return input = 0 ? "woman" : "man";
}
```
#### Dictionary statt if
* Bad
```c#
public void lala(string param){
    if(param == "op1"){
        //
    }
    else if(param == "op2"){
        //
    }
    else{
       //
    }
}
```
* Good
```c#
public void lala(string param){
    var operations = new Dictionary<string, Action>();
    operations["Op1"] = () => { /* */ };
    operations["Op2"] = () => { /* */ };

    operations[operationName].Invoke();

}
```
#### King Beispiel:
* https://gist.github.com/NMillard/2cd48fed21e5bf3b767d4feed3dc3b3d