[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/inputs"](../modules/_apis_avm_inputs_.md) › [SecpInput](_apis_avm_inputs_.secpinput.md)

# Class: SecpInput

## Hierarchy

* [Input](_apis_avm_inputs_.input.md)

  ↳ **SecpInput**

## Index

### Constructors

* [constructor](_apis_avm_inputs_.secpinput.md#constructor)

### Properties

* [amount](_apis_avm_inputs_.secpinput.md#protected-amount)
* [amountValue](_apis_avm_inputs_.secpinput.md#protected-amountvalue)
* [assetid](_apis_avm_inputs_.secpinput.md#protected-assetid)
* [inputid](_apis_avm_inputs_.secpinput.md#protected-inputid)
* [numAddr](_apis_avm_inputs_.secpinput.md#protected-numaddr)
* [sigIdxs](_apis_avm_inputs_.secpinput.md#protected-sigidxs)
* [txid](_apis_avm_inputs_.secpinput.md#protected-txid)
* [txidx](_apis_avm_inputs_.secpinput.md#protected-txidx)

### Methods

* [addSignatureIdx](_apis_avm_inputs_.secpinput.md#addsignatureidx)
* [fromBuffer](_apis_avm_inputs_.secpinput.md#frombuffer)
* [getAssetID](_apis_avm_inputs_.secpinput.md#getassetid)
* [getInputID](_apis_avm_inputs_.secpinput.md#getinputid)
* [getSigIdxs](_apis_avm_inputs_.secpinput.md#getsigidxs)
* [getUTXOID](_apis_avm_inputs_.secpinput.md#getutxoid)
* [toBuffer](_apis_avm_inputs_.secpinput.md#tobuffer)
* [toString](_apis_avm_inputs_.secpinput.md#tostring)
* [comparator](_apis_avm_inputs_.secpinput.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpInput**(`txid?`: Buffer, `txidx?`: Buffer, `amount?`: BN, `assetID?`: Buffer): *[SecpInput](_apis_avm_inputs_.secpinput.md)*

*Overrides [Input](_apis_avm_inputs_.input.md).[constructor](_apis_avm_inputs_.input.md#constructor)*

*Defined in [apis/avm/inputs.ts:230](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L230)*

Class representing an Input for a transaction.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txid?` | Buffer | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`txidx?` | Buffer | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [Input](_apis_avm_inputs_.input.md) |
`amount?` | BN | A [BN](https://github.com/indutny/bn.js/) containing the amount of the output to be consumed  |
`assetID?` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](_apis_avm_inputs_.input.md) |

**Returns:** *[SecpInput](_apis_avm_inputs_.secpinput.md)*

## Properties

### `Protected` amount

• **amount**: *Buffer* =  Buffer.alloc(8)

*Defined in [apis/avm/inputs.ts:147](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L147)*

___

### `Protected` amountValue

• **amountValue**: *BN* =  new BN(0)

*Defined in [apis/avm/inputs.ts:148](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L148)*

___

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [Input](_apis_avm_inputs_.input.md).[assetid](_apis_avm_inputs_.input.md#protected-assetid)*

*Defined in [apis/avm/inputs.ts:49](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L49)*

___

### `Protected` inputid

• **inputid**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Input](_apis_avm_inputs_.input.md).[inputid](_apis_avm_inputs_.input.md#protected-inputid)*

*Defined in [apis/avm/inputs.ts:50](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L50)*

___

### `Protected` numAddr

• **numAddr**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:149](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L149)*

___

### `Protected` sigIdxs

• **sigIdxs**: *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›* =  []

*Defined in [apis/avm/inputs.ts:150](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L150)*

___

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [Input](_apis_avm_inputs_.input.md).[txid](_apis_avm_inputs_.input.md#protected-txid)*

*Defined in [apis/avm/inputs.ts:47](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L47)*

___

### `Protected` txidx

• **txidx**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Input](_apis_avm_inputs_.input.md).[txidx](_apis_avm_inputs_.input.md#protected-txidx)*

*Defined in [apis/avm/inputs.ts:48](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L48)*

## Methods

###  addSignatureIdx

▸ **addSignatureIdx**(`addressIdx`: number, `address`: Buffer): *void*

*Defined in [apis/avm/inputs.ts:222](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L222)*

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

*Overrides [Input](_apis_avm_inputs_.input.md).[fromBuffer](_apis_avm_inputs_.input.md#frombuffer)*

*Defined in [apis/avm/inputs.ts:167](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L167)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [Input](_apis_avm_inputs_.input.md), parses it, populates the class, and returns the length of the [Input](_apis_avm_inputs_.input.md) in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [Input](_apis_avm_inputs_.input.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [Input](_apis_avm_inputs_.input.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:78](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L78)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInputID

▸ **getInputID**(): *number*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:71](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L71)*

Returns the number for the input type of the output class.

**Returns:** *number*

___

###  getSigIdxs

▸ **getSigIdxs**(): *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

*Defined in [apis/avm/inputs.ts:156](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L156)*

Returns the array of [SigIdx](_apis_avm_types_.sigidx.md) for this [Input](_apis_avm_inputs_.input.md)

**Returns:** *Array‹[SigIdx](_apis_avm_types_.sigidx.md)›*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:64](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L64)*

Returns a base-58 string representation of the UTXOID this [Input](_apis_avm_inputs_.input.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Input](_apis_avm_inputs_.input.md).[toBuffer](_apis_avm_inputs_.input.md#tobuffer)*

*Defined in [apis/avm/inputs.ts:189](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L189)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [Input](_apis_avm_inputs_.input.md).[toString](_apis_avm_inputs_.input.md#tostring)*

*Defined in [apis/avm/inputs.ts:212](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L212)*

Returns a base-58 representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:55](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L55)*

Returns a function used to sort an array of [Input](_apis_avm_inputs_.input.md)s

**Returns:** *function*

▸ (`a`: [Input](_apis_avm_inputs_.input.md), `b`: [Input](_apis_avm_inputs_.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](_apis_avm_inputs_.input.md) |
`b` | [Input](_apis_avm_inputs_.input.md) |
