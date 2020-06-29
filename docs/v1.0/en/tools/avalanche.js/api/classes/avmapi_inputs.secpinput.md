[avalanche](../README.md) › [AVMAPI-Inputs](../modules/avmapi_inputs.md) › [SecpInput](avmapi_inputs.secpinput.md)

# Class: SecpInput

## Hierarchy

  ↳ [AmountInput](avmapi_inputs.amountinput.md)

  ↳ **SecpInput**

## Index

### Constructors

* [constructor](avmapi_inputs.secpinput.md#constructor)

### Properties

* [amount](avmapi_inputs.secpinput.md#protected-amount)
* [amountValue](avmapi_inputs.secpinput.md#protected-amountvalue)
* [sigCount](avmapi_inputs.secpinput.md#protected-sigcount)
* [sigIdxs](avmapi_inputs.secpinput.md#protected-sigidxs)

### Methods

* [addSignatureIdx](avmapi_inputs.secpinput.md#addsignatureidx)
* [fromBuffer](avmapi_inputs.secpinput.md#frombuffer)
* [getAmount](avmapi_inputs.secpinput.md#getamount)
* [getCredentialID](avmapi_inputs.secpinput.md#getcredentialid)
* [getInputID](avmapi_inputs.secpinput.md#getinputid)
* [getSigIdxs](avmapi_inputs.secpinput.md#getsigidxs)
* [toBuffer](avmapi_inputs.secpinput.md#tobuffer)
* [toString](avmapi_inputs.secpinput.md#tostring)
* [comparator](avmapi_inputs.secpinput.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpInput**(`amount`: BN): *[SecpInput](avmapi_inputs.secpinput.md)*

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[constructor](avmapi_inputs.amountinput.md#constructor)*

*Overrides [Input](avmapi_inputs.input.md).[constructor](avmapi_inputs.input.md#constructor)*

*Defined in [apis/avm/inputs.ts:263](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L263)*

An [AmountInput](avmapi_inputs.amountinput.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the input  |

**Returns:** *[SecpInput](avmapi_inputs.secpinput.md)*

## Properties

### `Protected` amount

• **amount**: *Buffer* = Buffer.alloc(8)

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[amount](avmapi_inputs.amountinput.md#protected-amount)*

*Defined in [apis/avm/inputs.ts:235](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L235)*

___

### `Protected` amountValue

• **amountValue**: *BN* = new BN(0)

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[amountValue](avmapi_inputs.amountinput.md#protected-amountvalue)*

*Defined in [apis/avm/inputs.ts:236](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L236)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Input](avmapi_inputs.input.md).[sigCount](avmapi_inputs.input.md#protected-sigcount)*

*Defined in [apis/avm/inputs.ts:32](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Inherited from [Input](avmapi_inputs.input.md).[sigIdxs](avmapi_inputs.input.md#protected-sigidxs)*

*Defined in [apis/avm/inputs.ts:33](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L33)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Input](avmapi_inputs.input.md).[addSignatureIdx](avmapi_inputs.input.md#addsignatureidx)*

*Defined in [apis/avm/inputs.ts:54](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L54)*

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

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[fromBuffer](avmapi_inputs.amountinput.md#frombuffer)*

*Overrides [Input](avmapi_inputs.input.md).[fromBuffer](avmapi_inputs.input.md#frombuffer)*

*Defined in [apis/avm/inputs.ts:248](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L248)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [AmountInput](avmapi_inputs.amountinput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAmount

▸ **getAmount**(): *BN*

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[getAmount](avmapi_inputs.amountinput.md#getamount)*

*Defined in [apis/avm/inputs.ts:241](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L241)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Inherited from [Input](avmapi_inputs.input.md).[getCredentialID](avmapi_inputs.input.md#getcredentialid)*

*Defined in [apis/avm/inputs.ts:44](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L44)*

**Returns:** *number*

___

###  getInputID

▸ **getInputID**(): *number*

*Overrides [Input](avmapi_inputs.input.md).[getInputID](avmapi_inputs.input.md#abstract-getinputid)*

*Defined in [apis/avm/inputs.ts:283](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L283)*

Returns the inputID for this input

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Inherited from [Input](avmapi_inputs.input.md).[getSigIdxs](avmapi_inputs.input.md#getsigidxs)*

*Defined in [apis/avm/inputs.ts:40](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L40)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Input](avmapi_inputs.input.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[toBuffer](avmapi_inputs.amountinput.md#tobuffer)*

*Overrides [Input](avmapi_inputs.input.md).[toBuffer](avmapi_inputs.input.md#tobuffer)*

*Defined in [apis/avm/inputs.ts:258](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L258)*

Returns the buffer representing the [AmountInput](avmapi_inputs.amountinput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Input](avmapi_inputs.input.md).[toString](avmapi_inputs.input.md#tostring)*

*Defined in [apis/avm/inputs.ts:94](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L94)*

Returns a base-58 representation of the [Input](avmapi_inputs.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Input](avmapi_inputs.input.md).[comparator](avmapi_inputs.input.md#static-comparator)*

*Defined in [apis/avm/inputs.ts:98](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/inputs.ts#L98)*

**Returns:** *function*

▸ (`a`: [Input](avmapi_inputs.input.md), `b`: [Input](avmapi_inputs.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](avmapi_inputs.input.md) |
`b` | [Input](avmapi_inputs.input.md) |
