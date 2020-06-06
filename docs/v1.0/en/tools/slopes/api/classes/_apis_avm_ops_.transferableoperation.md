[slopes - v1.7.2](../README.md) › ["apis/avm/ops"](../modules/_apis_avm_ops_.md) › [TransferableOperation](_apis_avm_ops_.transferableoperation.md)

# Class: TransferableOperation

A class which contains an [Operation](_apis_avm_ops_.operation.md) for transfers.

## Hierarchy

* **TransferableOperation**

## Index

### Constructors

* [constructor](_apis_avm_ops_.transferableoperation.md#constructor)

### Properties

* [assetid](_apis_avm_ops_.transferableoperation.md#protected-assetid)
* [operation](_apis_avm_ops_.transferableoperation.md#protected-operation)
* [utxoIDs](_apis_avm_ops_.transferableoperation.md#protected-utxoids)

### Methods

* [fromBuffer](_apis_avm_ops_.transferableoperation.md#frombuffer)
* [getAssetID](_apis_avm_ops_.transferableoperation.md#getassetid)
* [getOperation](_apis_avm_ops_.transferableoperation.md#getoperation)
* [getUTXOIDs](_apis_avm_ops_.transferableoperation.md#getutxoids)
* [toBuffer](_apis_avm_ops_.transferableoperation.md#tobuffer)

## Constructors

###  constructor

\+ **new TransferableOperation**(`assetid`: Buffer, `utxoids`: Array‹[UTXOID](_apis_avm_types_.utxoid.md) | string | Buffer›, `operation`: [Operation](_apis_avm_ops_.operation.md)): *[TransferableOperation](_apis_avm_ops_.transferableoperation.md)*

*Defined in [apis/avm/ops.ts:175](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L175)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`assetid` | Buffer |  undefined |
`utxoids` | Array‹[UTXOID](_apis_avm_types_.utxoid.md) &#124; string &#124; Buffer› |  undefined |
`operation` | [Operation](_apis_avm_ops_.operation.md) |  undefined |

**Returns:** *[TransferableOperation](_apis_avm_ops_.transferableoperation.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/ops.ts:115](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L115)*

___

### `Protected` operation

• **operation**: *[Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:117](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L117)*

___

### `Protected` utxoIDs

• **utxoIDs**: *Array‹[UTXOID](_apis_avm_types_.utxoid.md)›* =  []

*Defined in [apis/avm/ops.ts:116](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L116)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/ops.ts:119](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L119)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/ops.ts:159](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L159)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOperation

▸ **getOperation**(): *[Operation](_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:173](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L173)*

Returns the operation

**Returns:** *[Operation](_apis_avm_ops_.operation.md)*

___

###  getUTXOIDs

▸ **getUTXOIDs**(): *Array‹[UTXOID](_apis_avm_types_.utxoid.md)›*

*Defined in [apis/avm/ops.ts:166](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L166)*

Returns an array of UTXOIDs in this operation.

**Returns:** *Array‹[UTXOID](_apis_avm_types_.utxoid.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/ops.ts:136](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L136)*

**Returns:** *Buffer*
