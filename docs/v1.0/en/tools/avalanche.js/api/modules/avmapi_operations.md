[avalanche](../README.md) › [AVMAPI-Operations](avmapi_operations.md)

# Module: AVMAPI-Operations

## Index

### Classes

* [NFTTransferOperation](../classes/avmapi_operations.nfttransferoperation.md)
* [Operation](../classes/avmapi_operations.operation.md)
* [TransferableOperation](../classes/avmapi_operations.transferableoperation.md)

### Variables

* [bintools](avmapi_operations.md#const-bintools)

### Functions

* [SelectOperationClass](avmapi_operations.md#const-selectoperationclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/utils_bintools.bintools.md)‹›* = BinTools.getInstance()

*Defined in [src/apis/avm/ops.ts:10](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L10)*

## Functions

### `Const` SelectOperationClass

▸ **SelectOperationClass**(`opid`: number, ...`args`: Array‹any›): *[Operation](../classes/avmapi_operations.operation.md)*

*Defined in [src/apis/avm/ops.ts:19](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/ops.ts#L19)*

Takes a buffer representing the output and returns the proper [Operation](../classes/avmapi_operations.operation.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opid` | number | A number representing the operation ID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Operation](../classes/avmapi_operations.operation.md)*

An instance of an [Operation](../classes/avmapi_operations.operation.md)-extended class.
