[avalanche](../README.md) › [Common-KeyChain](../modules/common_keychain.md) › [KeyChain](common_keychain.keychain.md)

# Class: KeyChain ‹**KPClass**›

Class for representing a key chain in Avalanche.
All endpoints that need key chains should extend on this class.

## Type parameters

▪ **KPClass**: *[KeyPair](common_keychain.keypair.md)*

extending [KeyPair](common_keychain.keypair.md) which is used as the key in [KeyChain](common_keychain.keychain.md)

## Hierarchy

* **KeyChain**

  ↳ [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)

## Index

### Constructors

* [constructor](common_keychain.keychain.md#constructor)

### Properties

* [importKey](common_keychain.keychain.md#importkey)
* [keys](common_keychain.keychain.md#protected-keys)
* [makeKey](common_keychain.keychain.md#makekey)

### Methods

* [addKey](common_keychain.keychain.md#addkey)
* [getAddressStrings](common_keychain.keychain.md#getaddressstrings)
* [getAddresses](common_keychain.keychain.md#getaddresses)
* [getKey](common_keychain.keychain.md#getkey)
* [hasKey](common_keychain.keychain.md#haskey)
* [removeKey](common_keychain.keychain.md#removekey)

## Constructors

###  constructor

\+ **new KeyChain**(): *[KeyChain](common_keychain.keychain.md)*

Defined in src/common/keychain.ts:199

Returns instance of [KeyChain](common_keychain.keychain.md).

**Returns:** *[KeyChain](common_keychain.keychain.md)*

## Properties

###  importKey

• **importKey**: *function*

Defined in src/common/keychain.ts:133

Given a private key, makes a new [KeyPair](common_keychain.keypair.md), returns the address.

**`param`** A [Buffer](https://github.com/feross/buffer) representing the private key

**`returns`** A new [KeyPair](common_keychain.keypair.md)

#### Type declaration:

▸ (`privk`: Buffer): *KPClass*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer |

___

### `Protected` keys

• **keys**: *object*

Defined in src/common/keychain.ts:117

#### Type declaration:

* \[ **address**: *string*\]: KPClass

___

###  makeKey

• **makeKey**: *function*

Defined in src/common/keychain.ts:124

Makes a new [KeyPair](common_keychain.keypair.md), returns the address.

**`returns`** Address of the new [KeyPair](common_keychain.keypair.md)

#### Type declaration:

▸ (): *KPClass*

## Methods

###  addKey

▸ **addKey**(`newKey`: KPClass): *void*

Defined in src/common/keychain.ts:156

Adds the key pair to the list of the keys managed in the [KeyChain](common_keychain.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`newKey` | KPClass | A key pair of the appropriate class to be added to the [KeyChain](common_keychain.keychain.md)  |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

Defined in src/common/keychain.ts:148

Gets an array of addresses stored in the [KeyChain](common_keychain.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

Defined in src/common/keychain.ts:141

Gets an array of addresses stored in the [KeyChain](common_keychain.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations
of the addresses

___

###  getKey

▸ **getKey**(`address`: Buffer): *KPClass*

Defined in src/common/keychain.ts:199

Returns the [KeyPair](common_keychain.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *KPClass*

A reference to the [KeyPair](common_keychain.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

Defined in src/common/keychain.ts:189

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

Defined in src/common/keychain.ts:168

Removes the key pair from the list of they keys managed in the [KeyChain](common_keychain.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | KPClass &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.
