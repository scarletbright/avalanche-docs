[avalanche](../README.md) › [AVMAPI-KeyChain](../modules/avmapi_keychain.md) › [AVMKeyPair](avmapi_keychain.avmkeypair.md)

# Class: AVMKeyPair

Class for representing a private and public keypair in the AVM.

## Hierarchy

* [KeyPair](utils_types.keypair.md)

  ↳ **AVMKeyPair**

## Index

### Constructors

* [constructor](avmapi_keychain.avmkeypair.md#constructor)

### Properties

* [chainid](avmapi_keychain.avmkeypair.md#protected-chainid)
* [entropy](avmapi_keychain.avmkeypair.md#protected-entropy)
* [keypair](avmapi_keychain.avmkeypair.md#protected-keypair)
* [privk](avmapi_keychain.avmkeypair.md#protected-privk)
* [pubk](avmapi_keychain.avmkeypair.md#protected-pubk)

### Methods

* [addressFromPublicKey](avmapi_keychain.avmkeypair.md#addressfrompublickey)
* [generateKey](avmapi_keychain.avmkeypair.md#generatekey)
* [getAddress](avmapi_keychain.avmkeypair.md#getaddress)
* [getAddressString](avmapi_keychain.avmkeypair.md#getaddressstring)
* [getChainID](avmapi_keychain.avmkeypair.md#getchainid)
* [getPrivateKey](avmapi_keychain.avmkeypair.md#getprivatekey)
* [getPrivateKeyString](avmapi_keychain.avmkeypair.md#getprivatekeystring)
* [getPublicKey](avmapi_keychain.avmkeypair.md#getpublickey)
* [getPublicKeyString](avmapi_keychain.avmkeypair.md#getpublickeystring)
* [importKey](avmapi_keychain.avmkeypair.md#importkey)
* [recover](avmapi_keychain.avmkeypair.md#recover)
* [setChainID](avmapi_keychain.avmkeypair.md#setchainid)
* [sign](avmapi_keychain.avmkeypair.md#sign)
* [verify](avmapi_keychain.avmkeypair.md#verify)

## Constructors

###  constructor

\+ **new AVMKeyPair**(`chainid`: string, `entropy`: Buffer): *[AVMKeyPair](avmapi_keychain.avmkeypair.md)*

*Overrides [KeyPair](utils_types.keypair.md).[constructor](utils_types.keypair.md#constructor)*

*Defined in [src/apis/avm/keychain.ts:183](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L183)*

Class for representing a private and public keypair in Avalanche.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`chainid` | string | - |
`entropy` | Buffer | undefined |

**Returns:** *[AVMKeyPair](avmapi_keychain.avmkeypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Inherited from [KeyPair](utils_types.keypair.md).[chainid](utils_types.keypair.md#protected-chainid)*

*Defined in [src/utils/types.ts:364](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L364)*

___

### `Protected` entropy

• **entropy**: *Buffer*

*Defined in [src/apis/avm/keychain.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L43)*

___

### `Protected` keypair

• **keypair**: *elliptic.ec.KeyPair*

*Defined in [src/apis/avm/keychain.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L41)*

___

### `Protected` privk

• **privk**: *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[privk](utils_types.keypair.md#protected-privk)*

*Defined in [src/utils/types.ts:362](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L362)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[pubk](utils_types.keypair.md#protected-pubk)*

*Defined in [src/utils/types.ts:360](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L360)*

## Methods

###  addressFromPublicKey

▸ **addressFromPublicKey**(`pubk`: Buffer): *Buffer*

*Defined in [src/apis/avm/keychain.ts:113](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L113)*

Returns an address given a public key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pubk` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the public key  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address of the public key.

___

###  generateKey

▸ **generateKey**(`entropy?`: Buffer): *void*

*Overrides [KeyPair](utils_types.keypair.md).[generateKey](utils_types.keypair.md#generatekey)*

*Defined in [src/apis/avm/keychain.ts:65](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L65)*

Generates a new keypair.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`entropy?` | Buffer | Optional parameter that may be necessary to produce secure keys  |

**Returns:** *void*

___

###  getAddress

▸ **getAddress**(): *Buffer*

*Overrides [KeyPair](utils_types.keypair.md).[getAddress](utils_types.keypair.md#getaddress)*

*Defined in [src/apis/avm/keychain.ts:94](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L94)*

Returns the address as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representation of the address

___

###  getAddressString

▸ **getAddressString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getAddressString](utils_types.keypair.md#getaddressstring)*

*Defined in [src/apis/avm/keychain.ts:101](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L101)*

Returns the address's string representation.

**Returns:** *string*

A string representation of the address

___

###  getChainID

▸ **getChainID**(): *string*

*Inherited from [KeyPair](utils_types.keypair.md).[getChainID](utils_types.keypair.md#getchainid)*

*Defined in [src/utils/types.ts:461](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L461)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](utils_types.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[getPrivateKey](utils_types.keypair.md#getprivatekey)*

*Defined in [src/utils/types.ts:419](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L419)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPrivateKeyString

▸ **getPrivateKeyString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getPrivateKeyString](utils_types.keypair.md#getprivatekeystring)*

*Defined in [src/apis/avm/keychain.ts:132](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L132)*

Returns a string representation of the private key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[getPublicKey](utils_types.keypair.md#getpublickey)*

*Defined in [src/utils/types.ts:426](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L426)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  getPublicKeyString

▸ **getPublicKeyString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getPublicKeyString](utils_types.keypair.md#getpublickeystring)*

*Defined in [src/apis/avm/keychain.ts:139](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L139)*

Returns the public key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  importKey

▸ **importKey**(`privk`: Buffer): *boolean*

*Overrides [KeyPair](utils_types.keypair.md).[importKey](utils_types.keypair.md#importkey)*

*Defined in [src/apis/avm/keychain.ts:81](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L81)*

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

*Overrides [KeyPair](utils_types.keypair.md).[recover](utils_types.keypair.md#recover)*

*Defined in [src/apis/avm/keychain.ts:179](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L179)*

Recovers the public key of a message signer from a message and its associated signature.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message that's signed |
`sig` | Buffer | The signature that's signed on the message  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key of the signer

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Inherited from [KeyPair](utils_types.keypair.md).[setChainID](utils_types.keypair.md#setchainid)*

*Defined in [src/utils/types.ts:468](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L468)*

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*

___

###  sign

▸ **sign**(`msg`: Buffer): *Buffer*

*Overrides [KeyPair](utils_types.keypair.md).[sign](utils_types.keypair.md#sign)*

*Defined in [src/apis/avm/keychain.ts:148](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L148)*

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

*Overrides [KeyPair](utils_types.keypair.md).[verify](utils_types.keypair.md#verify)*

*Defined in [src/apis/avm/keychain.ts:166](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L166)*

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message associated with the signature |
`sig` | Buffer | The signature of the signed message  |

**Returns:** *boolean*

True on success, false on failure
