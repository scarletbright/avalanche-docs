[avalanche](../README.md) › [API-PlatformVM-ExportTx](../modules/api_platformvm_exporttx.md) › [ImportTx](api_platformvm_exporttx.importtx.md)

# Class: ImportTx

Class representing an unsigned Import transaction.

## Hierarchy

  ↳ [BaseTx](api_platformvm_basetx.basetx.md)

  ↳ **ImportTx**

## Index

### Constructors

* [constructor](api_platformvm_exporttx.importtx.md#constructor)

### Properties

* [blockchainid](api_platformvm_exporttx.importtx.md#protected-blockchainid)
* [importIns](api_platformvm_exporttx.importtx.md#protected-importins)
* [ins](api_platformvm_exporttx.importtx.md#protected-ins)
* [memo](api_platformvm_exporttx.importtx.md#protected-memo)
* [networkid](api_platformvm_exporttx.importtx.md#protected-networkid)
* [numIns](api_platformvm_exporttx.importtx.md#protected-numins)
* [numins](api_platformvm_exporttx.importtx.md#protected-numins)
* [numouts](api_platformvm_exporttx.importtx.md#protected-numouts)
* [outs](api_platformvm_exporttx.importtx.md#protected-outs)
* [sourceChain](api_platformvm_exporttx.importtx.md#protected-sourcechain)

### Methods

* [fromBuffer](api_platformvm_exporttx.importtx.md#frombuffer)
* [getBlockchainID](api_platformvm_exporttx.importtx.md#getblockchainid)
* [getImportInputs](api_platformvm_exporttx.importtx.md#getimportinputs)
* [getIns](api_platformvm_exporttx.importtx.md#getins)
* [getMemo](api_platformvm_exporttx.importtx.md#getmemo)
* [getNetworkID](api_platformvm_exporttx.importtx.md#getnetworkid)
* [getOuts](api_platformvm_exporttx.importtx.md#getouts)
* [getTxType](api_platformvm_exporttx.importtx.md#gettxtype)
* [sign](api_platformvm_exporttx.importtx.md#sign)
* [toBuffer](api_platformvm_exporttx.importtx.md#tobuffer)
* [toString](api_platformvm_exporttx.importtx.md#tostring)

## Constructors

###  constructor

\+ **new ImportTx**(`networkid`: number, `blockchainid`: Buffer, `sourceChain`: Buffer, `outs`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›, `memo`: Buffer, `importIns`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›): *[ImportTx](api_platformvm_exporttx.importtx.md)*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[constructor](api_platformvm_basetx.basetx.md#constructor)*

Defined in src/apis/platformvm/importtx.ts:105

Class representing an unsigned Import transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`sourceChain` | Buffer | undefined | Optiona chainid for the source inputs to import. Default platform chainid. |
`outs` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) for the memo field |
`importIns` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› | undefined | Array of [TransferableInput](api_avm_inputs.transferableinput.md)s used in the transaction  |

**Returns:** *[ImportTx](api_platformvm_exporttx.importtx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

Defined in src/common/tx.ts:23

___

### `Protected` importIns

• **importIns**: *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›* = []

Defined in src/apis/platformvm/importtx.ts:27

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[ins](common_transactions.standardbasetx.md#protected-ins)*

Defined in src/common/tx.ts:27

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[memo](common_transactions.standardbasetx.md#protected-memo)*

Defined in src/common/tx.ts:28

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[networkid](common_transactions.standardbasetx.md#protected-networkid)*

Defined in src/common/tx.ts:22

___

### `Protected` numIns

• **numIns**: *Buffer* = Buffer.alloc(4)

Defined in src/apis/platformvm/importtx.ts:26

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numins](common_transactions.standardbasetx.md#protected-numins)*

Defined in src/common/tx.ts:26

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numouts](common_transactions.standardbasetx.md#protected-numouts)*

Defined in src/common/tx.ts:24

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[outs](common_transactions.standardbasetx.md#protected-outs)*

Defined in src/common/tx.ts:25

___

### `Protected` sourceChain

• **sourceChain**: *Buffer* = Buffer.alloc(32)

Defined in src/apis/platformvm/importtx.ts:25

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[fromBuffer](api_platformvm_basetx.basetx.md#frombuffer)*

Defined in src/apis/platformvm/importtx.ts:45

Takes a [Buffer](https://github.com/feross/buffer) containing an [ImportTx](api_platformvm_exporttx.importtx.md), parses it, populates the class, and returns the length of the [ImportTx](api_platformvm_exporttx.importtx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [ImportTx](api_platformvm_exporttx.importtx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [ImportTx](api_platformvm_exporttx.importtx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)*

Defined in src/common/tx.ts:43

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getImportInputs

▸ **getImportInputs**(): *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›*

Defined in src/apis/platformvm/importtx.ts:78

Returns an array of [TransferableInput](api_avm_inputs.transferableinput.md)s in this transaction.

**Returns:** *Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getIns](common_transactions.standardbasetx.md#getins)*

Defined in src/common/tx.ts:48

Returns the array of [TransferableInput](api_avm_inputs.transferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getMemo](common_transactions.standardbasetx.md#getmemo)*

Defined in src/common/tx.ts:58

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getNetworkID](common_transactions.standardbasetx.md#getnetworkid)*

Defined in src/common/tx.ts:38

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

Defined in src/common/tx.ts:53

Returns the array of [TransferableOutput](api_avm_outputs.transferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[getTxType](api_platformvm_basetx.basetx.md#gettxtype)*

Defined in src/apis/platformvm/importtx.ts:32

Returns the id of the [ImportTx](api_platformvm_exporttx.importtx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[sign](api_platformvm_basetx.basetx.md#sign)*

Defined in src/apis/platformvm/importtx.ts:90

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md) | An [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[toBuffer](common_transactions.standardbasetx.md#tobuffer)*

Defined in src/apis/platformvm/importtx.ts:63

Returns a [Buffer](https://github.com/feross/buffer) representation of the [ImportTx](api_platformvm_exporttx.importtx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

Defined in src/common/tx.ts:95

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
