[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [NFTTransferOperation](api_avm_operations.nfttransferoperation.md)

# Class: NFTTransferOperation

A [Operation](api_avm_operations.operation.md) class which specifies a NFT Transfer Op.

## Hierarchy

* [Operation](api_avm_operations.operation.md)

  ↳ **NFTTransferOperation**

## Index

### Constructors

* [constructor](api_avm_operations.nfttransferoperation.md#constructor)

### Properties

* [output](api_avm_operations.nfttransferoperation.md#protected-output)
* [sigCount](api_avm_operations.nfttransferoperation.md#protected-sigcount)
* [sigIdxs](api_avm_operations.nfttransferoperation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](api_avm_operations.nfttransferoperation.md#addsignatureidx)
* [fromBuffer](api_avm_operations.nfttransferoperation.md#frombuffer)
* [getCredentialID](api_avm_operations.nfttransferoperation.md#getcredentialid)
* [getOperationID](api_avm_operations.nfttransferoperation.md#getoperationid)
* [getOutput](api_avm_operations.nfttransferoperation.md#getoutput)
* [getSigIdxs](api_avm_operations.nfttransferoperation.md#getsigidxs)
* [toBuffer](api_avm_operations.nfttransferoperation.md#tobuffer)
* [toString](api_avm_operations.nfttransferoperation.md#tostring)
* [comparator](api_avm_operations.nfttransferoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOperation**(`output`: [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)): *[NFTTransferOperation](api_avm_operations.nfttransferoperation.md)*

*Overrides [Operation](api_avm_operations.operation.md).[constructor](api_avm_operations.operation.md#constructor)*

*Defined in [src/apis/avm/ops.ts:485](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L485)*

An [Operation](api_avm_operations.operation.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`output` | [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md) | undefined | An [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)  |

**Returns:** *[NFTTransferOperation](api_avm_operations.nfttransferoperation.md)*

## Properties

### `Protected` output

• **output**: *[NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)*

*Defined in [src/apis/avm/ops.ts:442](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L442)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Operation](api_avm_operations.operation.md).[sigCount](api_avm_operations.operation.md#protected-sigcount)*

*Defined in [src/apis/avm/ops.ts:38](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L38)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

*Inherited from [Operation](api_avm_operations.operation.md).[sigIdxs](api_avm_operations.operation.md#protected-sigidxs)*

*Defined in [src/apis/avm/ops.ts:40](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L40)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Operation](api_avm_operations.operation.md).[addSignatureIdx](api_avm_operations.operation.md#addsignatureidx)*

*Defined in [src/apis/avm/ops.ts:60](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L60)*

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

*Defined in [src/apis/avm/ops.ts:463](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L463)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTTransferOperation](api_avm_operations.nfttransferoperation.md) and returns the updated offset.

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

*Defined in [src/apis/avm/ops.ts:454](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L454)*

Returns the credential ID.

**Returns:** *number*

___

###  getOperationID

▸ **getOperationID**(): *number*

*Overrides [Operation](api_avm_operations.operation.md).[getOperationID](api_avm_operations.operation.md#abstract-getoperationid)*

*Defined in [src/apis/avm/ops.ts:447](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L447)*

Returns the operation ID.

**Returns:** *number*

___

###  getOutput

▸ **getOutput**(): *[NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)*

*Defined in [src/apis/avm/ops.ts:458](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L458)*

**Returns:** *[NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

*Inherited from [Operation](api_avm_operations.operation.md).[getSigIdxs](api_avm_operations.operation.md#getsigidxs)*

*Defined in [src/apis/avm/ops.ts:47](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L47)*

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Operation](api_avm_operations.operation.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Operation](api_avm_operations.operation.md).[toBuffer](api_avm_operations.operation.md#tobuffer)*

*Defined in [src/apis/avm/ops.ts:472](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L472)*

Returns the buffer representing the [NFTTransferOperation](api_avm_operations.nfttransferoperation.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [Operation](api_avm_operations.operation.md).[toString](api_avm_operations.operation.md#tostring)*

*Defined in [src/apis/avm/ops.ts:483](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L483)*

Returns a base-58 string representing the [NFTTransferOperation](api_avm_operations.nfttransferoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Operation](api_avm_operations.operation.md).[comparator](api_avm_operations.operation.md#static-comparator)*

*Defined in [src/apis/avm/ops.ts:104](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/ops.ts#L104)*

**Returns:** *function*

▸ (`a`: [Operation](api_avm_operations.operation.md), `b`: [Operation](api_avm_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](api_avm_operations.operation.md) |
`b` | [Operation](api_avm_operations.operation.md) |
