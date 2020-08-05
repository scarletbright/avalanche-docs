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

*Defined in [src/apis/avm/ops.ts:100](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L100)*

**Returns:** *[Operation](avmapi_operations.operation.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/ops.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Defined in [src/apis/avm/ops.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L34)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

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

*Defined in [src/apis/avm/ops.ts:61](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L61)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/apis/avm/ops.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L43)*

**Returns:** *number*

___

### `Abstract` getOperationID

▸ **getOperationID**(): *number*

*Defined in [src/apis/avm/ops.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L36)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Defined in [src/apis/avm/ops.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L41)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Operation](avmapi_operations.operation.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:76](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L76)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/ops.ts:88](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L88)*

**Returns:** *function*

▸ (`a`: [Operation](avmapi_operations.operation.md), `b`: [Operation](avmapi_operations.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](avmapi_operations.operation.md) |
`b` | [Operation](avmapi_operations.operation.md) |
