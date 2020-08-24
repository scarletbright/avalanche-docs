[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [Operation](api_avm_operations.operation.md)

# Class: Operation

A class representing an operation. All operation types must extend on this class.

## Hierarchy

* **Operation**

  ↳ [NFTMintOperation](api_avm_operations.nftmintoperation.md)

  ↳ [NFTTransferOperation](api_avm_operations.nfttransferoperation.md)

## Index

### Constructors

* [constructor](api_avm_operations.operation.md#constructor)

### Properties

* [sigCount](api_avm_operations.operation.md#protected-sigcount)
* [sigIdxs](api_avm_operations.operation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](api_avm_operations.operation.md#addsignatureidx)
* [fromBuffer](api_avm_operations.operation.md#frombuffer)
* [getCredentialID](api_avm_operations.operation.md#getcredentialid)
* [getOperationID](api_avm_operations.operation.md#abstract-getoperationid)
* [getSigIdxs](api_avm_operations.operation.md#getsigidxs)
* [toBuffer](api_avm_operations.operation.md#tobuffer)
* [comparator](api_avm_operations.operation.md#static-comparator)

## Constructors

###  constructor

\+ **new Operation**(): *[Operation](api_avm_operations.operation.md)*

Defined in src/apis/avm/ops.ts:107

**Returns:** *[Operation](api_avm_operations.operation.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

Defined in src/apis/avm/ops.ts:39

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

Defined in src/apis/avm/ops.ts:41

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

Defined in src/apis/avm/ops.ts:58

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

Defined in src/apis/avm/ops.ts:68

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

Defined in src/apis/avm/ops.ts:50

**Returns:** *number*

___

### `Abstract` getOperationID

▸ **getOperationID**(): *number*

Defined in src/apis/avm/ops.ts:43

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

Defined in src/apis/avm/ops.ts:48

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Operation](api_avm_operations.operation.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/apis/avm/ops.ts:83

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

Defined in src/apis/avm/ops.ts:95

**Returns:** *function*

▸ (`a`: [Operation](api_avm_operations.operation.md), `b`: [Operation](api_avm_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](api_avm_operations.operation.md) |
`b` | [Operation](api_avm_operations.operation.md) |
