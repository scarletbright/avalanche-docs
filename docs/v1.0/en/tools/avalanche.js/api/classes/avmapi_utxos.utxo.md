[avalanche](../README.md) › [AVMAPI-UTXOs](../modules/avmapi_utxos.md) › [UTXO](avmapi_utxos.utxo.md)

# Class: UTXO

Class for representing a single UTXO.

## Hierarchy

* **UTXO**

## Index

### Constructors

* [constructor](avmapi_utxos.utxo.md#constructor)

### Properties

* [assetid](avmapi_utxos.utxo.md#protected-assetid)
* [output](avmapi_utxos.utxo.md#protected-output)
* [outputidx](avmapi_utxos.utxo.md#protected-outputidx)
* [txid](avmapi_utxos.utxo.md#protected-txid)

### Methods

* [fromBuffer](avmapi_utxos.utxo.md#frombuffer)
* [fromString](avmapi_utxos.utxo.md#fromstring)
* [getAssetID](avmapi_utxos.utxo.md#getassetid)
* [getOutput](avmapi_utxos.utxo.md#getoutput)
* [getOutputIdx](avmapi_utxos.utxo.md#getoutputidx)
* [getTxID](avmapi_utxos.utxo.md#gettxid)
* [getUTXOID](avmapi_utxos.utxo.md#getutxoid)
* [toBuffer](avmapi_utxos.utxo.md#tobuffer)
* [toString](avmapi_utxos.utxo.md#tostring)

## Constructors

###  constructor

\+ **new UTXO**(`txid`: Buffer, `outputidx`: Buffer | number, `assetid`: Buffer, `output`: [Output](avmapi_outputs.output.md)): *[UTXO](avmapi_utxos.utxo.md)*

*Defined in [src/apis/avm/utxos.ts:124](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L124)*

Class for representing a single UTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of transaction ID for the UTXO |
`outputidx` | Buffer &#124; number | undefined | - |
`assetid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of the asset ID for the UTXO |
`output` | [Output](avmapi_outputs.output.md) | undefined | - |

**Returns:** *[UTXO](avmapi_utxos.utxo.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/utxos.ts:33](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L33)*

___

### `Protected` output

• **output**: *[Output](avmapi_outputs.output.md)* = undefined

*Defined in [src/apis/avm/utxos.ts:35](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L35)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/utxos.ts:31](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L31)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/utxos.ts:29](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L29)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/utxos.ts:73](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L73)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [UTXO](avmapi_utxos.utxo.md), parses it, populates the class, and returns the length of the UTXO in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [UTXO](avmapi_utxos.utxo.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [src/apis/avm/utxos.ts:110](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L110)*

Takes a base-58 string containing an [UTXO](avmapi_utxos.utxo.md), parses it, populates the class, and returns the length of the UTXO in bytes.

**`remarks`** 
unlike most fromStrings, it expects the string to be serialized in AVA format

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`serialized` | string | A base-58 string containing a raw [UTXO](avmapi_utxos.utxo.md)  |

**Returns:** *number*

The length of the raw [UTXO](avmapi_utxos.utxo.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/apis/avm/utxos.ts:54](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L54)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](avmapi_outputs.output.md)*

*Defined in [src/apis/avm/utxos.ts:66](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L66)*

Returns a reference to the output;

**Returns:** *[Output](avmapi_outputs.output.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [src/apis/avm/utxos.ts:47](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L47)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [src/apis/avm/utxos.ts:40](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L40)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [src/apis/avm/utxos.ts:59](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L59)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/utxos.ts:89](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L89)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [UTXO](avmapi_utxos.utxo.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/utxos.ts:121](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/utxos.ts#L121)*

Returns a base-58 representation of the [UTXO](avmapi_utxos.utxo.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
