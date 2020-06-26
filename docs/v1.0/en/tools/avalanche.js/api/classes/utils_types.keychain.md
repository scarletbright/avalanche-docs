[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [KeyChain](utils_types.keychain.md)

# Class: KeyChain ‹**KPClass**›

Class for representing a key chain in Avalanche.
All endpoints that need key chains should extend on this class.

## Type parameters

▪ **KPClass**: *[KeyPair](utils_types.keypair.md)*

extending [KeyPair](utils_types.keypair.md) which is used as the key in [KeyChain](utils_types.keychain.md)

## Hierarchy

* **KeyChain**

  ↳ [AVMKeyChain](avmapi_keychain.avmkeychain.md)

## Index

### Constructors

* [constructor](utils_types.keychain.md#constructor)

### Properties

* [chainid](utils_types.keychain.md#protected-chainid)
* [importKey](utils_types.keychain.md#importkey)
* [keys](utils_types.keychain.md#protected-keys)
* [makeKey](utils_types.keychain.md#makekey)

### Methods

* [addKey](utils_types.keychain.md#addkey)
* [getAddressStrings](utils_types.keychain.md#getaddressstrings)
* [getAddresses](utils_types.keychain.md#getaddresses)
* [getChainID](utils_types.keychain.md#getchainid)
* [getKey](utils_types.keychain.md#getkey)
* [hasKey](utils_types.keychain.md#haskey)
* [removeKey](utils_types.keychain.md#removekey)
* [setChainID](utils_types.keychain.md#setchainid)

## Constructors

###  constructor

\+ **new KeyChain**(`chainid`: string): *[KeyChain](utils_types.keychain.md)*

*Defined in [utils/types.ts:384](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L384)*

Returns instance of [KeyChain](utils_types.keychain.md).

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[KeyChain](utils_types.keychain.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Defined in [utils/types.ts:273](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L273)*

___

###  importKey

• **importKey**: *function*

*Defined in [utils/types.ts:291](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L291)*

Given a private key, makes a new [KeyPair](utils_types.keypair.md), returns the address.

**`param`** A [Buffer](https://github.com/feross/buffer) representing the private key

**`returns`** Address of the new [KeyPair](utils_types.keypair.md)

#### Type declaration:

▸ (`privk`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer |

___

### `Protected` keys

• **keys**: *object*

*Defined in [utils/types.ts:272](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L272)*

#### Type declaration:

* \[ **address**: *string*\]: KPClass

___

###  makeKey

• **makeKey**: *function*

*Defined in [utils/types.ts:282](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L282)*

Makes a new [KeyPair](utils_types.keypair.md), returns the address.

**`param`** Optional parameter that may be necessary to produce secure keys

**`returns`** Address of the new [KeyPair](utils_types.keypair.md)

#### Type declaration:

▸ (`entropy?`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`entropy?` | Buffer |

## Methods

###  addKey

▸ **addKey**(`newKey`: KPClass): *void*

*Defined in [utils/types.ts:316](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L316)*

Adds the key pair to the list of the keys managed in the [KeyChain](utils_types.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`newKey` | KPClass | A key pair of the appropriate class to be added to the [KeyChain](utils_types.keychain.md)  |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

*Defined in [utils/types.ts:307](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L307)*

Gets an array of addresses stored in the [KeyChain](utils_types.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [utils/types.ts:298](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L298)*

Gets an array of addresses stored in the [KeyChain](utils_types.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations of the addresses

___

###  getChainID

▸ **getChainID**(): *string*

*Defined in [utils/types.ts:370](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L370)*

Returns the chainID associated with this [KeyChain](utils_types.keychain.md).

**Returns:** *string*

The [KeyChain](utils_types.keychain.md)'s chainID

___

###  getKey

▸ **getKey**(`address`: Buffer): *KPClass*

*Defined in [utils/types.ts:361](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L361)*

Returns the [KeyPair](utils_types.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *KPClass*

A reference to the [KeyPair](utils_types.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

*Defined in [utils/types.ts:350](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L350)*

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

*Defined in [utils/types.ts:328](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L328)*

Removes the key pair from the list of they keys managed in the [KeyChain](utils_types.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | KPClass &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Defined in [utils/types.ts:379](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L379)*

Sets the the chainID associated with this [KeyChain](utils_types.keychain.md) and all associated keypairs.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*
