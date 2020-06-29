[avalanche](../README.md) › [AVMAPI-Inputs](avmapi_inputs.md)

# Module: AVMAPI-Inputs

## Index

### Classes

* [AmountInput](../classes/avmapi_inputs.amountinput.md)
* [Input](../classes/avmapi_inputs.input.md)
* [SecpInput](../classes/avmapi_inputs.secpinput.md)
* [TransferableInput](../classes/avmapi_inputs.transferableinput.md)

### Functions

* [SelectInputClass](avmapi_inputs.md#const-selectinputclass)

## Functions

### `Const` SelectInputClass

▸ **SelectInputClass**(`inputid`: number, ...`args`: Array‹any›): *[Input](../classes/avmapi_inputs.input.md)*

*Defined in [apis/avm/inputs.ts:22](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L22)*

Takes a buffer representing the output and returns the proper [Input](../classes/avmapi_inputs.input.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`inputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Input](../classes/avmapi_inputs.input.md)*

An instance of an [Input](../classes/avmapi_inputs.input.md)-extended class.
