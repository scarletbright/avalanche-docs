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

*Defined in [apis/avm/keychain.ts:190](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L190)*

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

*Defined in [utils/types.ts:344](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L344)*

___

### `Protected` keypair

• **keypair**: *elliptic.ec.KeyPair*

*Defined in [apis/avm/keychain.ts:42](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L42)*

___

### `Protected` privk

• **privk**: *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[privk](utils_types.keypair.md#protected-privk)*

*Defined in [utils/types.ts:343](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L343)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[pubk](utils_types.keypair.md#protected-pubk)*

*Defined in [utils/types.ts:342](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L342)*

## Methods

###  addressFromPublicKey

▸ **addressFromPublicKey**(`pubk`: Buffer): *Buffer*

*Defined in [apis/avm/keychain.ts:113](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L113)*

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

*Defined in [apis/avm/keychain.ts:64](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L64)*

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

*Defined in [apis/avm/keychain.ts:92](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L92)*

Returns the address as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representation of the address

___

###  getAddressString

▸ **getAddressString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getAddressString](utils_types.keypair.md#getaddressstring)*

*Defined in [apis/avm/keychain.ts:101](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L101)*

Returns the address's string representation.

**Returns:** *string*

A string representation of the address

___

###  getChainID

▸ **getChainID**(): *string*

*Inherited from [KeyPair](utils_types.keypair.md).[getChainID](utils_types.keypair.md#getchainid)*

*Defined in [utils/types.ts:442](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L442)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](utils_types.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[getPrivateKey](utils_types.keypair.md#getprivatekey)*

*Defined in [utils/types.ts:396](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L396)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPrivateKeyString

▸ **getPrivateKeyString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getPrivateKeyString](utils_types.keypair.md#getprivatekeystring)*

*Defined in [apis/avm/keychain.ts:135](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L135)*

Returns a string representation of the private key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Inherited from [KeyPair](utils_types.keypair.md).[getPublicKey](utils_types.keypair.md#getpublickey)*

*Defined in [utils/types.ts:405](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L405)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  getPublicKeyString

▸ **getPublicKeyString**(): *string*

*Overrides [KeyPair](utils_types.keypair.md).[getPublicKeyString](utils_types.keypair.md#getpublickeystring)*

*Defined in [apis/avm/keychain.ts:144](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L144)*

Returns the public key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  importKey

▸ **importKey**(`privk`: Buffer): *boolean*

*Overrides [KeyPair](utils_types.keypair.md).[importKey](utils_types.keypair.md#importkey)*

*Defined in [apis/avm/keychain.ts:79](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L79)*

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

*Defined in [apis/avm/keychain.ts:186](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L186)*

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

*Defined in [utils/types.ts:451](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L451)*

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

*Defined in [apis/avm/keychain.ts:155](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L155)*

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

*Defined in [apis/avm/keychain.ts:173](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/keychain.ts#L173)*

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message associated with the signature |
`sig` | Buffer | The signature of the signed message  |

**Returns:** *boolean*

True on success, false on failure
