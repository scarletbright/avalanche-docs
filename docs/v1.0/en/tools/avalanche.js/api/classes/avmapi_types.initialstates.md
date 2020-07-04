[avalanche](../README.md) › [AVMAPI-Types](../modules/avmapi_types.md) › [InitialStates](avmapi_types.initialstates.md)

# Class: InitialStates

Class for creating initial output states used in asset creation

## Hierarchy

* **InitialStates**

## Index

### Constructors

* [constructor](avmapi_types.initialstates.md#constructor)

### Properties

* [fxs](avmapi_types.initialstates.md#protected-fxs)

### Methods

* [addOutput](avmapi_types.initialstates.md#addoutput)
* [fromBuffer](avmapi_types.initialstates.md#frombuffer)
* [toBuffer](avmapi_types.initialstates.md#tobuffer)

## Constructors

###  constructor

\+ **new InitialStates**(): *[InitialStates](avmapi_types.initialstates.md)*

*Defined in [src/apis/avm/types.ts:262](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L262)*

**Returns:** *[InitialStates](avmapi_types.initialstates.md)*

## Properties

### `Protected` fxs

• **fxs**: *object*

*Defined in [src/apis/avm/types.ts:200](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L200)*

#### Type declaration:

* \[ **fxid**: *number*\]: Array‹[Output](avmapi_outputs.output.md)›

## Methods

###  addOutput

▸ **addOutput**(`out`: [Output](avmapi_outputs.output.md), `fxid`: number): *void*

*Defined in [src/apis/avm/types.ts:207](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L207)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`out` | [Output](avmapi_outputs.output.md) | - | The output state to add to the collection |
`fxid` | number | AVMConstants.SECPFXID | The FxID that will be used for this output, default AVMConstants.SECPFXID  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/types.ts:214](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L214)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/types.ts:239](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/types.ts#L239)*

**Returns:** *Buffer*
