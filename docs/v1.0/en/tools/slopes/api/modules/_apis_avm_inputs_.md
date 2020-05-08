[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/inputs"](_apis_avm_inputs_.md)

# External module: "apis/avm/inputs"

## Index

### Classes

* [Input](../classes/_apis_avm_inputs_.input.md)
* [SecpInput](../classes/_apis_avm_inputs_.secpinput.md)

### Functions

* [SelectInputClass](_apis_avm_inputs_.md#const-selectinputclass)

## Functions

### `Const` SelectInputClass

▸ **SelectInputClass**(`inbuffer`: Buffer, `args`: Array‹any›): *[Input](../classes/_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:35](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L35)*

Takes a buffer representing the output and returns the proper [Input](../classes/_apis_avm_inputs_.input.md) instance.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`inbuffer` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing the [Input](../classes/_apis_avm_inputs_.input.md) raw data.  |
`args` | Array‹any› |  [] | - |

**Returns:** *[Input](../classes/_apis_avm_inputs_.input.md)*

An instance of an [Input](../classes/_apis_avm_inputs_.input.md)-extended class: [SecpInput](../classes/_apis_avm_inputs_.secpinput.md).
