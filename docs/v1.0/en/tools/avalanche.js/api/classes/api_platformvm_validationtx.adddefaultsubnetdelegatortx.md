[avalanche](../README.md) › [API-PlatformVM-ValidationTx](../modules/api_platformvm_validationtx.md) › [AddPrimaryDelegatorTx](api_platformvm_validationtx.addprimarydelegatortx.md)

# Class: AddPrimaryDelegatorTx

Class representing an unsigned AddPrimaryDelegatorTx transaction.

## Hierarchy

  ↳ [ValidatorTx](api_platformvm_validationtx.validatortx.md)

  ↳ **AddPrimaryDelegatorTx**

## Index

### Constructors

* [constructor](api_platformvm_validationtx.addprimarydelegatortx.md#constructor)

### Properties

* [blockchainid](api_platformvm_validationtx.addprimarydelegatortx.md#protected-blockchainid)
* [endTime](api_platformvm_validationtx.addprimarydelegatortx.md#protected-endtime)
* [ins](api_platformvm_validationtx.addprimarydelegatortx.md#protected-ins)
* [memo](api_platformvm_validationtx.addprimarydelegatortx.md#protected-memo)
* [networkid](api_platformvm_validationtx.addprimarydelegatortx.md#protected-networkid)
* [nodeID](api_platformvm_validationtx.addprimarydelegatortx.md#protected-nodeid)
* [numins](api_platformvm_validationtx.addprimarydelegatortx.md#protected-numins)
* [numouts](api_platformvm_validationtx.addprimarydelegatortx.md#protected-numouts)
* [outs](api_platformvm_validationtx.addprimarydelegatortx.md#protected-outs)
* [rewardAddress](api_platformvm_validationtx.addprimarydelegatortx.md#protected-rewardaddress)
* [stakeAmount](api_platformvm_validationtx.addprimarydelegatortx.md#protected-stakeamount)
* [stakeOuts](api_platformvm_validationtx.addprimarydelegatortx.md#protected-stakeouts)
* [startTime](api_platformvm_validationtx.addprimarydelegatortx.md#protected-starttime)

### Methods

* [fromBuffer](api_platformvm_validationtx.addprimarydelegatortx.md#frombuffer)
* [getBlockchainID](api_platformvm_validationtx.addprimarydelegatortx.md#getblockchainid)
* [getEndTime](api_platformvm_validationtx.addprimarydelegatortx.md#getendtime)
* [getIns](api_platformvm_validationtx.addprimarydelegatortx.md#getins)
* [getMemo](api_platformvm_validationtx.addprimarydelegatortx.md#getmemo)
* [getNetworkID](api_platformvm_validationtx.addprimarydelegatortx.md#getnetworkid)
* [getNodeID](api_platformvm_validationtx.addprimarydelegatortx.md#getnodeid)
* [getNodeIDString](api_platformvm_validationtx.addprimarydelegatortx.md#getnodeidstring)
* [getOuts](api_platformvm_validationtx.addprimarydelegatortx.md#getouts)
* [getStartTime](api_platformvm_validationtx.addprimarydelegatortx.md#getstarttime)
* [getTxType](api_platformvm_validationtx.addprimarydelegatortx.md#gettxtype)
* [sign](api_platformvm_validationtx.addprimarydelegatortx.md#sign)
* [toBuffer](api_platformvm_validationtx.addprimarydelegatortx.md#tobuffer)
* [toString](api_platformvm_validationtx.addprimarydelegatortx.md#tostring)

## Constructors

###  constructor

\+ **new AddPrimaryDelegatorTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›, `memo`: Buffer, `nodeID`: Buffer, `startTime`: BN, `endTime`: BN, `stakeAmount`: BN, `stakeOuts`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `rewardAddress`: Buffer): *[AddPrimaryDelegatorTx](api_platformvm_validationtx.addprimarydelegatortx.md)*

*Overrides [ValidatorTx](api_platformvm_validationtx.validatortx.md).[constructor](api_platformvm_validationtx.validatortx.md#constructor)*

Defined in src/apis/platformvm/validationtx.ts:136

Class representing an unsigned Import transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Optional networkid, [DefaultNetworkID](../modules/common_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) for the memo field |
`nodeID` | Buffer | undefined | - |
`startTime` | BN | undefined | - |
`endTime` | BN | undefined | - |
`stakeAmount` | BN | undefined | - |
`stakeOuts` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | - |
`rewardAddress` | Buffer | undefined | - |

**Returns:** *[AddPrimaryDelegatorTx](api_platformvm_validationtx.addprimarydelegatortx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

Defined in src/common/tx.ts:24

___

### `Protected` endTime

• **endTime**: *Buffer* = Buffer.alloc(8)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[endTime](api_platformvm_validationtx.validatortx.md#protected-endtime)*

Defined in src/apis/platformvm/validationtx.ts:26

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

### `Protected` nodeID

• **nodeID**: *Buffer* = Buffer.alloc(20)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[nodeID](api_platformvm_validationtx.validatortx.md#protected-nodeid)*

Defined in src/apis/platformvm/validationtx.ts:24

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

___

### `Protected` rewardAddress

• **rewardAddress**: *Buffer* = Buffer.alloc(20)

Defined in src/apis/platformvm/validationtx.ts:93

___

### `Protected` stakeAmount

• **stakeAmount**: *Buffer* = Buffer.alloc(8)

Defined in src/apis/platformvm/validationtx.ts:91

___

### `Protected` stakeOuts

• **stakeOuts**: *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›* = []

Defined in src/apis/platformvm/validationtx.ts:92

___

### `Protected` startTime

• **startTime**: *Buffer* = Buffer.alloc(8)

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[startTime](api_platformvm_validationtx.validatortx.md#protected-starttime)*

Defined in src/apis/platformvm/validationtx.ts:25

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [ValidatorTx](api_platformvm_validationtx.validatortx.md).[fromBuffer](api_platformvm_validationtx.validatortx.md#frombuffer)*

Defined in src/apis/platformvm/validationtx.ts:102

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)*

Defined in src/common/tx.ts:44

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getEndTime

▸ **getEndTime**(): *BN‹›*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getEndTime](api_platformvm_validationtx.validatortx.md#getendtime)*

Defined in src/apis/platformvm/validationtx.ts:40

**Returns:** *BN‹›*

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

###  getNodeID

▸ **getNodeID**(): *Buffer*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getNodeID](api_platformvm_validationtx.validatortx.md#getnodeid)*

Defined in src/apis/platformvm/validationtx.ts:28

**Returns:** *Buffer*

___

###  getNodeIDString

▸ **getNodeIDString**(): *string*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getNodeIDString](api_platformvm_validationtx.validatortx.md#getnodeidstring)*

Defined in src/apis/platformvm/validationtx.ts:32

**Returns:** *string*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

Defined in src/common/tx.ts:54

Returns the array of [TransferableOutput](api_avm_outputs.transferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getStartTime

▸ **getStartTime**(): *BN‹›*

*Inherited from [ValidatorTx](api_platformvm_validationtx.validatortx.md).[getStartTime](api_platformvm_validationtx.validatortx.md#getstarttime)*

Defined in src/apis/platformvm/validationtx.ts:36

**Returns:** *BN‹›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[getTxType](api_platformvm_basetx.basetx.md#gettxtype)*

Defined in src/apis/platformvm/validationtx.ts:98

Returns the id of the [AddPrimaryDelegatorTx](api_platformvm_validationtx.addprimarydelegatortx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[sign](api_platformvm_basetx.basetx.md#sign)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[sign](common_transactions.standardbasetx.md#abstract-sign)*

Defined in src/apis/platformvm/basetx.ts:80

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [PlatformVMKeyChain](api_platformvm_keychain.platformvmkeychain.md) | An [KeyChain](common_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [ValidatorTx](api_platformvm_validationtx.validatortx.md).[toBuffer](api_platformvm_validationtx.validatortx.md#tobuffer)*

Defined in src/apis/platformvm/validationtx.ts:123

Returns a [Buffer](https://github.com/feross/buffer) representation of the [ImportTx](api_avm_importtx.importtx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

Defined in src/common/tx.ts:96

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
