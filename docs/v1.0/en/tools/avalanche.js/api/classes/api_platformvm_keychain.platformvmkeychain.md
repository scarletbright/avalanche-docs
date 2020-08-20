[avalanche](../README.md) › [API-PlatformVM-KeyChain](../modules/api_platformvm_keychain.md) › [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)

# Class: PlatformVMKeyChain

Class for representing a key chain in Avalanche.

**`typeparam`** Class extending [KeyPair](common_keychain.keypair.md) which is used as the key in [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)

## Hierarchy

  ↳ [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)‹[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)›

  ↳ **PlatformVMKeyChain**

## Index

### Constructors

* [constructor](api_platformvm_keychain.platformvmkeychain.md#constructor)

### Properties

* [chainid](api_platformvm_keychain.platformvmkeychain.md#chainid)
* [hrp](api_platformvm_keychain.platformvmkeychain.md#hrp)
* [keys](api_platformvm_keychain.platformvmkeychain.md#protected-keys)

### Methods

* [addKey](api_platformvm_keychain.platformvmkeychain.md#addkey)
* [getAddressStrings](api_platformvm_keychain.platformvmkeychain.md#getaddressstrings)
* [getAddresses](api_platformvm_keychain.platformvmkeychain.md#getaddresses)
* [getKey](api_platformvm_keychain.platformvmkeychain.md#getkey)
* [hasKey](api_platformvm_keychain.platformvmkeychain.md#haskey)
* [importKey](api_platformvm_keychain.platformvmkeychain.md#importkey)
* [makeKey](api_platformvm_keychain.platformvmkeychain.md#makekey)
* [removeKey](api_platformvm_keychain.platformvmkeychain.md#removekey)

## Constructors

###  constructor

\+ **new PlatformVMKeyChain**(`hrp`: string, `chainid`: string): *[PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[constructor](platformvmapi_keychain.secp256k1keychain.md#constructor)*

Defined in src/apis/platformvm/keychain.ts:121

Returns instance of PlatformVMKeyChain.

**Parameters:**

Name | Type |
------ | ------ |
`hrp` | string |
`chainid` | string |

**Returns:** *[PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)*

## Properties

###  chainid

• **chainid**: *string* = ""

Defined in src/apis/platformvm/keychain.ts:83

___

###  hrp

• **hrp**: *string* = ""

Defined in src/apis/platformvm/keychain.ts:82

___

### `Protected` keys

• **keys**: *object*

*Inherited from [KeyChain](common_keychain.keychain.md).[keys](common_keychain.keychain.md#protected-keys)*

Defined in src/common/keychain.ts:117

#### Type declaration:

* \[ **address**: *string*\]: [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)

## Methods

###  addKey

▸ **addKey**(`newKey`: [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)): *void*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[addKey](platformvmapi_keychain.secp256k1keychain.md#addkey)*

Defined in src/apis/platformvm/keychain.ts:96

**Parameters:**

Name | Type |
------ | ------ |
`newKey` | [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md) |

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

▸ **getKey**(`address`: Buffer): *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

*Inherited from [KeyChain](common_keychain.keychain.md).[getKey](common_keychain.keychain.md#getkey)*

Defined in src/common/keychain.ts:199

Returns the [KeyPair](common_keychain.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

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

▸ **importKey**(`privk`: Buffer | string): *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[importKey](platformvmapi_keychain.secp256k1keychain.md#importkey)*

Defined in src/apis/platformvm/keychain.ts:108

Given a private key, makes a new key pair, returns the address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`privk` | Buffer &#124; string | A [Buffer](https://github.com/feross/buffer) or cb58 serialized string representing the private key  |

**Returns:** *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

The new key pair

___

###  makeKey

▸ **makeKey**(): *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

*Overrides [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md).[makeKey](platformvmapi_keychain.secp256k1keychain.md#makekey)*

Defined in src/apis/platformvm/keychain.ts:90

Makes a new key pair, returns the address.

**Returns:** *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

The new key pair

___

###  removeKey

▸ **removeKey**(`key`: [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md) | Buffer): *boolean*

*Inherited from [KeyChain](common_keychain.keychain.md).[removeKey](common_keychain.keychain.md#removekey)*

Defined in src/common/keychain.ts:168

Removes the key pair from the list of they keys managed in the [KeyChain](common_keychain.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md) &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.
