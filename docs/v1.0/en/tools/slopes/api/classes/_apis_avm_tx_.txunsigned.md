[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [TxUnsigned](_apis_avm_tx_.txunsigned.md)

# Class: TxUnsigned

Class representing an unsigned transaction.

**`remarks`** 
Unsigned Tx:
TxID      | 4 bytes
NetworkID  | 4 bytes
BlockchainID   | 32 bytes
NumOuts    | 4 bytes
Repeated (NumOuts):
    Out    | ? bytes
NumIns     | 4 bytes
Repeated (NumIns):
    In     | ? bytes

## Hierarchy

* **TxUnsigned**

  ↳ [TxCreateAsset](_apis_avm_tx_.txcreateasset.md)

## Index

### Constructors

* [constructor](_apis_avm_tx_.txunsigned.md#constructor)

### Properties

* [blockchainid](_apis_avm_tx_.txunsigned.md#protected-blockchainid)
* [ins](_apis_avm_tx_.txunsigned.md#protected-ins)
* [networkid](_apis_avm_tx_.txunsigned.md#protected-networkid)
* [numins](_apis_avm_tx_.txunsigned.md#protected-numins)
* [numouts](_apis_avm_tx_.txunsigned.md#protected-numouts)
* [outs](_apis_avm_tx_.txunsigned.md#protected-outs)
* [txtype](_apis_avm_tx_.txunsigned.md#protected-txtype)

### Methods

* [fromBuffer](_apis_avm_tx_.txunsigned.md#frombuffer)
* [getBlockchainID](_apis_avm_tx_.txunsigned.md#getblockchainid)
* [getIns](_apis_avm_tx_.txunsigned.md#getins)
* [getNetworkID](_apis_avm_tx_.txunsigned.md#getnetworkid)
* [getOuts](_apis_avm_tx_.txunsigned.md#getouts)
* [getTxType](_apis_avm_tx_.txunsigned.md#gettxtype)
* [toBuffer](_apis_avm_tx_.txunsigned.md#tobuffer)
* [toString](_apis_avm_tx_.txunsigned.md#tostring)

## Constructors

###  constructor

\+ **new TxUnsigned**(`ins?`: Array‹[Input](_apis_avm_inputs_.input.md)›, `outs?`: Array‹[Output](_apis_avm_outputs_.output.md)›, `networkid`: number, `blockchainid`: Buffer, `txtype`: number): *[TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:160](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L160)*

Class representing an unsigned transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`ins?` | Array‹[Input](_apis_avm_inputs_.input.md)› | - | Optional array of the [Input](_apis_avm_inputs_.input.md)s |
`outs?` | Array‹[Output](_apis_avm_outputs_.output.md)› | - | Optional array of the [Output](_apis_avm_outputs_.output.md)s |
`networkid` | number | 2 | Optional networkid, default 2 |
`blockchainid` | Buffer |  Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`txtype` | number | 0 | Optional txtype, default 2  |

**Returns:** *[TxUnsigned](_apis_avm_tx_.txunsigned.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/tx.ts:42](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L42)*

___

### `Protected` ins

• **ins**: *Array‹[Input](_apis_avm_inputs_.input.md)›*

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L46)*

___

### `Protected` networkid

• **networkid**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:41](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L41)*

___

### `Protected` numins

• **numins**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:45](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L45)*

___

### `Protected` numouts

• **numouts**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:43](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L43)*

___

### `Protected` outs

• **outs**: *Array‹[Output](_apis_avm_outputs_.output.md)›*

*Defined in [apis/avm/tx.ts:44](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L44)*

___

### `Protected` txtype

• **txtype**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:40](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L40)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/tx.ts:92](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L92)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [TxUnsigned](_apis_avm_tx_.txunsigned.md), parses it, populates the class, and returns the length of the TxUnsigned in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [TxUnsigned](_apis_avm_tx_.txunsigned.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [TxUnsigned](_apis_avm_tx_.txunsigned.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Defined in [apis/avm/tx.ts:65](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L65)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[Input](_apis_avm_inputs_.input.md)›*

*Defined in [apis/avm/tx.ts:72](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L72)*

Returns the array of [Input](_apis_avm_inputs_.input.md)s

**Returns:** *Array‹[Input](_apis_avm_inputs_.input.md)›*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [apis/avm/tx.ts:58](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L58)*

Returns the number representation of the NetworkID

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[Output](_apis_avm_outputs_.output.md)›*

*Defined in [apis/avm/tx.ts:79](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L79)*

Returns the array of [Output](_apis_avm_outputs_.output.md)s

**Returns:** *Array‹[Output](_apis_avm_outputs_.output.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Defined in [apis/avm/tx.ts:51](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L51)*

Returns the number representation of the txtype

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:125](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L125)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [TxUnsigned](_apis_avm_tx_.txunsigned.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/tx.ts:158](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L158)*

Returns a base-58 representation of the [TxUnsigned](_apis_avm_tx_.txunsigned.md).

**Returns:** *string*
