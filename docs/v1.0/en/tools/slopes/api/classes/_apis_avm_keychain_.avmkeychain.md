[slopes - v1.7.2](../README.md) › ["apis/avm/keychain"](../modules/_apis_avm_keychain_.md) › [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)

# Class: AVMKeyChain

Class for representing a key chain in Slopes.

**`typeparam`** Class extending [KeyPair](_utils_types_.keypair.md) which is used as the key in [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)

## Hierarchy

* [KeyChain](_utils_types_.keychain.md)‹[AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)›

  ↳ **AVMKeyChain**

## Index

### Constructors

* [constructor](_apis_avm_keychain_.avmkeychain.md#constructor)

### Properties

* [chainid](_apis_avm_keychain_.avmkeychain.md#protected-chainid)
* [keys](_apis_avm_keychain_.avmkeychain.md#protected-keys)

### Methods

* [addKey](_apis_avm_keychain_.avmkeychain.md#addkey)
* [getAddressStrings](_apis_avm_keychain_.avmkeychain.md#getaddressstrings)
* [getAddresses](_apis_avm_keychain_.avmkeychain.md#getaddresses)
* [getChainID](_apis_avm_keychain_.avmkeychain.md#getchainid)
* [getKey](_apis_avm_keychain_.avmkeychain.md#getkey)
* [hasKey](_apis_avm_keychain_.avmkeychain.md#haskey)
* [importKey](_apis_avm_keychain_.avmkeychain.md#importkey)
* [makeKey](_apis_avm_keychain_.avmkeychain.md#makekey)
* [removeKey](_apis_avm_keychain_.avmkeychain.md#removekey)
* [setChainID](_apis_avm_keychain_.avmkeychain.md#setchainid)
* [signTx](_apis_avm_keychain_.avmkeychain.md#signtx)

## Constructors

###  constructor

\+ **new AVMKeyChain**(`chainid`: string): *[AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)*

*Overrides [KeyChain](_utils_types_.keychain.md).[constructor](_utils_types_.keychain.md#constructor)*

*Defined in [apis/avm/keychain.ts:255](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/keychain.ts#L255)*

Returns instance of AVMKeyChain.

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Inherited from [KeyChain](_utils_types_.keychain.md).[chainid](_utils_types_.keychain.md#protected-chainid)*

*Defined in [utils/types.ts:272](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L272)*

___

### `Protected` keys

• **keys**: *object*

*Inherited from [KeyChain](_utils_types_.keychain.md).[keys](_utils_types_.keychain.md#protected-keys)*

*Defined in [utils/types.ts:271](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L271)*

#### Type declaration:

* \[ **address**: *string*\]: [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)

## Methods

###  addKey

▸ **addKey**(`newKey`: [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)): *void*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:315](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L315)*

Adds the key pair to the list of the keys managed in the [KeyChain](_utils_types_.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`newKey` | [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md) | A key pair of the appropriate class to be added to the [KeyChain](_utils_types_.keychain.md)  |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:306](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L306)*

Gets an array of addresses stored in the [KeyChain](_utils_types_.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:297](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L297)*

Gets an array of addresses stored in the [KeyChain](_utils_types_.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations of the addresses

___

###  getChainID

▸ **getChainID**(): *string*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:369](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L369)*

Returns the chainID associated with this [KeyChain](_utils_types_.keychain.md).

**Returns:** *string*

The [KeyChain](_utils_types_.keychain.md)'s chainID

___

###  getKey

▸ **getKey**(`address`: Buffer): *[AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:360](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L360)*

Returns the [KeyPair](_utils_types_.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *[AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)*

A reference to the [KeyPair](_utils_types_.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:349](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L349)*

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

*Overrides [KeyChain](_utils_types_.keychain.md).[importKey](_utils_types_.keychain.md#importkey)*

*Defined in [apis/avm/keychain.ts:230](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/keychain.ts#L230)*

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

*Overrides [KeyChain](_utils_types_.keychain.md).[makeKey](_utils_types_.keychain.md#makekey)*

*Defined in [apis/avm/keychain.ts:217](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/keychain.ts#L217)*

Makes a new key pair, returns the address.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`entropy` | Buffer |  undefined | Optional parameter that may be necessary to produce secure keys  |

**Returns:** *Buffer*

Address of the new key pair

___

###  removeKey

▸ **removeKey**(`key`: [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md) | Buffer): *boolean*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:327](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L327)*

Removes the key pair from the list of they keys managed in the [KeyChain](_utils_types_.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md) &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Inherited from [KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:378](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L378)*

Sets the the chainID associated with this [KeyChain](_utils_types_.keychain.md) and all associated keypairs.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*

___

###  signTx

▸ **signTx**(`utx`: [UnsignedTx](_apis_avm_tx_.unsignedtx.md)): *[Tx](_apis_avm_tx_.tx.md)*

*Defined in [apis/avm/keychain.ts:253](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/keychain.ts#L253)*

DEPRECATED: use UnsignedTx.sign(keychain) instead
Signs a [UnsignedTx](_apis_avm_tx_.unsignedtx.md) and returns signed [Tx](_apis_avm_tx_.tx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`utx` | [UnsignedTx](_apis_avm_tx_.unsignedtx.md) | A [UnsignedTx](_apis_avm_tx_.unsignedtx.md) that needs to be signed  |

**Returns:** *[Tx](_apis_avm_tx_.tx.md)*

A signed [Tx](_apis_avm_tx_.tx.md)
