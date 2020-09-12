[avalanche](../README.md) › [API-PlatformVM-ValidationTx](../modules/api_platformvm_validationtx.md) › [ValidatorTx](api_platformvm_validationtx.validatortx.md)

# Class: ValidatorTx

Abstract class representing an transactions with validation information.

## Hierarchy

  ↳ [BaseTx](api_platformvm_basetx.basetx.md)

  ↳ **ValidatorTx**

  ↳ [WeightedValidatorTx](api_platformvm_validationtx.weightedvalidatortx.md)

## Index

### Constructors

* [constructor](api_platformvm_validationtx.validatortx.md#constructor)

### Properties

* [blockchainid](api_platformvm_validationtx.validatortx.md#protected-blockchainid)
* [endTime](api_platformvm_validationtx.validatortx.md#protected-endtime)
* [ins](api_platformvm_validationtx.validatortx.md#protected-ins)
* [memo](api_platformvm_validationtx.validatortx.md#protected-memo)
* [networkid](api_platformvm_validationtx.validatortx.md#protected-networkid)
* [nodeID](api_platformvm_validationtx.validatortx.md#protected-nodeid)
* [numins](api_platformvm_validationtx.validatortx.md#protected-numins)
* [numouts](api_platformvm_validationtx.validatortx.md#protected-numouts)
* [outs](api_platformvm_validationtx.validatortx.md#protected-outs)
* [startTime](api_platformvm_validationtx.validatortx.md#protected-starttime)

### Methods

* [clone](api_platformvm_validationtx.validatortx.md#clone)
* [create](api_platformvm_validationtx.validatortx.md#create)
* [fromBuffer](api_platformvm_validationtx.validatortx.md#frombuffer)
* [getBlockchainID](api_platformvm_validationtx.validatortx.md#getblockchainid)
* [getEndTime](api_platformvm_validationtx.validatortx.md#getendtime)
* [getIns](api_platformvm_validationtx.validatortx.md#getins)
* [getMemo](api_platformvm_validationtx.validatortx.md#getmemo)
* [getNetworkID](api_platformvm_validationtx.validatortx.md#getnetworkid)
* [getNodeID](api_platformvm_validationtx.validatortx.md#getnodeid)
* [getNodeIDString](api_platformvm_validationtx.validatortx.md#getnodeidstring)
* [getOuts](api_platformvm_validationtx.validatortx.md#getouts)
* [getStartTime](api_platformvm_validationtx.validatortx.md#getstarttime)
* [getTotalOuts](api_platformvm_validationtx.validatortx.md#gettotalouts)
* [getTxType](api_platformvm_validationtx.validatortx.md#gettxtype)
* [select](api_platformvm_validationtx.validatortx.md#select)
* [sign](api_platformvm_validationtx.validatortx.md#sign)
* [toBuffer](api_platformvm_validationtx.validatortx.md#tobuffer)
* [toString](api_platformvm_validationtx.validatortx.md#tostring)

## Constructors

###  constructor

\+ **new ValidatorTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›, `memo?`: Buffer, `nodeID?`: Buffer, `startTime?`: BN, `endTime?`: BN): *[ValidatorTx](api_platformvm_validationtx.validatortx.md)*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[constructor](api_platformvm_basetx.basetx.md#constructor)*

*Defined in [src/apis/platformvm/validationtx.ts:80](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L80)*

**Parameters:**

Name | Type |
------ | ------ |
`networkid` | number |
`blockchainid` | Buffer |
`outs` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› |
`ins` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› |
`memo?` | Buffer |
`nodeID?` | Buffer |
`startTime?` | BN |
`endTime?` | BN |

**Returns:** *[ValidatorTx](api_platformvm_validationtx.validatortx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

*Defined in [src/common/tx.ts:24](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L24)*

___

### `Protected` endTime

• **endTime**: *Buffer* = Buffer.alloc(8)

*Defined in [src/apis/platformvm/validationtx.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L28)*

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[ins](common_transactions.standardbasetx.md#protected-ins)*

*Defined in [src/common/tx.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L28)*

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[memo](common_transactions.standardbasetx.md#protected-memo)*

*Defined in [src/common/tx.ts:29](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L29)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[networkid](common_transactions.standardbasetx.md#protected-networkid)*

*Defined in [src/common/tx.ts:23](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L23)*

___

### `Protected` nodeID

• **nodeID**: *Buffer* = Buffer.alloc(20)

*Defined in [src/apis/platformvm/validationtx.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L26)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numins](common_transactions.standardbasetx.md#protected-numins)*

*Defined in [src/common/tx.ts:27](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L27)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numouts](common_transactions.standardbasetx.md#protected-numouts)*

*Defined in [src/common/tx.ts:25](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L25)*

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[outs](common_transactions.standardbasetx.md#protected-outs)*

*Defined in [src/common/tx.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L26)*

___

### `Protected` startTime

• **startTime**: *Buffer* = Buffer.alloc(8)

*Defined in [src/apis/platformvm/validationtx.ts:27](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L27)*

## Methods

###  clone

▸ **clone**(): *this*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[clone](api_platformvm_basetx.basetx.md#clone)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[clone](common_transactions.standardbasetx.md#abstract-clone)*

*Defined in [src/apis/platformvm/basetx.ts:102](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L102)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[create](api_platformvm_basetx.basetx.md#create)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[create](common_transactions.standardbasetx.md#abstract-create)*

*Defined in [src/apis/platformvm/basetx.ts:108](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L108)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](api_platformvm_basetx.basetx.md).[fromBuffer](api_platformvm_basetx.basetx.md#frombuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:57](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L57)*

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

*Defined in [src/common/tx.ts:44](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L44)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getEndTime

▸ **getEndTime**(): *BN‹›*

*Defined in [src/apis/platformvm/validationtx.ts:53](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L53)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN‹›*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getIns](common_transactions.standardbasetx.md#getins)*

*Defined in [src/common/tx.ts:49](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L49)*

Returns the array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getMemo](common_transactions.standardbasetx.md#getmemo)*

*Defined in [src/common/tx.ts:64](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L64)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getNetworkID](common_transactions.standardbasetx.md#getnetworkid)*

*Defined in [src/common/tx.ts:39](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L39)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getNodeID

▸ **getNodeID**(): *Buffer*

*Defined in [src/apis/platformvm/validationtx.ts:33](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L33)*

Returns a [Buffer](https://github.com/feross/buffer) for the stake amount.

**Returns:** *Buffer*

___

###  getNodeIDString

▸ **getNodeIDString**(): *string*

*Defined in [src/apis/platformvm/validationtx.ts:40](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L40)*

Returns a string for the nodeID amount.

**Returns:** *string*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

*Defined in [src/common/tx.ts:54](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L54)*

Returns the array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getStartTime

▸ **getStartTime**(): *BN‹›*

*Defined in [src/apis/platformvm/validationtx.ts:46](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L46)*

Returns a [BN](https://github.com/indutny/bn.js/) for the stake amount.

**Returns:** *BN‹›*

___

###  getTotalOuts

▸ **getTotalOuts**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[getTotalOuts](api_platformvm_basetx.basetx.md#gettotalouts)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[getTotalOuts](common_transactions.standardbasetx.md#abstract-gettotalouts)*

*Defined in [src/apis/platformvm/basetx.ts:73](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L73)*

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[getTxType](api_platformvm_basetx.basetx.md#gettxtype)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[getTxType](common_transactions.standardbasetx.md#abstract-gettxtype)*

*Defined in [src/apis/platformvm/basetx.ts:29](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L29)*

Returns the id of the [BaseTx](api_avm_basetx.basetx.md)

**Returns:** *number*

___

###  select

▸ **select**(`id`: number, ...`args`: any[]): *this*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[select](api_platformvm_basetx.basetx.md#select)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[select](common_transactions.standardbasetx.md#abstract-select)*

*Defined in [src/apis/platformvm/basetx.ts:112](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L112)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *this*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [KeyChain](api_platformvm_keychain.keychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Inherited from [BaseTx](api_platformvm_basetx.basetx.md).[sign](api_platformvm_basetx.basetx.md#sign)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[sign](common_transactions.standardbasetx.md#abstract-sign)*

*Defined in [src/apis/platformvm/basetx.ts:85](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/basetx.ts#L85)*

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [KeyChain](api_platformvm_keychain.keychain.md) | An [KeyChain](api_avm_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[toBuffer](common_transactions.standardbasetx.md#tobuffer)*

*Defined in [src/apis/platformvm/validationtx.ts:71](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/platformvm/validationtx.ts#L71)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [ValidatorTx](api_platformvm_validationtx.validatortx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

*Defined in [src/common/tx.ts:101](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L101)*

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
