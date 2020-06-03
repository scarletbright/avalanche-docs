[slopes - v1.7.2](../README.md) › ["apis/avm/keychain"](../modules/_apis_avm_keychain_.md) › [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)

# Class: AVMKeyPair

Class for representing a private and public keypair in the AVM.

## Hierarchy

* [KeyPair](_utils_types_.keypair.md)

  ↳ **AVMKeyPair**

## Index

### Constructors

* [constructor](_apis_avm_keychain_.avmkeypair.md#constructor)

### Properties

* [chainid](_apis_avm_keychain_.avmkeypair.md#protected-chainid)
* [keypair](_apis_avm_keychain_.avmkeypair.md#protected-keypair)
* [privk](_apis_avm_keychain_.avmkeypair.md#protected-privk)
* [pubk](_apis_avm_keychain_.avmkeypair.md#protected-pubk)

### Methods

* [addressFromPublicKey](_apis_avm_keychain_.avmkeypair.md#addressfrompublickey)
* [generateKey](_apis_avm_keychain_.avmkeypair.md#generatekey)
* [getAddress](_apis_avm_keychain_.avmkeypair.md#getaddress)
* [getAddressString](_apis_avm_keychain_.avmkeypair.md#getaddressstring)
* [getChainID](_apis_avm_keychain_.avmkeypair.md#getchainid)
* [getPrivateKey](_apis_avm_keychain_.avmkeypair.md#getprivatekey)
* [getPrivateKeyString](_apis_avm_keychain_.avmkeypair.md#getprivatekeystring)
* [getPublicKey](_apis_avm_keychain_.avmkeypair.md#getpublickey)
* [getPublicKeyString](_apis_avm_keychain_.avmkeypair.md#getpublickeystring)
* [importKey](_apis_avm_keychain_.avmkeypair.md#importkey)
* [recover](_apis_avm_keychain_.avmkeypair.md#recover)
* [setChainID](_apis_avm_keychain_.avmkeypair.md#setchainid)
* [sign](_apis_avm_keychain_.avmkeypair.md#sign)
* [verify](_apis_avm_keychain_.avmkeypair.md#verify)

## Constructors

###  constructor

\+ **new AVMKeyPair**(`chainid`: string, `entropy`: Buffer): *[AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)*

*Overrides [KeyPair](_utils_types_.keypair.md).[constructor](_utils_types_.keypair.md#constructor)*

*Defined in [apis/avm/keychain.ts:191](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L191)*

Class for representing a private and public keypair in Slopes.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`chainid` | string | - |
`entropy` | Buffer |  undefined |

**Returns:** *[AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Inherited from [KeyPair](_utils_types_.keypair.md).[chainid](_utils_types_.keypair.md#protected-chainid)*

*Defined in [utils/types.ts:148](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L148)*

___

### `Protected` keypair

• **keypair**: *elliptic.ec.KeyPair*

*Defined in [apis/avm/keychain.ts:43](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L43)*

___

### `Protected` privk

• **privk**: *Buffer*

*Inherited from [KeyPair](_utils_types_.keypair.md).[privk](_utils_types_.keypair.md#protected-privk)*

*Defined in [utils/types.ts:147](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L147)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Inherited from [KeyPair](_utils_types_.keypair.md).[pubk](_utils_types_.keypair.md#protected-pubk)*

*Defined in [utils/types.ts:146](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L146)*

## Methods

###  addressFromPublicKey

▸ **addressFromPublicKey**(`pubk`: Buffer): *Buffer*

*Defined in [apis/avm/keychain.ts:114](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L114)*

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

*Overrides [KeyPair](_utils_types_.keypair.md).[generateKey](_utils_types_.keypair.md#generatekey)*

*Defined in [apis/avm/keychain.ts:65](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L65)*

Generates a new keypair.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`entropy?` | Buffer | Optional parameter that may be necessary to produce secure keys  |

**Returns:** *void*

___

###  getAddress

▸ **getAddress**(): *Buffer*

*Overrides [KeyPair](_utils_types_.keypair.md).[getAddress](_utils_types_.keypair.md#getaddress)*

*Defined in [apis/avm/keychain.ts:93](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L93)*

Returns the address as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representation of the address

___

###  getAddressString

▸ **getAddressString**(): *string*

*Overrides [KeyPair](_utils_types_.keypair.md).[getAddressString](_utils_types_.keypair.md#getaddressstring)*

*Defined in [apis/avm/keychain.ts:102](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L102)*

Returns the address's string representation.

**Returns:** *string*

A string representation of the address

___

###  getChainID

▸ **getChainID**(): *string*

*Inherited from [KeyPair](_utils_types_.keypair.md)*

*Defined in [utils/types.ts:246](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L246)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](_utils_types_.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Inherited from [KeyPair](_utils_types_.keypair.md)*

*Defined in [utils/types.ts:200](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L200)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPrivateKeyString

▸ **getPrivateKeyString**(): *string*

*Overrides [KeyPair](_utils_types_.keypair.md).[getPrivateKeyString](_utils_types_.keypair.md#getprivatekeystring)*

*Defined in [apis/avm/keychain.ts:136](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L136)*

Returns a string representation of the private key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Inherited from [KeyPair](_utils_types_.keypair.md)*

*Defined in [utils/types.ts:209](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L209)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  getPublicKeyString

▸ **getPublicKeyString**(): *string*

*Overrides [KeyPair](_utils_types_.keypair.md).[getPublicKeyString](_utils_types_.keypair.md#getpublickeystring)*

*Defined in [apis/avm/keychain.ts:145](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L145)*

Returns the public key.

**Returns:** *string*

An AVA serialized string representation of the public key

___

###  importKey

▸ **importKey**(`privk`: Buffer): *boolean*

*Overrides [KeyPair](_utils_types_.keypair.md).[importKey](_utils_types_.keypair.md#importkey)*

*Defined in [apis/avm/keychain.ts:80](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L80)*

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

*Overrides [KeyPair](_utils_types_.keypair.md).[recover](_utils_types_.keypair.md#recover)*

*Defined in [apis/avm/keychain.ts:187](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L187)*

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

*Inherited from [KeyPair](_utils_types_.keypair.md)*

*Defined in [utils/types.ts:255](https://github.com/ava-labs/slopes/blob/2d2915d/src/utils/types.ts#L255)*

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*

___

###  sign

▸ **sign**(`msg`: Buffer): *Buffer*

*Overrides [KeyPair](_utils_types_.keypair.md).[sign](_utils_types_.keypair.md#sign)*

*Defined in [apis/avm/keychain.ts:156](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L156)*

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

*Overrides [KeyPair](_utils_types_.keypair.md).[verify](_utils_types_.keypair.md#verify)*

*Defined in [apis/avm/keychain.ts:174](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/keychain.ts#L174)*

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message associated with the signature |
`sig` | Buffer | The signature of the signed message  |

**Returns:** *boolean*

True on success, false on failure
