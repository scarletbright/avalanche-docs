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

*Defined in [src/apis/avm/inputs.ts:249](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L249)*

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

*Defined in [src/apis/avm/inputs.ts:222](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L222)*

___

### `Protected` amountValue

• **amountValue**: *BN* = new BN(0)

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[amountValue](avmapi_inputs.amountinput.md#protected-amountvalue)*

*Defined in [src/apis/avm/inputs.ts:224](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L224)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* = Buffer.alloc(4)

*Inherited from [Input](avmapi_inputs.input.md).[sigCount](avmapi_inputs.input.md#protected-sigcount)*

*Defined in [src/apis/avm/inputs.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L32)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](avmapi_types.sigidx.md)›* = []

*Inherited from [Input](avmapi_inputs.input.md).[sigIdxs](avmapi_inputs.input.md#protected-sigidxs)*

*Defined in [src/apis/avm/inputs.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L34)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Input](avmapi_inputs.input.md).[addSignatureIdx](avmapi_inputs.input.md#addsignatureidx)*

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

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[fromBuffer](avmapi_inputs.amountinput.md#frombuffer)*

*Overrides [Input](avmapi_inputs.input.md).[fromBuffer](avmapi_inputs.input.md#frombuffer)*

*Defined in [src/apis/avm/inputs.ts:234](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L234)*

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

*Defined in [src/apis/avm/inputs.ts:229](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L229)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Inherited from [Input](avmapi_inputs.input.md).[getCredentialID](avmapi_inputs.input.md#getcredentialid)*

*Defined in [src/apis/avm/inputs.ts:43](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L43)*

**Returns:** *number*

___

###  getInputID

▸ **getInputID**(): *number*

*Overrides [Input](avmapi_inputs.input.md).[getInputID](avmapi_inputs.input.md#abstract-getinputid)*

*Defined in [src/apis/avm/inputs.ts:269](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L269)*

Returns the inputID for this input

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](avmapi_types.sigidx.md)›*

*Inherited from [Input](avmapi_inputs.input.md).[getSigIdxs](avmapi_inputs.input.md#getsigidxs)*

*Defined in [src/apis/avm/inputs.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L41)*

Returns the array of [SigIdx](avmapi_types.sigidx.md) for this [Input](avmapi_inputs.input.md)

**Returns:** *Array‹[SigIdx](avmapi_types.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [AmountInput](avmapi_inputs.amountinput.md).[toBuffer](avmapi_inputs.amountinput.md#tobuffer)*

*Overrides [Input](avmapi_inputs.input.md).[toBuffer](avmapi_inputs.input.md#tobuffer)*

*Defined in [src/apis/avm/inputs.ts:244](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L244)*

Returns the buffer representing the [AmountInput](avmapi_inputs.amountinput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Input](avmapi_inputs.input.md).[toString](avmapi_inputs.input.md#tostring)*

*Defined in [src/apis/avm/inputs.ts:91](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L91)*

Returns a base-58 representation of the [Input](avmapi_inputs.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Input](avmapi_inputs.input.md).[comparator](avmapi_inputs.input.md#static-comparator)*

*Defined in [src/apis/avm/inputs.ts:95](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L95)*

**Returns:** *function*

▸ (`a`: [Input](avmapi_inputs.input.md), `b`: [Input](avmapi_inputs.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](avmapi_inputs.input.md) |
`b` | [Input](avmapi_inputs.input.md) |
