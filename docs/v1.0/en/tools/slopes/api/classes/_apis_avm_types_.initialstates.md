[slopes - v1.7.3](../README.md) › ["apis/avm/types"](../modules/_apis_avm_types_.md) › [InitialStates](_apis_avm_types_.initialstates.md)

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

*Defined in [apis/avm/types.ts:235](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/types.ts#L235)*

**Returns:** *[InitialStates](_apis_avm_types_.initialstates.md)*

## Properties

### `Protected` fxs

• **fxs**: *object*

*Defined in [apis/avm/types.ts:173](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/types.ts#L173)*

#### Type declaration:

* \[ **fxid**: *number*\]: Array‹[Output](_apis_avm_outputs_.output.md)›

## Methods

###  addOutput

▸ **addOutput**(`out`: [Output](_apis_avm_outputs_.output.md), `fxid`: number): *void*

*Defined in [apis/avm/types.ts:180](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/types.ts#L180)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`out` | [Output](_apis_avm_outputs_.output.md) | - | The output state to add to the collection |
`fxid` | number |  AVMConstants.SECPFXID | The FxID that will be used for this output, default AVMConstants.SECPFXID  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/types.ts:187](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/types.ts#L187)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/types.ts:212](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/types.ts#L212)*

**Returns:** *Buffer*
