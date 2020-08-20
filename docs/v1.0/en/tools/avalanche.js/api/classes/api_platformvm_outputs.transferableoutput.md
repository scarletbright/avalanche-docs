[avalanche](../README.md) › [API-PlatformVM-Outputs](../modules/api_platformvm_outputs.md) › [TransferableOutput](api_platformvm_outputs.transferableoutput.md)

# Class: TransferableOutput

## Hierarchy

* [StandardTransferableOutput](common_output.standardtransferableoutput.md)

  ↳ **TransferableOutput**

## Index

### Constructors

* [constructor](api_platformvm_outputs.transferableoutput.md#constructor)

### Properties

* [assetID](api_platformvm_outputs.transferableoutput.md#protected-assetid)
* [output](api_platformvm_outputs.transferableoutput.md#protected-output)

### Methods

* [fromBuffer](api_platformvm_outputs.transferableoutput.md#frombuffer)
* [getAssetID](api_platformvm_outputs.transferableoutput.md#getassetid)
* [getOutput](api_platformvm_outputs.transferableoutput.md#getoutput)
* [toBuffer](api_platformvm_outputs.transferableoutput.md#tobuffer)
* [comparator](api_platformvm_outputs.transferableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableOutput**(`assetID`: Buffer, `output`: [Output](common_output.output.md)): *[TransferableOutput](api_platformvm_outputs.transferableoutput.md)*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[constructor](common_output.standardtransferableoutput.md#constructor)*

Defined in src/common/output.ts:303

Class representing an [StandardTransferableOutput](common_output.standardtransferableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Output](common_output.output.md) |
`output` | [Output](common_output.output.md) | undefined | A number representing the InputID of the [StandardTransferableOutput](common_output.standardtransferableoutput.md)  |

**Returns:** *[TransferableOutput](api_platformvm_outputs.transferableoutput.md)*

## Properties

### `Protected` assetID

• **assetID**: *Buffer* = undefined

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[assetID](common_output.standardtransferableoutput.md#protected-assetid)*

Defined in src/common/output.ts:277

___

### `Protected` output

• **output**: *[Output](common_output.output.md)*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[output](common_output.standardtransferableoutput.md#protected-output)*

Defined in src/common/output.ts:279

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardTransferableOutput](common_output.standardtransferableoutput.md).[fromBuffer](common_output.standardtransferableoutput.md#abstract-frombuffer)*

Defined in src/apis/platformvm/outputs.ts:28

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[getAssetID](common_output.standardtransferableoutput.md#getassetid)*

Defined in src/common/output.ts:290

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[getOutput](common_output.standardtransferableoutput.md#getoutput)*

Defined in src/common/output.ts:292

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[toBuffer](common_output.standardtransferableoutput.md#tobuffer)*

Defined in src/common/output.ts:297

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[comparator](common_output.standardtransferableoutput.md#static-comparator)*

Defined in src/common/output.ts:284

Returns a function used to sort an array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *function*

▸ (`a`: [StandardTransferableOutput](common_output.standardtransferableoutput.md), `b`: [StandardTransferableOutput](common_output.standardtransferableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardTransferableOutput](common_output.standardtransferableoutput.md) |
`b` | [StandardTransferableOutput](common_output.standardtransferableoutput.md) |
