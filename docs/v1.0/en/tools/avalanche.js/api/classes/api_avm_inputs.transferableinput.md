[avalanche](../README.md) › [API-AVM-Inputs](../modules/api_avm_inputs.md) › [TransferableInput](api_avm_inputs.transferableinput.md)

# Class: TransferableInput

## Hierarchy

* [StandardTransferableInput](common_inputs.standardtransferableinput.md)

  ↳ **TransferableInput**

## Index

### Constructors

* [constructor](api_avm_inputs.transferableinput.md#constructor)

### Properties

* [assetid](api_avm_inputs.transferableinput.md#protected-assetid)
* [input](api_avm_inputs.transferableinput.md#protected-input)
* [outputidx](api_avm_inputs.transferableinput.md#protected-outputidx)
* [txid](api_avm_inputs.transferableinput.md#protected-txid)

### Methods

* [fromBuffer](api_avm_inputs.transferableinput.md#frombuffer)
* [getAssetID](api_avm_inputs.transferableinput.md#getassetid)
* [getInput](api_avm_inputs.transferableinput.md#getinput)
* [getOutputIdx](api_avm_inputs.transferableinput.md#getoutputidx)
* [getTxID](api_avm_inputs.transferableinput.md#gettxid)
* [getUTXOID](api_avm_inputs.transferableinput.md#getutxoid)
* [toBuffer](api_avm_inputs.transferableinput.md#tobuffer)
* [toString](api_avm_inputs.transferableinput.md#tostring)
* [comparator](api_avm_inputs.transferableinput.md#static-comparator)

## Constructors

###  constructor

\+ **new TransferableInput**(`txid`: Buffer, `outputidx`: Buffer, `assetID`: Buffer, `input`: [Input](common_inputs.input.md)): *[TransferableInput](api_avm_inputs.transferableinput.md)*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[constructor](common_inputs.standardtransferableinput.md#constructor)*

Defined in src/common/input.ts:166

Class representing an [StandardTransferableInput](common_inputs.standardtransferableinput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`outputidx` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](common_inputs.input.md) |
`input` | [Input](common_inputs.input.md) | undefined | An [Input](common_inputs.input.md) to be made transferable  |

**Returns:** *[TransferableInput](api_avm_inputs.transferableinput.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[assetid](common_inputs.standardtransferableinput.md#protected-assetid)*

Defined in src/common/input.ts:102

___

### `Protected` input

• **input**: *[Input](common_inputs.input.md)*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[input](common_inputs.standardtransferableinput.md#protected-input)*

Defined in src/common/input.ts:104

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[outputidx](common_inputs.standardtransferableinput.md#protected-outputidx)*

Defined in src/common/input.ts:100

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[txid](common_inputs.standardtransferableinput.md#protected-txid)*

Defined in src/common/input.ts:98

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardTransferableInput](common_inputs.standardtransferableinput.md).[fromBuffer](common_inputs.standardtransferableinput.md#abstract-frombuffer)*

Defined in src/apis/avm/inputs.ts:40

Takes a [Buffer](https://github.com/feross/buffer) containing a [TransferableInput](api_avm_inputs.transferableinput.md), parses it, populates the class, and returns the length of the [TransferableInput](api_avm_inputs.transferableinput.md) in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [TransferableInput](api_avm_inputs.transferableinput.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [TransferableInput](api_avm_inputs.transferableinput.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[getAssetID](common_inputs.standardtransferableinput.md#getassetid)*

Defined in src/common/input.ts:142

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInput

▸ **getInput**(): *[Input](common_inputs.input.md)*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[getInput](common_inputs.standardtransferableinput.md#getinput)*

Defined in src/common/input.ts:137

Returns the input.

**Returns:** *[Input](common_inputs.input.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[getOutputIdx](common_inputs.standardtransferableinput.md#getoutputidx)*

Defined in src/common/input.ts:125

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[getTxID](common_inputs.standardtransferableinput.md#gettxid)*

Defined in src/common/input.ts:118

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[getUTXOID](common_inputs.standardtransferableinput.md#getutxoid)*

Defined in src/common/input.ts:132

Returns a base-58 string representation of the UTXOID this [StandardTransferableInput](common_inputs.standardtransferableinput.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[toBuffer](common_inputs.standardtransferableinput.md#tobuffer)*

Defined in src/common/input.ts:150

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardTransferableInput](common_inputs.standardtransferableinput.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[toString](common_inputs.standardtransferableinput.md#tostring)*

Defined in src/common/input.ts:163

Returns a base-58 representation of the [StandardTransferableInput](common_inputs.standardtransferableinput.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [StandardTransferableInput](common_inputs.standardtransferableinput.md).[comparator](common_inputs.standardtransferableinput.md#static-comparator)*

Defined in src/common/input.ts:109

Returns a function used to sort an array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *function*

▸ (`a`: [StandardTransferableInput](common_inputs.standardtransferableinput.md), `b`: [StandardTransferableInput](common_inputs.standardtransferableinput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
`b` | [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
