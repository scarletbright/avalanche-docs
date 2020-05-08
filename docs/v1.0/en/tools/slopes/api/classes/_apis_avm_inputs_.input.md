[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/inputs"](../modules/_apis_avm_inputs_.md) › [Input](_apis_avm_inputs_.input.md)

# Class: Input

## Hierarchy

* **Input**

  ↳ [SecpInput](_apis_avm_inputs_.secpinput.md)

## Index

### Constructors

* [constructor](_apis_avm_inputs_.input.md#constructor)

### Properties

* [assetid](_apis_avm_inputs_.input.md#protected-assetid)
* [inputid](_apis_avm_inputs_.input.md#protected-inputid)
* [txid](_apis_avm_inputs_.input.md#protected-txid)
* [txidx](_apis_avm_inputs_.input.md#protected-txidx)

### Methods

* [fromBuffer](_apis_avm_inputs_.input.md#frombuffer)
* [getAssetID](_apis_avm_inputs_.input.md#getassetid)
* [getInputID](_apis_avm_inputs_.input.md#getinputid)
* [getUTXOID](_apis_avm_inputs_.input.md#getutxoid)
* [toBuffer](_apis_avm_inputs_.input.md#tobuffer)
* [toString](_apis_avm_inputs_.input.md#tostring)
* [comparator](_apis_avm_inputs_.input.md#static-comparator)

## Constructors

###  constructor

\+ **new Input**(`txid?`: Buffer, `txidx?`: Buffer, `assetID?`: Buffer, `inputid?`: number): *[Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:125](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L125)*

Class representing an Input for a transaction.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`txid?` | Buffer | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`txidx?` | Buffer | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [Input](_apis_avm_inputs_.input.md) |
`assetID?` | Buffer | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](_apis_avm_inputs_.input.md) |
`inputid?` | number | A number representing the InputID of the [Input](_apis_avm_inputs_.input.md)  |

**Returns:** *[Input](_apis_avm_inputs_.input.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:49](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L49)*

___

### `Protected` inputid

• **inputid**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:50](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L50)*

___

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:47](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L47)*

___

### `Protected` txidx

• **txidx**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:48](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L48)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/inputs.ts:90](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L90)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [Input](_apis_avm_inputs_.input.md), parses it, populates the class, and returns the length of the Input in bytes.

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

*Defined in [apis/avm/inputs.ts:78](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L78)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInputID

▸ **getInputID**(): *number*

*Defined in [apis/avm/inputs.ts:71](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L71)*

Returns the number for the input type of the output class.

**Returns:** *number*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [apis/avm/inputs.ts:64](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L64)*

Returns a base-58 string representation of the UTXOID this [Input](_apis_avm_inputs_.input.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/inputs.ts:105](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L105)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/inputs.ts:122](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L122)*

Returns a base-58 representation of the [Input](_apis_avm_inputs_.input.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/inputs.ts:55](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/inputs.ts#L55)*

Returns a function used to sort an array of [Input](_apis_avm_inputs_.input.md)s

**Returns:** *function*

▸ (`a`: [Input](_apis_avm_inputs_.input.md), `b`: [Input](_apis_avm_inputs_.input.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Input](_apis_avm_inputs_.input.md) |
`b` | [Input](_apis_avm_inputs_.input.md) |
