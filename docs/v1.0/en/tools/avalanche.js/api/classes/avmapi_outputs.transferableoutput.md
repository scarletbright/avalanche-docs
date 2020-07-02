[avalanche](../README.md) › [AVMAPI-Outputs](../modules/avmapi_outputs.md) › [TransferableOutput](avmapi_outputs.transferableoutput.md)

# Class: TransferableOutput

## Hierarchy

* **TransferableOutput**

## Index

### Constructors

* [constructor](avmapi_outputs.transferableoutput.md#constructor)

### Properties

* [assetID](avmapi_outputs.transferableoutput.md#protected-assetid)
* [output](avmapi_outputs.transferableoutput.md#protected-output)

### Methods

* [fromBuffer](avmapi_outputs.transferableoutput.md#frombuffer)
* [getAssetID](avmapi_outputs.transferableoutput.md#getassetid)
* [getOutput](avmapi_outputs.transferableoutput.md#getoutput)
* [toBuffer](avmapi_outputs.transferableoutput.md#tobuffer)
* [comparator](avmapi_outputs.transferableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableOutput**(`assetID`: Buffer, `output`: [Output](avmapi_outputs.output.md)): *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

*Defined in [apis/avm/outputs.ts:278](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L278)*

Class representing an [TransferableOutput](avmapi_outputs.transferableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Output](avmapi_outputs.output.md) |
`output` | [Output](avmapi_outputs.output.md) | undefined | A number representing the InputID of the [TransferableOutput](avmapi_outputs.transferableoutput.md)  |

**Returns:** *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

## Properties

### `Protected` assetID

• **assetID**: *Buffer* = Buffer.alloc(AVMConstants.ASSETIDLEN)

*Defined in [apis/avm/outputs.ts:241](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L241)*

___

### `Protected` output

• **output**: *[Output](avmapi_outputs.output.md)*

*Defined in [apis/avm/outputs.ts:242](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L242)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/outputs.ts:263](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L263)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/outputs.ts:255](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L255)*

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](avmapi_outputs.output.md)*

*Defined in [apis/avm/outputs.ts:259](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L259)*

**Returns:** *[Output](avmapi_outputs.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/outputs.ts:272](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L272)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/outputs.ts:247](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/outputs.ts#L247)*

Returns a function used to sort an array of [TransferableOutput](avmapi_outputs.transferableoutput.md)s

**Returns:** *function*

▸ (`a`: [TransferableOutput](avmapi_outputs.transferableoutput.md), `b`: [TransferableOutput](avmapi_outputs.transferableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableOutput](avmapi_outputs.transferableoutput.md) |
`b` | [TransferableOutput](avmapi_outputs.transferableoutput.md) |
