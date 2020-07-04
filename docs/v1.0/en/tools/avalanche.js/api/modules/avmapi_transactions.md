[avalanche](../README.md) › [AVMAPI-Transactions](avmapi_transactions.md)

# Module: AVMAPI-Transactions

## Index

### Classes

* [BaseTx](../classes/avmapi_transactions.basetx.md)
* [CreateAssetTx](../classes/avmapi_transactions.createassettx.md)
* [OperationTx](../classes/avmapi_transactions.operationtx.md)
* [Tx](../classes/avmapi_transactions.tx.md)
* [UnsignedTx](../classes/avmapi_transactions.unsignedtx.md)

### Functions

* [SelectTxClass](avmapi_transactions.md#const-selecttxclass)

## Functions

### `Const` SelectTxClass

▸ **SelectTxClass**(`txtype`: number, ...`args`: Array‹any›): *[BaseTx](../classes/avmapi_transactions.basetx.md)*

*Defined in [src/apis/avm/tx.ts:555](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L555)*

Takes a buffer representing the output and returns the proper [BaseTx](../classes/avmapi_transactions.basetx.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txtype` | number | The id of the transaction type  |
`...args` | Array‹any› | - |

**Returns:** *[BaseTx](../classes/avmapi_transactions.basetx.md)*

An instance of an [BaseTx](../classes/avmapi_transactions.basetx.md)-extended class.
