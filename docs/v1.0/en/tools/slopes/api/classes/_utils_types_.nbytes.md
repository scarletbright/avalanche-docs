[slopes - v1.7.1](../README.md) › ["utils/types"](../modules/_utils_types_.md) › [NBytes](_utils_types_.nbytes.md)

# Class: NBytes

Abstract class that implements basic functionality for managing a [Buffer](https://github.com/feross/buffer) of an exact length.

Create a class that extends this one and override bsize to make it validate for exactly the correct length.

## Hierarchy

* **NBytes**

  ↳ [SigIdx](_apis_avm_types_.sigidx.md)

  ↳ [Signature](_apis_avm_types_.signature.md)

  ↳ [Address](_apis_avm_types_.address.md)

  ↳ [UTXOID](_apis_avm_types_.utxoid.md)

## Index

### Constructors

* [constructor](_utils_types_.nbytes.md#constructor)

### Properties

* [bsize](_utils_types_.nbytes.md#protected-bsize)
* [bytes](_utils_types_.nbytes.md#protected-bytes)

### Methods

* [fromBuffer](_utils_types_.nbytes.md#frombuffer)
* [fromString](_utils_types_.nbytes.md#fromstring)
* [getSize](_utils_types_.nbytes.md#getsize)
* [toBuffer](_utils_types_.nbytes.md#tobuffer)
* [toString](_utils_types_.nbytes.md#tostring)

## Constructors

###  constructor

\+ **new NBytes**(): *[NBytes](_utils_types_.nbytes.md)*

*Defined in [utils/types.ts:466](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L466)*

Returns instance of [NBytes](_utils_types_.nbytes.md).

**Returns:** *[NBytes](_utils_types_.nbytes.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Defined in [utils/types.ts:400](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L400)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Defined in [utils/types.ts:399](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L399)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Defined in [utils/types.ts:433](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L433)*

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

*Defined in [utils/types.ts:416](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L416)*

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

*Defined in [utils/types.ts:407](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L407)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [utils/types.ts:455](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L455)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Defined in [utils/types.ts:464](https://github.com/ava-labs/slopes/blob/0d1acbd/src/utils/types.ts#L464)*

Returns a base-58 string of the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
