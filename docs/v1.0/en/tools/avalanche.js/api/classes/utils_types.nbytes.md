[avalanche](../README.md) › [Utils-Types](../modules/utils_types.md) › [NBytes](utils_types.nbytes.md)

# Class: NBytes

Abstract class that implements basic functionality for managing a
[Buffer](https://github.com/feross/buffer) of an exact length.

Create a class that extends this one and override bsize to make it validate for exactly
the correct length.

## Hierarchy

* **NBytes**

  ↳ [SigIdx](avmapi_types.sigidx.md)

  ↳ [Signature](avmapi_types.signature.md)

  ↳ [Address](avmapi_types.address.md)

  ↳ [UTXOID](avmapi_types.utxoid.md)

## Index

### Constructors

* [constructor](utils_types.nbytes.md#constructor)

### Properties

* [bsize](utils_types.nbytes.md#protected-bsize)
* [bytes](utils_types.nbytes.md#protected-bytes)

### Methods

* [fromBuffer](utils_types.nbytes.md#frombuffer)
* [fromString](utils_types.nbytes.md#fromstring)
* [getSize](utils_types.nbytes.md#getsize)
* [toBuffer](utils_types.nbytes.md#tobuffer)
* [toString](utils_types.nbytes.md#tostring)

## Constructors

###  constructor

\+ **new NBytes**(): *[NBytes](utils_types.nbytes.md)*

*Defined in [src/utils/types.ts:674](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L674)*

Returns instance of [NBytes](utils_types.nbytes.md).

**Returns:** *[NBytes](utils_types.nbytes.md)*

## Properties

### `Protected` bsize

• **bsize**: *number*

*Defined in [src/utils/types.ts:610](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L610)*

___

### `Protected` bytes

• **bytes**: *Buffer*

*Defined in [src/utils/types.ts:608](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L608)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`buff`: Buffer, `offset`: number): *number*

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

▸ **fromString**(`b58str`: string): *number*

*Defined in [src/utils/types.ts:624](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L624)*

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

*Defined in [src/utils/types.ts:617](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L617)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/utils/types.ts:663](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L663)*

Returns the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

A reference to the stored [Buffer](https://github.com/feross/buffer)

___

###  toString

▸ **toString**(): *string*

*Defined in [src/utils/types.ts:672](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/utils/types.ts#L672)*

Returns a base-58 string of the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
