[slopes - v1.7.2](../README.md) › ["apis/avm/ops"](../modules/_apis_avm_ops_.md) › [NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md)

# Class: NFTTransferOperation

A [Operation](_apis_avm_ops_.operation.md) class which specifies a NFT Transfer Op.

## Hierarchy

* [Operation](_apis_avm_ops_.operation.md)

  ↳ **NFTTransferOperation**

## Index

### Constructors

* [constructor](_apis_avm_ops_.nfttransferoperation.md#constructor)

### Properties

* [output](_apis_avm_ops_.nfttransferoperation.md#protected-output)
* [sigCount](_apis_avm_ops_.nfttransferoperation.md#protected-sigcount)
* [sigIdxs](_apis_avm_ops_.nfttransferoperation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](_apis_avm_ops_.nfttransferoperation.md#addsignatureidx)
* [fromBuffer](_apis_avm_ops_.nfttransferoperation.md#frombuffer)
* [getCredentialID](_apis_avm_ops_.nfttransferoperation.md#getcredentialid)
* [getOperationID](_apis_avm_ops_.nfttransferoperation.md#getoperationid)
* [getOutput](_apis_avm_ops_.nfttransferoperation.md#getoutput)
* [getSigIdxs](_apis_avm_ops_.nfttransferoperation.md#getsigidxs)
* [toBuffer](_apis_avm_ops_.nfttransferoperation.md#tobuffer)
* [toString](_apis_avm_ops_.nfttransferoperation.md#tostring)
* [comparator](_apis_avm_ops_.nfttransferoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOperation**(`output`: [NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)): *[NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md)*

*Overrides [Operation](_apis_avm_ops_.operation.md).[constructor](_apis_avm_ops_.operation.md#constructor)*

*Defined in [apis/avm/ops.ts:242](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L242)*

An [Operation](_apis_avm_ops_.operation.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`output` | [NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md) |  undefined | An [NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)  |

**Returns:** *[NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md)*

## Properties

### `Protected` output

• **output**: *[NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)*

*Defined in [apis/avm/ops.ts:204](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L204)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Operation](_apis_avm_ops_.operation.md).[sigCount](_apis_avm_ops_.operation.md#protected-sigcount)*

*Defined in [apis/avm/ops.ts:31](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L31)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›* =  []

*Inherited from [Operation](_apis_avm_ops_.operation.md).[sigIdxs](_apis_avm_ops_.operation.md#protected-sigidxs)*

*Defined in [apis/avm/ops.ts:32](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L32)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:53](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L53)*

Creates and adds a [SigIdx](_apis_avm_types_.sigidx.md) to the [Operation](_apis_avm_ops_.operation.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [Operation](_apis_avm_ops_.operation.md).[fromBuffer](_apis_avm_ops_.operation.md#frombuffer)*

*Defined in [apis/avm/ops.ts:220](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L220)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Inherited from [Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:43](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L43)*

**Returns:** *number*

___

###  getOperationID

▸ **getOperationID**(): *number*

*Overrides [Operation](_apis_avm_ops_.operation.md).[getOperationID](_apis_avm_ops_.operation.md#abstract-getoperationid)*

*Defined in [apis/avm/ops.ts:209](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L209)*

Returns the operation ID.

**Returns:** *number*

___

###  getOutput

▸ **getOutput**(): *[NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)*

*Defined in [apis/avm/ops.ts:213](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L213)*

**Returns:** *[NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

*Inherited from [Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:39](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L39)*

Returns the array of [SigIdx](_apis_avm_types_.sigidx.md) for this [Operation](_apis_avm_ops_.operation.md)

**Returns:** *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Operation](_apis_avm_ops_.operation.md).[toBuffer](_apis_avm_ops_.operation.md#tobuffer)*

*Defined in [apis/avm/ops.ts:229](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L229)*

Returns the buffer representing the [NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/ops.ts:240](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L240)*

Returns a base-58 string representing the [NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:90](https://github.com/ava-labs/slopes/blob/2d2915d/src/apis/avm/ops.ts#L90)*

**Returns:** *function*

▸ (`a`: [Operation](_apis_avm_ops_.operation.md), `b`: [Operation](_apis_avm_ops_.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](_apis_avm_ops_.operation.md) |
`b` | [Operation](_apis_avm_ops_.operation.md) |
