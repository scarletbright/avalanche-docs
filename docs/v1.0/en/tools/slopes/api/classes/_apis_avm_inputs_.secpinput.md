[slopes - v1.7.2](../README.md) › ["apis/avm/inputs"](../modules/_apis_avm_inputs_.md) › [SecpInput](_apis_avm_inputs_.secpinput.md)

# Class: SecpInput

## Hierarchy

  ↳ [AmountInput](_apis_avm_inputs_.amountinput.md)

  ↳ **SecpInput**

## Index

### Constructors

* [constructor](_apis_avm_inputs_.secpinput.md#constructor)

### Properties

* [amount](_apis_avm_inputs_.secpinput.md#protected-amount)
* [amountValue](_apis_avm_inputs_.secpinput.md#protected-amountvalue)
* [sigCount](_apis_avm_inputs_.secpinput.md#protected-sigcount)
* [sigIdxs](_apis_avm_inputs_.secpinput.md#protected-sigidxs)

### Methods

* [addSignatureIdx](_apis_avm_inputs_.secpinput.md#addsignatureidx)
* [fromBuffer](_apis_avm_inputs_.secpinput.md#frombuffer)
* [getAmount](_apis_avm_inputs_.secpinput.md#getamount)
* [getCredentialID](_apis_avm_inputs_.secpinput.md#getcredentialid)
* [getInputID](_apis_avm_inputs_.secpinput.md#getinputid)
* [getSigIdxs](_apis_avm_inputs_.secpinput.md#getsigidxs)
* [toBuffer](_apis_avm_inputs_.secpinput.md#tobuffer)
* [toString](_apis_avm_inputs_.secpinput.md#tostring)
* [comparator](_apis_avm_inputs_.secpinput.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpInput**(`amount`: BN): *[SecpInput](_apis_avm_inputs_.secpinput.md)*

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md).[constructor](_apis_avm_inputs_.amountinput.md#constructor)*

*Overrides [Input](_apis_avm_inputs_.input.md).[constructor](_apis_avm_inputs_.input.md#constructor)*

*Defined in [apis/avm/inputs.ts:262](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L262)*

An [AmountInput](_apis_avm_inputs_.amountinput.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN |  undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the input  |

**Returns:** *[SecpInput](_apis_avm_inputs_.secpinput.md)*

## Properties

### `Protected` amount

• **amount**: *Buffer* =  Buffer.alloc(8)

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md).[amount](_apis_avm_inputs_.amountinput.md#protected-amount)*

*Defined in [apis/avm/inputs.ts:234](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L234)*

___

### `Protected` amountValue

• **amountValue**: *BN* =  new BN(0)

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md).[amountValue](_apis_avm_inputs_.amountinput.md#protected-amountvalue)*

*Defined in [apis/avm/inputs.ts:235](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L235)*

___

### `Protected` sigCount

• **sigCount**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Input](_apis_avm_inputs_.input.md).[sigCount](_apis_avm_inputs_.input.md#protected-sigcount)*

*Defined in [apis/avm/inputs.ts:31](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L31)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›* =  []

*Inherited from [Input](_apis_avm_inputs_.input.md).[sigIdxs](_apis_avm_inputs_.input.md#protected-sigidxs)*

*Defined in [apis/avm/inputs.ts:32](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L32)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:53](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L53)*

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

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md).[fromBuffer](_apis_avm_inputs_.amountinput.md#frombuffer)*

*Overrides [Input](_apis_avm_inputs_.input.md).[fromBuffer](_apis_avm_inputs_.input.md#frombuffer)*

*Defined in [apis/avm/inputs.ts:247](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L247)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [AmountInput](_apis_avm_inputs_.amountinput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAmount

▸ **getAmount**(): *BN*

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md)*

*Defined in [apis/avm/inputs.ts:240](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L240)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getCredentialID

▸ **getCredentialID**(): *number*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:43](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L43)*

**Returns:** *number*

___

###  getInputID

▸ **getInputID**(): *number*

*Overrides [Input](_apis_avm_inputs_.input.md).[getInputID](_apis_avm_inputs_.input.md#abstract-getinputid)*

*Defined in [apis/avm/inputs.ts:282](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L282)*

Returns the inputID for this input

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:39](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L39)*

Returns the array of [SigIdx](_apis_avm_types_.sigidx.md) for this [Input](_apis_avm_inputs_.input.md)

**Returns:** *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [AmountInput](_apis_avm_inputs_.amountinput.md).[toBuffer](_apis_avm_inputs_.amountinput.md#tobuffer)*

*Overrides [Input](_apis_avm_inputs_.input.md).[toBuffer](_apis_avm_inputs_.input.md#tobuffer)*

*Defined in [apis/avm/inputs.ts:257](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L257)*

Returns the buffer representing the [AmountInput](_apis_avm_inputs_.amountinput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Input](_apis_avm_inputs_.input.md).[toString](_apis_avm_inputs_.input.md#tostring)*

*Defined in [apis/avm/inputs.ts:93](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L93)*

Returns a base-58 representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:97](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/inputs.ts#L97)*

**Returns:** *function*

▸ (`a`: [Input](_apis_avm_inputs_.input.md), `b`: [Input](_apis_avm_inputs_.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](_apis_avm_inputs_.input.md) |
`b` | [Input](_apis_avm_inputs_.input.md) |
