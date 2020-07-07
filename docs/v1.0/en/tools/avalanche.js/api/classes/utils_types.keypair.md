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

*Defined in [src/utils/types.ts:470](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L470)*

**Parameters:**

Name | Type |
------ | ------ |
`chainid` | string |

**Returns:** *[KeyPair](utils_types.keypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

*Defined in [src/utils/types.ts:364](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L364)*

___

###  generateKey

• **generateKey**: *function*

*Defined in [src/utils/types.ts:371](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L371)*

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

*Defined in [src/utils/types.ts:447](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L447)*

Returns the address.

**`returns`** A [Buffer](https://github.com/feross/buffer)  representation of the address

#### Type declaration:

▸ (): *Buffer*

___

###  getAddressString

• **getAddressString**: *function*

*Defined in [src/utils/types.ts:454](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L454)*

Returns the address's string representation.

**`returns`** A string representation of the address

#### Type declaration:

▸ (): *string*

___

###  getPrivateKeyString

• **getPrivateKeyString**: *function*

*Defined in [src/utils/types.ts:433](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L433)*

Returns a string representation of the private key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  getPublicKeyString

• **getPublicKeyString**: *function*

*Defined in [src/utils/types.ts:440](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L440)*

Returns the public key.

**`returns`** A string representation of the public key

#### Type declaration:

▸ (): *string*

___

###  importKey

• **importKey**: *function*

*Defined in [src/utils/types.ts:380](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L380)*

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

*Defined in [src/utils/types.ts:362](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L362)*

___

### `Protected` pubk

• **pubk**: *Buffer*

*Defined in [src/utils/types.ts:360](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L360)*

___

###  recover

• **recover**: *function*

*Defined in [src/utils/types.ts:400](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L400)*

Recovers the public key of a message signer from a message and its associated signature.

**`param`** The message that's signed

**`param`** The signature that's signed on the message

**`returns`** A [Buffer](https://github.com/feross/buffer) containing the public
key of the signer

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

*Defined in [src/utils/types.ts:389](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L389)*

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

*Defined in [src/utils/types.ts:412](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L412)*

Verifies that the private key associated with the provided public key produces the
signature associated with the given message.

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

*Defined in [src/utils/types.ts:461](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L461)*

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](utils_types.keypair.md)'s chainID

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Defined in [src/utils/types.ts:419](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L419)*

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Defined in [src/utils/types.ts:426](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L426)*

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  setChainID

▸ **setChainID**(`chainid`: string): *void*

*Defined in [src/utils/types.ts:468](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L468)*

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*
