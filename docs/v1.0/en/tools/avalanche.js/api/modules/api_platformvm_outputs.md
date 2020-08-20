[avalanche](../README.md) › [API-PlatformVM-Outputs](api_platformvm_outputs.md)

# Module: API-PlatformVM-Outputs

## Index

### Classes

* [AmountOutput](../classes/api_platformvm_outputs.amountoutput.md)
* [SecpOutput](../classes/api_platformvm_outputs.secpoutput.md)
* [TransferableOutput](../classes/api_platformvm_outputs.transferableoutput.md)

### Variables

* [bintools](api_platformvm_outputs.md#const-bintools)

### Functions

* [SelectOutputClass](api_platformvm_outputs.md#const-selectoutputclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/utils_bintools.bintools.md)‹›* = BinTools.getInstance()

Defined in src/apis/platformvm/outputs.ts:10

## Functions

### `Const` SelectOutputClass

▸ **SelectOutputClass**(`outputid`: number, ...`args`: Array‹any›): *[Output](../classes/common_output.output.md)*

Defined in src/apis/platformvm/outputs.ts:19

Takes a buffer representing the output and returns the proper Output instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`outputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Output](../classes/common_output.output.md)*

An instance of an [Output](../classes/common_output.output.md)-extended class.
