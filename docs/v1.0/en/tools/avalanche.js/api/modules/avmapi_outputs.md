[avalanche](../README.md) › [AVMAPI-Outputs](avmapi_outputs.md)

# Module: AVMAPI-Outputs

## Index

### Classes

* [AmountOutput](../classes/avmapi_outputs.amountoutput.md)
* [NFTOutBase](../classes/avmapi_outputs.nftoutbase.md)
* [NFTTransferOutput](../classes/avmapi_outputs.nfttransferoutput.md)
* [Output](../classes/avmapi_outputs.output.md)
* [SecpOutput](../classes/avmapi_outputs.secpoutput.md)
* [TransferableOutput](../classes/avmapi_outputs.transferableoutput.md)

### Variables

* [bintools](avmapi_outputs.md#const-bintools)

### Functions

* [SelectOutputClass](avmapi_outputs.md#const-selectoutputclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/utils_bintools.bintools.md)‹›* = BinTools.getInstance()

*Defined in [apis/avm/outputs.ts:10](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L10)*

## Functions

### `Const` SelectOutputClass

▸ **SelectOutputClass**(`outputid`: number, ...`args`: Array‹any›): *[Output](../classes/avmapi_outputs.output.md)*

*Defined in [apis/avm/outputs.ts:19](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L19)*

Takes a buffer representing the output and returns the proper Output instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`outputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Output](../classes/avmapi_outputs.output.md)*

An instance of an [Output](../classes/avmapi_outputs.output.md)-extended class.
