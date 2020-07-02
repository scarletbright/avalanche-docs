[avalanche](../README.md) › [AVMAPI-Types](../modules/avmapi_types.md) › [UTXOID](avmapi_types.utxoid.md)

# Class: UTXOID

Class for representing a UTXOID used in [[TransferableOp]] types

## Hierarchy

* [NBytes](utils_types.nbytes.md)

  ↳ **UTXOID**

## Index

### Constructors

* [constructor](avmapi_types.utxoid.md#constructor)

### Properties

* [bsize](avmapi_types.utxoid.md#protected-bsize)
* [bytes](avmapi_types.utxoid.md#protected-bytes)

### Methods

* [fromBuffer](avmapi_types.utxoid.md#frombuffer)
* [fromString](avmapi_types.utxoid.md#fromstring)
* [getSize](avmapi_types.utxoid.md#getsize)
* [toBuffer](avmapi_types.utxoid.md#tobuffer)
* [toString](avmapi_types.utxoid.md#tostring)
* [comparitor](avmapi_types.utxoid.md#static-comparitor)

## Constructors

###  constructor

\+ **new UTXOID**(): *[UTXOID](avmapi_types.utxoid.md)*

*Overrides [NBytes](utils_types.nbytes.md).[constructor](utils_types.nbytes.md#constructor)*

*Defined in [apis/avm/types.ts:158](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L158)*

Class for representing a UTXOID used in [[TransferableOp]] types

**Returns:** *[UTXOID](avmapi_types.utxoid.md)*

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

▸ **fromString**(`utxoid`: string): *number*

*Overrides [NBytes](utils_types.nbytes.md).[fromString](utils_types.nbytes.md#fromstring)*

*Defined in [apis/avm/types.ts:142](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L142)*

Takes a base-58 string containing an [UTXOID](avmapi_types.utxoid.md), parses it, populates the class, and returns the length of the UTXOID in bytes.

**Parameters:**

Name | Type |
------ | ------ |
`utxoid` | string |

**Returns:** *number*

The length of the raw [UTXOID](avmapi_types.utxoid.md)

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

*Overrides [NBytes](utils_types.nbytes.md).[toString](utils_types.nbytes.md#tostring)*

*Defined in [apis/avm/types.ts:132](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L132)*

Returns a base-58 representation of the [UTXOID](avmapi_types.utxoid.md).

**Returns:** *string*

___

### `Static` comparitor

▸ **comparitor**(): *function*

*Defined in [apis/avm/types.ts:124](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L124)*

Returns a function used to sort an array of [UTXOID](avmapi_types.utxoid.md)s

**Returns:** *function*

▸ (`a`: [UTXOID](avmapi_types.utxoid.md), `b`: [UTXOID](avmapi_types.utxoid.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [UTXOID](avmapi_types.utxoid.md) |
`b` | [UTXOID](avmapi_types.utxoid.md) |
