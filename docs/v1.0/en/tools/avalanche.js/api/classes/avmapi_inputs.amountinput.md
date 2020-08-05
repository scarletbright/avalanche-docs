[avalanche](../README.md) › [AVMAPI-Inputs](../modules/avmapi_inputs.md) › [AmountInput](avmapi_inputs.amountinput.md)

# Class: AmountInput

An [Input](avmapi_inputs.input.md) class which specifies a token amount .

## Hierarchy

* [Input](avmapi_inputs.input.md)

  ↳ **AmountInput**

  ↳ [SecpInput](avmapi_inputs.secpinput.md)

## Index

### Constructors

* [constructor](avmapi_inputs.amountinput.md#constructor)

### Properties

* [amount](avmapi_inputs.amountinput.md#protected-amount)
* [amountValue](avmapi_inputs.amountinput.md#protected-amountvalue)
* [sigCount](avmapi_inputs.amountinput.md#protected-sigcount)
* [sigIdxs](avmapi_inputs.amountinput.md#protected-sigidxs)

### Methods

* [addSignatureIdx](avmapi_inputs.amountinput.md#addsignatureidx)
* [fromBuffer](avmapi_inputs.amountinput.md#frombuffer)
* [getAmount](avmapi_inputs.amountinput.md#getamount)
* [getCredentialID](avmapi_inputs.amountinput.md#getcredentialid)
* [getInputID](avmapi_inputs.amountinput.md#abstract-getinputid)
* [getSigIdxs](avmapi_inputs.amountinput.md#getsigidxs)
* [toBuffer](avmapi_inputs.amountinput.md#tobuffer)
* [toString](avmapi_inputs.amountinput.md#tostring)
* [comparator](avmapi_inputs.amountinput.md#static-comparator)

## Constructors

###  constructor

\+ **new AmountInput**(`amount`: BN): *[AmountInput](avmapi_inputs.amountinput.md)*

*Overrides [Input](avmapi_inputs.input.md).[constructor](avmapi_inputs.input.md#constructor)*

*Defined in [src/apis/avm/inputs.ts:249](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L249)*

An [AmountInput](avmapi_inputs.amountinput.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the input  |

**Returns:** *[AmountInput](avmapi_inputs.amountinput.md)*

## Properties

### `Protected` amount

• **amount**: *Buffer* = Buffer.alloc(8)

*Defined in [src/apis/avm/inputs.ts:222](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L222)*

___

### `Protected` amountValue

• **amountValue**: *BN* = new BN(0)

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

### `Abstract` getInputID

▸ **getInputID**(): *number*

*Inherited from [Input](avmapi_inputs.input.md).[getInputID](avmapi_inputs.input.md#abstract-getinputid)*

*Defined in [src/apis/avm/inputs.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L36)*

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
