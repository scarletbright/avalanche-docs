[avalanche](../README.md) › [Common-Signature](../modules/common_signature.md) › [SigIdx](common_signature.sigidx.md)

# Class: SigIdx

Type representing a [Signature](common_signature.signature.md) index used in [Input](common_inputs.input.md)

## Hierarchy

* [NBytes](common_nbytes.nbytes.md)

  ↳ **SigIdx**

## Index

### Constructors

* [constructor](common_signature.sigidx.md#constructor)

### Properties

* [bsize](common_signature.sigidx.md#protected-bsize)
* [bytes](common_signature.sigidx.md#protected-bytes)
* [source](common_signature.sigidx.md#source)

### Methods

* [clone](common_signature.sigidx.md#clone)
* [create](common_signature.sigidx.md#create)
* [fromBuffer](common_signature.sigidx.md#frombuffer)
* [fromString](common_signature.sigidx.md#fromstring)
* [getSize](common_signature.sigidx.md#getsize)
* [getSource](common_signature.sigidx.md#getsource)
* [setSource](common_signature.sigidx.md#setsource)
* [toBuffer](common_signature.sigidx.md#tobuffer)
* [toString](common_signature.sigidx.md#tostring)

## Constructors

###  constructor

\+ **new SigIdx**(): *[SigIdx](common_signature.sigidx.md)*

*Overrides [NBytes](common_nbytes.nbytes.md).[constructor](common_nbytes.nbytes.md#constructor)*

*Defined in [src/common/credentials.ts:41](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L41)*

Type representing a [Signature](common_signature.signature.md) index used in [Input](common_inputs.input.md)

**Returns:** *[SigIdx](common_signature.sigidx.md)*

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

___

###  source

• **source**: *Buffer*

*Defined in [src/common/credentials.ts:19](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L19)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [NBytes](common_nbytes.nbytes.md).[clone](common_nbytes.nbytes.md#abstract-clone)*

*Defined in [src/common/credentials.ts:33](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L33)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [NBytes](common_nbytes.nbytes.md).[create](common_nbytes.nbytes.md#abstract-create)*

*Defined in [src/common/credentials.ts:39](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L39)*

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

###  getSource

▸ **getSource**(): *Buffer*

*Defined in [src/common/credentials.ts:31](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L31)*

Retrieves the source address for the signature

**Returns:** *Buffer*

___

###  setSource

▸ **setSource**(`address`: Buffer): *void*

*Defined in [src/common/credentials.ts:24](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/credentials.ts#L24)*

Sets the source address for the signature

**Parameters:**

Name | Type |
------ | ------ |
`address` | Buffer |

**Returns:** *void*

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
