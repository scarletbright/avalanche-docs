[avalanche](../README.md) › [API-PlatformVM-Inputs](api_platformvm_inputs.md)

# Module: API-PlatformVM-Inputs

## Index

### Classes

* [AmountInput](../classes/api_platformvm_inputs.amountinput.md)
* [SECPTransferInput](../classes/api_platformvm_inputs.secptransferinput.md)
* [TransferableInput](../classes/api_platformvm_inputs.transferableinput.md)

### Functions

* [SelectInputClass](api_platformvm_inputs.md#const-selectinputclass)

## Functions

### `Const` SelectInputClass

▸ **SelectInputClass**(`inputid`: number, ...`args`: Array‹any›): *[Input](../classes/common_inputs.input.md)*

*Defined in [src/apis/platformvm/inputs.ts:23](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/inputs.ts#L23)*

Takes a buffer representing the output and returns the proper [Input](../classes/common_inputs.input.md) instance.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`inputid` | number | A number representing the inputID parsed prior to the bytes passed in  |
`...args` | Array‹any› | - |

**Returns:** *[Input](../classes/common_inputs.input.md)*

An instance of an [Input](../classes/common_inputs.input.md)-extended class.
