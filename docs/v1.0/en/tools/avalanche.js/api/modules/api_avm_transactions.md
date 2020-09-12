[avalanche](../README.md) › [API-AVM-Transactions](api_avm_transactions.md)

# Module: API-AVM-Transactions

## Index

### Classes

* [Tx](../classes/api_avm_transactions.tx.md)
* [UnsignedTx](../classes/api_avm_transactions.unsignedtx.md)

### Functions

* [SelectTxClass](api_avm_transactions.md#const-selecttxclass)

## Functions

### `Const` SelectTxClass

▸ **SelectTxClass**(`txtype`: number, ...`args`: Array‹any›): *[BaseTx](../classes/api_avm_basetx.basetx.md)*

*Defined in [src/apis/avm/tx.ts:83](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/tx.ts#L83)*

Takes a buffer representing the output and returns the proper [BaseTx](../classes/api_avm_basetx.basetx.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txtype` | number | The id of the transaction type  |
`...args` | Array‹any› | - |

**Returns:** *[BaseTx](../classes/api_avm_basetx.basetx.md)*

An instance of an [BaseTx](../classes/api_avm_basetx.basetx.md)-extended class.
