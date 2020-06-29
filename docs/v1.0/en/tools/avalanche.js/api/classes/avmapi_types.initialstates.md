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

*Defined in [apis/avm/types.ts:236](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L236)*

**Returns:** *[InitialStates](avmapi_types.initialstates.md)*

## Properties

### `Protected` fxs

• **fxs**: *object*

*Defined in [apis/avm/types.ts:174](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L174)*

#### Type declaration:

* \[ **fxid**: *number*\]: Array‹[Output](avmapi_outputs.output.md)›

## Methods

###  addOutput

▸ **addOutput**(`out`: [Output](avmapi_outputs.output.md), `fxid`: number): *void*

*Defined in [apis/avm/types.ts:181](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L181)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`out` | [Output](avmapi_outputs.output.md) | - | The output state to add to the collection |
`fxid` | number | AVMConstants.SECPFXID | The FxID that will be used for this output, default AVMConstants.SECPFXID  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/types.ts:188](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L188)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/types.ts:213](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/types.ts#L213)*

**Returns:** *Buffer*
