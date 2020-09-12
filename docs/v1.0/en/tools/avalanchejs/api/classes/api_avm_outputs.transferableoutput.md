[avalanche](../README.md) › [API-AVM-Outputs](../modules/api_avm_outputs.md) › [TransferableOutput](api_avm_outputs.transferableoutput.md)

# Class: TransferableOutput

## Hierarchy

  ↳ [StandardTransferableOutput](common_output.standardtransferableoutput.md)

  ↳ **TransferableOutput**

## Index

### Constructors

* [constructor](api_avm_outputs.transferableoutput.md#constructor)

### Properties

* [assetID](api_avm_outputs.transferableoutput.md#protected-assetid)
* [output](api_avm_outputs.transferableoutput.md#protected-output)

### Methods

* [fromBuffer](api_avm_outputs.transferableoutput.md#frombuffer)
* [getAssetID](api_avm_outputs.transferableoutput.md#getassetid)
* [getOutput](api_avm_outputs.transferableoutput.md#getoutput)
* [toBuffer](api_avm_outputs.transferableoutput.md#tobuffer)
* [comparator](api_avm_outputs.transferableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableOutput**(`assetID`: Buffer, `output`: [Output](common_output.output.md)): *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[constructor](common_output.standardtransferableoutput.md#constructor)*

*Overrides [StandardParseableOutput](common_output.standardparseableoutput.md).[constructor](common_output.standardparseableoutput.md#constructor)*

*Defined in [src/common/output.ts:346](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L346)*

Class representing an [StandardTransferableOutput](common_output.standardtransferableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Output](common_output.output.md) |
`output` | [Output](common_output.output.md) | undefined | A number representing the InputID of the [StandardTransferableOutput](common_output.standardtransferableoutput.md)  |

**Returns:** *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

## Properties

### `Protected` assetID

• **assetID**: *Buffer* = undefined

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[assetID](common_output.standardtransferableoutput.md#protected-assetid)*

*Defined in [src/common/output.ts:333](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L333)*

___

### `Protected` output

• **output**: *[Output](common_output.output.md)*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[output](common_output.standardtransferableoutput.md#protected-output)*

*Overrides [StandardParseableOutput](common_output.standardparseableoutput.md).[output](common_output.standardparseableoutput.md#protected-output)*

*Defined in [src/common/output.ts:335](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L335)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardTransferableOutput](common_output.standardtransferableoutput.md).[fromBuffer](common_output.standardtransferableoutput.md#abstract-frombuffer)*

*Defined in [src/apis/avm/outputs.ts:38](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L38)*

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

*Defined in [src/common/output.ts:337](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L337)*

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[getOutput](common_output.standardparseableoutput.md#getoutput)*

*Defined in [src/common/output.ts:307](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L307)*

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardTransferableOutput](common_output.standardtransferableoutput.md).[toBuffer](common_output.standardtransferableoutput.md#tobuffer)*

*Overrides [StandardParseableOutput](common_output.standardparseableoutput.md).[toBuffer](common_output.standardparseableoutput.md#tobuffer)*

*Defined in [src/common/output.ts:342](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L342)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[comparator](common_output.standardparseableoutput.md#static-comparator)*

*Defined in [src/common/output.ts:301](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L301)*

Returns a function used to sort an array of [ParseableOutput](api_platformvm_outputs.parseableoutput.md)s

**Returns:** *function*

▸ (`a`: [StandardParseableOutput](common_output.standardparseableoutput.md), `b`: [StandardParseableOutput](common_output.standardparseableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
`b` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
