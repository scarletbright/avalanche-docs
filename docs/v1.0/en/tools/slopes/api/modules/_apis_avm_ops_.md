[slopes - v1.7.2](../README.md) › ["apis/avm/ops"](_apis_avm_ops_.md)

# External module: "apis/avm/ops"

## Index

### Classes

* [NFTTransferOperation](../classes/_apis_avm_ops_.nfttransferoperation.md)
* [Operation](../classes/_apis_avm_ops_.operation.md)
* [TransferableOperation](../classes/_apis_avm_ops_.transferableoperation.md)

### Variables

* [bintools](_apis_avm_ops_.md#const-bintools)

### Functions

* [SelectOperationClass](_apis_avm_ops_.md#const-selectoperationclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/_utils_bintools_.bintools.md)‹›* =  BinTools.getInstance()

*Defined in [apis/avm/ops.ts:9](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L9)*

## Functions

### `Const` SelectOperationClass

▸ **SelectOperationClass**(`opid`: number, ...`args`: Array‹any›): *[Operation](../classes/_apis_avm_ops_.operation.md)*

*Defined in [apis/avm/ops.ts:18](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/ops.ts#L18)*

Takes a buffer representing the output and returns the proper [Operation](../classes/_apis_avm_ops_.operation.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`opid` | number | A number representing the operation ID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Operation](../classes/_apis_avm_ops_.operation.md)*

An instance of an [Operation](../classes/_apis_avm_ops_.operation.md)-extended class.
