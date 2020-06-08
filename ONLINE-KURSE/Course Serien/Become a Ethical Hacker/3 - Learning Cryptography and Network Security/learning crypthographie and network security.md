### 1 - Network Security
#### 1 - Understanding why encryption is necessary
* zwei Type der Verschlüsselung
    1. Asymmetrisch - Public Key
    2. Symmetrisch - Conventional Encryption
* atom.smasher.org, atom.smasher.org/pgp
* www.networkdls.com
#### 2 - Providing confidentiality, integrity authentication, and non-repudiation
* www.ietf.org/rfc
* 5 Security Services:
    1. Confidentiality - Daten von unauthorisiertem Zugang schützen
    2. Integrity - Daten sollen nicht verändert, gelöscht werden (Hash)
    3. Accountability - (Digitale Signatur)
    4. Availability -  Zugänglichkeit
    5. Authentication - Bestätigung der Identität (Message Authentication Code)
* Security Services werden von Security Mechanismen implemenitert: hash, digest, CA usw.
#### 3 - Comparing passive and active network attacks
* www.gao.gov/assets/
* zwei Typen der Angriffe:
    1. Passive Attack - Eavesdropping, Beobachtung des Traffics (Passwörter usw.), ist hart den Angriff zu erkennen -> Verteidigung mehr die Prevension (Encryption)
        * Reconnaissance - Scanning: Ping scan, Port scan
            1. Ping Scan - sendet ICMP, um IP-Range zu erfahren
            2. Port Scan - welche Ports (=Service) sind offen, dann den Exploit starten
    2. Active Attack - Versuch in das System einzubrechen
        1. Denial of Service
        2. Buffer Overflow
        3. Password Attack
        4. 
#### 4 - Introducing common cryptographic concepts and terminology
* Begriffe: 
    * Trusted Third Party (TTP)
    * Encryption Keys:
        1. Symmentric - single Key
        2. Asymmetric - public + private keys
    * Certificates - Beweis der Identität
* Public Key Infrastructure - Framework um digitale Zertifikate zu generieren, manangen, distributen speichern und ablaufen. Benutzt TTP
#### 5 - Reiview the history of cryptography
* Classis Encryption - benutzt Substitution und Transposition
* Chiffer lernen: www.cs.du.edu/~snarayan/crypt/vigenere.html
#### 6,7 - Challenge: Codding with the Enigma machine
* http://enigmaco.de/enigma/enigma.html - Mit Enigam Maschine rumspielen

### 2 - Symmetric Encryption
#### 1 - Introducing symmetric encryption
* besteht aus 5 Teilen:
    1. Plain Text
    2. Encryption Algorith
    3. Shared Secret Key
    4. Cyphertext 
    5. Decryption Algorith
* DES:
    * verschlüsselt 64-Bit mit 56-Bit key
    * vom 56 Bit-Key werden 16 Subkeys generiert
* man muss Keys oft ädnern
    * sicher Keys generieren und distributen
* Triple DES :
    * 168 Bits
* Blowfish
* IDEA
* Twofish
#### 2 - Making sence of the Feistel cipher
* Algorithm:
    * exclusive OR, left Shift, Number 2 pencil
* Feistel Cipher:
    * Splits the block
    * Multiple rounds
    * rechter Teil wird unverändert, linker Teil wird anhand des recthten Teils und Subkeys verschlüsselt
    * man braucht nur einen Pencil
* Bsp:
    * Daten: 10111000
    * Split L0=1011 und R0=1000
    * Subkey K1 = 0001
    * R1 = RO 1000 xor K1 0001 = 1001
    * R2 = circular shift von 1001 => 0011
    * L1 = R2 0011 xor LO 1011 = 1000
    * Output: RO L1 = 1000 1000
* Block size -> je größer desto sicherer
* Key lenght -> je größer desto besser
* Number of rounds -> Je mehr Runden desto besser
#### 3 - Working with the Advanced Ecryption Standard(AES)
* AES (Rijndael):
    * verarbeitet ganzen Block
    * 4 Opertionen (Mehrmals)
        * Sibstitute Bytes
        * Shift rows
        * Mix columns
        * Add round key
    * Block länge 128 Bit = 4x4-Byte-Matrix; Key 128, 192.256
* www.formaestudio.com/rijndaelinspector
#### 4 - Dissecting block and steam ciphers
* Symmetric Encr - zwei Typen:
    1. Block chiper: DES, AES
        * macht aus Plain Text Blocks (Matrizen)
    2. Stream cipher: RC4, SEAL
        * schnell, benutzen weniger Code
        * excl. OR + random Key
* Chiper Modes:
    * Chaining Mode - definiert, wie Stream generiert wird
* Electronic Codebook (ECB) - Plain Text + Key + Encrypt Alg = Chipertest
* Cipher Block Chaining (CBC) - Plain Text + excl OR mit vorherigem Block + Key + Encrypt Alg = Chipertest
* Cipher Feedback (CFB) - vorheriger Block + Key + Encrypt Alg + excl OR mit Plain Text +  = Chipertest
* Ooutput Feedback (OFB) = vorheriger Block + Key + Encrypt Alg + excl OR mit Plain Text +  = Chipertest
* RC4:
     * 40-140 Bit Key
     * 24 Bit initialisation Vector (IV)
* Stream Cipher werden bei Verschlüsselung von Wireless Communication benutzt (WEP - Wired Equivalent Privacy benutzt RC4)
#### 5 - Using Wireshark to crack WEP
* Edit -> Preferences -> Protocols -> IEEE 802.11 -> Enabele Encrypted -> Decryption Keys: (Edit...) -> eingeben
* ein TCP-Paket auswählen -> Rechtsklicken auf *Stream index: x* -> Follow the TCP Stream
* Rechtsklick auf TPC-Packet -> Follow this Stream -> Inhalt des Stream anshen

