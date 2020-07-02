[avalanche](../README.md) › [AVMAPI-Types](../modules/avmapi_types.md) › [SigIdx](avmapi_types.sigidx.md)

# Class: SigIdx

Type representing a [Signature](avmapi_types.signature.md) index used in [Input](avmapi_inputs.input.md)

## Hierarchy

* [NBytes](utils_types.nbytes.md)

  ↳ **SigIdx**

## Index

### Constructors

* [constructor](avmapi_types.sigidx.md#constructor)

### Properties

* [bsize](avmapi_types.sigidx.md#protected-bsize)
* [bytes](avmapi_types.sigidx.md#protected-bytes)
* [source](avmapi_types.sigidx.md#source)

### Methods

* [fromBuffer](avmapi_types.sigidx.md#frombuffer)
* [fromString](avmapi_types.sigidx.md#fromstring)
* [getSize](avmapi_types.sigidx.md#getsize)
* [getSource](avmapi_types.sigidx.md#getsource)
* [setSource](avmapi_types.sigidx.md#setsource)
* [toBuffer](avmapi_types.sigidx.md#tobuffer)
* [toString](avmapi_types.sigidx.md#tostring)

## Constructors

###  constructor

\+ **new SigIdx**(): *[SigIdx](avmapi_types.sigidx.md)*

*Overrides [NBytes](utils_types.nbytes.md).[constructor](utils_types.nbytes.md#constructor)*

*Defined in [apis/avm/types.ts:35](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L35)*

Type representing a [Signature](avmapi_types.signature.md) index used in [Input](avmapi_inputs.input.md)

**Returns:** *[SigIdx](avmapi_types.sigidx.md)*

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

___

###  source

• **source**: *Buffer*

*Defined in [apis/avm/types.ts:21](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L21)*

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

▸ **fromString**(`b58str`: string): *number*

*Inherited from [NBytes](utils_types.nbytes.md).[fromString](utils_types.nbytes.md#fromstring)*

*Defined in [utils/types.ts:612](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L612)*

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

*Inherited from [NBytes](utils_types.nbytes.md).[getSize](utils_types.nbytes.md#getsize)*

*Defined in [utils/types.ts:603](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L603)*

Returns the length of the [Buffer](https://github.com/feross/buffer).

**Returns:** *number*

The exact length requirement of this class

___

###  getSource

▸ **getSource**(): *Buffer*

*Defined in [apis/avm/types.ts:33](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L33)*

Retrieves the source address for the signature

**Returns:** *Buffer*

___

###  setSource

▸ **setSource**(`address`: Buffer): *void*

*Defined in [apis/avm/types.ts:26](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/types.ts#L26)*

Sets the source address for the signature

**Parameters:**

Name | Type |
------ | ------ |
`address` | Buffer |

**Returns:** *void*

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

*Inherited from [NBytes](utils_types.nbytes.md).[toString](utils_types.nbytes.md#tostring)*

*Defined in [utils/types.ts:660](https://github.com/ava-labs/avalanche.js/blob/c723742/src/utils/types.ts#L660)*

Returns a base-58 string of the stored [Buffer](https://github.com/feross/buffer).

**Returns:** *string*

A base-58 string of the stored [Buffer](https://github.com/feross/buffer)
