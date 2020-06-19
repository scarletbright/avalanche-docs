# Tutorial &mdash; Managing AVM Keys

Avalanche.js comes with its own AVM Keychain. This keychain is used in the functions of the API, enabling them to sign using keys it's registered. The first step in this process is to create an instance of Avalanche.js connected to our AVA Platform endpoint of choice.

```js
let myNetworkID = 12345; //default is 3, we want to override that for our local network
let myBlockchainID = "GJABrZ9A6UQFpwjPU8MDxDd8vuyRoDVeDAXc694wJ5t3zEkhU"; // The AVM blockchainID on this network
let ava = new avalanche.Avalanche("localhost", 9650, "http", myNetworkID, myBlockchainID);
let avm = ava.AVM(); //returns a reference to the AVM API used by Avalanche.js
```

## Accessing the keychain

The keychain is accessed through the AVM API and can be referenced directly or through a reference variable.

```js
let myKeychain = avm.keyChain();
```

This exposes the instance of the class AVM Keychain which is created when the AVM API is created. At present, this supports secp256k1 curve for ECDSA key pairs.

## Creating AVM key pairs

The keychain has the ability to create new keypairs for you and return the address assocated with the key pair.

```js
let newAddress1 = myKeychain.makeKey(); //returns a Buffer for the address
```

You may also import your exsting private key into the keychain using either a Buffer...

```js
let mypk = bintools.avaDeserialize("24jUJ9vZexUM6expyMcT48LBx27k1m7xpraoV62oSQAHdziao5"); //returns a Buffer
let newAddress2 = myKeychain.importKey(mypk); //returns a Buffer for the address
```

... or an AVA serialized string works, too:

```js
let mypk = "24jUJ9vZexUM6expyMcT48LBx27k1m7xpraoV62oSQAHdziao5";
let newAddress2 = myKeychain.importKey(mypk); //returns a Buffer for the address
```

## Working with keychains

The AVMKeyChain extends the global KeyChain class, which has standardized key management capabilities. The following functions are available on any keychain that implements this interface.

```js
let addresses = myKeychain.getAddresses(); //returns an array of Buffers for the addresses
let addressStrings = myKeychain.getAddressStrings(); //returns an array of strings for the addresses
let exists = myKeychain.hasKey(newAddress1); //returns true if the address is managed
let keypair = myKeychain.getKey(newAddress1); //returns the keypair class
```

## Working with keypairs

The AVMKeyPair class implements the global KeyPair class, which has standardized keypair functionality. The following operations are available on any keypair that implements this interface.

```js
let address = keypair.getAddress(); //returns Buffer
let addressString = keypair.getAddressString(); //returns string

let pubk = keypair.getPublicKey(); //returns Buffer
let pubkstr = keypair.getPublicKeyString(); //returns an AVA serialized string

let privk = keypair.getPrivateKey(); //returns Buffer
let privkstr = keypair.getPrivateKeyString(); //returns an AVA serialized string

keypair.generateKey(); //creates a new random keypair

let mypk = "24jUJ9vZexUM6expyMcT48LBx27k1m7xpraoV62oSQAHdziao5";
let successul = keypair.importKey(mypk); //returns boolean if private key imported successfully

let message = Buffer.from("Wubalubadubdub");
let signature = keypair.sign(message); //returns a Buffer with the signature
let signerPubk = keypair.recover(message, signature);
let isValid = keypair.verify(message, signature); //returns a boolean
```
