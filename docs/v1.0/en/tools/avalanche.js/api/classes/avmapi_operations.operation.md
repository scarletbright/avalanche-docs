[avalanche](../README.md) › [AVMAPI-Operations](../modules/avmapi_operations.md) › [Operation](avmapi_operations.operation.md)

# Class: Operation

A class representing an operation. All operation types must extend on this class.

## Hierarchy

* **Operation**

  ↳ [NFTTransferOperation](avmapi_operations.nfttransferoperation.md)

## Index

### Constructors

* [constructor](avmapi_operations.operation.md#constructor)

### Properties

* [sigCount](avmapi_operations.operation.md#protected-sigcount)
* [sigIdxs](avmapi_operations.operation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](avmapi_operations.operation.md#addsignatureidx)
* [fromBuffer](avmapi_operations.operation.md#frombuffer)
* [getCredentialID](avmapi_operations.operation.md#getcredentialid)
* [getOperationID](avmapi_operations.operation.md#abstract-getoperationid)
* [getSigIdxs](avmapi_operations.operation.md#getsigidxs)
* [toBuffer](avmapi_operations.operation.md#tobuffer)
* [comparator](avmapi_operations.operation.md#static-comparator)

## Constructors

###  constructor

\+ **new Operation**(): *[Operation](avmapi_operations.operation.md)*

*Defined in [apis/avm/ops.ts:105](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L105)*

**Returns:** *[Operation](avmapi_operations.operation.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Defined in [apis/avm/ops.ts:32](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Defined in [apis/avm/ops.ts:33](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L33)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [apis/avm/ops.ts:54](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L54)*

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

*Defined in [apis/avm/ops.ts:64](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L64)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [apis/avm/ops.ts:44](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L44)*

**Returns:** *number*

___

### `Abstract` getOperationID

▸ **getOperationID**(): *number*

*Defined in [apis/avm/ops.ts:35](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L35)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Defined in [apis/avm/ops.ts:40](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L40)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Operation](avmapi_operations.operation.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/ops.ts:79](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L79)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/ops.ts:91](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/ops.ts#L91)*

**Returns:** *function*

▸ (`a`: [Operation](avmapi_operations.operation.md), `b`: [Operation](avmapi_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](avmapi_operations.operation.md) |
`b` | [Operation](avmapi_operations.operation.md) |
