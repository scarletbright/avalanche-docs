[slopes - v1.7.2](../README.md) › ["apis/avm/ops"](../modules/_apis_avm_ops_.md) › [Operation](_apis_avm_ops_.operation.md)

# Class: Operation

A class representing an operation. All operation types must extend on this class.

## Hierarchy

* **Operation**

  ↳ [NFTTransferOperation](_apis_avm_ops_.nfttransferoperation.md)

## Index

### Constructors

* [constructor](_apis_avm_ops_.operation.md#constructor)

### Properties

* [sigCount](_apis_avm_ops_.operation.md#protected-sigcount)
* [sigIdxs](_apis_avm_ops_.operation.md#protected-sigidxs)

### Methods

* [addSignatureIdx](_apis_avm_ops_.operation.md#addsignatureidx)
* [fromBuffer](_apis_avm_ops_.operation.md#frombuffer)
* [getCredentialID](_apis_avm_ops_.operation.md#getcredentialid)
* [getOperationID](_apis_avm_ops_.operation.md#abstract-getoperationid)
* [getSigIdxs](_apis_avm_ops_.operation.md#getsigidxs)
* [toBuffer](_apis_avm_ops_.operation.md#tobuffer)
* [comparator](_apis_avm_ops_.operation.md#static-comparator)

## Constructors

###  constructor

\+ **new Operation**(): *[Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:104](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L104)*

**Returns:** *[Operation](_apis_avm_ops_.operation.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/ops.ts:31](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L31)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›* =  []

*Defined in [apis/avm/ops.ts:32](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L32)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [apis/avm/ops.ts:53](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L53)*

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

*Defined in [apis/avm/ops.ts:63](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L63)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [apis/avm/ops.ts:43](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L43)*

**Returns:** *number*

___

### `Abstract` getOperationID

▸ **getOperationID**(): *number*

*Defined in [apis/avm/ops.ts:34](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L34)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

*Defined in [apis/avm/ops.ts:39](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L39)*

Returns the array of [SigIdx](_apis_avm_types_.sigidx.md) for this [Operation](_apis_avm_ops_.operation.md)

**Returns:** *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/ops.ts:78](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L78)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/ops.ts:90](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/ops.ts#L90)*

**Returns:** *function*

▸ (`a`: [Operation](_apis_avm_ops_.operation.md), `b`: [Operation](_apis_avm_ops_.operation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Operation](_apis_avm_ops_.operation.md) |
`b` | [Operation](_apis_avm_ops_.operation.md) |
