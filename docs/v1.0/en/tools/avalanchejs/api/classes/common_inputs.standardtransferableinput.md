[avalanche](../README.md) › [Common-Inputs](../modules/common_inputs.md) › [StandardTransferableInput](common_inputs.standardtransferableinput.md)

# Class: StandardTransferableInput

## Hierarchy

* **StandardTransferableInput**

  ↳ [TransferableInput](api_avm_inputs.transferableinput.md)

  ↳ [TransferableInput](api_platformvm_inputs.transferableinput.md)

## Index

### Constructors

* [constructor](common_inputs.standardtransferableinput.md#constructor)

### Properties

* [assetid](common_inputs.standardtransferableinput.md#protected-assetid)
* [input](common_inputs.standardtransferableinput.md#protected-input)
* [outputidx](common_inputs.standardtransferableinput.md#protected-outputidx)
* [txid](common_inputs.standardtransferableinput.md#protected-txid)

### Methods

* [fromBuffer](common_inputs.standardtransferableinput.md#abstract-frombuffer)
* [getAssetID](common_inputs.standardtransferableinput.md#getassetid)
* [getInput](common_inputs.standardtransferableinput.md#getinput)
* [getOutputIdx](common_inputs.standardtransferableinput.md#getoutputidx)
* [getTxID](common_inputs.standardtransferableinput.md#gettxid)
* [getUTXOID](common_inputs.standardtransferableinput.md#getutxoid)
* [toBuffer](common_inputs.standardtransferableinput.md#tobuffer)
* [toString](common_inputs.standardtransferableinput.md#tostring)
* [comparator](common_inputs.standardtransferableinput.md#static-comparator)

## Constructors

###  constructor

\+ **new StandardTransferableInput**(`txid`: Buffer, `outputidx`: Buffer, `assetID`: Buffer, `input`: [Input](common_inputs.input.md)): *[StandardTransferableInput](common_inputs.standardtransferableinput.md)*

*Defined in [src/common/input.ts:172](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L172)*

Class representing an [StandardTransferableInput](common_inputs.standardtransferableinput.md) for a transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the transaction ID of the referenced UTXO |
`outputidx` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) containing the index of the output in the transaction consumed in the [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
`assetID` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) representing the assetID of the [Input](common_inputs.input.md) |
`input` | [Input](common_inputs.input.md) | undefined | An [Input](common_inputs.input.md) to be made transferable  |

**Returns:** *[StandardTransferableInput](common_inputs.standardtransferableinput.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/input.ts:108](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L108)*

___

### `Protected` input

• **input**: *[Input](common_inputs.input.md)*

*Defined in [src/common/input.ts:110](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L110)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/input.ts:106](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L106)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/input.ts:104](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L104)*

## Methods

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

*Defined in [src/common/input.ts:151](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L151)*

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset?` | number |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/common/input.ts:148](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L148)*

Returns the assetID of the input.

**Returns:** *Buffer*

___

###  getInput

▸ **getInput**(): *[Input](common_inputs.input.md)*

*Defined in [src/common/input.ts:143](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L143)*

Returns the input.

**Returns:** *[Input](common_inputs.input.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [src/common/input.ts:131](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L131)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [src/common/input.ts:124](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L124)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [src/common/input.ts:138](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L138)*

Returns a base-58 string representation of the UTXOID this [StandardTransferableInput](common_inputs.standardtransferableinput.md) references.

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/input.ts:156](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L156)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardTransferableInput](common_inputs.standardtransferableinput.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/common/input.ts:169](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L169)*

Returns a base-58 representation of the [StandardTransferableInput](common_inputs.standardtransferableinput.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/common/input.ts:115](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/input.ts#L115)*

Returns a function used to sort an array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *function*

▸ (`a`: [StandardTransferableInput](common_inputs.standardtransferableinput.md), `b`: [StandardTransferableInput](common_inputs.standardtransferableinput.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
`b` | [StandardTransferableInput](common_inputs.standardtransferableinput.md) |
