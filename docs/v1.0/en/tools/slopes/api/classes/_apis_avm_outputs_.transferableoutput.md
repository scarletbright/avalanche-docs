[slopes - v1.7.2](../README.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)

# Class: TransferableOutput

## Hierarchy

* **TransferableOutput**

## Index

### Constructors

* [constructor](_apis_avm_outputs_.transferableoutput.md#constructor)

### Properties

* [assetID](_apis_avm_outputs_.transferableoutput.md#protected-assetid)
* [output](_apis_avm_outputs_.transferableoutput.md#protected-output)

### Methods

* [fromBuffer](_apis_avm_outputs_.transferableoutput.md#frombuffer)
* [getAssetID](_apis_avm_outputs_.transferableoutput.md#getassetid)
* [getOutput](_apis_avm_outputs_.transferableoutput.md#getoutput)
* [toBuffer](_apis_avm_outputs_.transferableoutput.md#tobuffer)
* [comparator](_apis_avm_outputs_.transferableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableOutput**(`assetID`: Buffer, `output`: [Output](_apis_avm_outputs_.output.md)): *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

*Defined in [apis/avm/outputs.ts:277](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L277)*

Class representing an [TransferableOutput](_apis_avm_outputs_.transferableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`assetID` | Buffer |  undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Output](_apis_avm_outputs_.output.md) |
`output` | [Output](_apis_avm_outputs_.output.md) |  undefined | A number representing the InputID of the [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)  |

**Returns:** *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

## Properties

### `Protected` assetID

• **assetID**: *Buffer* =  Buffer.alloc(AVMConstants.ASSETIDLEN)

*Defined in [apis/avm/outputs.ts:240](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L240)*

___

### `Protected` output

• **output**: *[Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:241](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L241)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/outputs.ts:262](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L262)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/outputs.ts:254](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L254)*

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:258](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L258)*

**Returns:** *[Output](_apis_avm_outputs_.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/outputs.ts:271](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L271)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/outputs.ts:246](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/outputs.ts#L246)*

Returns a function used to sort an array of [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s

**Returns:** *function*

▸ (`a`: [TransferableOutput](_apis_avm_outputs_.transferableoutput.md), `b`: [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableOutput](_apis_avm_outputs_.transferableoutput.md) |
`b` | [TransferableOutput](_apis_avm_outputs_.transferableoutput.md) |
