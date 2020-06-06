[slopes - v1.7.2](../README.md) › ["apis/avm/types"](../modules/_apis_avm_types_.md) › [Signature](_apis_avm_types_.signature.md)

# Class: Signature

Signature for a [Tx](_apis_avm_tx_.tx.md)

## Hierarchy

* [NBytes](_utils_types_.nbytes.md)

  ↳ **Signature**

## Index

### Constructors

* [constructor](_apis_avm_types_.signature.md#constructor)

### Properties

* [bsize](_apis_avm_types_.signature.md#protected-bsize)
* [bytes](_apis_avm_types_.signature.md#protected-bytes)

### Methods

* [fromBuffer](_apis_avm_types_.signature.md#frombuffer)
* [fromString](_apis_avm_types_.signature.md#fromstring)
* [getSize](_apis_avm_types_.signature.md#getsize)
* [toBuffer](_apis_avm_types_.signature.md#tobuffer)
* [toString](_apis_avm_types_.signature.md#tostring)

## Constructors

###  constructor

\+ **new Signature**(): *[Signature](_apis_avm_types_.signature.md)*

*Overrides [NBytes](_utils_types_.nbytes.md).[constructor](_utils_types_.nbytes.md#constructor)*

*Defined in [apis/avm/types.ts:49](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/types.ts#L49)*

Signature for a [Tx](_apis_avm_tx_.tx.md)

**Returns:** *[Signature](_apis_avm_types_.signature.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](_utils_types_.nbytes.md).[bsize](_utils_types_.nbytes.md#protected-bsize)*

*Defined in [utils/types.ts:400](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L400)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](_utils_types_.nbytes.md).[bytes](_utils_types_.nbytes.md#protected-bytes)*

*Defined in [utils/types.ts:399](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L399)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](_utils_types_.nbytes.md).[fromBuffer](_utils_types_.nbytes.md#frombuffer)*

*Defined in [utils/types.ts:433](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L433)*

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

*Inherited from [NBytes](_utils_types_.nbytes.md).[fromString](_utils_types_.nbytes.md#fromstring)*

*Defined in [utils/types.ts:416](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L416)*

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

*Inherited from [NBytes](_utils_types_.nbytes.md)*

*Defined in [utils/types.ts:407](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L407)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](_utils_types_.nbytes.md).[toBuffer](_utils_types_.nbytes.md#tobuffer)*

*Defined in [utils/types.ts:455](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L455)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Inherited from [NBytes](_utils_types_.nbytes.md).[toString](_utils_types_.nbytes.md#tostring)*

*Defined in [utils/types.ts:464](https://github.com/ava-labs/slopes/blob/ba50532/src/utils/types.ts#L464)*

Returns a base-58 string of the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
