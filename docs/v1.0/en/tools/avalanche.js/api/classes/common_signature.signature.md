[avalanche](../README.md) › [Common-Signature](../modules/common_signature.md) › [Signature](common_signature.signature.md)

# Class: Signature

Signature for a [Tx](api_avm_transactions.tx.md)

## Hierarchy

* [NBytes](common_nbytes.nbytes.md)

  ↳ **Signature**

## Index

### Constructors

* [constructor](common_signature.signature.md#constructor)

### Properties

* [bsize](common_signature.signature.md#protected-bsize)
* [bytes](common_signature.signature.md#protected-bytes)

### Methods

* [clone](common_signature.signature.md#clone)
* [create](common_signature.signature.md#create)
* [fromBuffer](common_signature.signature.md#frombuffer)
* [fromString](common_signature.signature.md#fromstring)
* [getSize](common_signature.signature.md#getsize)
* [toBuffer](common_signature.signature.md#tobuffer)
* [toString](common_signature.signature.md#tostring)

## Constructors

###  constructor

\+ **new Signature**(): *[Signature](common_signature.signature.md)*

*Overrides [NBytes](common_nbytes.nbytes.md).[constructor](common_nbytes.nbytes.md#constructor)*

*Defined in [src/common/credentials.ts:67](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L67)*

Signature for a [Tx](api_avm_transactions.tx.md)

**Returns:** *[Signature](common_signature.signature.md)*

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

*Defined in [src/common/credentials.ts:59](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L59)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [NBytes](common_nbytes.nbytes.md).[create](common_nbytes.nbytes.md#abstract-create)*

*Defined in [src/common/credentials.ts:65](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L65)*

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

▸ **fromString**(`b58str`: string): *number*

*Inherited from [NBytes](common_nbytes.nbytes.md).[fromString](common_nbytes.nbytes.md#fromstring)*

*Defined in [src/common/nbytes.ts:39](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L39)*

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

*Inherited from [NBytes](common_nbytes.nbytes.md).[toString](common_nbytes.nbytes.md#tostring)*

*Defined in [src/common/nbytes.ts:83](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/nbytes.ts#L83)*

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
