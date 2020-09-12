[avalanche](../README.md) › [API-PlatformVM-Outputs](../modules/api_platformvm_outputs.md) › [ParseableOutput](api_platformvm_outputs.parseableoutput.md)

# Class: ParseableOutput

## Hierarchy

* [StandardParseableOutput](common_output.standardparseableoutput.md)

  ↳ **ParseableOutput**

## Index

### Constructors

* [constructor](api_platformvm_outputs.parseableoutput.md#constructor)

### Properties

* [output](api_platformvm_outputs.parseableoutput.md#protected-output)

### Methods

* [fromBuffer](api_platformvm_outputs.parseableoutput.md#frombuffer)
* [getOutput](api_platformvm_outputs.parseableoutput.md#getoutput)
* [toBuffer](api_platformvm_outputs.parseableoutput.md#tobuffer)
* [comparator](api_platformvm_outputs.parseableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new ParseableOutput**(`output`: [Output](common_output.output.md)): *[ParseableOutput](api_platformvm_outputs.parseableoutput.md)*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[constructor](common_output.standardparseableoutput.md#constructor)*

*Defined in [src/common/output.ts:318](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L318)*

Class representing an [ParseableOutput](api_platformvm_outputs.parseableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`output` | [Output](common_output.output.md) | undefined | A number representing the InputID of the [ParseableOutput](api_platformvm_outputs.parseableoutput.md)  |

**Returns:** *[ParseableOutput](api_platformvm_outputs.parseableoutput.md)*

## Properties

### `Protected` output

• **output**: *[Output](common_output.output.md)*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[output](common_output.standardparseableoutput.md#protected-output)*

*Defined in [src/common/output.ts:296](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L296)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardParseableOutput](common_output.standardparseableoutput.md).[fromBuffer](common_output.standardparseableoutput.md#abstract-frombuffer)*

*Defined in [src/apis/platformvm/outputs.ts:40](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/outputs.ts#L40)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[getOutput](common_output.standardparseableoutput.md#getoutput)*

*Defined in [src/common/output.ts:307](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L307)*

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[toBuffer](common_output.standardparseableoutput.md#tobuffer)*

*Defined in [src/common/output.ts:312](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L312)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [StandardParseableOutput](common_output.standardparseableoutput.md).[comparator](common_output.standardparseableoutput.md#static-comparator)*

*Defined in [src/common/output.ts:301](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L301)*

Returns a function used to sort an array of [ParseableOutput](api_platformvm_outputs.parseableoutput.md)s

**Returns:** *function*

▸ (`a`: [StandardParseableOutput](common_output.standardparseableoutput.md), `b`: [StandardParseableOutput](common_output.standardparseableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
`b` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
