[avalanche](../README.md) › [API-AVM-Operations](../modules/api_avm_operations.md) › [TransferableOperation](api_avm_operations.transferableoperation.md)

# Class: TransferableOperation

A class which contains an [Operation](api_avm_operations.operation.md) for transfers.

## Hierarchy

* **TransferableOperation**

## Index

### Constructors

* [constructor](api_avm_operations.transferableoperation.md#constructor)

### Properties

* [assetid](api_avm_operations.transferableoperation.md#protected-assetid)
* [operation](api_avm_operations.transferableoperation.md#protected-operation)
* [utxoIDs](api_avm_operations.transferableoperation.md#protected-utxoids)

### Methods

* [fromBuffer](api_avm_operations.transferableoperation.md#frombuffer)
* [getAssetID](api_avm_operations.transferableoperation.md#getassetid)
* [getOperation](api_avm_operations.transferableoperation.md#getoperation)
* [getUTXOIDs](api_avm_operations.transferableoperation.md#getutxoids)
* [toBuffer](api_avm_operations.transferableoperation.md#tobuffer)
* [comparator](api_avm_operations.transferableoperation.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableOperation**(`assetid`: Buffer, `utxoids`: Array‹[UTXOID](api_avm_operations.utxoid.md) | string | Buffer›, `operation`: [Operation](api_avm_operations.operation.md)): *[TransferableOperation](api_avm_operations.transferableoperation.md)*

*Defined in [src/apis/avm/ops.ts:192](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L192)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`assetid` | Buffer | undefined |
`utxoids` | Array‹[UTXOID](api_avm_operations.utxoid.md) &#124; string &#124; Buffer› | undefined |
`operation` | [Operation](api_avm_operations.operation.md) | undefined |

**Returns:** *[TransferableOperation](api_avm_operations.transferableoperation.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/ops.ts:126](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L126)*

___

### `Protected` operation

• **operation**: *[Operation](api_avm_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:130](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L130)*

___

### `Protected` utxoIDs

• **utxoIDs**: *Array‹[UTXOID](api_avm_operations.utxoid.md)›* = []

*Defined in [src/apis/avm/ops.ts:128](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L128)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/ops.ts:141](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L141)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:182](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L182)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOperation

▸ **getOperation**(): *[Operation](api_avm_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:192](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L192)*

Returns the operation

**Returns:** *[Operation](api_avm_operations.operation.md)*

___

###  getUTXOIDs

▸ **getUTXOIDs**(): *Array‹[UTXOID](api_avm_operations.utxoid.md)›*

*Defined in [src/apis/avm/ops.ts:187](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L187)*

Returns an array of UTXOIDs in this operation.

**Returns:** *Array‹[UTXOID](api_avm_operations.utxoid.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:158](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L158)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/ops.ts:135](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/ops.ts#L135)*

Returns a function used to sort an array of [TransferableOperation](api_avm_operations.transferableoperation.md)s

**Returns:** *function*

▸ (`a`: [TransferableOperation](api_avm_operations.transferableoperation.md), `b`: [TransferableOperation](api_avm_operations.transferableoperation.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableOperation](api_avm_operations.transferableoperation.md) |
`b` | [TransferableOperation](api_avm_operations.transferableoperation.md) |
