[avalanche](../README.md) › [Utils-Crypto](../modules/utils_crypto.md) › [CryptoHelpers](utils_crypto.cryptohelpers.md)

# Class: CryptoHelpers

Helper utility for encryption and password hashing, browser-safe.
Encryption is using XChaCha20Poly1305 with a random public nonce.

## Hierarchy

* **CryptoHelpers**

## Index

### Constructors

* [constructor](utils_crypto.cryptohelpers.md#constructor)

### Properties

* [libsodium](utils_crypto.cryptohelpers.md#protected-libsodium)
* [memlimit](utils_crypto.cryptohelpers.md#protected-memlimit)
* [opslimit](utils_crypto.cryptohelpers.md#protected-opslimit)

### Methods

* [_pwcleaner](utils_crypto.cryptohelpers.md#_pwcleaner)
* [decrypt](utils_crypto.cryptohelpers.md#decrypt)
* [encrypt](utils_crypto.cryptohelpers.md#encrypt)
* [getMemoryLimit](utils_crypto.cryptohelpers.md#getmemorylimit)
* [getOpsLimit](utils_crypto.cryptohelpers.md#getopslimit)
* [makeSalt](utils_crypto.cryptohelpers.md#makesalt)
* [pwhash](utils_crypto.cryptohelpers.md#pwhash)
* [setMemoryLimit](utils_crypto.cryptohelpers.md#setmemorylimit)
* [setOpsLimit](utils_crypto.cryptohelpers.md#setopslimit)
* [sha256](utils_crypto.cryptohelpers.md#sha256)

## Constructors

###  constructor

\+ **new CryptoHelpers**(): *[CryptoHelpers](utils_crypto.cryptohelpers.md)*

*Defined in [utils/crypto.ts:177](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L177)*

**Returns:** *[CryptoHelpers](utils_crypto.cryptohelpers.md)*

## Properties

### `Protected` libsodium

• **libsodium**: *typeof libsodiumWrapper*

*Defined in [utils/crypto.ts:17](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L17)*

___

### `Protected` memlimit

• **memlimit**: *number* = 524288000

*Defined in [utils/crypto.ts:15](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L15)*

___

### `Protected` opslimit

• **opslimit**: *number* = 3

*Defined in [utils/crypto.ts:16](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L16)*

## Methods

###  _pwcleaner

▸ **_pwcleaner**(`password`: string, `salt`: Uint8Array): *Promise‹Uint8Array›*

*Defined in [utils/crypto.ts:68](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L68)*

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

*Defined in [utils/crypto.ts:172](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L172)*

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

*Defined in [utils/crypto.ts:137](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L137)*

Encrypts plaintext with the provided password using XChaCha20Poly1305.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`password` | string | - | A string for the password |
`plaintext` | Buffer &#124; string | - | The plaintext to encrypt |
`salt` | Buffer | undefined | An optional [Buffer](https://github.com/feross/buffer) for the salt to use in the encryption process  |

**Returns:** *Promise‹object›*

An object containing the "salt", "nonce", and "ciphertext", all as [Buffer](https://github.com/feross/buffer).

___

###  getMemoryLimit

▸ **getMemoryLimit**(): *number*

*Defined in [utils/crypto.ts:22](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L22)*

Retrieves the memory limit that can be spent generating password-safe hashes.

**Returns:** *number*

___

###  getOpsLimit

▸ **getOpsLimit**(): *number*

*Defined in [utils/crypto.ts:38](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L38)*

Retrieves the cpu limit that can be spent generating password-safe hashes.

**Returns:** *number*

___

###  makeSalt

▸ **makeSalt**(): *Promise‹Buffer›*

*Defined in [utils/crypto.ts:102](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L102)*

Generates a randomized [Buffer](https://github.com/feross/buffer) to be used as a salt

**Returns:** *Promise‹Buffer›*

___

###  pwhash

▸ **pwhash**(`password`: string, `salt`: Buffer): *Promise‹object›*

*Defined in [utils/crypto.ts:115](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L115)*

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

*Defined in [utils/crypto.ts:31](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L31)*

Sets the memory limit that can be spent generating password-safe hashes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`memlimit` | number | The number representing the memory limit, in bytes, that the password-safe algorithm can use  |

**Returns:** *void*

___

###  setOpsLimit

▸ **setOpsLimit**(`opslimit`: number): *void*

*Defined in [utils/crypto.ts:47](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L47)*

Retrieves the cpu limit that can be spent generating password-safe hashes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opslimit` | number | The number representing the cpu limit that the password-safe algorithm can use. Lower is faster.  |

**Returns:** *void*

___

###  sha256

▸ **sha256**(`message`: string | Buffer | Uint8Array): *Buffer*

*Defined in [utils/crypto.ts:89](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/utils/crypto.ts#L89)*

A SHA256 helper function.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`message` | string &#124; Buffer &#124; Uint8Array | The message to hash  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) containing the SHA256 hash of the message
