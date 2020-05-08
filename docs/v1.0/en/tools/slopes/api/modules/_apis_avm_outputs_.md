[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/outputs"](_apis_avm_outputs_.md)

# External module: "apis/avm/outputs"

## Index

### Classes

* [Output](../classes/_apis_avm_outputs_.output.md)
* [SecpOutBase](../classes/_apis_avm_outputs_.secpoutbase.md)
* [SecpOutput](../classes/_apis_avm_outputs_.secpoutput.md)

### Variables

* [bintools](_apis_avm_outputs_.md#const-bintools)

### Functions

* [SelectOutputClass](_apis_avm_outputs_.md#const-selectoutputclass)

## Variables

### `Const` bintools

• **bintools**: *[BinTools](../classes/_utils_bintools_.bintools.md)‹›* =  BinTools.getInstance()

*Defined in [apis/avm/outputs.ts:9](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L9)*

## Functions

### `Const` SelectOutputClass

▸ **SelectOutputClass**(`outbuffer`: Buffer, `args`: Array‹any›): *[Output](../classes/_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:18](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L18)*

Takes a buffer representing the output and returns the proper Output instance.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`outbuffer` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing the Output raw data.  |
`args` | Array‹any› |  [] | - |

**Returns:** *[Output](../classes/_apis_avm_outputs_.output.md)*

An instance of an [Output](../classes/_apis_avm_outputs_.output.md)-extended class: [[OutputPayment]], [[OutTakeOrLeave]], [[OutCreateAsset]].
