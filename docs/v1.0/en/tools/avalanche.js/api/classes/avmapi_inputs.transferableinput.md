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

*Defined in [src/apis/avm/inputs.ts:198](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L198)*

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

*Defined in [src/apis/avm/inputs.ts:117](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L117)*

___

### `Protected` input

• **input**: *[Input](avmapi_inputs.input.md)*

*Defined in [src/apis/avm/inputs.ts:119](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L119)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/inputs.ts:115](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L115)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/inputs.ts:113](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L113)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/inputs.ts:166](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L166)*

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

*Defined in [src/apis/avm/inputs.ts:157](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L157)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInput

▸ **getInput**(): *[Input](avmapi_inputs.input.md)*

*Defined in [src/apis/avm/inputs.ts:152](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L152)*

Returns the input.

**Returns:** *[Input](avmapi_inputs.input.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [src/apis/avm/inputs.ts:140](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L140)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [src/apis/avm/inputs.ts:133](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L133)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [src/apis/avm/inputs.ts:147](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L147)*

Returns a base-58 string representation of the UTXOID this [TransferableInput](avmapi_inputs.transferableinput.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/inputs.ts:182](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L182)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [TransferableInput](avmapi_inputs.transferableinput.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/inputs.ts:195](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L195)*

Returns a base-58 representation of the [TransferableInput](avmapi_inputs.transferableinput.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/inputs.ts:124](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/inputs.ts#L124)*

Returns a function used to sort an array of [TransferableInput](avmapi_inputs.transferableinput.md)s

**Returns:** *function*

▸ (`a`: [TransferableInput](avmapi_inputs.transferableinput.md), `b`: [TransferableInput](avmapi_inputs.transferableinput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [TransferableInput](avmapi_inputs.transferableinput.md) |
`b` | [TransferableInput](avmapi_inputs.transferableinput.md) |
