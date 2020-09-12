[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [SECPMintOperation](api_avm_operations.secpmintoperation.md)

# Class: SECPMintOperation

An [Operation](api_avm_operations.operation.md) class which specifies a SECP256k1 Mint Op.

## Hierarchy

* [Operation](api_avm_operations.operation.md)

  ↳ **SECPMintOperation**

## Index

### Constructors

* [constructor](api_avm_operations.secpmintoperation.md#constructor)

### Properties

* [mintOutput](api_avm_operations.secpmintoperation.md#protected-mintoutput)
* [sigCount](api_avm_operations.secpmintoperation.md#protected-sigcount)
* [sigIdxs](api_avm_operations.secpmintoperation.md#protected-sigidxs)
* [transferOutputs](api_avm_operations.secpmintoperation.md#protected-transferoutputs)

### Methods

* [addSignatureIdx](api_avm_operations.secpmintoperation.md#addsignatureidx)
* [fromBuffer](api_avm_operations.secpmintoperation.md#frombuffer)
* [getCredentialID](api_avm_operations.secpmintoperation.md#getcredentialid)
* [getMintOutput](api_avm_operations.secpmintoperation.md#getmintoutput)
* [getOperationID](api_avm_operations.secpmintoperation.md#getoperationid)
* [getSigIdxs](api_avm_operations.secpmintoperation.md#getsigidxs)
* [getTransferOutputs](api_avm_operations.secpmintoperation.md#gettransferoutputs)
* [toBuffer](api_avm_operations.secpmintoperation.md#tobuffer)
* [toString](api_avm_operations.secpmintoperation.md#tostring)
* [comparator](api_avm_operations.secpmintoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new SECPMintOperation**(`mintOutput`: [SECPMintOutput](api_avm_outputs.secpmintoutput.md), `transferOutputs`: Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)›): *[SECPMintOperation](api_avm_operations.secpmintoperation.md)*

*Overrides [Operation](api_avm_operations.operation.md).[constructor](api_avm_operations.operation.md#constructor)*

*Defined in [src/apis/avm/ops.ts:292](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L292)*

An [Operation](api_avm_operations.operation.md) class which mints new tokens on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`mintOutput` | [SECPMintOutput](api_avm_outputs.secpmintoutput.md) | undefined | The [SECPMintOutput](api_avm_outputs.secpmintoutput.md) that will be produced by this transaction. |
`transferOutputs` | Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)› | undefined | An array of [SECPTransferOutput](api_avm_outputs.secptransferoutput.md)s that will be produced from this minting operation.  |

**Returns:** *[SECPMintOperation](api_avm_operations.secpmintoperation.md)*

## Properties

### `Protected` mintOutput

• **mintOutput**: *[SECPMintOutput](api_avm_outputs.secpmintoutput.md)* = undefined

*Defined in [src/apis/avm/ops.ts:221](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L221)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Operation](api_avm_operations.operation.md).[sigCount](api_avm_operations.operation.md#protected-sigcount)*

*Defined in [src/apis/avm/ops.ts:38](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L38)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

*Inherited from [Operation](api_avm_operations.operation.md).[sigIdxs](api_avm_operations.operation.md#protected-sigidxs)*

*Defined in [src/apis/avm/ops.ts:40](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L40)*

___

### `Protected` transferOutputs

• **transferOutputs**: *Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)›* = []

*Defined in [src/apis/avm/ops.ts:222](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L222)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Operation](api_avm_operations.operation.md).[addSignatureIdx](api_avm_operations.operation.md#addsignatureidx)*

*Defined in [src/apis/avm/ops.ts:60](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L60)*

Creates and adds a [SigIdx](common_signature.sigidx.md) to the [Operation](api_avm_operations.operation.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [Operation](api_avm_operations.operation.md).[fromBuffer](api_avm_operations.operation.md#frombuffer)*

*Defined in [src/apis/avm/ops.ts:255](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L255)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [SECPMintOperation](api_avm_operations.secpmintoperation.md) and returns the updated offset.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Overrides [Operation](api_avm_operations.operation.md).[getCredentialID](api_avm_operations.operation.md#abstract-getcredentialid)*

*Defined in [src/apis/avm/ops.ts:234](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L234)*

Returns the credential ID.

**Returns:** *number*

___

###  getMintOutput

▸ **getMintOutput**(): *[SECPMintOutput](api_avm_outputs.secpmintoutput.md)*

*Defined in [src/apis/avm/ops.ts:241](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L241)*

Returns the [SECPMintOutput](api_avm_outputs.secpmintoutput.md) to be produced by this operation.

**Returns:** *[SECPMintOutput](api_avm_outputs.secpmintoutput.md)*

___

###  getOperationID

▸ **getOperationID**(): *number*

*Overrides [Operation](api_avm_operations.operation.md).[getOperationID](api_avm_operations.operation.md#abstract-getoperationid)*

*Defined in [src/apis/avm/ops.ts:227](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L227)*

Returns the operation ID.

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

*Inherited from [Operation](api_avm_operations.operation.md).[getSigIdxs](api_avm_operations.operation.md#getsigidxs)*

*Defined in [src/apis/avm/ops.ts:47](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L47)*

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Operation](api_avm_operations.operation.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

###  getTransferOutputs

▸ **getTransferOutputs**(): *Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)›*

*Defined in [src/apis/avm/ops.ts:248](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L248)*

Returns the array of [SECPTransferOutput](api_avm_outputs.secptransferoutput.md)s to be produced by this operation.

**Returns:** *Array‹[SECPTransferOutput](api_avm_outputs.secptransferoutput.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Operation](api_avm_operations.operation.md).[toBuffer](api_avm_operations.operation.md#tobuffer)*

*Defined in [src/apis/avm/ops.ts:273](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L273)*

Returns the buffer representing the [SECPMintOperation](api_avm_operations.secpmintoperation.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Operation](api_avm_operations.operation.md).[toString](api_avm_operations.operation.md#tostring)*

*Defined in [src/apis/avm/ops.ts:100](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L100)*

Returns a base-58 string representing the [NFTMintOperation](api_avm_operations.nftmintoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Operation](api_avm_operations.operation.md).[comparator](api_avm_operations.operation.md#static-comparator)*

*Defined in [src/apis/avm/ops.ts:104](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L104)*

**Returns:** *function*

▸ (`a`: [Operation](api_avm_operations.operation.md), `b`: [Operation](api_avm_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](api_avm_operations.operation.md) |
`b` | [Operation](api_avm_operations.operation.md) |
