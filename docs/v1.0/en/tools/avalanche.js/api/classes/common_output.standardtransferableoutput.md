[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [StandardTransferableOutput](common_output.standardtransferableoutput.md)

# Class: StandardTransferableOutput

## Hierarchy

* **StandardTransferableOutput**

  ↳ [TransferableOutput](api_avm_outputs.transferableoutput.md)

  ↳ [TransferableOutput](api_platformvm_outputs.transferableoutput.md)

## Index

### Constructors

* [constructor](common_output.standardtransferableoutput.md#constructor)

### Properties

* [assetID](common_output.standardtransferableoutput.md#protected-assetid)
* [output](common_output.standardtransferableoutput.md#protected-output)

### Methods

* [fromBuffer](common_output.standardtransferableoutput.md#abstract-frombuffer)
* [getAssetID](common_output.standardtransferableoutput.md#getassetid)
* [getOutput](common_output.standardtransferableoutput.md#getoutput)
* [toBuffer](common_output.standardtransferableoutput.md#tobuffer)
* [comparator](common_output.standardtransferableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new StandardTransferableOutput**(`assetID`: Buffer, `output`: [Output](common_output.output.md)): *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

Defined in src/common/output.ts:303

Class representing an [StandardTransferableOutput](common_output.standardtransferableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Output](common_output.output.md) |
`output` | [Output](common_output.output.md) | undefined | A number representing the InputID of the [StandardTransferableOutput](common_output.standardtransferableoutput.md)  |

**Returns:** *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

## Properties

### `Protected` assetID

• **assetID**: *Buffer* = undefined

Defined in src/common/output.ts:277

___

### `Protected` output

• **output**: *[Output](common_output.output.md)*

Defined in src/common/output.ts:279

## Methods

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

Defined in src/common/output.ts:295

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset?` | number |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

Defined in src/common/output.ts:290

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

Defined in src/common/output.ts:292

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/common/output.ts:297

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

Defined in src/common/output.ts:284

Returns a function used to sort an array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *function*

▸ (`a`: [StandardTransferableOutput](common_output.standardtransferableoutput.md), `b`: [StandardTransferableOutput](common_output.standardtransferableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardTransferableOutput](common_output.standardtransferableoutput.md) |
`b` | [StandardTransferableOutput](common_output.standardtransferableoutput.md) |
