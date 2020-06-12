[slopes - v1.7.5](../README.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [BaseTx](_apis_avm_tx_.basetx.md)

# Class: BaseTx

Class representing a base for all transactions.

## Hierarchy

* **BaseTx**

  ↳ [CreateAssetTx](_apis_avm_tx_.createassettx.md)

  ↳ [OperationTx](_apis_avm_tx_.operationtx.md)

## Index

### Constructors

* [constructor](_apis_avm_tx_.basetx.md#constructor)

### Properties

* [blockchainid](_apis_avm_tx_.basetx.md#protected-blockchainid)
* [ins](_apis_avm_tx_.basetx.md#protected-ins)
* [networkid](_apis_avm_tx_.basetx.md#protected-networkid)
* [numins](_apis_avm_tx_.basetx.md#protected-numins)
* [numouts](_apis_avm_tx_.basetx.md#protected-numouts)
* [outs](_apis_avm_tx_.basetx.md#protected-outs)

### Methods

* [fromBuffer](_apis_avm_tx_.basetx.md#frombuffer)
* [getBlockchainID](_apis_avm_tx_.basetx.md#getblockchainid)
* [getIns](_apis_avm_tx_.basetx.md#getins)
* [getNetworkID](_apis_avm_tx_.basetx.md#getnetworkid)
* [getOuts](_apis_avm_tx_.basetx.md#getouts)
* [getTxType](_apis_avm_tx_.basetx.md#gettxtype)
* [sign](_apis_avm_tx_.basetx.md#sign)
* [toBuffer](_apis_avm_tx_.basetx.md#tobuffer)
* [toString](_apis_avm_tx_.basetx.md#tostring)

## Constructors

###  constructor

\+ **new BaseTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›, `ins`: Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›): *[BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:179](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L179)*

Class representing a BaseTx which is the foundation for all transactions.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer |  Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)› |  undefined | Optional array of the [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)› |  undefined | Optional array of the [TransferableInput](_apis_avm_inputs_.transferableinput.md)s  |

**Returns:** *[BaseTx](_apis_avm_tx_.basetx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L46)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Defined in [apis/avm/tx.ts:50](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L50)*

___

### `Protected` networkid

• **networkid**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:45](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L45)*

___

### `Protected` numins

• **numins**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:49](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L49)*

___

### `Protected` numouts

• **numouts**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:47](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L47)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Defined in [apis/avm/tx.ts:48](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L48)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/tx.ts:96](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L96)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [BaseTx](_apis_avm_tx_.basetx.md), parses it, populates the class, and returns the length of the BaseTx in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [BaseTx](_apis_avm_tx_.basetx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [BaseTx](_apis_avm_tx_.basetx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Defined in [apis/avm/tx.ts:69](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L69)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Defined in [apis/avm/tx.ts:76](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L76)*

Returns the array of [TransferableInput](_apis_avm_inputs_.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [apis/avm/tx.ts:62](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L62)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Defined in [apis/avm/tx.ts:83](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L83)*

Returns the array of [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Defined in [apis/avm/tx.ts:55](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L55)*

Returns the id of the [BaseTx](_apis_avm_tx_.basetx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)): *Array‹[Credential](_apis_avm_credentials_.credential.md)›*

*Defined in [apis/avm/tx.ts:164](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L164)*

Takes the bytes of an [UnsignedTx](_apis_avm_tx_.unsignedtx.md) and returns an array of [Credential](_apis_avm_credentials_.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](_apis_avm_tx_.unsignedtx.md) |
`kc` | [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md) | An [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md) used in signing  |

**Returns:** *Array‹[Credential](_apis_avm_credentials_.credential.md)›*

An array of [Credential](_apis_avm_credentials_.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:126](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L126)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [BaseTx](_apis_avm_tx_.basetx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/tx.ts:152](https://github.com/ava-labs/slopes/blob/db73b16/src/apis/avm/tx.ts#L152)*

Returns a base-58 representation of the [BaseTx](_apis_avm_tx_.basetx.md).

**Returns:** *string*
