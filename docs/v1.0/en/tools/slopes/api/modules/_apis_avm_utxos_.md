[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/utxos"](_apis_avm_utxos_.md)

# External module: "apis/avm/utxos"

## Index

### Classes

* [SecpUTXO](../classes/_apis_avm_utxos_.secputxo.md)
* [UTXO](../classes/_apis_avm_utxos_.utxo.md)
* [UTXOSet](../classes/_apis_avm_utxos_.utxoset.md)

### Functions

* [SelectUTXOClass](_apis_avm_utxos_.md#const-selectutxoclass)

## Functions

### `Const` SelectUTXOClass

▸ **SelectUTXOClass**(`utxobuffer`: Buffer, `args`: Array‹any›): *[UTXO](../classes/_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:25](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L25)*

Takes a buffer representing the output and returns the proper UTXO instance.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`utxobuffer` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing the [UTXO](../classes/_apis_avm_utxos_.utxo.md) raw data.  |
`args` | Array‹any› |  [] | - |

**Returns:** *[UTXO](../classes/_apis_avm_utxos_.utxo.md)*

An instance of an [UTXO](../classes/_apis_avm_utxos_.utxo.md)-extended class. ex. [SecpUTXO](../classes/_apis_avm_utxos_.secputxo.md).
