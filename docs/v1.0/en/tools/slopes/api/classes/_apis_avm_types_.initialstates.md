[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/types"](../modules/_apis_avm_types_.md) › [InitialStates](_apis_avm_types_.initialstates.md)

# Class: InitialStates

Class for creating initial output states used in asset creation

## Hierarchy

* **InitialStates**

## Index

### Constructors

* [constructor](_apis_avm_types_.initialstates.md#constructor)

### Properties

* [fxs](_apis_avm_types_.initialstates.md#protected-fxs)

### Methods

* [addOutput](_apis_avm_types_.initialstates.md#addoutput)
* [fromBuffer](_apis_avm_types_.initialstates.md#frombuffer)
* [toBuffer](_apis_avm_types_.initialstates.md#tobuffer)

## Constructors

###  constructor

\+ **new InitialStates**(): *[InitialStates](_apis_avm_types_.initialstates.md)*

*Defined in [apis/avm/types.ts:178](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L178)*

**Returns:** *[InitialStates](_apis_avm_types_.initialstates.md)*

## Properties

### `Protected` fxs

• **fxs**: *object*

*Defined in [apis/avm/types.ts:118](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L118)*

#### Type declaration:

* \[ **fxid**: *number*\]: Array‹[Output](_apis_avm_outputs_.output.md)›

## Methods

###  addOutput

▸ **addOutput**(`out`: [Output](_apis_avm_outputs_.output.md), `fxid`: number): *void*

*Defined in [apis/avm/types.ts:125](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L125)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`out` | [Output](_apis_avm_outputs_.output.md) | - | The output state to add to the collection |
`fxid` | number |  AVMConstants.SECPFXID | The FxID that will be used for this output, default AVMConstants.SECPFXID  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/types.ts:132](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L132)*

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset` | number |

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/types.ts:158](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/types.ts#L158)*

**Returns:** *Buffer*