### 3 - Asymmetric Encryption and Digital Signatures
#### 1 - Overview and cryptographic requirements
* benutzt private and public Key, die mathematisch zu einadner in Bezug stehen.
* benutzung beinhaltet
    1. Key exchange
    2. Encryption - Public Key benutzen um Shared Secret Key zu senden
    3. Authentication - wenn Alice eine Nachrict an Bob sendet, benutzt sie Bob public Key und nur Bob kann diese Nachricht mit seinem Private Key entschlüsseln
    4. Dig. Signature - Hash von der Nachricht generieren (Message Digest), Hash mit Alice Private Key verschlüsseln um Signature zu erstellen
* um die Nachrict zu enschlüsseln braucht man public und private Key => Nachrichten zum Sender werden mit sienem Public Key verschlüsselt
+ Meisten System sind hybrid (sym + unsym )
#### 2 - Dissecting the public key algorithms: RSA and Diffie-Hellman
* Diffei-Hellman -Alg:
    * Key exchange algorithm (nicht für Verschlüsselung)
    * Bsp: Alice muss Bob Nachricht mittels symmetic encryption senden. Beide müssen zuerst den gleichen shared Key bekommen (4 Schritte): 
        1. Alice und Bob bestimmen ein Paar non-secret prime Numbers: P und g (Base); g<P
        2. Alice sucht random int *a* aus und rechnet Av aus, Av=g^a, dann A ausrechnen A=MOD(Av,P) (a<P)
        3. Bob sucht random Int *b* aus und berechnet Bv=g*b, B=MOD(Bv,P) (b<P)
        4. Alice berechent Sa=B^a und SS=MOD(Sa,P); Bob berechnet Sb=A^b und SS=MOD(Sb,P), Beide kommen auf die gleiche Zahl = deren Shared Secret
* RSA - Block cipher
    * benutzt für Authentication und Key Exchange in SSL mit AES
#### 3 - Creating key pairs for the Diffie-Hellman algorithm
+ siehe Exercise Files
#### 4 - Managing keys
* PGP - Pretty Good Privacy - jeder der Teilnemhme sendet seinen public Key zu einer Stelle, die dann diese Public Key verteilt, was A nach B kommunizieren will
    * Assign Trust:
        * Unknown - Basiszustand
        * None - Besitzer hatte ungültige Keys davor
        * Marginal - Leute die man per Remote kennt
        * Full - Trust
* Public Key Infrastructure - ist ein Framework mit Trusted Third Party
    * Trusted third authority ist CA (Certificate Authority)
    * CA stellt Certificate für die ganze Einheit
    * CA - stellt aus/ widerruft usw. die Certifikate
        * Digitale Signature: Public Key + User ID des Besitzers werden von CA signiert = Public Key gehört dieser Einheit
    * x.509 - Standard um dig. Certificates zu erstellen
#### 5 - Using certificates
1. Alice: Public + Privat Keys
2. Bob: Public + Prvate Keys
3. CA: Public + Private Keys
    * Bob und Alice senden deren Pub Keys + deren IDs (= Unsigned Cert) -> Hash des Unsigned Certificates wird erstellt -> mit CAs Private Key zu Signatur verschlüsselt -> Signatur am Ende des Unsigned Cert anhängen => signed Cert. 
    * Wenn man jetzt die Certificate versendet => Public Key wird ebenfalls versendet
    * Signatur wird zuerst mit Public Key von CA entschlüsselt und die Hash bestimmt des Unsigned Keys verglichen -> 

### 4 - Hash Algorithms, Message Digests and Authentication
#### 1 - Diving into hash algorithms and message digests
* Hash wird benutzt in:
    1. Authenticating a message
    2. Monitoring Data integrity
    3. Storing Password
* - nimmt variable Länge als Input an und prodziert fixed Länge für Output
* Hash-Alg:
    1. SHA (160 Bits)
    2. MD5 (128 Bits)
* tools für Hash
    * gfsw.exe - GUI File Signature
#### 2 - Looking deeper into message digests
* wofür Hash:
    1. Integrity - unterwegs nicht verändert (Message Digest)
    2. Authentication - inside von MAC-Message Authentication Code
        * Message Digest mit Shared Secret benutzen = MAC 
    3. Non-Repudiation + Accountability - in Digitalen Signaturen
#### 3 - Understanding passwords, hash, salt and reainbow tables
* Passwörter speichern:
    * Password erstellen -> vom Passwort Hash bilden -> und Hash speichern -> wenn man Password eingibt => wird Hash generiert, wenn Hashes gleich sind => OK
* Rainbow Tables = DB mit Hash-Passwörtern/Werten
* Salt - hash = password + salt => noch mehr Sicherheit

#### 4/5 - Challenge: Password strength tests
* http://www.passwordmeter.com/
* sha1-online.com
* hashkiller.co.uk
### 5 - Secure Sockets Layer(SSL)
#### 1 - Introducing Secure Sockets Layer
#### 2 - Exploring the security of SSL with Wireshark

### 6 - Email Security
#### 1 - Inverstigating email privacy and authentication concerns
#### 2 - Implementing PGP email security with GPG

### 7 - Internet Protocol Security
#### 1 - Exploring Internet Protocol Security (IPSec)
#### 2 - Dissecting the authentication header
#### 3 - Encapsulating security payloads
#### 4 - Using operating mechanisms
#### 5 - 