[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [Address](common_output.address.md)

# Class: Address

Class for representing an address used in [Output](common_output.output.md) types

## Hierarchy

* [NBytes](common_nbytes.nbytes.md)

  ↳ **Address**

## Index

### Constructors

* [constructor](common_output.address.md#constructor)

### Properties

* [bsize](common_output.address.md#protected-bsize)
* [bytes](common_output.address.md#protected-bytes)

### Methods

* [clone](common_output.address.md#clone)
* [create](common_output.address.md#create)
* [fromBuffer](common_output.address.md#frombuffer)
* [fromString](common_output.address.md#fromstring)
* [getSize](common_output.address.md#getsize)
* [toBuffer](common_output.address.md#tobuffer)
* [toString](common_output.address.md#tostring)
* [comparator](common_output.address.md#static-comparator)

## Constructors

###  constructor

\+ **new Address**(): *[Address](common_output.address.md)*

*Overrides [NBytes](common_nbytes.nbytes.md).[constructor](common_nbytes.nbytes.md#constructor)*

*Defined in [src/common/output.ts:68](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L68)*

Class for representing an address used in [Output](common_output.output.md) types

**Returns:** *[Address](common_output.address.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](common_nbytes.nbytes.md).[bsize](common_nbytes.nbytes.md#protected-bsize)*

*Defined in [src/common/nbytes.ts:25](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L25)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](common_nbytes.nbytes.md).[bytes](common_nbytes.nbytes.md#protected-bytes)*

*Defined in [src/common/nbytes.ts:23](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L23)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [NBytes](common_nbytes.nbytes.md).[clone](common_nbytes.nbytes.md#abstract-clone)*

*Defined in [src/common/output.ts:60](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L60)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [NBytes](common_nbytes.nbytes.md).[create](common_nbytes.nbytes.md#abstract-create)*

*Defined in [src/common/output.ts:66](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L66)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](common_nbytes.nbytes.md).[fromBuffer](common_nbytes.nbytes.md#frombuffer)*

*Defined in [src/common/nbytes.ts:56](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L56)*

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

▸ **fromString**(`addr`: string): *number*

*Overrides [NBytes](common_nbytes.nbytes.md).[fromString](common_nbytes.nbytes.md#fromstring)*

*Defined in [src/common/output.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L42)*

Takes a base-58 string containing an [Address](common_output.address.md), parses it, populates the class, and returns the length of the Address in bytes.

**Parameters:**

Name | Type |
------ | ------ |
`addr` | string |

**Returns:** *number*

The length of the raw [Address](common_output.address.md)

___

###  getSize

▸ **getSize**(): *number*

*Inherited from [NBytes](common_nbytes.nbytes.md).[getSize](common_nbytes.nbytes.md#getsize)*

*Defined in [src/common/nbytes.ts:32](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L32)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](common_nbytes.nbytes.md).[toBuffer](common_nbytes.nbytes.md#tobuffer)*

*Defined in [src/common/nbytes.ts:76](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L76)*

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Overrides [NBytes](common_nbytes.nbytes.md).[toString](common_nbytes.nbytes.md#tostring)*

*Defined in [src/common/output.ts:31](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L31)*

Returns a base-58 representation of the [Address](common_output.address.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/common/output.ts:24](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L24)*

Returns a function used to sort an array of [Address](common_output.address.md)es

**Returns:** *function*

▸ (`a`: [Address](common_output.address.md), `b`: [Address](common_output.address.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Address](common_output.address.md) |
`b` | [Address](common_output.address.md) |
