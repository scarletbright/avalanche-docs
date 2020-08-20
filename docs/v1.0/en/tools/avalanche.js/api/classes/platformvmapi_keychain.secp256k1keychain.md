[avalanche](../README.md) › [PlatformVMAPI-KeyChain](../modules/platformvmapi_keychain.md) › [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)

# Class: SECP256k1KeyChain ‹**SECPKPClass**›

Class for representing a key chain in Avalanche.

**`typeparam`** Class extending [KeyPair](common_keychain.keypair.md) which is used as the key in [SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)

## Type parameters

▪ **SECPKPClass**: *[SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)*

## Hierarchy

* [KeyChain](common_keychain.keychain.md)‹SECPKPClass›

  ↳ **SECP256k1KeyChain**

  ↳ [AVMKeyChain](api_avm_keychain.avmkeychain.md)

  ↳ [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)

## Index

### Constructors

* [constructor](platformvmapi_keychain.secp256k1keychain.md#constructor)

### Properties

* [importKey](platformvmapi_keychain.secp256k1keychain.md#importkey)
* [keys](platformvmapi_keychain.secp256k1keychain.md#protected-keys)
* [makeKey](platformvmapi_keychain.secp256k1keychain.md#makekey)

### Methods

* [addKey](platformvmapi_keychain.secp256k1keychain.md#addkey)
* [getAddressStrings](platformvmapi_keychain.secp256k1keychain.md#getaddressstrings)
* [getAddresses](platformvmapi_keychain.secp256k1keychain.md#getaddresses)
* [getKey](platformvmapi_keychain.secp256k1keychain.md#getkey)
* [hasKey](platformvmapi_keychain.secp256k1keychain.md#haskey)
* [removeKey](platformvmapi_keychain.secp256k1keychain.md#removekey)

## Constructors

###  constructor

\+ **new SECP256k1KeyChain**(): *[SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)*

*Overrides [KeyChain](common_keychain.keychain.md).[constructor](common_keychain.keychain.md#constructor)*

Defined in src/common/secp256k1.ts:219

Returns instance of SECP256k1KeyChain.

**Returns:** *[SECP256k1KeyChain](platformvmapi_keychain.secp256k1keychain.md)*

## Properties

###  importKey

• **importKey**: *function*

*Overrides [KeyChain](common_keychain.keychain.md).[importKey](common_keychain.keychain.md#importkey)*

Defined in src/common/secp256k1.ts:219

Given a private key, makes a new key pair, returns the address.

**`param`** A [Buffer](https://github.com/feross/buffer) or cb58 serialized string representing the private key

**`returns`** Address of the new key pair

#### Type declaration:

▸ (`privk`: Buffer | string): *SECPKPClass*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer &#124; string |

___

### `Protected` keys

• **keys**: *object*

*Inherited from [KeyChain](common_keychain.keychain.md).[keys](common_keychain.keychain.md#protected-keys)*

Defined in src/common/keychain.ts:117

#### Type declaration:

* \[ **address**: *string*\]: SECPKPClass

___

###  makeKey

• **makeKey**: *function*

*Overrides [KeyChain](common_keychain.keychain.md).[makeKey](common_keychain.keychain.md#makekey)*

Defined in src/common/secp256k1.ts:206

Makes a new key pair, returns the address.

**`returns`** Address of the new key pair

#### Type declaration:

▸ (): *SECPKPClass*

## Methods

###  addKey

▸ **addKey**(`newKey`: SECPKPClass): *void*

*Overrides [KeyChain](common_keychain.keychain.md).[addKey](common_keychain.keychain.md#addkey)*

Defined in src/common/secp256k1.ts:208

**Parameters:**

Name | Type |
------ | ------ |
`newKey` | SECPKPClass |

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

▸ **getKey**(`address`: Buffer): *SECPKPClass*

*Inherited from [KeyChain](common_keychain.keychain.md).[getKey](common_keychain.keychain.md#getkey)*

Defined in src/common/keychain.ts:199

Returns the [KeyPair](common_keychain.keypair.md) listed under the provided address

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | The [Buffer](https://github.com/feross/buffer) of the address to retrieve from the keys database  |

**Returns:** *SECPKPClass*

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

###  removeKey

▸ **removeKey**(`key`: SECPKPClass | Buffer): *boolean*

*Inherited from [KeyChain](common_keychain.keychain.md).[removeKey](common_keychain.keychain.md#removekey)*

Defined in src/common/keychain.ts:168

Removes the key pair from the list of they keys managed in the [KeyChain](common_keychain.keychain.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`key` | SECPKPClass &#124; Buffer | A [Buffer](https://github.com/feross/buffer) for the address or KPClass to remove  |

**Returns:** *boolean*

The boolean true if a key was removed.
