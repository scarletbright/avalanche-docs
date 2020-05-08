[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [Output](_apis_avm_outputs_.output.md)

# Class: Output

A class representing a transaction output. All output types must extend on this class.

## Hierarchy

* **Output**

  ↳ [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)

## Index

### Constructors

* [constructor](_apis_avm_outputs_.output.md#constructor)

### Properties

* [outputid](_apis_avm_outputs_.output.md#protected-outputid)
* [outputidnum](_apis_avm_outputs_.output.md#protected-outputidnum)

### Methods

* [fromBuffer](_apis_avm_outputs_.output.md#frombuffer)
* [getOutputID](_apis_avm_outputs_.output.md#getoutputid)
* [toBuffer](_apis_avm_outputs_.output.md#tobuffer)
* [toString](_apis_avm_outputs_.output.md#tostring)
* [comparator](_apis_avm_outputs_.output.md#static-comparator)

## Constructors

###  constructor

\+ **new Output**(`outputidnum`: number): *[Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:58](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L58)*

**Parameters:**

Name | Type |
------ | ------ |
`outputidnum` | number |

**Returns:** *[Output](_apis_avm_outputs_.output.md)*

## Properties

### `Protected` outputid

• **outputid**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L33)*

___

### `Protected` outputidnum

• **outputidnum**: *number*

*Defined in [apis/avm/outputs.ts:34](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L34)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`outbuff`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/outputs.ts:40](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L40)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`outbuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Defined in [apis/avm/outputs.ts:36](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L36)*

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/outputs.ts:46](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L46)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/outputs.ts:50](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L50)*

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/outputs.ts:54](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L54)*

**Returns:** *function*

▸ (`a`: [Output](_apis_avm_outputs_.output.md), `b`: [Output](_apis_avm_outputs_.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](_apis_avm_outputs_.output.md) |
`b` | [Output](_apis_avm_outputs_.output.md) |
