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

*Defined in [apis/avm/ops.ts:176](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L176)*

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

*Defined in [apis/avm/ops.ts:116](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L116)*

___

### `Protected` operation

• **operation**: *[Operation](avmapi_operations.operation.md)*

*Defined in [apis/avm/ops.ts:118](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L118)*

___

### `Protected` utxoIDs

• **utxoIDs**: *Array‹[UTXOID](avmapi_types.utxoid.md)›* = []

*Defined in [apis/avm/ops.ts:117](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L117)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/ops.ts:120](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L120)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/ops.ts:160](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L160)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOperation

▸ **getOperation**(): *[Operation](avmapi_operations.operation.md)*

*Defined in [apis/avm/ops.ts:174](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L174)*

Returns the operation

**Returns:** *[Operation](avmapi_operations.operation.md)*

___

###  getUTXOIDs

▸ **getUTXOIDs**(): *Array‹[UTXOID](avmapi_types.utxoid.md)›*

*Defined in [apis/avm/ops.ts:167](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L167)*

Returns an array of UTXOIDs in this operation.

**Returns:** *Array‹[UTXOID](avmapi_types.utxoid.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/ops.ts:137](https://github.com/ava-labs/avalanche.js/blob/c723742/src/apis/avm/ops.ts#L137)*

**Returns:** *Buffer*
