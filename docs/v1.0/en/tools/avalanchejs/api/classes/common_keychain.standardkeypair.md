[avalanche](../README.md) › [Common-KeyChain](../modules/common_keychain.md) › [StandardKeyPair](common_keychain.standardkeypair.md)

# Class: StandardKeyPair

Class for representing a private and public keypair in Avalanche.
All APIs that need key pairs should extend on this class.

## Hierarchy

* **StandardKeyPair**

  ↳ [SECP256k1KeyPair](common_secp256k1keychain.secp256k1keypair.md)

## Index

### Constructors

* [constructor](common_keychain.standardkeypair.md#constructor)

### Properties

* [generateKey](common_keychain.standardkeypair.md#generatekey)
* [getAddress](common_keychain.standardkeypair.md#getaddress)
* [getAddressString](common_keychain.standardkeypair.md#getaddressstring)
* [getPrivateKeyString](common_keychain.standardkeypair.md#getprivatekeystring)
* [getPublicKeyString](common_keychain.standardkeypair.md#getpublickeystring)
* [importKey](common_keychain.standardkeypair.md#importkey)
* [privk](common_keychain.standardkeypair.md#protected-privk)
* [pubk](common_keychain.standardkeypair.md#protected-pubk)
* [recover](common_keychain.standardkeypair.md#recover)
* [sign](common_keychain.standardkeypair.md#sign)
* [verify](common_keychain.standardkeypair.md#verify)

### Methods

* [clone](common_keychain.standardkeypair.md#abstract-clone)
* [create](common_keychain.standardkeypair.md#abstract-create)
* [getPrivateKey](common_keychain.standardkeypair.md#getprivatekey)
* [getPublicKey](common_keychain.standardkeypair.md#getpublickey)

## Constructors

###  constructor

\+ **new StandardKeyPair**(): *[StandardKeyPair](common_keychain.standardkeypair.md)*

*Defined in [src/common/keychain.ts:109](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L109)*

**Returns:** *[StandardKeyPair](common_keychain.standardkeypair.md)*

## Properties

###  generateKey

• **generateKey**: *function*

*Defined in [src/common/keychain.ts:22](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L22)*

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

*Defined in [src/common/keychain.ts:98](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L98)*

Returns the address.

**`returns`** A [Buffer](https://github.com/feross/buffer)  representation of the address

#### Type declaration:

▸ (): *Buffer*

___

###  getAddressString

• **getAddressString**: *function*

*Defined in [src/common/keychain.ts:105](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L105)*

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

###  getPrivateKeyString

• **getPrivateKeyString**: *function*

*Defined in [src/common/keychain.ts:84](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L84)*

Returns a string representation of the private key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  getPublicKeyString

• **getPublicKeyString**: *function*

*Defined in [src/common/keychain.ts:91](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L91)*

Returns the public key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  importKey

• **importKey**: *function*

*Defined in [src/common/keychain.ts:31](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L31)*

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

*Defined in [src/common/keychain.ts:15](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L15)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Defined in [src/common/keychain.ts:13](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L13)*

___

###  recover

• **recover**: *function*

*Defined in [src/common/keychain.ts:51](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L51)*

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

*Defined in [src/common/keychain.ts:40](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L40)*

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

*Defined in [src/common/keychain.ts:63](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L63)*

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

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/keychain.ts:109](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L109)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Defined in [src/common/keychain.ts:107](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L107)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Defined in [src/common/keychain.ts:70](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L70)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Defined in [src/common/keychain.ts:77](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/keychain.ts#L77)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key
