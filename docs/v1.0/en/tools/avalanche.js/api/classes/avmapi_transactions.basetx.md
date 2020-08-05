[avalanche](../README.md) › [AVMAPI-Transactions](../modules/avmapi_transactions.md) › [BaseTx](avmapi_transactions.basetx.md)

# Class: BaseTx

Class representing a base for all transactions.

## Hierarchy

* **BaseTx**

  ↳ [CreateAssetTx](avmapi_transactions.createassettx.md)

  ↳ [OperationTx](avmapi_transactions.operationtx.md)

## Index

### Constructors

* [constructor](avmapi_transactions.basetx.md#constructor)

### Properties

* [blockchainid](avmapi_transactions.basetx.md#protected-blockchainid)
* [ins](avmapi_transactions.basetx.md#protected-ins)
* [networkid](avmapi_transactions.basetx.md#protected-networkid)
* [numins](avmapi_transactions.basetx.md#protected-numins)
* [numouts](avmapi_transactions.basetx.md#protected-numouts)
* [outs](avmapi_transactions.basetx.md#protected-outs)

### Methods

* [fromBuffer](avmapi_transactions.basetx.md#frombuffer)
* [getBlockchainID](avmapi_transactions.basetx.md#getblockchainid)
* [getIns](avmapi_transactions.basetx.md#getins)
* [getNetworkID](avmapi_transactions.basetx.md#getnetworkid)
* [getOuts](avmapi_transactions.basetx.md#getouts)
* [getTxType](avmapi_transactions.basetx.md#gettxtype)
* [sign](avmapi_transactions.basetx.md#sign)
* [toBuffer](avmapi_transactions.basetx.md#tobuffer)
* [toString](avmapi_transactions.basetx.md#tostring)

## Constructors

###  constructor

\+ **new BaseTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›): *[BaseTx](avmapi_transactions.basetx.md)*

*Defined in [src/apis/avm/tx.ts:157](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L157)*

Class representing a BaseTx which is the foundation for all transactions.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](avmapi_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](avmapi_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](avmapi_inputs.transferableinput.md)s  |

**Returns:** *[BaseTx](avmapi_transactions.basetx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/apis/avm/tx.ts:28](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L28)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Defined in [src/apis/avm/tx.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L36)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/tx.ts:26](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L26)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/tx.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L34)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/tx.ts:30](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L30)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Defined in [src/apis/avm/tx.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L32)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/tx.ts:74](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L74)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [BaseTx](avmapi_transactions.basetx.md), parses it, populates the class, and returns the length of the BaseTx in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [BaseTx](avmapi_transactions.basetx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [BaseTx](avmapi_transactions.basetx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Defined in [src/apis/avm/tx.ts:53](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L53)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Defined in [src/apis/avm/tx.ts:58](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L58)*

Returns the array of [TransferableInput](avmapi_inputs.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [src/apis/avm/tx.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L48)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Defined in [src/apis/avm/tx.ts:63](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L63)*

Returns the array of [TransferableOutput](avmapi_outputs.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Defined in [src/apis/avm/tx.ts:41](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L41)*

Returns the id of the [BaseTx](avmapi_transactions.basetx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](avmapi_keychain.avmkeychain.md)): *Array‹[Credential](avmapi_credentials.credential.md)›*

*Defined in [src/apis/avm/tx.ts:142](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L142)*

Takes the bytes of an [UnsignedTx](avmapi_transactions.unsignedtx.md) and returns an array of [Credential](avmapi_credentials.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](avmapi_transactions.unsignedtx.md) |
`kc` | [AVMKeyChain](avmapi_keychain.avmkeychain.md) | An [AVMKeyChain](avmapi_keychain.avmkeychain.md) used in signing  |

**Returns:** *Array‹[Credential](avmapi_credentials.credential.md)›*

An array of [Credential](avmapi_credentials.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/apis/avm/tx.ts:104](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L104)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [BaseTx](avmapi_transactions.basetx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/tx.ts:130](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L130)*

Returns a base-58 representation of the [BaseTx](avmapi_transactions.basetx.md).

**Returns:** *string*
