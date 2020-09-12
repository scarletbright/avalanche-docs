[avalanche](../README.md) › [Common-UTXOs](../modules/common_utxos.md) › [StandardUTXO](common_utxos.standardutxo.md)

# Class: StandardUTXO

Class for representing a single StandardUTXO.

## Hierarchy

* **StandardUTXO**

  ↳ [UTXO](api_avm_utxos.utxo.md)

  ↳ [UTXO](api_platformvm_utxos.utxo.md)

## Index

### Constructors

* [constructor](common_utxos.standardutxo.md#constructor)

### Properties

* [assetid](common_utxos.standardutxo.md#protected-assetid)
* [codecid](common_utxos.standardutxo.md#protected-codecid)
* [output](common_utxos.standardutxo.md#protected-output)
* [outputidx](common_utxos.standardutxo.md#protected-outputidx)
* [txid](common_utxos.standardutxo.md#protected-txid)

### Methods

* [clone](common_utxos.standardutxo.md#abstract-clone)
* [create](common_utxos.standardutxo.md#abstract-create)
* [fromBuffer](common_utxos.standardutxo.md#abstract-frombuffer)
* [fromString](common_utxos.standardutxo.md#abstract-fromstring)
* [getAssetID](common_utxos.standardutxo.md#getassetid)
* [getCodecID](common_utxos.standardutxo.md#getcodecid)
* [getCodecIDBuffer](common_utxos.standardutxo.md#getcodecidbuffer)
* [getOutput](common_utxos.standardutxo.md#getoutput)
* [getOutputIdx](common_utxos.standardutxo.md#getoutputidx)
* [getTxID](common_utxos.standardutxo.md#gettxid)
* [getUTXOID](common_utxos.standardutxo.md#getutxoid)
* [toBuffer](common_utxos.standardutxo.md#tobuffer)
* [toString](common_utxos.standardutxo.md#abstract-tostring)

## Constructors

###  constructor

\+ **new StandardUTXO**(`codecID`: number, `txid`: Buffer, `outputidx`: Buffer | number, `assetid`: Buffer, `output`: [Output](common_output.output.md)): *[StandardUTXO](common_utxos.standardutxo.md)*

*Defined in [src/common/utxos.ts:105](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L105)*

Class for representing a single StandardUTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`codecID` | number | 0 | Optional number which specifies the codeID of the UTXO. Default 1 |
`txid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of transaction ID for the StandardUTXO |
`outputidx` | Buffer &#124; number | undefined | - |
`assetid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of the asset ID for the StandardUTXO |
`output` | [Output](common_output.output.md) | undefined | - |

**Returns:** *[StandardUTXO](common_utxos.standardutxo.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/utxos.ts:28](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L28)*

___

### `Protected` codecid

• **codecid**: *Buffer* = Buffer.alloc(2)

*Defined in [src/common/utxos.ts:22](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L22)*

___

### `Protected` output

• **output**: *[Output](common_output.output.md)* = undefined

*Defined in [src/common/utxos.ts:30](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L30)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/utxos.ts:26](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L26)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/utxos.ts:24](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L24)*

## Methods

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/utxos.ts:100](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L100)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(`codecID?`: number, `txid?`: Buffer, `outputidx?`: Buffer | number, `assetid?`: Buffer, `output?`: [Output](common_output.output.md)): *this*

*Defined in [src/common/utxos.ts:102](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L102)*

**Parameters:**

Name | Type |
------ | ------ |
`codecID?` | number |
`txid?` | Buffer |
`outputidx?` | Buffer &#124; number |
`assetid?` | Buffer |
`output?` | [Output](common_output.output.md) |

**Returns:** *this*

___

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

*Defined in [src/common/utxos.ts:80](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L80)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [StandardUTXO](common_utxos.standardutxo.md), parses it, populates the class, and returns the length of the StandardUTXO in bytes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer | A [Buffer](https://github.com/feross/buffer) containing a raw [StandardUTXO](common_utxos.standardutxo.md)  |
`offset?` | number | - |

**Returns:** *number*

___

### `Abstract` fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [src/common/utxos.ts:96](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L96)*

**Parameters:**

Name | Type |
------ | ------ |
`serialized` | string |

**Returns:** *number*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [src/common/utxos.ts:61](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L61)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getCodecID

▸ **getCodecID**(): *number*

*Defined in [src/common/utxos.ts:35](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L35)*

Returns the numeric representation of the CodecID.

**Returns:** *number*

___

###  getCodecIDBuffer

▸ **getCodecIDBuffer**(): *Buffer*

*Defined in [src/common/utxos.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L42)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the CodecID

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Defined in [src/common/utxos.ts:73](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L73)*

Returns a reference to the output;

**Returns:** *[Output](common_output.output.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Defined in [src/common/utxos.ts:54](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L54)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Defined in [src/common/utxos.ts:47](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L47)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Defined in [src/common/utxos.ts:66](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L66)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/utxos.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L85)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardUTXO](common_utxos.standardutxo.md).

**Returns:** *Buffer*

___

### `Abstract` toString

▸ **toString**(): *string*

*Defined in [src/common/utxos.ts:98](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/utxos.ts#L98)*

**Returns:** *string*
