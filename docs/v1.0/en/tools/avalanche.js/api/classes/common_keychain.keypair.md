[avalanche](../README.md) › [Common-KeyChain](../modules/common_keychain.md) › [KeyPair](common_keychain.keypair.md)

# Class: KeyPair

Class for representing a private and public keypair in Avalanche.
All APIs that need key pairs should extend on this class.

## Hierarchy

* **KeyPair**

  ↳ [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)

## Index

### Constructors

* [constructor](common_keychain.keypair.md#constructor)

### Properties

* [generateKey](common_keychain.keypair.md#generatekey)
* [getAddress](common_keychain.keypair.md#getaddress)
* [getAddressString](common_keychain.keypair.md#getaddressstring)
* [getPrivateKeyString](common_keychain.keypair.md#getprivatekeystring)
* [getPublicKeyString](common_keychain.keypair.md#getpublickeystring)
* [importKey](common_keychain.keypair.md#importkey)
* [privk](common_keychain.keypair.md#protected-privk)
* [pubk](common_keychain.keypair.md#protected-pubk)
* [recover](common_keychain.keypair.md#recover)
* [sign](common_keychain.keypair.md#sign)
* [verify](common_keychain.keypair.md#verify)

### Methods

* [getPrivateKey](common_keychain.keypair.md#getprivatekey)
* [getPublicKey](common_keychain.keypair.md#getpublickey)

## Constructors

###  constructor

\+ **new KeyPair**(): *[KeyPair](common_keychain.keypair.md)*

Defined in src/common/keychain.ts:105

**Returns:** *[KeyPair](common_keychain.keypair.md)*

## Properties

###  generateKey

• **generateKey**: *function*

Defined in src/common/keychain.ts:22

Generates a new keypair.

**`param`** Optional parameter that may be necessary to produce secure keys

#### Type declaration:

▸ (`entropy?`: Buffer): *void*

**Parameters:**

Name | Type |
------ | ------ |
`entropy?` | Buffer |

___

###  getAddress

• **getAddress**: *function*

Defined in src/common/keychain.ts:98

Returns the address.

**`returns`** A [Buffer](https://github.com/feross/buffer)  representation of the address

#### Type declaration:

▸ (): *Buffer*

___

###  getAddressString

• **getAddressString**: *function*

Defined in src/common/keychain.ts:105

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

###  getPrivateKeyString

• **getPrivateKeyString**: *function*

Defined in src/common/keychain.ts:84

Returns a string representation of the private key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  getPublicKeyString

• **getPublicKeyString**: *function*

Defined in src/common/keychain.ts:91

Returns the public key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  importKey

• **importKey**: *function*

Defined in src/common/keychain.ts:31

Imports a private key and generates the appropriate public key.

**`param`** A [Buffer](https://github.com/feross/buffer) representing the private key

**`returns`** true on success, false on failure

#### Type declaration:

▸ (`privk`: Buffer): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer |

___

### `Protected` privk

• **privk**: *Buffer*

Defined in src/common/keychain.ts:15

___

### `Protected` pubk

• **pubk**: *Buffer*

Defined in src/common/keychain.ts:13

___

###  recover

• **recover**: *function*

Defined in src/common/keychain.ts:51

Recovers the public key of a message signer from a message and its associated signature.

**`param`** The message that's signed

**`param`** The signature that's signed on the message

**`returns`** A [Buffer](https://github.com/feross/buffer) containing the public
key of the signer

#### Type declaration:

▸ (`msg`: Buffer, `sig`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |
`sig` | Buffer |

___

###  sign

• **sign**: *function*

Defined in src/common/keychain.ts:40

Takes a message, signs it, and returns the signature.

**`param`** The message to sign

**`returns`** A [Buffer](https://github.com/feross/buffer) containing the signature

#### Type declaration:

▸ (`msg`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |

___

###  verify

• **verify**: *function*

Defined in src/common/keychain.ts:63

Verifies that the private key associated with the provided public key produces the
signature associated with the given message.

**`param`** The message associated with the signature

**`param`** The signature of the signed message

**`param`** The public key associated with the message signature

**`returns`** True on success, false on failure

#### Type declaration:

▸ (`msg`: Buffer, `sig`: Buffer, `pubk`: Buffer): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |
`sig` | Buffer |
`pubk` | Buffer |

## Methods

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

Defined in src/common/keychain.ts:70

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

Defined in src/common/keychain.ts:77

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key
