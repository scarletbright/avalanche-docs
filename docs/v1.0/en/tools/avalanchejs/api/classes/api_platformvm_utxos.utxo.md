[avalanche](../README.md) › [API-PlatformVM-UTXOs](../modules/api_platformvm_utxos.md) › [UTXO](api_platformvm_utxos.utxo.md)

# Class: UTXO

Class for representing a single UTXO.

## Hierarchy

* [StandardUTXO](common_utxos.standardutxo.md)

  ↳ **UTXO**

## Index

### Constructors

* [constructor](api_platformvm_utxos.utxo.md#constructor)

### Properties

* [assetid](api_platformvm_utxos.utxo.md#protected-assetid)
* [codecid](api_platformvm_utxos.utxo.md#protected-codecid)
* [output](api_platformvm_utxos.utxo.md#protected-output)
* [outputidx](api_platformvm_utxos.utxo.md#protected-outputidx)
* [txid](api_platformvm_utxos.utxo.md#protected-txid)

### Methods

* [clone](api_platformvm_utxos.utxo.md#clone)
* [create](api_platformvm_utxos.utxo.md#create)
* [fromBuffer](api_platformvm_utxos.utxo.md#frombuffer)
* [fromString](api_platformvm_utxos.utxo.md#fromstring)
* [getAssetID](api_platformvm_utxos.utxo.md#getassetid)
* [getCodecID](api_platformvm_utxos.utxo.md#getcodecid)
* [getCodecIDBuffer](api_platformvm_utxos.utxo.md#getcodecidbuffer)
* [getOutput](api_platformvm_utxos.utxo.md#getoutput)
* [getOutputIdx](api_platformvm_utxos.utxo.md#getoutputidx)
* [getTxID](api_platformvm_utxos.utxo.md#gettxid)
* [getUTXOID](api_platformvm_utxos.utxo.md#getutxoid)
* [toBuffer](api_platformvm_utxos.utxo.md#tobuffer)
* [toString](api_platformvm_utxos.utxo.md#tostring)

## Constructors

###  constructor

\+ **new UTXO**(`codecID`: number, `txid`: Buffer, `outputidx`: Buffer | number, `assetid`: Buffer, `output`: [Output](common_output.output.md)): *[UTXO](api_platformvm_utxos.utxo.md)*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[constructor](common_utxos.standardutxo.md#constructor)*

*Defined in [src/common/utxos.ts:105](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L105)*

Class for representing a single StandardUTXO.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`codecID` | number | 0 | Optional number which specifies the codeID of the UTXO. Default 1 |
`txid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of transaction ID for the StandardUTXO |
`outputidx` | Buffer &#124; number | undefined | - |
`assetid` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) of the asset ID for the StandardUTXO |
`output` | [Output](common_output.output.md) | undefined | - |

**Returns:** *[UTXO](api_platformvm_utxos.utxo.md)*

## Properties

### `Protected` assetid

• **assetid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[assetid](common_utxos.standardutxo.md#protected-assetid)*

*Defined in [src/common/utxos.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L28)*

___

### `Protected` codecid

• **codecid**: *Buffer* = Buffer.alloc(2)

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[codecid](common_utxos.standardutxo.md#protected-codecid)*

*Defined in [src/common/utxos.ts:22](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L22)*

___

### `Protected` output

• **output**: *[Output](common_output.output.md)* = undefined

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[output](common_utxos.standardutxo.md#protected-output)*

*Defined in [src/common/utxos.ts:30](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L30)*

___

### `Protected` outputidx

• **outputidx**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[outputidx](common_utxos.standardutxo.md#protected-outputidx)*

*Defined in [src/common/utxos.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L26)*

___

### `Protected` txid

• **txid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[txid](common_utxos.standardutxo.md#protected-txid)*

*Defined in [src/common/utxos.ts:24](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L24)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [StandardUTXO](common_utxos.standardutxo.md).[clone](common_utxos.standardutxo.md#abstract-clone)*

*Defined in [src/apis/platformvm/utxos.ts:74](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/utxos.ts#L74)*

**Returns:** *this*

___

###  create

▸ **create**(`codecID`: number, `txid`: Buffer, `outputidx`: Buffer | number, `assetid`: Buffer, `output`: [Output](common_output.output.md)): *this*

*Overrides [StandardUTXO](common_utxos.standardutxo.md).[create](common_utxos.standardutxo.md#abstract-create)*

*Defined in [src/apis/platformvm/utxos.ts:80](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/utxos.ts#L80)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`codecID` | number | PlatformVMConstants.LATESTCODEC |
`txid` | Buffer | undefined |
`outputidx` | Buffer &#124; number | undefined |
`assetid` | Buffer | undefined |
`output` | [Output](common_output.output.md) | undefined |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardUTXO](common_utxos.standardutxo.md).[fromBuffer](common_utxos.standardutxo.md#abstract-frombuffer)*

*Defined in [src/apis/platformvm/utxos.ts:33](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/utxos.ts#L33)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Overrides [StandardUTXO](common_utxos.standardutxo.md).[fromString](common_utxos.standardutxo.md#abstract-fromstring)*

*Defined in [src/apis/platformvm/utxos.ts:58](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/utxos.ts#L58)*

Takes a base-58 string containing a [UTXO](api_platformvm_utxos.utxo.md), parses it, populates the class, and returns the length of the StandardUTXO in bytes.

**`remarks`** 
unlike most fromStrings, it expects the string to be serialized in cb58 format

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`serialized` | string | A base-58 string containing a raw [UTXO](api_platformvm_utxos.utxo.md)  |

**Returns:** *number*

The length of the raw [UTXO](api_platformvm_utxos.utxo.md)

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getAssetID](common_utxos.standardutxo.md#getassetid)*

*Defined in [src/common/utxos.ts:61](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L61)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getCodecID

▸ **getCodecID**(): *number*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getCodecID](common_utxos.standardutxo.md#getcodecid)*

*Defined in [src/common/utxos.ts:35](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L35)*

Returns the numeric representation of the CodecID.

**Returns:** *number*

___

###  getCodecIDBuffer

▸ **getCodecIDBuffer**(): *Buffer*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getCodecIDBuffer](common_utxos.standardutxo.md#getcodecidbuffer)*

*Defined in [src/common/utxos.ts:42](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L42)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the CodecID

**Returns:** *Buffer*

___

###  getOutput

▸ **getOutput**(): *[Output](common_output.output.md)*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getOutput](common_utxos.standardutxo.md#getoutput)*

*Defined in [src/common/utxos.ts:73](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L73)*

Returns a reference to the output;

**Returns:** *[Output](common_output.output.md)*

___

###  getOutputIdx

▸ **getOutputIdx**(): *Buffer*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getOutputIdx](common_utxos.standardutxo.md#getoutputidx)*

*Defined in [src/common/utxos.ts:54](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L54)*

Returns a [Buffer](https://github.com/feross/buffer)  of the OutputIdx.

**Returns:** *Buffer*

___

###  getTxID

▸ **getTxID**(): *Buffer*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getTxID](common_utxos.standardutxo.md#gettxid)*

*Defined in [src/common/utxos.ts:47](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L47)*

Returns a [Buffer](https://github.com/feross/buffer) of the TxID.

**Returns:** *Buffer*

___

###  getUTXOID

▸ **getUTXOID**(): *string*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[getUTXOID](common_utxos.standardutxo.md#getutxoid)*

*Defined in [src/common/utxos.ts:66](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L66)*

Returns the UTXOID as a base-58 string (UTXOID is a string )

**Returns:** *string*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardUTXO](common_utxos.standardutxo.md).[toBuffer](common_utxos.standardutxo.md#tobuffer)*

*Defined in [src/common/utxos.ts:85](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/utxos.ts#L85)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardUTXO](common_utxos.standardutxo.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [StandardUTXO](common_utxos.standardutxo.md).[toString](common_utxos.standardutxo.md#abstract-tostring)*

*Defined in [src/apis/platformvm/utxos.ts:69](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/utxos.ts#L69)*

Returns a base-58 representation of the [UTXO](api_platformvm_utxos.utxo.md).

**`remarks`** 
unlike most toStrings, this returns in cb58 serialization format

**Returns:** *string*
