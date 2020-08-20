[avalanche](../README.md) › [PlatformVMAPI-KeyChain](../modules/platformvmapi_keychain.md) › [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)

# Class: SECP256k1KeyPair

Class for representing a private and public keypair on the Platform Chain.

## Hierarchy

* [KeyPair](common_keychain.keypair.md)

  ↳ **SECP256k1KeyPair**

  ↳ [AVMKeyPair](api_avm_keychain.avmkeypair.md)

  ↳ [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)

## Index

### Constructors

* [constructor](platformvmapi_keychain.secp256k1keypair.md#constructor)

### Properties

* [getAddressString](platformvmapi_keychain.secp256k1keypair.md#getaddressstring)
* [keypair](platformvmapi_keychain.secp256k1keypair.md#protected-keypair)
* [privk](platformvmapi_keychain.secp256k1keypair.md#protected-privk)
* [pubk](platformvmapi_keychain.secp256k1keypair.md#protected-pubk)

### Methods

* [addressFromPublicKey](platformvmapi_keychain.secp256k1keypair.md#addressfrompublickey)
* [generateKey](platformvmapi_keychain.secp256k1keypair.md#generatekey)
* [getAddress](platformvmapi_keychain.secp256k1keypair.md#getaddress)
* [getPrivateKey](platformvmapi_keychain.secp256k1keypair.md#getprivatekey)
* [getPrivateKeyString](platformvmapi_keychain.secp256k1keypair.md#getprivatekeystring)
* [getPublicKey](platformvmapi_keychain.secp256k1keypair.md#getpublickey)
* [getPublicKeyString](platformvmapi_keychain.secp256k1keypair.md#getpublickeystring)
* [importKey](platformvmapi_keychain.secp256k1keypair.md#importkey)
* [recover](platformvmapi_keychain.secp256k1keypair.md#recover)
* [sign](platformvmapi_keychain.secp256k1keypair.md#sign)
* [verify](platformvmapi_keychain.secp256k1keypair.md#verify)

## Constructors

###  constructor

\+ **new SECP256k1KeyPair**(): *[SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)*

*Overrides [KeyPair](common_keychain.keypair.md).[constructor](common_keychain.keypair.md#constructor)*

Defined in src/common/secp256k1.ts:182

Class for representing a private and public keypair in Avalanche PlatformVM.

**Returns:** *[SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)*

## Properties

###  getAddressString

• **getAddressString**: *function*

*Overrides [KeyPair](common_keychain.keypair.md).[getAddressString](common_keychain.keypair.md#getaddressstring)*

Defined in src/common/secp256k1.ts:98

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

### `Protected` keypair

• **keypair**: *elliptic.ec.KeyPair*

Defined in src/common/secp256k1.ts:41

___

### `Protected` privk

• **privk**: *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[privk](common_keychain.keypair.md#protected-privk)*

Defined in src/common/keychain.ts:15

___

### `Protected` pubk

• **pubk**: *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[pubk](common_keychain.keypair.md#protected-pubk)*

Defined in src/common/keychain.ts:13

## Methods

###  addressFromPublicKey

▸ **addressFromPublicKey**(`pubk`: Buffer): *Buffer*

Defined in src/common/secp256k1.ts:107

Returns an address given a public key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pubk` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the public key  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address of the public key.

___

###  generateKey

▸ **generateKey**(): *void*

*Overrides [KeyPair](common_keychain.keypair.md).[generateKey](common_keychain.keypair.md#generatekey)*

Defined in src/common/secp256k1.ts:61

Generates a new keypair.

**Returns:** *void*

___

###  getAddress

▸ **getAddress**(): *Buffer*

*Overrides [KeyPair](common_keychain.keypair.md).[getAddress](common_keychain.keypair.md#getaddress)*

Defined in src/common/secp256k1.ts:89

Returns the address as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representation of the address

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[getPrivateKey](common_keychain.keypair.md#getprivatekey)*

Defined in src/common/keychain.ts:70

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPrivateKeyString

▸ **getPrivateKeyString**(): *string*

*Overrides [KeyPair](common_keychain.keypair.md).[getPrivateKeyString](common_keychain.keypair.md#getprivatekeystring)*

Defined in src/common/secp256k1.ts:126

Returns a string representation of the private key.

**Returns:** *string*

A cb58 serialized string representation of the public key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[getPublicKey](common_keychain.keypair.md#getpublickey)*

Defined in src/common/keychain.ts:77

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  getPublicKeyString

▸ **getPublicKeyString**(): *string*

*Overrides [KeyPair](common_keychain.keypair.md).[getPublicKeyString](common_keychain.keypair.md#getpublickeystring)*

Defined in src/common/secp256k1.ts:135

Returns the public key.

**Returns:** *string*

A cb58 serialized string representation of the public key

___

###  importKey

▸ **importKey**(`privk`: Buffer): *boolean*

*Overrides [KeyPair](common_keychain.keypair.md).[importKey](common_keychain.keypair.md#importkey)*

Defined in src/common/secp256k1.ts:76

Imports a private key and generates the appropriate public key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`privk` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the private key  |

**Returns:** *boolean*

true on success, false on failure

___

###  recover

▸ **recover**(`msg`: Buffer, `sig`: Buffer): *Buffer*

*Overrides [KeyPair](common_keychain.keypair.md).[recover](common_keychain.keypair.md#recover)*

Defined in src/common/secp256k1.ts:178

Recovers the public key of a message signer from a message and its associated signature.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message that's signed |
`sig` | Buffer | The signature that's signed on the message  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key of the signer

___

###  sign

▸ **sign**(`msg`: Buffer): *Buffer*

*Overrides [KeyPair](common_keychain.keypair.md).[sign](common_keychain.keypair.md#sign)*

Defined in src/common/secp256k1.ts:147

Takes a message, signs it, and returns the signature.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message to sign, be sure to hash first if expected  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the signature

___

###  verify

▸ **verify**(`msg`: Buffer, `sig`: Buffer): *boolean*

*Overrides [KeyPair](common_keychain.keypair.md).[verify](common_keychain.keypair.md#verify)*

Defined in src/common/secp256k1.ts:165

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message associated with the signature |
`sig` | Buffer | The signature of the signed message  |

**Returns:** *boolean*

True on success, false on failure
