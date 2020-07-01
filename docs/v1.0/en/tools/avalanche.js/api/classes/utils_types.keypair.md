[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [KeyPair](utils_types.keypair.md)

# Class: KeyPair

Class for representing a private and public keypair in Avalanche.
All APIs that need key pairs should extend on this class.

## Hierarchy

* **KeyPair**

  ↳ [AVMKeyPair](avmapi_keychain.avmkeypair.md)

## Index

### Constructors

* [constructor](utils_types.keypair.md#constructor)

### Properties

* [chainid](utils_types.keypair.md#protected-chainid)
* [generateKey](utils_types.keypair.md#generatekey)
* [getAddress](utils_types.keypair.md#getaddress)
* [getAddressString](utils_types.keypair.md#getaddressstring)
* [getPrivateKeyString](utils_types.keypair.md#getprivatekeystring)
* [getPublicKeyString](utils_types.keypair.md#getpublickeystring)
* [importKey](utils_types.keypair.md#importkey)
* [privk](utils_types.keypair.md#protected-privk)
* [pubk](utils_types.keypair.md#protected-pubk)
* [recover](utils_types.keypair.md#recover)
* [sign](utils_types.keypair.md#sign)
* [verify](utils_types.keypair.md#verify)

### Methods

* [getChainID](utils_types.keypair.md#getchainid)
* [getPrivateKey](utils_types.keypair.md#getprivatekey)
* [getPublicKey](utils_types.keypair.md#getpublickey)
* [setChainID](utils_types.keypair.md#setchainid)

## Constructors

###  constructor

\+ **new KeyPair**(`chainid`: string): *[KeyPair](utils_types.keypair.md)*

*Defined in [utils/types.ts:258](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L258)*

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[KeyPair](utils_types.keypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Defined in [utils/types.ts:149](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L149)*

___

###  generateKey

• **generateKey**: *function*

*Defined in [utils/types.ts:156](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L156)*

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

*Defined in [utils/types.ts:233](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L233)*

Returns the address.

**`returns`** A [Buffer](https://github.com/feross/buffer)  representation of the address

#### Type declaration:

▸ (): *Buffer*

___

###  getAddressString

• **getAddressString**: *function*

*Defined in [utils/types.ts:240](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L240)*

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

###  getPrivateKeyString

• **getPrivateKeyString**: *function*

*Defined in [utils/types.ts:219](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L219)*

Returns a string representation of the private key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  getPublicKeyString

• **getPublicKeyString**: *function*

*Defined in [utils/types.ts:226](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L226)*

Returns the public key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  importKey

• **importKey**: *function*

*Defined in [utils/types.ts:164](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L164)*

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

*Defined in [utils/types.ts:148](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L148)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Defined in [utils/types.ts:147](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L147)*

___

###  recover

• **recover**: *function*

*Defined in [utils/types.ts:183](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L183)*

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

*Defined in [utils/types.ts:173](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L173)*

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

*Defined in [utils/types.ts:194](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L194)*

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

*Defined in [utils/types.ts:247](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L247)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](utils_types.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Defined in [utils/types.ts:201](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L201)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Defined in [utils/types.ts:210](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L210)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Defined in [utils/types.ts:256](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L256)*

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*
