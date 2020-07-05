[avalanche](../README.md) › [AVMAPI-Operations](../modules/avmapi_operations.md) › [TransferableOperation](avmapi_operations.transferableoperation.md)

# Class: TransferableOperation

A class which contains an [Operation](avmapi_operations.operation.md) for transfers.

## Hierarchy

* **TransferableOperation**

## Index

### Constructors

* [constructor](avmapi_operations.transferableoperation.md#constructor)

### Properties

* [assetid](avmapi_operations.transferableoperation.md#protected-assetid)
* [operation](avmapi_operations.transferableoperation.md#protected-operation)
* [utxoIDs](avmapi_operations.transferableoperation.md#protected-utxoids)

### Methods

* [fromBuffer](avmapi_operations.transferableoperation.md#frombuffer)
* [getAssetID](avmapi_operations.transferableoperation.md#getassetid)
* [getOperation](avmapi_operations.transferableoperation.md#getoperation)
* [getUTXOIDs](avmapi_operations.transferableoperation.md#getutxoids)
* [toBuffer](avmapi_operations.transferableoperation.md#tobuffer)

## Constructors

###  constructor

\+ **new TransferableOperation**(`assetid`: Buffer, `utxoids`: Array‹[UTXOID](avmapi_types.utxoid.md) | string | Buffer›, `operation`: [Operation](avmapi_operations.operation.md)): *[TransferableOperation](avmapi_operations.transferableoperation.md)*

*Defined in [src/apis/avm/ops.ts:166](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L166)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`assetid` | Buffer | undefined |
`utxoids` | Array‹[UTXOID](avmapi_types.utxoid.md) &#124; string &#124; Buffer› | undefined |
`operation` | [Operation](avmapi_operations.operation.md) | undefined |

**Returns:** *[TransferableOperation](avmapi_operations.transferableoperation.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/ops.ts:110](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L110)*

___

### `Protected` operation

• **operation**: *[Operation](avmapi_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:114](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L114)*

___

### `Protected` utxoIDs

• **utxoIDs**: *Array‹[UTXOID](avmapi_types.utxoid.md)›* = []

*Defined in [src/apis/avm/ops.ts:112](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L112)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/ops.ts:116](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L116)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:156](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L156)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOperation

▸ **getOperation**(): *[Operation](avmapi_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:166](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L166)*

Returns the operation

**Returns:** *[Operation](avmapi_operations.operation.md)*

___

###  getUTXOIDs

▸ **getUTXOIDs**(): *Array‹[UTXOID](avmapi_types.utxoid.md)›*

*Defined in [src/apis/avm/ops.ts:161](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L161)*

Returns an array of UTXOIDs in this operation.

**Returns:** *Array‹[UTXOID](avmapi_types.utxoid.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/ops.ts:133](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L133)*

**Returns:** *Buffer*
