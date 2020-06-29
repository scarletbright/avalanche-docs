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

*Defined in [apis/avm/types.ts:104](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/types.ts#L104)*

Class for representing an address used in [Output](avmapi_outputs.output.md) types

**Returns:** *[Address](avmapi_types.address.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Inherited from [NBytes](utils_types.nbytes.md).[bsize](utils_types.nbytes.md#protected-bsize)*

*Defined in [utils/types.ts:401](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L401)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[bytes](utils_types.nbytes.md#protected-bytes)*

*Defined in [utils/types.ts:400](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L400)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[fromBuffer](utils_types.nbytes.md#frombuffer)*

*Defined in [utils/types.ts:434](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L434)*

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

*Defined in [apis/avm/types.ts:88](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/types.ts#L88)*

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

*Defined in [utils/types.ts:408](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L408)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [NBytes](utils_types.nbytes.md).[toBuffer](utils_types.nbytes.md#tobuffer)*

*Defined in [utils/types.ts:456](https://github.com/ava-labs/avalanche.js/blob/3888064/src/utils/types.ts#L456)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Overrides [NBytes](utils_types.nbytes.md).[toString](utils_types.nbytes.md#tostring)*

*Defined in [apis/avm/types.ts:78](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/types.ts#L78)*

Returns a base-58 representation of the [Address](avmapi_types.address.md).

**Returns:** *string*

___

### `Static` comparitor

▸ **comparitor**(): *function*

*Defined in [apis/avm/types.ts:70](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/types.ts#L70)*

Returns a function used to sort an array of [Address](avmapi_types.address.md)es

**Returns:** *function*

▸ (`a`: [Address](avmapi_types.address.md), `b`: [Address](avmapi_types.address.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Address](avmapi_types.address.md) |
`b` | [Address](avmapi_types.address.md) |
