[avalanche](../README.md) › [AVMAPI-Inputs](../modules/avmapi_inputs.md) › [TransferableInput](avmapi_inputs.transferableinput.md)

# Class: TransferableInput

## Hierarchy

* **TransferableInput**

## Index

### Constructors

* [constructor](avmapi_inputs.transferableinput.md#constructor)

### Properties

* [assetid](avmapi_inputs.transferableinput.md#protected-assetid)
* [input](avmapi_inputs.transferableinput.md#protected-input)
* [outputidx](avmapi_inputs.transferableinput.md#protected-outputidx)
* [txid](avmapi_inputs.transferableinput.md#protected-txid)

### Methods

* [fromBuffer](avmapi_inputs.transferableinput.md#frombuffer)
* [getAssetID](avmapi_inputs.transferableinput.md#getassetid)
* [getInput](avmapi_inputs.transferableinput.md#getinput)
* [getOutputIdx](avmapi_inputs.transferableinput.md#getoutputidx)
* [getTxID](avmapi_inputs.transferableinput.md#gettxid)
* [getUTXOID](avmapi_inputs.transferableinput.md#getutxoid)
* [toBuffer](avmapi_inputs.transferableinput.md#tobuffer)
* [toString](avmapi_inputs.transferableinput.md#tostring)
* [comparator](avmapi_inputs.transferableinput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableInput**(`txid`: Buffer, `outputidx`: Buffer, `assetID`: Buffer, `input`: [Input](avmapi_inputs.input.md)): *[TransferableInput](avmapi_inputs.transferableinput.md)*

*Defined in [apis/avm/inputs.ts:211](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L211)*

Class representing an [TransferableInput](avmapi_inputs.transferableinput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`outputidx` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [TransferableInput](avmapi_inputs.transferableinput.md) |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](avmapi_inputs.input.md) |
`input` | [Input](avmapi_inputs.input.md) | undefined | An [Input](avmapi_inputs.input.md) to be made transferable  |

**Returns:** *[TransferableInput](avmapi_inputs.transferableinput.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:121](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L121)*

___

### `Protected` input

• **input**: *[Input](avmapi_inputs.input.md)*

*Defined in [apis/avm/inputs.ts:122](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L122)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Defined in [apis/avm/inputs.ts:120](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L120)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Defined in [apis/avm/inputs.ts:119](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L119)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/inputs.ts:179](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L179)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [TransferableInput](avmapi_inputs.transferableinput.md), parses it, populates the class, and returns the length of the [TransferableInput](avmapi_inputs.transferableinput.md) in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [TransferableInput](avmapi_inputs.transferableinput.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [TransferableInput](avmapi_inputs.transferableinput.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/inputs.ts:168](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L168)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInput

▸ **getInput**(): *[Input](avmapi_inputs.input.md)*

*Defined in [apis/avm/inputs.ts:161](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L161)*

Returns the input.

**Returns:** *[Input](avmapi_inputs.input.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [apis/avm/inputs.ts:146](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L146)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [apis/avm/inputs.ts:138](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L138)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [apis/avm/inputs.ts:154](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L154)*

Returns a base-58 string representation of the UTXOID this [TransferableInput](avmapi_inputs.transferableinput.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/inputs.ts:195](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L195)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [TransferableInput](avmapi_inputs.transferableinput.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/inputs.ts:208](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L208)*

Returns a base-58 representation of the [TransferableInput](avmapi_inputs.transferableinput.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/inputs.ts:127](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/inputs.ts#L127)*

Returns a function used to sort an array of [TransferableInput](avmapi_inputs.transferableinput.md)s

**Returns:** *function*

▸ (`a`: [TransferableInput](avmapi_inputs.transferableinput.md), `b`: [TransferableInput](avmapi_inputs.transferableinput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableInput](avmapi_inputs.transferableinput.md) |
`b` | [TransferableInput](avmapi_inputs.transferableinput.md) |
