[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/utxos"](../modules/_apis_avm_utxos_.md) › [SecpUTXO](_apis_avm_utxos_.secputxo.md)

# Class: SecpUTXO

Class for representing a single UTXO.

## Hierarchy

* [UTXO](_apis_avm_utxos_.utxo.md)

  ↳ **SecpUTXO**

## Index

### Constructors

* [constructor](_apis_avm_utxos_.secputxo.md#constructor)

### Properties

* [output](_apis_avm_utxos_.secputxo.md#protected-output)
* [txid](_apis_avm_utxos_.secputxo.md#protected-txid)
* [txidx](_apis_avm_utxos_.secputxo.md#protected-txidx)

### Methods

* [fromBuffer](_apis_avm_utxos_.secputxo.md#frombuffer)
* [fromString](_apis_avm_utxos_.secputxo.md#fromstring)
* [getAddress](_apis_avm_utxos_.secputxo.md#getaddress)
* [getAddressIdx](_apis_avm_utxos_.secputxo.md#getaddressidx)
* [getAddresses](_apis_avm_utxos_.secputxo.md#getaddresses)
* [getAmount](_apis_avm_utxos_.secputxo.md#getamount)
* [getAssetID](_apis_avm_utxos_.secputxo.md#getassetid)
* [getLocktime](_apis_avm_utxos_.secputxo.md#getlocktime)
* [getOuputID](_apis_avm_utxos_.secputxo.md#getouputid)
* [getSpenders](_apis_avm_utxos_.secputxo.md#getspenders)
* [getTxID](_apis_avm_utxos_.secputxo.md#gettxid)
* [getTxIdx](_apis_avm_utxos_.secputxo.md#gettxidx)
* [getUTXOID](_apis_avm_utxos_.secputxo.md#getutxoid)
* [meetsThreshold](_apis_avm_utxos_.secputxo.md#meetsthreshold)
* [toBuffer](_apis_avm_utxos_.secputxo.md#tobuffer)
* [toString](_apis_avm_utxos_.secputxo.md#tostring)

## Constructors

###  constructor

\+ **new SecpUTXO**(`txid`: Buffer, `txidx`: number, `secpoutput`: [SecpOutput](_apis_avm_outputs_.secpoutput.md)): *[SecpUTXO](_apis_avm_utxos_.secputxo.md)*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[constructor](_apis_avm_utxos_.utxo.md#constructor)*

*Defined in [apis/avm/utxos.ts:295](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L295)*

Class for representing a single UTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`txid` | Buffer |  undefined | Optional [Buffer](https://github.com/feross/buffer) representing the transaction ID |
`txidx` | number |  undefined | Optional number for the transaction index  |
`secpoutput` | [SecpOutput](_apis_avm_outputs_.secpoutput.md) |  undefined | - |

**Returns:** *[SecpUTXO](_apis_avm_utxos_.secputxo.md)*

## Properties

### `Protected` output

• **output**: *[SecpOutput](_apis_avm_outputs_.secpoutput.md)* =  undefined

*Defined in [apis/avm/utxos.ts:149](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L149)*

___

### `Protected` txid

• **txid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [UTXO](_apis_avm_utxos_.utxo.md).[txid](_apis_avm_utxos_.utxo.md#protected-txid)*

*Defined in [apis/avm/utxos.ts:44](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L44)*

___

### `Protected` txidx

• **txidx**: *Buffer* =  Buffer.alloc(4)

*Inherited from [UTXO](_apis_avm_utxos_.utxo.md).[txidx](_apis_avm_utxos_.utxo.md#protected-txidx)*

*Defined in [apis/avm/utxos.ts:45](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L45)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[fromBuffer](_apis_avm_utxos_.utxo.md#frombuffer)*

*Defined in [apis/avm/utxos.ts:234](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L234)*

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

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[fromString](_apis_avm_utxos_.utxo.md#fromstring)*

*Defined in [apis/avm/utxos.ts:252](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L252)*

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

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Defined in [apis/avm/utxos.ts:185](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L185)*

Gets the address at the index.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`idx` | number | The index of the address  |

**Returns:** *Buffer*

A [Buffer](https://github.com/feross/buffer) representing the address.

___

###  getAddressIdx

▸ **getAddressIdx**(`address`: Buffer): *number*

*Defined in [apis/avm/utxos.ts:174](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L174)*

Gets the index of the address in the output.

**Parameters:**

Name | Type |
------ | ------ |
`address` | Buffer |

**Returns:** *number*

An array of size two, the first index representing the index of the address, the second a boolean representing whether this result was a fallback (TakeItOrLeaveIt)

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:165](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L165)*

Gets the addresses in the UTXO as map of address to the locktime for the address as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *Array‹Buffer›*

___

###  getAmount

▸ **getAmount**(): *BN*

*Defined in [apis/avm/utxos.ts:158](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L158)*

Gets the amount in the UTXO as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/utxos.ts:192](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L192)*

Returns a [Buffer](https://github.com/feross/buffer) of the assetID.

**Returns:** *Buffer*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [apis/avm/utxos.ts:218](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L218)*

Returns a [BN](https://github.com/indutny/bn.js/) of the locktime.

**Returns:** *BN*

___

###  getOuputID

▸ **getOuputID**(): *number*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[getOuputID](_apis_avm_utxos_.utxo.md#getouputid)*

*Defined in [apis/avm/utxos.ts:151](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L151)*

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [apis/avm/utxos.ts:286](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L286)*

Given an array of addresses and an optional timestamp, returns an array of address strings of qualified spenders for the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN |  undefined |

**Returns:** *Array‹Buffer›*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[getTxID](_apis_avm_utxos_.utxo.md#gettxid)*

*Defined in [apis/avm/utxos.ts:204](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L204)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getTxIdx

▸ **getTxIdx**(): *Buffer*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[getTxIdx](_apis_avm_utxos_.utxo.md#gettxidx)*

*Defined in [apis/avm/utxos.ts:211](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L211)*

Returns a [Buffer](https://github.com/feross/buffer)  of the TxIdx.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[getUTXOID](_apis_avm_utxos_.utxo.md#getutxoid)*

*Defined in [apis/avm/utxos.ts:225](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L225)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [apis/avm/utxos.ts:293](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L293)*

Given an array of addresses and an optional timestamp, returns true if the addresses meet the threshold required to spend the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN |  undefined |

**Returns:** *boolean*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[toBuffer](_apis_avm_utxos_.utxo.md#tobuffer)*

*Defined in [apis/avm/utxos.ts:259](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L259)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [UTXO](_apis_avm_utxos_.utxo.md).[toString](_apis_avm_utxos_.utxo.md#tostring)*

*Defined in [apis/avm/utxos.ts:279](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/utxos.ts#L279)*

Returns a base-58 representation of the [UTXO](_apis_avm_utxos_.utxo.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
