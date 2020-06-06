[slopes - v1.7.2](../README.md) › ["apis/avm/utxos"](../modules/_apis_avm_utxos_.md) › [UTXO](_apis_avm_utxos_.utxo.md)

# Class: UTXO

Class for representing a single UTXO.

## Hierarchy

* **UTXO**

## Index

### Constructors

* [constructor](_apis_avm_utxos_.utxo.md#constructor)

### Properties

* [assetid](_apis_avm_utxos_.utxo.md#protected-assetid)
* [output](_apis_avm_utxos_.utxo.md#protected-output)
* [outputidx](_apis_avm_utxos_.utxo.md#protected-outputidx)
* [txid](_apis_avm_utxos_.utxo.md#protected-txid)

### Methods

* [fromBuffer](_apis_avm_utxos_.utxo.md#frombuffer)
* [fromString](_apis_avm_utxos_.utxo.md#fromstring)
* [getAssetID](_apis_avm_utxos_.utxo.md#getassetid)
* [getOutput](_apis_avm_utxos_.utxo.md#getoutput)
* [getOutputIdx](_apis_avm_utxos_.utxo.md#getoutputidx)
* [getTxID](_apis_avm_utxos_.utxo.md#gettxid)
* [getUTXOID](_apis_avm_utxos_.utxo.md#getutxoid)
* [toBuffer](_apis_avm_utxos_.utxo.md#tobuffer)
* [toString](_apis_avm_utxos_.utxo.md#tostring)

## Constructors

###  constructor

\+ **new UTXO**(`txid`: Buffer, `outputidx`: Buffer | number, `assetid`: Buffer, `output`: [Output](_apis_avm_outputs_.output.md)): *[UTXO](_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:121](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L121)*

Class for representing a single UTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer |  undefined | Optional [Buffer](https://github.com/feross/buffer) of transaction ID for the UTXO |
`outputidx` | Buffer &#124; number |  undefined | - |
`assetid` | Buffer |  undefined | Optional [Buffer](https://github.com/feross/buffer) of the asset ID for the UTXO |
`output` | [Output](_apis_avm_outputs_.output.md) |  undefined | - |

**Returns:** *[UTXO](_apis_avm_utxos_.utxo.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/utxos.ts:25](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L25)*

___

### `Protected` output

• **output**: *[Output](_apis_avm_outputs_.output.md)* =  undefined

*Defined in [apis/avm/utxos.ts:26](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L26)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/utxos.ts:24](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L24)*

___

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/utxos.ts:23](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L23)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/utxos.ts:73](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L73)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [UTXO](_apis_avm_utxos_.utxo.md), parses it, populates the class, and returns the length of the UTXO in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [UTXO](_apis_avm_utxos_.utxo.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [apis/avm/utxos.ts:107](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L107)*

Takes a base-58 string containing an [UTXO](_apis_avm_utxos_.utxo.md), parses it, populates the class, and returns the length of the UTXO in bytes.

**`remarks`** 
unlike most fromStrings, it expects the string to be serialized in AVA format

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`serialized` | string | A base-58 string containing a raw [UTXO](_apis_avm_utxos_.utxo.md)  |

**Returns:** *number*

The length of the raw [UTXO](_apis_avm_utxos_.utxo.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/utxos.ts:47](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L47)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/utxos.ts:63](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L63)*

Returns a reference to the output;

**Returns:** *[Output](_apis_avm_outputs_.output.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [apis/avm/utxos.ts:39](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L39)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [apis/avm/utxos.ts:31](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L31)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [apis/avm/utxos.ts:54](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L54)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/utxos.ts:89](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L89)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/utxos.ts:118](https://github.com/ava-labs/slopes/blob/65cee65/src/apis/avm/utxos.ts#L118)*

Returns a base-58 representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
