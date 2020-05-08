[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/utxos"](../modules/_apis_avm_utxos_.md) › [UTXO](_apis_avm_utxos_.utxo.md)

# Class: UTXO

Class for representing a single UTXO.

## Hierarchy

* **UTXO**

  ↳ [SecpUTXO](_apis_avm_utxos_.secputxo.md)

## Index

### Constructors

* [constructor](_apis_avm_utxos_.utxo.md#constructor)

### Properties

* [txid](_apis_avm_utxos_.utxo.md#protected-txid)
* [txidx](_apis_avm_utxos_.utxo.md#protected-txidx)

### Methods

* [fromBuffer](_apis_avm_utxos_.utxo.md#frombuffer)
* [fromString](_apis_avm_utxos_.utxo.md#fromstring)
* [getOuputID](_apis_avm_utxos_.utxo.md#getouputid)
* [getTxID](_apis_avm_utxos_.utxo.md#gettxid)
* [getTxIdx](_apis_avm_utxos_.utxo.md#gettxidx)
* [getUTXOID](_apis_avm_utxos_.utxo.md#getutxoid)
* [toBuffer](_apis_avm_utxos_.utxo.md#tobuffer)
* [toString](_apis_avm_utxos_.utxo.md#tostring)

## Constructors

###  constructor

\+ **new UTXO**(`txid`: Buffer, `txidx`: number): *[UTXO](_apis_avm_utxos_.utxo.md)*

*Defined in [apis/avm/utxos.ts:128](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L128)*

Class for representing a single UTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer |  undefined | Optional [Buffer](https://github.com/feross/buffer) of transaction ID for the UTXO |
`txidx` | number |  undefined | Optional number for the index of the transaction's [Output](_apis_avm_outputs_.output.md)  |

**Returns:** *[UTXO](_apis_avm_utxos_.utxo.md)*

## Properties

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/utxos.ts:44](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L44)*

___

### `Protected` txidx

• **txidx**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/utxos.ts:45](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L45)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/utxos.ts:80](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L80)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [UTXO](_apis_avm_utxos_.utxo.md), parses it, populates the class, and returns the length of the UTXO in bytes.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`utxobuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [apis/avm/utxos.ts:98](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L98)*

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

###  getOuputID

▸ **getOuputID**(): *number*

*Defined in [apis/avm/utxos.ts:47](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L47)*

**Returns:** *number*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [apis/avm/utxos.ts:54](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L54)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getTxIdx

▸ **getTxIdx**(): *Buffer*

*Defined in [apis/avm/utxos.ts:62](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L62)*

Returns a [Buffer](https://github.com/feross/buffer)  of the TxIdx.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [apis/avm/utxos.ts:70](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L70)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/utxos.ts:106](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L106)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/utxos.ts:125](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L125)*

Returns a base-58 representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
