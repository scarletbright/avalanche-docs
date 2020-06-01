[slopes - v1.7.1](../README.md) › ["utils/crypto"](../modules/_utils_crypto_.md) › [CryptoHelpers](_utils_crypto_.cryptohelpers.md)

# Class: CryptoHelpers

Helper utility for encryption and password hashing, browser-safe.
Encryption is using XChaCha20Poly1305 with a random public nonce.

## Hierarchy

* **CryptoHelpers**

## Index

### Constructors

* [constructor](_utils_crypto_.cryptohelpers.md#constructor)

### Properties

* [libsodium](_utils_crypto_.cryptohelpers.md#protected-libsodium)
* [memlimit](_utils_crypto_.cryptohelpers.md#protected-memlimit)
* [opslimit](_utils_crypto_.cryptohelpers.md#protected-opslimit)

### Methods

* [_pwcleaner](_utils_crypto_.cryptohelpers.md#_pwcleaner)
* [decrypt](_utils_crypto_.cryptohelpers.md#decrypt)
* [encrypt](_utils_crypto_.cryptohelpers.md#encrypt)
* [getMemoryLimit](_utils_crypto_.cryptohelpers.md#getmemorylimit)
* [getOpsLimit](_utils_crypto_.cryptohelpers.md#getopslimit)
* [makeSalt](_utils_crypto_.cryptohelpers.md#makesalt)
* [pwhash](_utils_crypto_.cryptohelpers.md#pwhash)
* [setMemoryLimit](_utils_crypto_.cryptohelpers.md#setmemorylimit)
* [setOpsLimit](_utils_crypto_.cryptohelpers.md#setopslimit)
* [sha256](_utils_crypto_.cryptohelpers.md#sha256)

## Constructors

###  constructor

\+ **new CryptoHelpers**(): *[CryptoHelpers](_utils_crypto_.cryptohelpers.md)*

*Defined in [utils/crypto.ts:176](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L176)*

**Returns:** *[CryptoHelpers](_utils_crypto_.cryptohelpers.md)*

## Properties

### `Protected` libsodium

• **libsodium**: *"/Users/carloscardona/Sites/AVALabs/slopes/node_modules/@types/libsodium-wrappers/index"*

*Defined in [utils/crypto.ts:16](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L16)*

___

### `Protected` memlimit

• **memlimit**: *number* = 524288000

*Defined in [utils/crypto.ts:14](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L14)*

___

### `Protected` opslimit

• **opslimit**: *number* = 3

*Defined in [utils/crypto.ts:15](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L15)*

## Methods

###  _pwcleaner

▸ **_pwcleaner**(`password`: string, `salt`: Uint8Array): *Promise‹Uint8Array›*

*Defined in [utils/crypto.ts:67](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L67)*

Internal-intended function for cleaning passwords.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`password` | string | - |
`salt` | Uint8Array |   |

**Returns:** *Promise‹Uint8Array›*

___

###  decrypt

▸ **decrypt**(`password`: string, `ciphertext`: Buffer, `salt`: Buffer, `nonce`: Buffer): *Promise‹Buffer›*

*Defined in [utils/crypto.ts:171](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L171)*

Decrypts ciphertext with the provided password, nonce, ans salt.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`password` | string | A string for the password |
`ciphertext` | Buffer | A [Buffer](https://github.com/feross/buffer) for the ciphertext |
`salt` | Buffer | A [Buffer](https://github.com/feross/buffer) for the salt |
`nonce` | Buffer | A [Buffer](https://github.com/feross/buffer) for the nonce  |

**Returns:** *Promise‹Buffer›*

___

###  encrypt

▸ **encrypt**(`password`: string, `plaintext`: Buffer | string, `salt`: Buffer): *Promise‹object›*

*Defined in [utils/crypto.ts:136](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L136)*

Encrypts plaintext with the provided password using XChaCha20Poly1305.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`password` | string | - | A string for the password |
`plaintext` | Buffer &#124; string | - | The plaintext to encrypt |
`salt` | Buffer |  undefined | An optional [Buffer](https://github.com/feross/buffer) for the salt to use in the encryption process  |

**Returns:** *Promise‹object›*

An object containing the "salt", "nonce", and "ciphertext", all as [Buffer](https://github.com/feross/buffer).

___

###  getMemoryLimit

▸ **getMemoryLimit**(): *number*

*Defined in [utils/crypto.ts:21](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L21)*

Retrieves the memory limit that can be spent generating password-safe hashes.

**Returns:** *number*

___

###  getOpsLimit

▸ **getOpsLimit**(): *number*

*Defined in [utils/crypto.ts:37](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L37)*

Retrieves the cpu limit that can be spent generating password-safe hashes.

**Returns:** *number*

___

###  makeSalt

▸ **makeSalt**(): *Promise‹Buffer›*

*Defined in [utils/crypto.ts:101](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L101)*

Generates a randomized [Buffer](https://github.com/feross/buffer) to be used as a salt

**Returns:** *Promise‹Buffer›*

___

###  pwhash

▸ **pwhash**(`password`: string, `salt`: Buffer): *Promise‹object›*

*Defined in [utils/crypto.ts:114](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L114)*

Produces a password-safe hash.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`password` | string | A string for the password |
`salt` | Buffer | An optional [Buffer](https://github.com/feross/buffer) containing a salt used in the password hash  |

**Returns:** *Promise‹object›*

An object containing the "salt" and the "hash" produced by this function, both as [Buffer](https://github.com/feross/buffer).

___

###  setMemoryLimit

▸ **setMemoryLimit**(`memlimit`: number): *void*

*Defined in [utils/crypto.ts:30](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L30)*

Sets the memory limit that can be spent generating password-safe hashes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`memlimit` | number | The number representing the memory limit, in bytes, that the password-safe algorithm can use  |

**Returns:** *void*

___

###  setOpsLimit

▸ **setOpsLimit**(`opslimit`: number): *void*

*Defined in [utils/crypto.ts:46](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L46)*

Retrieves the cpu limit that can be spent generating password-safe hashes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opslimit` | number | The number representing the cpu limit that the password-safe algorithm can use. Lower is faster.  |

**Returns:** *void*

___

###  sha256

▸ **sha256**(`message`: string | Buffer | Uint8Array): *Buffer*

*Defined in [utils/crypto.ts:88](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/crypto.ts#L88)*

A SHA256 helper function.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`message` | string &#124; Buffer &#124; Uint8Array | The message to hash  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the SHA256 hash of the message
