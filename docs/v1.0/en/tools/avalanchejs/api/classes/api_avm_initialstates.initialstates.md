[avalanche](../README.md) › [API-AVM-InitialStates](../modules/api_avm_initialstates.md) › [InitialStates](api_avm_initialstates.initialstates.md)

# Class: InitialStates

Class for creating initial output states used in asset creation

## Hierarchy

* **InitialStates**

## Index

### Constructors

* [constructor](api_avm_initialstates.initialstates.md#constructor)

### Properties

* [fxs](api_avm_initialstates.initialstates.md#protected-fxs)

### Methods

* [addOutput](api_avm_initialstates.initialstates.md#addoutput)
* [fromBuffer](api_avm_initialstates.initialstates.md#frombuffer)
* [toBuffer](api_avm_initialstates.initialstates.md#tobuffer)

## Constructors

###  constructor

\+ **new InitialStates**(): *[InitialStates](api_avm_initialstates.initialstates.md)*

*Defined in [src/apis/avm/initialstates.ts:83](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/initialstates.ts#L83)*

**Returns:** *[InitialStates](api_avm_initialstates.initialstates.md)*

## Properties

### `Protected` fxs

• **fxs**: *object*

*Defined in [src/apis/avm/initialstates.ts:21](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/initialstates.ts#L21)*

#### Type declaration:

* \[ **fxid**: *number*\]: Array‹[Output](common_output.output.md)›

## Methods

###  addOutput

▸ **addOutput**(`out`: [Output](common_output.output.md), `fxid`: number): *void*

*Defined in [src/apis/avm/initialstates.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/initialstates.ts#L28)*

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`out` | [Output](common_output.output.md) | - | The output state to add to the collection |
`fxid` | number | AVMConstants.SECPFXID | The FxID that will be used for this output, default AVMConstants.SECPFXID  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/initialstates.ts:35](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/initialstates.ts#L35)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/initialstates.ts:60](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/initialstates.ts#L60)*

**Returns:** *Buffer*
