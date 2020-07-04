[avalanche](../README.md) › [AVMAPI-Inputs](../modules/avmapi_inputs.md) › [Input](avmapi_inputs.input.md)

# Class: Input

## Hierarchy

* **Input**

  ↳ [AmountInput](avmapi_inputs.amountinput.md)

## Index

### Constructors

* [constructor](avmapi_inputs.input.md#constructor)

### Properties

* [sigCount](avmapi_inputs.input.md#protected-sigcount)
* [sigIdxs](avmapi_inputs.input.md#protected-sigidxs)

### Methods

* [addSignatureIdx](avmapi_inputs.input.md#addsignatureidx)
* [fromBuffer](avmapi_inputs.input.md#frombuffer)
* [getCredentialID](avmapi_inputs.input.md#getcredentialid)
* [getInputID](avmapi_inputs.input.md#abstract-getinputid)
* [getSigIdxs](avmapi_inputs.input.md#getsigidxs)
* [toBuffer](avmapi_inputs.input.md#tobuffer)
* [toString](avmapi_inputs.input.md#tostring)
* [comparator](avmapi_inputs.input.md#static-comparator)

## Constructors

###  constructor

\+ **new Input**(): *[Input](avmapi_inputs.input.md)*

*Defined in [src/apis/avm/inputs.ts:107](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L107)*

**Returns:** *[Input](avmapi_inputs.input.md)*

## Properties

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/inputs.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Defined in [src/apis/avm/inputs.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L34)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [src/apis/avm/inputs.ts:51](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L51)*

Creates and adds a [SigIdx](avmapi_types.sigidx.md) to the [Input](avmapi_inputs.input.md).

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`addressIdx` | number | The index of the address to reference in the signatures |
`address` | Buffer | The address of the source of the signature  |

**Returns:** *void*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/inputs.ts:61](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L61)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Defined in [src/apis/avm/inputs.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L43)*

**Returns:** *number*

___

### `Abstract` getInputID

▸ **getInputID**(): *number*

*Defined in [src/apis/avm/inputs.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L36)*

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Defined in [src/apis/avm/inputs.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L41)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Input](avmapi_inputs.input.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/inputs.ts:76](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L76)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/inputs.ts:91](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L91)*

Returns a base-58 representation of the [Input](avmapi_inputs.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/inputs.ts:95](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L95)*

**Returns:** *function*

▸ (`a`: [Input](avmapi_inputs.input.md), `b`: [Input](avmapi_inputs.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](avmapi_inputs.input.md) |
`b` | [Input](avmapi_inputs.input.md) |
