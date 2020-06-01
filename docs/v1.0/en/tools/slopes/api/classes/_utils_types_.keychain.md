[slopes - v1.7.1](../README.md) › ["utils/types"](../modules/_utils_types_.md) › [KeyChain](_utils_types_.keychain.md)

# Class: KeyChain <**KPClass**>

Class for representing a key chain in Slopes.
All endpoints that need key chains should extend on this class.

## Type parameters

▪ **KPClass**: *[KeyPair](_utils_types_.keypair.md)*

extending [KeyPair](_utils_types_.keypair.md) which is used as the key in [KeyChain](_utils_types_.keychain.md)

## Hierarchy

* **KeyChain**

  ↳ [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)

## Index

### Constructors

* [constructor](_utils_types_.keychain.md#constructor)

### Properties

* [chainid](_utils_types_.keychain.md#protected-chainid)
* [importKey](_utils_types_.keychain.md#importkey)
* [keys](_utils_types_.keychain.md#protected-keys)
* [makeKey](_utils_types_.keychain.md#makekey)

### Methods

* [addKey](_utils_types_.keychain.md#addkey)
* [getAddressStrings](_utils_types_.keychain.md#getaddressstrings)
* [getAddresses](_utils_types_.keychain.md#getaddresses)
* [getChainID](_utils_types_.keychain.md#getchainid)
* [getKey](_utils_types_.keychain.md#getkey)
* [hasKey](_utils_types_.keychain.md#haskey)
* [removeKey](_utils_types_.keychain.md#removekey)
* [setChainID](_utils_types_.keychain.md#setchainid)

## Constructors

###  constructor

\+ **new KeyChain**(`chainid`: string): *[KeyChain](_utils_types_.keychain.md)*

*Defined in [utils/types.ts:383](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L383)*

Returns instance of [KeyChain](_utils_types_.keychain.md).

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[KeyChain](_utils_types_.keychain.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Defined in [utils/types.ts:272](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L272)*

___

###  importKey

• **importKey**: *function*

*Defined in [utils/types.ts:290](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L290)*

Given a private key, makes a new [KeyPair](_utils_types_.keypair.md), returns the address.

**`param`** A [Buffer](https://github.com/feross/buffer) representing the private key

**`returns`** Address of the new [KeyPair](_utils_types_.keypair.md)

#### Type declaration:

▸ (`privk`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer |

___

### `Protected` keys

• **keys**: *object*

*Defined in [utils/types.ts:271](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L271)*

#### Type declaration:

* \[ **address**: *string*\]: KPClass

___

###  makeKey

• **makeKey**: *function*

*Defined in [utils/types.ts:281](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L281)*

Makes a new [KeyPair](_utils_types_.keypair.md), returns the address.

**`param`** Optional parameter that may be necessary to produce secure keys

**`returns`** Address of the new [KeyPair](_utils_types_.keypair.md)

#### Type declaration:

▸ (`entropy?`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`entropy?` | Buffer |

## Methods

###  addKey

▸ **addKey**(`newKey`: KPClass): *void*

*Defined in [utils/types.ts:315](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L315)*

Adds the key pair to the list of the keys managed in the [KeyChain](_utils_types_.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`newKey` | KPClass | A key pair of the appropriate class to be added to the [KeyChain](_utils_types_.keychain.md)  |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

*Defined in [utils/types.ts:306](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L306)*

Gets an array of addresses stored in the [KeyChain](_utils_types_.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [utils/types.ts:297](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L297)*

Gets an array of addresses stored in the [KeyChain](_utils_types_.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations of the addresses

___

###  getChainID

▸ **getChainID**(): *string*

*Defined in [utils/types.ts:369](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L369)*

Returns the chainID associated with this [KeyChain](_utils_types_.keychain.md).

**Returns:** *string*

The [KeyChain](_utils_types_.keychain.md)'s chainID

___

###  getKey

▸ **getKey**(`address`: Buffer): *KPClass*

*Defined in [utils/types.ts:360](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L360)*

Returns the [KeyPair](_utils_types_.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *KPClass*

A reference to the [KeyPair](_utils_types_.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

*Defined in [utils/types.ts:349](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L349)*

Checks if there is a key associated with the provided address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The address to check for existence in the keys database  |

**Returns:** *boolean*

True on success, false if not found

___

###  removeKey

▸ **removeKey**(`key`: KPClass | Buffer): *boolean*

*Defined in [utils/types.ts:327](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L327)*

Removes the key pair from the list of they keys managed in the [KeyChain](_utils_types_.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | KPClass &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Defined in [utils/types.ts:378](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L378)*

Sets the the chainID associated with this [KeyChain](_utils_types_.keychain.md) and all associated keypairs.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*
