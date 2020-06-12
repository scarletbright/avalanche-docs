[slopes - v1.7.5](../README.md) › ["apis/avm/tx"](_apis_avm_tx_.md)

# External module: "apis/avm/tx"

## Index

### Classes

* [BaseTx](../classes/_apis_avm_tx_.basetx.md)
* [CreateAssetTx](../classes/_apis_avm_tx_.createassettx.md)
* [OperationTx](../classes/_apis_avm_tx_.operationtx.md)
* [Tx](../classes/_apis_avm_tx_.tx.md)
* [UnsignedTx](../classes/_apis_avm_tx_.unsignedtx.md)

### Functions

* [SelectTxClass](_apis_avm_tx_.md#const-selecttxclass)

## Functions

### `Const` SelectTxClass

▸ **SelectTxClass**(`txtype`: number, ...`args`: Array‹any›): *[BaseTx](../classes/_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:26](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L26)*

Takes a buffer representing the output and returns the proper [BaseTx](../classes/_apis_avm_tx_.basetx.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txtype` | number | The id of the transaction type  |
`...args` | Array‹any› | - |

**Returns:** *[BaseTx](../classes/_apis_avm_tx_.basetx.md)*

An instance of an [BaseTx](../classes/_apis_avm_tx_.basetx.md)-extended class.
