[slopes - v1.7.2](../README.md) › ["apis/avm/types"](../modules/_apis_avm_types_.md) › [UTXOID](_apis_avm_types_.utxoid.md)

# Class: UTXOID

Class for representing a UTXOID used in [[TransferableOp]] types

## Hierarchy

* [NBytes](_utils_types_.nbytes.md)

  ↳ **UTXOID**

## Index

### Constructors

* [constructor](_apis_avm_types_.utxoid.md#constructor)

### Properties

* [bsize](_apis_avm_types_.utxoid.md#protected-bsize)
* [bytes](_apis_avm_types_.utxoid.md#protected-bytes)

### Methods

* [fromBuffer](_apis_avm_types_.utxoid.md#frombuffer)
* [fromString](_apis_avm_types_.utxoid.md#fromstring)
* [getSize](_apis_avm_types_.utxoid.md#getsize)
* [toBuffer](_apis_avm_types_.utxoid.md#tobuffer)
* [toString](_apis_avm_types_.utxoid.md#tostring)
* [comparitor](_apis_avm_types_.utxoid.md#static-comparitor)

## Constructors

###  constructor

\+ **new UTXOID**(): *[UTXOID](_apis_avm_types_.utxoid.md)*

*Overrides [NBytes](_utils_types_.nbytes.md).[constructor](_utils_types_.nbytes.md#constructor)*

*Defined in [apis/avm/types.ts:157](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/types.ts#L157)*

Class for representing a UTXOID used in [[TransferableOp]] types

**Returns:** *[UTXOID](_apis_avm_types_.utxoid.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](_utils_types_.nbytes.md).[bsize](_utils_types_.nbytes.md#protected-bsize)*

*Defined in [utils/types.ts:400](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L400)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](_utils_types_.nbytes.md).[bytes](_utils_types_.nbytes.md#protected-bytes)*

*Defined in [utils/types.ts:399](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L399)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](_utils_types_.nbytes.md).[fromBuffer](_utils_types_.nbytes.md#frombuffer)*

*Defined in [utils/types.ts:433](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L433)*

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

*Overrides [NBytes](_utils_types_.nbytes.md).[fromString](_utils_types_.nbytes.md#fromstring)*

*Defined in [apis/avm/types.ts:141](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/types.ts#L141)*

Takes a base-58 string containing an [UTXOID](_apis_avm_types_.utxoid.md), parses it, populates the class, and returns the length of the UTXOID in bytes.

**Parameters:**

Name | Type |
------ | ------ |
`utxoid` | string |

**Returns:** *number*

The length of the raw [UTXOID](_apis_avm_types_.utxoid.md)

___

###  getSize

▸ **getSize**(): *number*

*Inherited from [NBytes](_utils_types_.nbytes.md)*

*Defined in [utils/types.ts:407](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L407)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](_utils_types_.nbytes.md).[toBuffer](_utils_types_.nbytes.md#tobuffer)*

*Defined in [utils/types.ts:455](https://github.com/ava-labs/slopes/blob/65cee65/src/utils/types.ts#L455)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Overrides [NBytes](_utils_types_.nbytes.md).[toString](_utils_types_.nbytes.md#tostring)*

*Defined in [apis/avm/types.ts:131](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/types.ts#L131)*

Returns a base-58 representation of the [UTXOID](_apis_avm_types_.utxoid.md).

**Returns:** *string*

___

### `Static` comparitor

▸ **comparitor**(): *function*

*Defined in [apis/avm/types.ts:123](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/types.ts#L123)*

Returns a function used to sort an array of [UTXOID](_apis_avm_types_.utxoid.md)s

**Returns:** *function*

▸ (`a`: [UTXOID](_apis_avm_types_.utxoid.md), `b`: [UTXOID](_apis_avm_types_.utxoid.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [UTXOID](_apis_avm_types_.utxoid.md) |
`b` | [UTXOID](_apis_avm_types_.utxoid.md) |
