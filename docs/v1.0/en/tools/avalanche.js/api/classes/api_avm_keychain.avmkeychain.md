[avalanche](../README.md) › [API-AVM-KeyChain](../modules/api_avm_keychain.md) › [AVMKeyChain](api_avm_keychain.avmkeychain.md)

# Class: AVMKeyChain

Class for representing a key chain in Avalanche.

**`typeparam`** Class extending [KeyPair](common_keychain.keypair.md) which is used as the key in [AVMKeyChain](api_avm_keychain.avmkeychain.md)

## Hierarchy

  ↳ [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)‹[AVMKeyPair](api_avm_keychain.avmkeypair.md)›

  ↳ **AVMKeyChain**

## Index

### Constructors

* [constructor](api_avm_keychain.avmkeychain.md#constructor)

### Properties

* [chainid](api_avm_keychain.avmkeychain.md#chainid)
* [hrp](api_avm_keychain.avmkeychain.md#hrp)
* [keys](api_avm_keychain.avmkeychain.md#protected-keys)

### Methods

* [addKey](api_avm_keychain.avmkeychain.md#addkey)
* [getAddressStrings](api_avm_keychain.avmkeychain.md#getaddressstrings)
* [getAddresses](api_avm_keychain.avmkeychain.md#getaddresses)
* [getKey](api_avm_keychain.avmkeychain.md#getkey)
* [hasKey](api_avm_keychain.avmkeychain.md#haskey)
* [importKey](api_avm_keychain.avmkeychain.md#importkey)
* [makeKey](api_avm_keychain.avmkeychain.md#makekey)
* [removeKey](api_avm_keychain.avmkeychain.md#removekey)

## Constructors

###  constructor

\+ **new AVMKeyChain**(`hrp`: string, `chainid`: string): *[AVMKeyChain](api_avm_keychain.avmkeychain.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[constructor](platformvmapi_keychain.secp256k1keychain.md#constructor)*

Defined in src/apis/avm/keychain.ts:121

Returns instance of AVMKeyChain.

**Parameters:**

Name | Type |
------ | ------ |
`hrp` | string |
`chainid` | string |

**Returns:** *[AVMKeyChain](api_avm_keychain.avmkeychain.md)*

## Properties

###  chainid

• **chainid**: *string* = ""

Defined in src/apis/avm/keychain.ts:83

___

###  hrp

• **hrp**: *string* = ""

Defined in src/apis/avm/keychain.ts:82

___

### `Protected` keys

• **keys**: *object*

*Inherited from [KeyChain](common_keychain.keychain.md).[keys](common_keychain.keychain.md#protected-keys)*

Defined in src/common/keychain.ts:117

#### Type declaration:

* \[ **address**: *string*\]: [AVMKeyPair](api_avm_keychain.avmkeypair.md)

## Methods

###  addKey

▸ **addKey**(`newKey`: [AVMKeyPair](api_avm_keychain.avmkeypair.md)): *void*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[addKey](platformvmapi_keychain.secp256k1keychain.md#addkey)*

Defined in src/apis/avm/keychain.ts:96

**Parameters:**

Name | Type |
------ | ------ |
`newKey` | [AVMKeyPair](api_avm_keychain.avmkeypair.md) |

**Returns:** *void*

___

###  getAddressStrings

▸ **getAddressStrings**(): *Array‹string›*

*Inherited from [KeyChain](common_keychain.keychain.md).[getAddressStrings](common_keychain.keychain.md#getaddressstrings)*

Defined in src/common/keychain.ts:148

Gets an array of addresses stored in the [KeyChain](common_keychain.keychain.md).

**Returns:** *Array‹string›*

An array of string representations of the addresses

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Inherited from [KeyChain](common_keychain.keychain.md).[getAddresses](common_keychain.keychain.md#getaddresses)*

Defined in src/common/keychain.ts:141

Gets an array of addresses stored in the [KeyChain](common_keychain.keychain.md).

**Returns:** *Array‹Buffer›*

An array of [Buffer](https://github.com/feross/buffer)  representations
of the addresses

___

###  getKey

▸ **getKey**(`address`: Buffer): *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

*Inherited from [KeyChain](common_keychain.keychain.md).[getKey](common_keychain.keychain.md#getkey)*

Defined in src/common/keychain.ts:199

Returns the [KeyPair](common_keychain.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

A reference to the [KeyPair](common_keychain.keypair.md) in the keys database

___

###  hasKey

▸ **hasKey**(`address`: Buffer): *boolean*

*Inherited from [KeyChain](common_keychain.keychain.md).[hasKey](common_keychain.keychain.md#haskey)*

Defined in src/common/keychain.ts:189

Checks if there is a key associated with the provided address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The address to check for existence in the keys database  |

**Returns:** *boolean*

True on success, false if not found

___

###  importKey

▸ **importKey**(`privk`: Buffer | string): *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[importKey](platformvmapi_keychain.secp256k1keychain.md#importkey)*

Defined in src/apis/avm/keychain.ts:108

Given a private key, makes a new key pair, returns the address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`privk` | Buffer &#124; string | A [Buffer](https://github.com/feross/buffer) or cb58 serialized string representing the private key  |

**Returns:** *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

The new key pair

___

###  makeKey

▸ **makeKey**(): *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[makeKey](platformvmapi_keychain.secp256k1keychain.md#makekey)*

Defined in src/apis/avm/keychain.ts:90

Makes a new key pair, returns the address.

**Returns:** *[AVMKeyPair](api_avm_keychain.avmkeypair.md)*

The new key pair

___

###  removeKey

▸ **removeKey**(`key`: [AVMKeyPair](api_avm_keychain.avmkeypair.md) | Buffer): *boolean*

*Inherited from [KeyChain](common_keychain.keychain.md).[removeKey](common_keychain.keychain.md#removekey)*

Defined in src/common/keychain.ts:168

Removes the key pair from the list of they keys managed in the [KeyChain](common_keychain.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | [AVMKeyPair](api_avm_keychain.avmkeypair.md) &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.
