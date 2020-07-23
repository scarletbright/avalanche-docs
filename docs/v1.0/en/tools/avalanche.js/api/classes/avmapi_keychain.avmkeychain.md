[avalanche](../README.md) › [AVMAPI-KeyChain](../modules/avmapi_keychain.md) › [AVMKeyChain](avmapi_keychain.avmkeychain.md)

# Class: AVMKeyChain

Class for representing a key chain in Avalanche.

**`typeparam`** Class extending [KeyPair](utils_types.keypair.md) which is used as the key in [AVMKeyChain](avmapi_keychain.avmkeychain.md)

## Hierarchy

* [KeyChain](utils_types.keychain.md)‹[AVMKeyPair](avmapi_keychain.avmkeypair.md)›

  ↳ **AVMKeyChain**

## Index

### Constructors

* [constructor](avmapi_keychain.avmkeychain.md#constructor)

### Properties

* [chainid](avmapi_keychain.avmkeychain.md#protected-chainid)
* [keys](avmapi_keychain.avmkeychain.md#protected-keys)

### Methods

* [addKey](avmapi_keychain.avmkeychain.md#addkey)
* [getAddressStrings](avmapi_keychain.avmkeychain.md#getaddressstrings)
* [getAddresses](avmapi_keychain.avmkeychain.md#getaddresses)
* [getChainID](avmapi_keychain.avmkeychain.md#getchainid)
* [getKey](avmapi_keychain.avmkeychain.md#getkey)
* [hasKey](avmapi_keychain.avmkeychain.md#haskey)
* [importKey](avmapi_keychain.avmkeychain.md#importkey)
* [makeKey](avmapi_keychain.avmkeychain.md#makekey)
* [removeKey](avmapi_keychain.avmkeychain.md#removekey)
* [setChainID](avmapi_keychain.avmkeychain.md#setchainid)
* [signTx](avmapi_keychain.avmkeychain.md#signtx)

## Constructors

###  constructor

\+ **new AVMKeyChain**(`chainid`: string): *[AVMKeyChain](avmapi_keychain.avmkeychain.md)*

*Overrides [KeyChain](utils_types.keychain.md).[constructor](utils_types.keychain.md#constructor)*

*Defined in [src/apis/avm/keychain.ts:244](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L244)*

Returns instance of AVMKeyChain.

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[AVMKeyChain](avmapi_keychain.avmkeychain.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Inherited from [KeyChain](utils_types.keychain.md).[chainid](utils_types.keychain.md#protected-chainid)*

*Defined in [src/utils/types.ts:486](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L486)*

___

### `Protected` keys

• **keys**: *object*

*Inherited from [KeyChain](utils_types.keychain.md).[keys](utils_types.keychain.md#protected-keys)*

*Defined in [src/utils/types.ts:484](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L484)*

#### Type declaration:

* \[ **address**: *string*\]: [AVMKeyPair](avmapi_keychain.avmkeypair.md)

## Methods

###  addKey

▸ **addKey**(`newKey`: [AVMKeyPair](avmapi_keychain.avmkeypair.md)): *void*

*Inherited from [KeyChain](utils_types.keychain.md).[addKey](utils_types.keychain.md#addkey)*

*Defined in [src/utils/types.ts:527](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L527)*

Adds the key pair to the list of the keys managed in the [KeyChain](utils_types.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`newKey` | [AVMKeyPair](avmapi_keychain.avmkeypair.md) | A key pair of the appropriate class to be added to the [KeyChain](utils_types.keychain.md)  |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

*Inherited from [KeyChain](utils_types.keychain.md).[getAddressStrings](utils_types.keychain.md#getaddressstrings)*

*Defined in [src/utils/types.ts:519](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L519)*

Gets an array of addresses stored in the [KeyChain](utils_types.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Inherited from [KeyChain](utils_types.keychain.md).[getAddresses](utils_types.keychain.md#getaddresses)*

*Defined in [src/utils/types.ts:512](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L512)*

Gets an array of addresses stored in the [KeyChain](utils_types.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations
of the addresses

___

###  getChainID

▸ **getChainID**(): *string*

*Inherited from [KeyChain](utils_types.keychain.md).[getChainID](utils_types.keychain.md#getchainid)*

*Defined in [src/utils/types.ts:578](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L578)*

Returns the chainID associated with this [KeyChain](utils_types.keychain.md).

**Returns:** *string*

The [KeyChain](utils_types.keychain.md)'s chainID

___

###  getKey

▸ **getKey**(`address`: Buffer): *[AVMKeyPair](avmapi_keychain.avmkeypair.md)*

*Inherited from [KeyChain](utils_types.keychain.md).[getKey](utils_types.keychain.md#getkey)*

*Defined in [src/utils/types.ts:571](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L571)*

Returns the [KeyPair](utils_types.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *[AVMKeyPair](avmapi_keychain.avmkeypair.md)*

A reference to the [KeyPair](utils_types.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

*Inherited from [KeyChain](utils_types.keychain.md).[hasKey](utils_types.keychain.md#haskey)*

*Defined in [src/utils/types.ts:561](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L561)*

Checks if there is a key associated with the provided address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The address to check for existence in the keys database  |

**Returns:** *boolean*

True on success, false if not found

___

###  importKey

▸ **importKey**(`privk`: Buffer | string): *Buffer*

*Overrides [KeyChain](utils_types.keychain.md).[importKey](utils_types.keychain.md#importkey)*

*Defined in [src/apis/avm/keychain.ts:221](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L221)*

Given a private key, makes a new key pair, returns the address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`privk` | Buffer &#124; string | A [Buffer](https://github.com/feross/buffer) or AVA serialized string representing the private key  |

**Returns:** *Buffer*

Address of the new key pair

___

###  makeKey

▸ **makeKey**(`entropy`: Buffer): *Buffer*

*Overrides [KeyChain](utils_types.keychain.md).[makeKey](utils_types.keychain.md#makekey)*

*Defined in [src/apis/avm/keychain.ts:208](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L208)*

Makes a new key pair, returns the address.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`entropy` | Buffer | undefined | Optional parameter that may be necessary to produce secure keys  |

**Returns:** *Buffer*

Address of the new key pair

___

###  removeKey

▸ **removeKey**(`key`: [AVMKeyPair](avmapi_keychain.avmkeypair.md) | Buffer): *boolean*

*Inherited from [KeyChain](utils_types.keychain.md).[removeKey](utils_types.keychain.md#removekey)*

*Defined in [src/utils/types.ts:540](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L540)*

Removes the key pair from the list of they keys managed in the [KeyChain](utils_types.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | [AVMKeyPair](avmapi_keychain.avmkeypair.md) &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Inherited from [KeyChain](utils_types.keychain.md).[setChainID](utils_types.keychain.md#setchainid)*

*Defined in [src/utils/types.ts:585](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L585)*

Sets the the chainID associated with this [KeyChain](utils_types.keychain.md) and all associated keypairs.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*

___

###  signTx

▸ **signTx**(`utx`: [UnsignedTx](avmapi_transactions.unsignedtx.md)): *[Tx](avmapi_transactions.tx.md)*

*Defined in [src/apis/avm/keychain.ts:244](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/keychain.ts#L244)*

DEPRECATED: use UnsignedTx.sign(keychain) instead
Signs a [UnsignedTx](avmapi_transactions.unsignedtx.md) and returns signed [Tx](avmapi_transactions.tx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utx` | [UnsignedTx](avmapi_transactions.unsignedtx.md) | A [UnsignedTx](avmapi_transactions.unsignedtx.md) that needs to be signed  |

**Returns:** *[Tx](avmapi_transactions.tx.md)*

A signed [Tx](avmapi_transactions.tx.md)
