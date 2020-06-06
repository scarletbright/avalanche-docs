[slopes - v1.7.2](../README.md) › ["apis/avm/inputs"](_apis_avm_inputs_.md)

# External module: "apis/avm/inputs"

## Index

### Classes

* [AmountInput](../classes/_apis_avm_inputs_.amountinput.md)
* [Input](../classes/_apis_avm_inputs_.input.md)
* [SecpInput](../classes/_apis_avm_inputs_.secpinput.md)
* [TransferableInput](../classes/_apis_avm_inputs_.transferableinput.md)

### Functions

* [SelectInputClass](_apis_avm_inputs_.md#const-selectinputclass)

## Functions

### `Const` SelectInputClass

▸ **SelectInputClass**(`inputid`: number, ...`args`: Array‹any›): *[Input](../classes/_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:21](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L21)*

Takes a buffer representing the output and returns the proper [Input](../classes/_apis_avm_inputs_.input.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`inputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Input](../classes/_apis_avm_inputs_.input.md)*

An instance of an [Input](../classes/_apis_avm_inputs_.input.md)-extended class.
