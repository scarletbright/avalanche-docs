[avalanche](../README.md) › [AVMAPI-Operations](../modules/avmapi_operations.md) › [NFTTransferOperation](avmapi_operations.nfttransferoperation.md)

# Class: NFTTransferOperation

A [Operation](avmapi_operations.operation.md) class which specifies a NFT Transfer Op.

## Hierarchy

* [Operation](avmapi_operations.operation.md)

  ↳ **NFTTransferOperation**

## Index

### Constructors

* [constructor](avmapi_operations.nfttransferoperation.md#constructor)

### Properties

* [output](avmapi_operations.nfttransferoperation.md#protected-output)
* [sigCount](avmapi_operations.nfttransferoperation.md#protected-sigcount)
* [sigIdxs](avmapi_operations.nfttransferoperation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](avmapi_operations.nfttransferoperation.md#addsignatureidx)
* [fromBuffer](avmapi_operations.nfttransferoperation.md#frombuffer)
* [getCredentialID](avmapi_operations.nfttransferoperation.md#getcredentialid)
* [getOperationID](avmapi_operations.nfttransferoperation.md#getoperationid)
* [getOutput](avmapi_operations.nfttransferoperation.md#getoutput)
* [getSigIdxs](avmapi_operations.nfttransferoperation.md#getsigidxs)
* [toBuffer](avmapi_operations.nfttransferoperation.md#tobuffer)
* [toString](avmapi_operations.nfttransferoperation.md#tostring)
* [comparator](avmapi_operations.nfttransferoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOperation**(`output`: [NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)): *[NFTTransferOperation](avmapi_operations.nfttransferoperation.md)*

*Overrides [Operation](avmapi_operations.operation.md).[constructor](avmapi_operations.operation.md#constructor)*

*Defined in [src/apis/avm/ops.ts:231](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L231)*

An [Operation](avmapi_operations.operation.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`output` | [NFTTransferOutput](avmapi_outputs.nfttransferoutput.md) | undefined | An [NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)  |

**Returns:** *[NFTTransferOperation](avmapi_operations.nfttransferoperation.md)*

## Properties

### `Protected` output

• **output**: *[NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)*

*Defined in [src/apis/avm/ops.ts:195](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L195)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Operation](avmapi_operations.operation.md).[sigCount](avmapi_operations.operation.md#protected-sigcount)*

*Defined in [src/apis/avm/ops.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Inherited from [Operation](avmapi_operations.operation.md).[sigIdxs](avmapi_operations.operation.md#protected-sigidxs)*

*Defined in [src/apis/avm/ops.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L34)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Operation](avmapi_operations.operation.md).[addSignatureIdx](avmapi_operations.operation.md#addsignatureidx)*

*Defined in [src/apis/avm/ops.ts:51](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L51)*

Creates and adds a [SigIdx](avmapi_types.sigidx.md) to the [Operation](avmapi_operations.operation.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [Operation](avmapi_operations.operation.md).[fromBuffer](avmapi_operations.operation.md#frombuffer)*

*Defined in [src/apis/avm/ops.ts:209](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L209)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTTransferOperation](avmapi_operations.nfttransferoperation.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Inherited from [Operation](avmapi_operations.operation.md).[getCredentialID](avmapi_operations.operation.md#getcredentialid)*

*Defined in [src/apis/avm/ops.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L43)*

**Returns:** *number*

___

###  getOperationID

▸ **getOperationID**(): *number*

*Overrides [Operation](avmapi_operations.operation.md).[getOperationID](avmapi_operations.operation.md#abstract-getoperationid)*

*Defined in [src/apis/avm/ops.ts:200](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L200)*

Returns the operation ID.

**Returns:** *number*

___

###  getOutput

▸ **getOutput**(): *[NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)*

*Defined in [src/apis/avm/ops.ts:204](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L204)*

**Returns:** *[NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Inherited from [Operation](avmapi_operations.operation.md).[getSigIdxs](avmapi_operations.operation.md#getsigidxs)*

*Defined in [src/apis/avm/ops.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L41)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Operation](avmapi_operations.operation.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Operation](avmapi_operations.operation.md).[toBuffer](avmapi_operations.operation.md#tobuffer)*

*Defined in [src/apis/avm/ops.ts:218](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L218)*

Returns the buffer representing the [NFTTransferOperation](avmapi_operations.nfttransferoperation.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/ops.ts:229](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L229)*

Returns a base-58 string representing the [NFTTransferOperation](avmapi_operations.nfttransferoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Operation](avmapi_operations.operation.md).[comparator](avmapi_operations.operation.md#static-comparator)*

*Defined in [src/apis/avm/ops.ts:88](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L88)*

**Returns:** *function*

▸ (`a`: [Operation](avmapi_operations.operation.md), `b`: [Operation](avmapi_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](avmapi_operations.operation.md) |
`b` | [Operation](avmapi_operations.operation.md) |
