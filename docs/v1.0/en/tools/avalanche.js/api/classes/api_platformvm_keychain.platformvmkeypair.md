[avalanche](../README.md) › [API-PlatformVM-KeyChain](../modules/api_platformvm_keychain.md) › [PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)

# Class: PlatformVMKeyPair

Class for representing a private and public keypair on the Platform Chain.

## Hierarchy

  ↳ [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md)

  ↳ **PlatformVMKeyPair**

## Index

### Constructors

* [constructor](api_platformvm_keychain.platformvmkeypair.md#constructor)

### Properties

* [chainid](api_platformvm_keychain.platformvmkeypair.md#protected-chainid)
* [hrp](api_platformvm_keychain.platformvmkeypair.md#protected-hrp)
* [keypair](api_platformvm_keychain.platformvmkeypair.md#protected-keypair)
* [privk](api_platformvm_keychain.platformvmkeypair.md#protected-privk)
* [pubk](api_platformvm_keychain.platformvmkeypair.md#protected-pubk)

### Methods

* [addressFromPublicKey](api_platformvm_keychain.platformvmkeypair.md#addressfrompublickey)
* [generateKey](api_platformvm_keychain.platformvmkeypair.md#generatekey)
* [getAddress](api_platformvm_keychain.platformvmkeypair.md#getaddress)
* [getAddressString](api_platformvm_keychain.platformvmkeypair.md#getaddressstring)
* [getChainID](api_platformvm_keychain.platformvmkeypair.md#getchainid)
* [getHRP](api_platformvm_keychain.platformvmkeypair.md#gethrp)
* [getPrivateKey](api_platformvm_keychain.platformvmkeypair.md#getprivatekey)
* [getPrivateKeyString](api_platformvm_keychain.platformvmkeypair.md#getprivatekeystring)
* [getPublicKey](api_platformvm_keychain.platformvmkeypair.md#getpublickey)
* [getPublicKeyString](api_platformvm_keychain.platformvmkeypair.md#getpublickeystring)
* [importKey](api_platformvm_keychain.platformvmkeypair.md#importkey)
* [recover](api_platformvm_keychain.platformvmkeypair.md#recover)
* [setChainID](api_platformvm_keychain.platformvmkeypair.md#setchainid)
* [setHRP](api_platformvm_keychain.platformvmkeypair.md#sethrp)
* [sign](api_platformvm_keychain.platformvmkeypair.md#sign)
* [verify](api_platformvm_keychain.platformvmkeypair.md#verify)

## Constructors

###  constructor

\+ **new PlatformVMKeyPair**(`hrp`: string, `chainid`: string): *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

*Overrides [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[constructor](platformvmapi_keychain.secp256k1keypair.md#constructor)*

Defined in src/apis/platformvm/keychain.ts:64

**Parameters:**

Name | Type |
------ | ------ |
`hrp` | string |
`chainid` | string |

**Returns:** *[PlatformVMKeyPair](api_platformvm_keychain.platformvmkeypair.md)*

## Properties

### `Protected` chainid

• **chainid**: *string* = ""

Defined in src/apis/platformvm/keychain.ts:20

___

### `Protected` hrp

• **hrp**: *string* = ""

Defined in src/apis/platformvm/keychain.ts:21

___

### `Protected` keypair

• **keypair**: *elliptic.ec.KeyPair*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[keypair](platformvmapi_keychain.secp256k1keypair.md#protected-keypair)*

Defined in src/common/secp256k1.ts:41

___

### `Protected` privk

• **privk**: *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[privk](common_keychain.keypair.md#protected-privk)*

Defined in src/common/keychain.ts:15

___

### `Protected` pubk

• **pubk**: *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[pubk](common_keychain.keypair.md#protected-pubk)*

Defined in src/common/keychain.ts:13

## Methods

###  addressFromPublicKey

▸ **addressFromPublicKey**(`pubk`: Buffer): *Buffer*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[addressFromPublicKey](platformvmapi_keychain.secp256k1keypair.md#addressfrompublickey)*

Defined in src/common/secp256k1.ts:107

Returns an address given a public key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`pubk` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the public key  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) for the address of the public key.

___

###  generateKey

▸ **generateKey**(): *void*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[generateKey](platformvmapi_keychain.secp256k1keypair.md#generatekey)*

*Overrides [KeyPair](common_keychain.keypair.md).[generateKey](common_keychain.keypair.md#generatekey)*

Defined in src/common/secp256k1.ts:61

Generates a new keypair.

**Returns:** *void*

___

###  getAddress

▸ **getAddress**(): *Buffer*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[getAddress](platformvmapi_keychain.secp256k1keypair.md#getaddress)*

*Overrides [KeyPair](common_keychain.keypair.md).[getAddress](common_keychain.keypair.md#getaddress)*

Defined in src/common/secp256k1.ts:89

Returns the address as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representation of the address

___

###  getAddressString

▸ **getAddressString**(): *string*

*Overrides [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[getAddressString](platformvmapi_keychain.secp256k1keypair.md#getaddressstring)*

Defined in src/apis/platformvm/keychain.ts:28

Returns the address's string representation.

**Returns:** *string*

A string representation of the address

___

###  getChainID

▸ **getChainID**(): *string*

Defined in src/apis/platformvm/keychain.ts:38

Returns the chainID associated with this key.

**Returns:** *string*

The [KeyPair](common_keychain.keypair.md)'s chainID

___

###  getHRP

▸ **getHRP**(): *string*

Defined in src/apis/platformvm/keychain.ts:55

Returns the Human-Readable-Part of the network associated with this key.

**Returns:** *string*

The [KeyPair](common_keychain.keypair.md)'s Human-Readable-Part of the network's Bech32 addressing scheme

___

###  getPrivateKey

▸ **getPrivateKey**(): *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[getPrivateKey](common_keychain.keypair.md#getprivatekey)*

Defined in src/common/keychain.ts:70

Returns a reference to the private key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the private key

___

###  getPrivateKeyString

▸ **getPrivateKeyString**(): *string*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[getPrivateKeyString](platformvmapi_keychain.secp256k1keypair.md#getprivatekeystring)*

*Overrides [KeyPair](common_keychain.keypair.md).[getPrivateKeyString](common_keychain.keypair.md#getprivatekeystring)*

Defined in src/common/secp256k1.ts:126

Returns a string representation of the private key.

**Returns:** *string*

A cb58 serialized string representation of the public key

___

###  getPublicKey

▸ **getPublicKey**(): *Buffer*

*Inherited from [KeyPair](common_keychain.keypair.md).[getPublicKey](common_keychain.keypair.md#getpublickey)*

Defined in src/common/keychain.ts:77

Returns a reference to the public key.

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the public key

___

###  getPublicKeyString

▸ **getPublicKeyString**(): *string*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[getPublicKeyString](platformvmapi_keychain.secp256k1keypair.md#getpublickeystring)*

*Overrides [KeyPair](common_keychain.keypair.md).[getPublicKeyString](common_keychain.keypair.md#getpublickeystring)*

Defined in src/common/secp256k1.ts:135

Returns the public key.

**Returns:** *string*

A cb58 serialized string representation of the public key

___

###  importKey

▸ **importKey**(`privk`: Buffer): *boolean*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[importKey](platformvmapi_keychain.secp256k1keypair.md#importkey)*

*Overrides [KeyPair](common_keychain.keypair.md).[importKey](common_keychain.keypair.md#importkey)*

Defined in src/common/secp256k1.ts:76

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

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[recover](platformvmapi_keychain.secp256k1keypair.md#recover)*

*Overrides [KeyPair](common_keychain.keypair.md).[recover](common_keychain.keypair.md#recover)*

Defined in src/common/secp256k1.ts:178

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

Defined in src/apis/platformvm/keychain.ts:45

Sets the the chainID associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`chainid` | string | String for the chainID  |

**Returns:** *void*

___

###  setHRP

▸ **setHRP**(`hrp`: string): *void*

Defined in src/apis/platformvm/keychain.ts:62

Sets the the Human-Readable-Part of the network associated with this key.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`hrp` | string | String for the Human-Readable-Part of Bech32 addresses  |

**Returns:** *void*

___

###  sign

▸ **sign**(`msg`: Buffer): *Buffer*

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[sign](platformvmapi_keychain.secp256k1keypair.md#sign)*

*Overrides [KeyPair](common_keychain.keypair.md).[sign](common_keychain.keypair.md#sign)*

Defined in src/common/secp256k1.ts:147

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

*Inherited from [SECP256k1KeyPair](platformvmapi_keychain.secp256k1keypair.md).[verify](platformvmapi_keychain.secp256k1keypair.md#verify)*

*Overrides [KeyPair](common_keychain.keypair.md).[verify](common_keychain.keypair.md#verify)*

Defined in src/common/secp256k1.ts:165

Verifies that the private key associated with the provided public key produces the signature associated with the given message.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | The message associated with the signature |
`sig` | Buffer | The signature of the signed message  |

**Returns:** *boolean*

True on success, false on failure
