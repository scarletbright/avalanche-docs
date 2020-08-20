[avalanche](../README.md) › [Common-Transactions](../modules/common_transactions.md) › [StandardBaseTx](common_transactions.standardbasetx.md)

# Class: StandardBaseTx ‹**KPClass, KCClass**›

Class representing a base for all transactions.

## Type parameters

▪ **KPClass**: *[KeyPair](common_keychain.keypair.md)*

▪ **KCClass**: *[KeyChain](common_keychain.keychain.md)‹KPClass›*

## Hierarchy

* **StandardBaseTx**

  ↳ [BaseTx](api_avm_basetx.basetx.md)

  ↳ [BaseTx](api_platformvm_basetx.basetx.md)

## Index

### Constructors

* [constructor](common_transactions.standardbasetx.md#constructor)

### Properties

* [blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)
* [getTxType](common_transactions.standardbasetx.md#abstract-gettxtype)
* [ins](common_transactions.standardbasetx.md#protected-ins)
* [memo](common_transactions.standardbasetx.md#protected-memo)
* [networkid](common_transactions.standardbasetx.md#protected-networkid)
* [numins](common_transactions.standardbasetx.md#protected-numins)
* [numouts](common_transactions.standardbasetx.md#protected-numouts)
* [outs](common_transactions.standardbasetx.md#protected-outs)

### Methods

* [getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)
* [getIns](common_transactions.standardbasetx.md#getins)
* [getMemo](common_transactions.standardbasetx.md#getmemo)
* [getNetworkID](common_transactions.standardbasetx.md#getnetworkid)
* [getOuts](common_transactions.standardbasetx.md#getouts)
* [sign](common_transactions.standardbasetx.md#abstract-sign)
* [toBuffer](common_transactions.standardbasetx.md#tobuffer)
* [toString](common_transactions.standardbasetx.md#tostring)

## Constructors

###  constructor

\+ **new StandardBaseTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›, `ins`: Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›, `memo`: Buffer): *[StandardBaseTx](common_transactions.standardbasetx.md)*

Defined in src/common/tx.ts:107

Class representing a StandardBaseTx which is the foundation for all transactions.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) for the memo field  |

**Returns:** *[StandardBaseTx](common_transactions.standardbasetx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

Defined in src/common/tx.ts:23

___

### `Abstract` getTxType

• **getTxType**: *function*

Defined in src/common/tx.ts:33

Returns the id of the [StandardBaseTx](common_transactions.standardbasetx.md)

#### Type declaration:

▸ (): *number*

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

Defined in src/common/tx.ts:27

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

Defined in src/common/tx.ts:28

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

Defined in src/common/tx.ts:22

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

Defined in src/common/tx.ts:26

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

Defined in src/common/tx.ts:24

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

Defined in src/common/tx.ts:25

## Methods

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

Defined in src/common/tx.ts:43

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

Defined in src/common/tx.ts:48

Returns the array of [TransferableInput](api_avm_inputs.transferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

Defined in src/common/tx.ts:58

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

Defined in src/common/tx.ts:38

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

Defined in src/common/tx.ts:53

Returns the array of [TransferableOutput](api_avm_outputs.transferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

### `Abstract` sign

▸ **sign**(`msg`: Buffer, `kc`: [KeyChain](common_keychain.keychain.md)‹KPClass›): *Array‹[Credential](common_signature.credential.md)›*

Defined in src/common/tx.ts:107

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [KeyChain](common_keychain.keychain.md)‹KPClass› | An [KeyChain](common_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/common/tx.ts:63

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

Defined in src/common/tx.ts:95

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
