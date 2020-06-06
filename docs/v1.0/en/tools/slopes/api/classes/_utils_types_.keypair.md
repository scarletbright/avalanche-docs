[slopes - v1.7.2](../README.md) › ["utils/types"](../modules/_utils_types_.md) › [KeyPair](_utils_types_.keypair.md)

# Class: KeyPair

Class for representing a private and public keypair in Slopes.
All APIs that need key pairs should extend on this class.

## Hierarchy

* **KeyPair**

  ↳ [AVMKeyPair](_apis_avm_keychain_.avmkeypair.md)

## Index

### Constructors

* [constructor](_utils_types_.keypair.md#constructor)

### Properties

* [chainid](_utils_types_.keypair.md#protected-chainid)
* [generateKey](_utils_types_.keypair.md#generatekey)
* [getAddress](_utils_types_.keypair.md#getaddress)
* [getAddressString](_utils_types_.keypair.md#getaddressstring)
* [getPrivateKeyString](_utils_types_.keypair.md#getprivatekeystring)
* [getPublicKeyString](_utils_types_.keypair.md#getpublickeystring)
* [importKey](_utils_types_.keypair.md#importkey)
* [privk](_utils_types_.keypair.md#protected-privk)
* [pubk](_utils_types_.keypair.md#protected-pubk)
* [recover](_utils_types_.keypair.md#recover)
* [sign](_utils_types_.keypair.md#sign)
* [verify](_utils_types_.keypair.md#verify)

### Methods

* [getChainID](_utils_types_.keypair.md#getchainid)
* [getPrivateKey](_utils_types_.keypair.md#getprivatekey)
* [getPublicKey](_utils_types_.keypair.md#getpublickey)
* [setChainID](_utils_types_.keypair.md#setchainid)

## Constructors

###  constructor

\+ **new KeyPair**(`chainid`: string): *[KeyPair](_utils_types_.keypair.md)*

*Defined in [utils/types.ts:257](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L257)*

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[KeyPair](_utils_types_.keypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Defined in [utils/types.ts:148](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L148)*

___

###  generateKey

• **generateKey**: *function*

*Defined in [utils/types.ts:155](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L155)*

Generates a new keypair.

**`param`** Optional parameter that may be necessary to produce secure keys

#### Type declaration:

▸ (`entropy?`: Buffer): *void*

**Parameters:**

Name | Type |
------ | ------ |
`entropy?` | Buffer |

___

###  getAddress

• **getAddress**: *function*

*Defined in [utils/types.ts:232](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L232)*

Returns the address.

**`returns`** A [Buffer](https://github.com/feross/buffer)  representation of the address

#### Type declaration:

▸ (): *Buffer*

___

###  getAddressString

• **getAddressString**: *function*

*Defined in [utils/types.ts:239](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L239)*

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

###  getPrivateKeyString

• **getPrivateKeyString**: *function*

*Defined in [utils/types.ts:218](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L218)*

Returns a string representation of the private key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  getPublicKeyString

• **getPublicKeyString**: *function*

*Defined in [utils/types.ts:225](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L225)*

Returns the public key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  importKey

• **importKey**: *function*

*Defined in [utils/types.ts:163](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L163)*

Imports a private key and generates the appropriate public key.

**`param`** A [Buffer](https://github.com/feross/buffer) representing the private key

**`returns`** true on success, false on failure

#### Type declaration:

▸ (`privk`: Buffer): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`privk` | Buffer |

___

### `Protected` privk

• **privk**: *Buffer*

*Defined in [utils/types.ts:147](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L147)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Defined in [utils/types.ts:146](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L146)*

___

###  recover

• **recover**: *function*

*Defined in [utils/types.ts:182](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L182)*

Recovers the public key of a message signer from a message and its associated signature.

**`param`** The message that's signed

**`param`** The signature that's signed on the message

**`returns`** A [Buffer](https://github.com/feross/buffer) containing the public key of the signer

#### Type declaration:

▸ (`msg`: Buffer, `sig`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |
`sig` | Buffer |

___

###  sign

• **sign**: *function*

*Defined in [utils/types.ts:172](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L172)*

Takes a message, signs it, and returns the signature.

**`param`** The message to sign

**`returns`** A [Buffer](https://github.com/feross/buffer) containing the signature

#### Type declaration:

▸ (`msg`: Buffer): *Buffer*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |

___

###  verify

• **verify**: *function*

*Defined in [utils/types.ts:193](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L193)*

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**`param`** The message associated with the signature

**`param`** The signature of the signed message

**`param`** The public key associated with the message signature

**`returns`** True on success, false on failure

#### Type declaration:

▸ (`msg`: Buffer, `sig`: Buffer, `pubk`: Buffer): *boolean*

**Parameters:**

Name | Type |
------ | ------ |
`msg` | Buffer |
`sig` | Buffer |
`pubk` | Buffer |

## Methods

###  getChainID

▸ **getChainID**(): *string*

*Defined in [utils/types.ts:246](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L246)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](_utils_types_.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Defined in [utils/types.ts:200](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L200)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Defined in [utils/types.ts:209](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L209)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Defined in [utils/types.ts:255](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L255)*

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*
