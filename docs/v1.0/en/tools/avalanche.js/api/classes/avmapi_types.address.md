[avalanche](../README.md) › [AVMAPI-Types](../modules/avmapi_types.md) › [Address](avmapi_types.address.md)

# Class: Address

Class for representing an address used in [Output](avmapi_outputs.output.md) types

## Hierarchy

* [NBytes](utils_types.nbytes.md)

  ↳ **Address**

## Index

### Constructors

* [constructor](avmapi_types.address.md#constructor)

### Properties

* [bsize](avmapi_types.address.md#protected-bsize)
* [bytes](avmapi_types.address.md#protected-bytes)

### Methods

* [fromBuffer](avmapi_types.address.md#frombuffer)
* [fromString](avmapi_types.address.md#fromstring)
* [getSize](avmapi_types.address.md#getsize)
* [toBuffer](avmapi_types.address.md#tobuffer)
* [toString](avmapi_types.address.md#tostring)
* [comparitor](avmapi_types.address.md#static-comparitor)

## Constructors

###  constructor

\+ **new Address**(): *[Address](avmapi_types.address.md)*

*Overrides [NBytes](utils_types.nbytes.md).[constructor](utils_types.nbytes.md#constructor)*

*Defined in [src/apis/avm/types.ts:132](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L132)*

Class for representing an address used in [Output](avmapi_outputs.output.md) types

**Returns:** *[Address](avmapi_types.address.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](utils_types.nbytes.md).[bsize](utils_types.nbytes.md#protected-bsize)*

*Defined in [src/utils/types.ts:610](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L610)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[bytes](utils_types.nbytes.md#protected-bytes)*

*Defined in [src/utils/types.ts:608](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L608)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[fromBuffer](utils_types.nbytes.md#frombuffer)*

*Defined in [src/utils/types.ts:641](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L641)*

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

*Overrides [NBytes](utils_types.nbytes.md).[fromString](utils_types.nbytes.md#fromstring)*

*Defined in [src/apis/avm/types.ts:116](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L116)*

Takes a base-58 string containing an [Address](avmapi_types.address.md), parses it, populates the class, and returns the length of the Address in bytes.

**Parameters:**

Name | Type |
------ | ------ |
`addr` | string |

**Returns:** *number*

The length of the raw [Address](avmapi_types.address.md)

___

###  getSize

▸ **getSize**(): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[getSize](utils_types.nbytes.md#getsize)*

*Defined in [src/utils/types.ts:617](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L617)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[toBuffer](utils_types.nbytes.md#tobuffer)*

*Defined in [src/utils/types.ts:663](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L663)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Overrides [NBytes](utils_types.nbytes.md).[toString](utils_types.nbytes.md#tostring)*

*Defined in [src/apis/avm/types.ts:105](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L105)*

Returns a base-58 representation of the [Address](avmapi_types.address.md).

**Returns:** *string*

___

### `Static` comparitor

▸ **comparitor**(): *function*

*Defined in [src/apis/avm/types.ts:98](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L98)*

Returns a function used to sort an array of [Address](avmapi_types.address.md)es

**Returns:** *function*

▸ (`a`: [Address](avmapi_types.address.md), `b`: [Address](avmapi_types.address.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Address](avmapi_types.address.md) |
`b` | [Address](avmapi_types.address.md) |
