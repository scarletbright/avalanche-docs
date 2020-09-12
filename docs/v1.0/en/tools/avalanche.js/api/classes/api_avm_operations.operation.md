[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [Operation](api_avm_operations.operation.md)

# Class: Operation

A class representing an operation. All operation types must extend on this class.

## Hierarchy

* **Operation**

  ↳ [SECPMintOperation](api_avm_operations.secpmintoperation.md)

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
* [getCredentialID](api_avm_operations.operation.md#abstract-getcredentialid)
* [getOperationID](api_avm_operations.operation.md#abstract-getoperationid)
* [getSigIdxs](api_avm_operations.operation.md#getsigidxs)
* [toBuffer](api_avm_operations.operation.md#tobuffer)
* [toString](api_avm_operations.operation.md#tostring)
* [comparator](api_avm_operations.operation.md#static-comparator)

## Constructors

###  constructor

\+ **new Operation**(): *[Operation](api_avm_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:116](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L116)*

**Returns:** *[Operation](api_avm_operations.operation.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/ops.ts:38](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L38)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](common_signature.sigidx.md)›* = []

*Defined in [src/apis/avm/ops.ts:40](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L40)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

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

*Defined in [src/apis/avm/ops.ts:70](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L70)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

### `Abstract` getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/apis/avm/ops.ts:52](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L52)*

Returns the credential ID.

**Returns:** *number*

___

### `Abstract` getOperationID

▸ **getOperationID**(): *number*

*Defined in [src/apis/avm/ops.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L42)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](common_signature.sigidx.md)›*

*Defined in [src/apis/avm/ops.ts:47](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L47)*

Returns the array of [SigIdx](common_signature.sigidx.md) for this [Operation](api_avm_operations.operation.md)

**Returns:** *Array‹[SigIdx](common_signature.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L85)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/ops.ts:100](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L100)*

Returns a base-58 string representing the [NFTMintOperation](api_avm_operations.nftmintoperation.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/ops.ts:104](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L104)*

**Returns:** *function*

▸ (`a`: [Operation](api_avm_operations.operation.md), `b`: [Operation](api_avm_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](api_avm_operations.operation.md) |
`b` | [Operation](api_avm_operations.operation.md) |
