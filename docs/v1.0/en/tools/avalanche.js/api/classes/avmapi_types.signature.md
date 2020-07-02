[avalanche](../README.md) › [AVMAPI-Types](../modules/avmapi_types.md) › [Signature](avmapi_types.signature.md)

# Class: Signature

Signature for a [Tx](avmapi_transactions.tx.md)

## Hierarchy

* [NBytes](utils_types.nbytes.md)

  ↳ **Signature**

## Index

### Constructors

* [constructor](avmapi_types.signature.md#constructor)

### Properties

* [bsize](avmapi_types.signature.md#protected-bsize)
* [bytes](avmapi_types.signature.md#protected-bytes)

### Methods

* [fromBuffer](avmapi_types.signature.md#frombuffer)
* [fromString](avmapi_types.signature.md#fromstring)
* [getSize](avmapi_types.signature.md#getsize)
* [toBuffer](avmapi_types.signature.md#tobuffer)
* [toString](avmapi_types.signature.md#tostring)

## Constructors

###  constructor

\+ **new Signature**(): *[Signature](avmapi_types.signature.md)*

*Overrides [NBytes](utils_types.nbytes.md).[constructor](utils_types.nbytes.md#constructor)*

*Defined in [apis/avm/types.ts:50](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L50)*

Signature for a [Tx](avmapi_transactions.tx.md)

**Returns:** *[Signature](avmapi_types.signature.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](utils_types.nbytes.md).[bsize](utils_types.nbytes.md#protected-bsize)*

*Defined in [utils/types.ts:596](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L596)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[bytes](utils_types.nbytes.md#protected-bytes)*

*Defined in [utils/types.ts:595](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L595)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[fromBuffer](utils_types.nbytes.md#frombuffer)*

*Defined in [utils/types.ts:629](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L629)*

Takes a [[Buffer]], verifies its length, and stores it.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`buff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

The size of the [Buffer](https://github.com/feross/buffer)

___

###  fromString

▸ **fromString**(`b58str`: string): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[fromString](utils_types.nbytes.md#fromstring)*

*Defined in [utils/types.ts:612](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L612)*

Takes a base-58 encoded string, verifies its length, and stores it.

**Parameters:**

Name | Type |
------ | ------ |
`b58str` | string |

**Returns:** *number*

The size of the [Buffer](https://github.com/feross/buffer)

___

###  getSize

▸ **getSize**(): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[getSize](utils_types.nbytes.md#getsize)*

*Defined in [utils/types.ts:603](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L603)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[toBuffer](utils_types.nbytes.md#tobuffer)*

*Defined in [utils/types.ts:651](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L651)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Inherited from [NBytes](utils_types.nbytes.md).[toString](utils_types.nbytes.md#tostring)*

*Defined in [utils/types.ts:660](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L660)*

Returns a base-58 string of the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
