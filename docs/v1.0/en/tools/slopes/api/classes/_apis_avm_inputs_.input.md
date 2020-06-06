[slopes - v1.7.3](../README.md) › ["apis/avm/inputs"](../modules/_apis_avm_inputs_.md) › [Input](_apis_avm_inputs_.input.md)

# Class: Input

## Hierarchy

* **Input**

  ↳ [AmountInput](_apis_avm_inputs_.amountinput.md)

## Index

### Constructors

* [constructor](_apis_avm_inputs_.input.md#constructor)

### Properties

* [sigCount](_apis_avm_inputs_.input.md#protected-sigcount)
* [sigIdxs](_apis_avm_inputs_.input.md#protected-sigidxs)

### Methods

* [addSignatureIdx](_apis_avm_inputs_.input.md#addsignatureidx)
* [fromBuffer](_apis_avm_inputs_.input.md#frombuffer)
* [getCredentialID](_apis_avm_inputs_.input.md#getcredentialid)
* [getInputID](_apis_avm_inputs_.input.md#abstract-getinputid)
* [getSigIdxs](_apis_avm_inputs_.input.md#getsigidxs)
* [toBuffer](_apis_avm_inputs_.input.md#tobuffer)
* [toString](_apis_avm_inputs_.input.md#tostring)
* [comparator](_apis_avm_inputs_.input.md#static-comparator)

## Constructors

###  constructor

\+ **new Input**(): *[Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:111](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L111)*

**Returns:** *[Input](_apis_avm_inputs_.input.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:31](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L31)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›* =  []

*Defined in [apis/avm/inputs.ts:32](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L32)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [apis/avm/inputs.ts:53](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L53)*

Creates and adds a [SigIdx](_apis_avm_types_.sigidx.md) to the [Input](_apis_avm_inputs_.input.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/inputs.ts:63](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L63)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [apis/avm/inputs.ts:43](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L43)*

**Returns:** *number*

___

### `Abstract` getInputID

▸ **getInputID**(): *number*

*Defined in [apis/avm/inputs.ts:34](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L34)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

*Defined in [apis/avm/inputs.ts:39](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L39)*

Returns the array of [SigIdx](_apis_avm_types_.sigidx.md) for this [Input](_apis_avm_inputs_.input.md)

**Returns:** *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/inputs.ts:78](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L78)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/inputs.ts:93](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L93)*

Returns a base-58 representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/inputs.ts:97](https://github.com/ava-labs/slopes/blob/48cc94f/src/apis/avm/inputs.ts#L97)*

**Returns:** *function*

▸ (`a`: [Input](_apis_avm_inputs_.input.md), `b`: [Input](_apis_avm_inputs_.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](_apis_avm_inputs_.input.md) |
`b` | [Input](_apis_avm_inputs_.input.md) |
