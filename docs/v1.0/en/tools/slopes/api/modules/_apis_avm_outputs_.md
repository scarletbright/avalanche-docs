[slopes - v1.7.3](../README.md) › ["apis/avm/outputs"](_apis_avm_outputs_.md)

# External module: "apis/avm/outputs"

## Index

### Classes

* [AmountOutput](../classes/_apis_avm_outputs_.amountoutput.md)
* [NFTOutBase](../classes/_apis_avm_outputs_.nftoutbase.md)
* [NFTTransferOutput](../classes/_apis_avm_outputs_.nfttransferoutput.md)
* [Output](../classes/_apis_avm_outputs_.output.md)
* [SecpOutput](../classes/_apis_avm_outputs_.secpoutput.md)
* [TransferableOutput](../classes/_apis_avm_outputs_.transferableoutput.md)

### Variables

* [bintools](_apis_avm_outputs_.md#const-bintools)

### Functions

* [SelectOutputClass](_apis_avm_outputs_.md#const-selectoutputclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/_utils_bintools_.bintools.md)‹›* =  BinTools.getInstance()

*Defined in [apis/avm/outputs.ts:9](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/outputs.ts#L9)*

## Functions

### `Const` SelectOutputClass

▸ **SelectOutputClass**(`outputid`: number, ...`args`: Array‹any›): *[Output](../classes/_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:18](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/outputs.ts#L18)*

Takes a buffer representing the output and returns the proper Output instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`outputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Output](../classes/_apis_avm_outputs_.output.md)*

An instance of an [Output](../classes/_apis_avm_outputs_.output.md)-extended class.
