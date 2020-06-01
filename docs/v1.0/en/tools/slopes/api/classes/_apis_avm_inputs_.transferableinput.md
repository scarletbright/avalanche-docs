[slopes - v1.7.1](../README.md) › ["apis/avm/inputs"](../modules/_apis_avm_inputs_.md) › [TransferableInput](_apis_avm_inputs_.transferableinput.md)

# Class: TransferableInput

## Hierarchy

* **TransferableInput**

## Index

### Constructors

* [constructor](_apis_avm_inputs_.transferableinput.md#constructor)

### Properties

* [assetid](_apis_avm_inputs_.transferableinput.md#protected-assetid)
* [input](_apis_avm_inputs_.transferableinput.md#protected-input)
* [outputidx](_apis_avm_inputs_.transferableinput.md#protected-outputidx)
* [txid](_apis_avm_inputs_.transferableinput.md#protected-txid)

### Methods

* [fromBuffer](_apis_avm_inputs_.transferableinput.md#frombuffer)
* [getAssetID](_apis_avm_inputs_.transferableinput.md#getassetid)
* [getInput](_apis_avm_inputs_.transferableinput.md#getinput)
* [getOutputIdx](_apis_avm_inputs_.transferableinput.md#getoutputidx)
* [getTxID](_apis_avm_inputs_.transferableinput.md#gettxid)
* [getUTXOID](_apis_avm_inputs_.transferableinput.md#getutxoid)
* [toBuffer](_apis_avm_inputs_.transferableinput.md#tobuffer)
* [toString](_apis_avm_inputs_.transferableinput.md#tostring)
* [comparator](_apis_avm_inputs_.transferableinput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableInput**(`txid`: Buffer, `outputidx`: Buffer, `assetID`: Buffer, `input`: [Input](_apis_avm_inputs_.input.md)): *[TransferableInput](_apis_avm_inputs_.transferableinput.md)*

*Defined in [apis/avm/inputs.ts:210](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L210)*

Class representing an [TransferableInput](_apis_avm_inputs_.transferableinput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer |  undefined | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`outputidx` | Buffer |  undefined | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [TransferableInput](_apis_avm_inputs_.transferableinput.md) |
`assetID` | Buffer |  undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](_apis_avm_inputs_.input.md) |
`input` | [Input](_apis_avm_inputs_.input.md) |  undefined | An [Input](_apis_avm_inputs_.input.md) to be made transferable  |

**Returns:** *[TransferableInput](_apis_avm_inputs_.transferableinput.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:120](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L120)*

___

### `Protected` input

• **input**: *[Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:121](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L121)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:119](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L119)*

___

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:118](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L118)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/inputs.ts:178](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L178)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [TransferableInput](_apis_avm_inputs_.transferableinput.md), parses it, populates the class, and returns the length of the [TransferableInput](_apis_avm_inputs_.transferableinput.md) in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [TransferableInput](_apis_avm_inputs_.transferableinput.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [TransferableInput](_apis_avm_inputs_.transferableinput.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/inputs.ts:167](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L167)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInput

▸ **getInput**(): *[Input](_apis_avm_inputs_.input.md)*

*Defined in [apis/avm/inputs.ts:160](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L160)*

Returns the input.

**Returns:** *[Input](_apis_avm_inputs_.input.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [apis/avm/inputs.ts:145](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L145)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [apis/avm/inputs.ts:137](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L137)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [apis/avm/inputs.ts:153](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L153)*

Returns a base-58 string representation of the UTXOID this [TransferableInput](_apis_avm_inputs_.transferableinput.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/inputs.ts:194](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L194)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [TransferableInput](_apis_avm_inputs_.transferableinput.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/inputs.ts:207](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L207)*

Returns a base-58 representation of the [TransferableInput](_apis_avm_inputs_.transferableinput.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/inputs.ts:126](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/inputs.ts#L126)*

Returns a function used to sort an array of [TransferableInput](_apis_avm_inputs_.transferableinput.md)s

**Returns:** *function*

▸ (`a`: [TransferableInput](_apis_avm_inputs_.transferableinput.md), `b`: [TransferableInput](_apis_avm_inputs_.transferableinput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableInput](_apis_avm_inputs_.transferableinput.md) |
`b` | [TransferableInput](_apis_avm_inputs_.transferableinput.md) |
