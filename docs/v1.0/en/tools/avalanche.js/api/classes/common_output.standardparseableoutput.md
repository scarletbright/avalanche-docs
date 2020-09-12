[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [StandardParseableOutput](common_output.standardparseableoutput.md)

# Class: StandardParseableOutput

## Hierarchy

* **StandardParseableOutput**

  ↳ [StandardTransferableOutput](common_output.standardtransferableoutput.md)

  ↳ [ParseableOutput](api_platformvm_outputs.parseableoutput.md)

## Index

### Constructors

* [constructor](common_output.standardparseableoutput.md#constructor)

### Properties

* [output](common_output.standardparseableoutput.md#protected-output)

### Methods

* [fromBuffer](common_output.standardparseableoutput.md#abstract-frombuffer)
* [getOutput](common_output.standardparseableoutput.md#getoutput)
* [toBuffer](common_output.standardparseableoutput.md#tobuffer)
* [comparator](common_output.standardparseableoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new StandardParseableOutput**(`output`: [Output](common_output.output.md)): *[StandardParseableOutput](common_output.standardparseableoutput.md)*

*Defined in [src/common/output.ts:318](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L318)*

Class representing an [ParseableOutput](api_platformvm_outputs.parseableoutput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`output` | [Output](common_output.output.md) | undefined | A number representing the InputID of the [ParseableOutput](api_platformvm_outputs.parseableoutput.md)  |

**Returns:** *[StandardParseableOutput](common_output.standardparseableoutput.md)*

## Properties

### `Protected` output

• **output**: *[Output](common_output.output.md)*

*Defined in [src/common/output.ts:296](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L296)*

## Methods

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

*Defined in [src/common/output.ts:310](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L310)*

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset?` | number |

**Returns:** *number*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Defined in [src/common/output.ts:307](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L307)*

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/output.ts:312](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L312)*

**Returns:** *Buffer*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/common/output.ts:301](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L301)*

Returns a function used to sort an array of [ParseableOutput](api_platformvm_outputs.parseableoutput.md)s

**Returns:** *function*

▸ (`a`: [StandardParseableOutput](common_output.standardparseableoutput.md), `b`: [StandardParseableOutput](common_output.standardparseableoutput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
`b` | [StandardParseableOutput](common_output.standardparseableoutput.md) |
