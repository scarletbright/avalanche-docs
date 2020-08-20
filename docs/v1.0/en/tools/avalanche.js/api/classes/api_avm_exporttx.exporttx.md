[avalanche](../README.md) › [API-AVM-ExportTx](../modules/api_avm_exporttx.md) › [ExportTx](api_avm_exporttx.exporttx.md)

# Class: ExportTx

Class representing an unsigned Export transaction.

## Hierarchy

  ↳ [BaseTx](api_avm_basetx.basetx.md)

  ↳ **ExportTx**

## Index

### Constructors

* [constructor](api_avm_exporttx.exporttx.md#constructor)

### Properties

* [blockchainid](api_avm_exporttx.exporttx.md#protected-blockchainid)
* [destinationChain](api_avm_exporttx.exporttx.md#protected-destinationchain)
* [exportOuts](api_avm_exporttx.exporttx.md#protected-exportouts)
* [ins](api_avm_exporttx.exporttx.md#protected-ins)
* [memo](api_avm_exporttx.exporttx.md#protected-memo)
* [networkid](api_avm_exporttx.exporttx.md#protected-networkid)
* [numOuts](api_avm_exporttx.exporttx.md#protected-numouts)
* [numins](api_avm_exporttx.exporttx.md#protected-numins)
* [numouts](api_avm_exporttx.exporttx.md#protected-numouts)
* [outs](api_avm_exporttx.exporttx.md#protected-outs)

### Methods

* [fromBuffer](api_avm_exporttx.exporttx.md#frombuffer)
* [getBlockchainID](api_avm_exporttx.exporttx.md#getblockchainid)
* [getDestinationChain](api_avm_exporttx.exporttx.md#getdestinationchain)
* [getExportOutputs](api_avm_exporttx.exporttx.md#getexportoutputs)
* [getExportOuts](api_avm_exporttx.exporttx.md#getexportouts)
* [getIns](api_avm_exporttx.exporttx.md#getins)
* [getMemo](api_avm_exporttx.exporttx.md#getmemo)
* [getNetworkID](api_avm_exporttx.exporttx.md#getnetworkid)
* [getOuts](api_avm_exporttx.exporttx.md#getouts)
* [getTxType](api_avm_exporttx.exporttx.md#gettxtype)
* [sign](api_avm_exporttx.exporttx.md#sign)
* [toBuffer](api_avm_exporttx.exporttx.md#tobuffer)
* [toString](api_avm_exporttx.exporttx.md#tostring)

## Constructors

###  constructor

\+ **new ExportTx**(`networkid`: number, `blockchainid`: Buffer, `destinationChain`: Buffer, `outs`: Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_avm_inputs.transferableinput.md)›, `memo`: Buffer, `exportOuts`: Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›): *[ExportTx](api_avm_exporttx.exporttx.md)*

*Overrides [BaseTx](api_avm_basetx.basetx.md).[constructor](api_avm_basetx.basetx.md#constructor)*

Defined in src/apis/avm/exporttx.ts:93

Class representing an unsigned Export transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Optional networkid, [DefaultNetworkID](../modules/common_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`destinationChain` | Buffer | undefined | Optional chainid which identifies where the funds will send to. |
`outs` | Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](api_avm_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | - |
`exportOuts` | Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)› | undefined | Array of [[TransferableOutputs]]s used in the transaction  |

**Returns:** *[ExportTx](api_avm_exporttx.exporttx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

Defined in src/common/tx.ts:24

___

### `Protected` destinationChain

• **destinationChain**: *Buffer* = undefined

Defined in src/apis/avm/exporttx.ts:24

___

### `Protected` exportOuts

• **exportOuts**: *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›* = []

Defined in src/apis/avm/exporttx.ts:26

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[ins](common_transactions.standardbasetx.md#protected-ins)*

Defined in src/common/tx.ts:28

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[memo](common_transactions.standardbasetx.md#protected-memo)*

Defined in src/common/tx.ts:29

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[networkid](common_transactions.standardbasetx.md#protected-networkid)*

Defined in src/common/tx.ts:23

___

### `Protected` numOuts

• **numOuts**: *Buffer* = Buffer.alloc(4)

Defined in src/apis/avm/exporttx.ts:25

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numins](common_transactions.standardbasetx.md#protected-numins)*

Defined in src/common/tx.ts:27

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numouts](common_transactions.standardbasetx.md#protected-numouts)*

Defined in src/common/tx.ts:25

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[outs](common_transactions.standardbasetx.md#protected-outs)*

Defined in src/common/tx.ts:26

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](api_avm_basetx.basetx.md).[fromBuffer](api_avm_basetx.basetx.md#frombuffer)*

Defined in src/apis/avm/exporttx.ts:58

Takes a [Buffer](https://github.com/feross/buffer) containing an [ExportTx](api_avm_exporttx.exporttx.md), parses it, populates the class, and returns the length of the [ExportTx](api_avm_exporttx.exporttx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [ExportTx](api_avm_exporttx.exporttx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [ExportTx](api_avm_exporttx.exporttx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)*

Defined in src/common/tx.ts:44

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getDestinationChain

▸ **getDestinationChain**(): *Buffer*

Defined in src/apis/avm/exporttx.ts:45

Returns a [Buffer](https://github.com/feross/buffer) for the destination chainid.

**Returns:** *Buffer*

___

###  getExportOutputs

▸ **getExportOutputs**(): *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

Defined in src/apis/avm/exporttx.ts:91

Returns an array of [TransferableOutput](api_avm_outputs.transferableoutput.md)s in this transaction.

**Returns:** *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

___

###  getExportOuts

▸ **getExportOuts**(): *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

Defined in src/apis/avm/exporttx.ts:38

Returns the exported outputs as an array of [TransferableOutput](api_avm_outputs.transferableoutput.md)

**Returns:** *Array‹[TransferableOutput](api_avm_outputs.transferableoutput.md)›*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getIns](common_transactions.standardbasetx.md#getins)*

Defined in src/common/tx.ts:49

Returns the array of [TransferableInput](api_avm_inputs.transferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getMemo](common_transactions.standardbasetx.md#getmemo)*

Defined in src/common/tx.ts:59

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getNetworkID](common_transactions.standardbasetx.md#getnetworkid)*

Defined in src/common/tx.ts:39

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

Defined in src/common/tx.ts:54

Returns the array of [TransferableOutput](api_avm_outputs.transferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](api_avm_basetx.basetx.md).[getTxType](api_avm_basetx.basetx.md#gettxtype)*

Defined in src/apis/avm/exporttx.ts:31

Returns the id of the [ExportTx](api_avm_exporttx.exporttx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](api_avm_keychain.avmkeychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Inherited from [BaseTx](api_avm_basetx.basetx.md).[sign](api_avm_basetx.basetx.md#sign)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[sign](common_transactions.standardbasetx.md#abstract-sign)*

Defined in src/apis/avm/basetx.ts:80

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [AVMKeyChain](api_avm_keychain.avmkeychain.md) | An [KeyChain](common_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[toBuffer](common_transactions.standardbasetx.md#tobuffer)*

Defined in src/apis/avm/exporttx.ts:76

Returns a [Buffer](https://github.com/feross/buffer) representation of the [ExportTx](api_avm_exporttx.exporttx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

Defined in src/common/tx.ts:96

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
