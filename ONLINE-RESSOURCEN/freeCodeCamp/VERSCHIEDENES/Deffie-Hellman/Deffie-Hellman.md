* Verschlüsselungsalgorithmus = nimmt Key und gibt zurück einen verschlüsselten Wert = ChipherText.
* Symmetrischer Key = Key der auf beiden Seiten gleich ist.
### Bsp: Dummy-Symmentric-Encryption-Algorithmus:
```js
function encryption(message, key){
    chipherText = message.split('').map(character => {
        const characterAsciiCode = character.charAt(0)
        return String.fromCharCode(characterAsciiCode + key.length)
    })
    chipherText = chipherText.join('');
    return chipherText;
}
```
* Char wird in anderen Char gemappt, basierend auf der Länge des Keys
* z.B M in `('Message', 'Key')` =>  M +`'Key'.length`
* Text decrypten:
```js
function decrypt(chipher, key){
    let message = chipher.split('').map(character => {
        const characterAsciiCode = character.charCodeAt(0);
        return String.fromCharCode(characterAsciiCode-key.length)
    });
    message = message.join('');
    return message;
}
```
* Test
```js
const message = "Hi Bob, here is a confidential message!";
const key = "password";

const cipher = encrypt(message, key);
console.log("Encrypted message:", cipher);
// Encrypted message: Pq(Jwj4(pmzm(q{(i(kwvnqlmv|qit(um{{iom)

const decryptedMessage = decrypt(cipher, key);
console.log("Decrypted message:", decryptedMessage);
// Decrypted message: Hi Bob, here is a confidential message!
```
* Probleme: 
    1. Wörter gleicher Länge können den Code decrypten.
    2. Logik ist zu einfach: einfach shiften
    3. es gibt keine Min-Key-Length: Moderene Algorithemen benutzen 128 Bit = 16 char. => die Menge der Keys wird erhöht.
    4. Algorithmus wird schnell ausgeführt => braucht wenig Zeit, um zu knacken.
* Symetrische Algorithmen: Twofish, Serpent, AES, Blowfish, CAST5, RC4, TDES, IDEA
### Diffie-Hellman Key Exchange
* Ausgangssituation
    1. große Primzahl die allen bekannt ist - public: `p` bzw. `modulus`
    2. zweite Primzahl die public ist: `g` bzw. `base`
    3. (momentan unwichtig, wie `p` und `g` generiert werden)
* Schritte:
    1. Sender(Alice) wählt viel kleinere Zahl als `p` und sendet diese an Reciever(Bob). z.B `p=25`. Bob wählt `g=5`
    2. Beide Alice und Bob wählen eine randome Zahl = secret number. Bsp: Alice hat `a=4` ausgefühlt; Bob wählt `b=3`
    3. Beide kalkulieren: 
        1. Alice: $A=g^a%p$
        2. Bob: $B=g^b%p$
Bsp:
```java
// base
const g = 5;
// modulus
const p = 23;

// Alice's randomly picked number
const a = 4;
// Alice's calculated value
const A = Math.pow(g, a)%p;

// Do the same for Bob
const b = 3;
const B = Math.pow(g, b)%p;

console.log("Alice's calculated value (A):", A);
// Alice's calculated value (A): 4
console.log("Bob's calculated value (B):", B);
// Bob's calculated value (B): 10
```
* jetzt senden Alice und Bob ihre `A` und `B`
* und beide führen folgende Schritte durch:
    1. Alice: $s=B^a%p$
    2. Bob: $s=A^b%p$
    3. Beide `s` sind gleich => common secret = `s` wurde generiert
```java
// Alice calculate the common secret
const secretOfAlice = Math.pow(B, a)%p;
console.log("Alice's calculated secret:", secretOfAlice);
// Alice's calculated secret: 18

// Bob will calculate
const secretOfBob = Math.pow(A, b)%p;
console.log("Bob's calculated secret:", secretOfBob);
// Bob's calculated secret: 18
```
### Fazit:
1. `A,B,p,g` wurden öffentlich versendet
2. Aber nach Modulo = z.B x%4=4 => x kann beliebige Zahl sein
3. `p` und `g` sind Zahlen aus 2000 oder 4000 Bits.