[avalanche](../README.md) › [API-PlatformVM-BaseTx](../modules/api_platformvm_basetx.md) › [BaseTx](api_platformvm_basetx.basetx.md)

# Class: BaseTx

Class representing a base for all transactions.

## Hierarchy

* [StandardBaseTx](common_transactions.standardbasetx.md)‹[KeyPair](api_platformvm_keychain.keypair.md), [KeyChain](api_platformvm_keychain.keychain.md)›

  ↳ **BaseTx**

  ↳ [ImportTx](api_platformvm_importtx.importtx.md)

  ↳ [ExportTx](api_platformvm_exporttx.exporttx.md)

  ↳ [ValidatorTx](api_platformvm_validationtx.validatortx.md)

  ↳ [CreateSubnetTx](api_platformvm_createsubnettx.createsubnettx.md)

## Index

### Constructors

* [constructor](api_platformvm_basetx.basetx.md#constructor)

### Properties

* [blockchainid](api_platformvm_basetx.basetx.md#protected-blockchainid)
* [ins](api_platformvm_basetx.basetx.md#protected-ins)
* [memo](api_platformvm_basetx.basetx.md#protected-memo)
* [networkid](api_platformvm_basetx.basetx.md#protected-networkid)
* [numins](api_platformvm_basetx.basetx.md#protected-numins)
* [numouts](api_platformvm_basetx.basetx.md#protected-numouts)
* [outs](api_platformvm_basetx.basetx.md#protected-outs)

### Methods

* [clone](api_platformvm_basetx.basetx.md#clone)
* [create](api_platformvm_basetx.basetx.md#create)
* [fromBuffer](api_platformvm_basetx.basetx.md#frombuffer)
* [getBlockchainID](api_platformvm_basetx.basetx.md#getblockchainid)
* [getIns](api_platformvm_basetx.basetx.md#getins)
* [getMemo](api_platformvm_basetx.basetx.md#getmemo)
* [getNetworkID](api_platformvm_basetx.basetx.md#getnetworkid)
* [getOuts](api_platformvm_basetx.basetx.md#getouts)
* [getTotalOuts](api_platformvm_basetx.basetx.md#gettotalouts)
* [getTxType](api_platformvm_basetx.basetx.md#gettxtype)
* [select](api_platformvm_basetx.basetx.md#select)
* [sign](api_platformvm_basetx.basetx.md#sign)
* [toBuffer](api_platformvm_basetx.basetx.md#tobuffer)
* [toString](api_platformvm_basetx.basetx.md#tostring)

## Constructors

###  constructor

\+ **new BaseTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)›, `memo`: Buffer): *[BaseTx](api_platformvm_basetx.basetx.md)*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[constructor](common_transactions.standardbasetx.md#constructor)*

*Defined in [src/apis/platformvm/basetx.ts:115](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L115)*

Class representing a BaseTx which is the foundation for all transactions.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Optional networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](api_platformvm_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) for the memo field  |

**Returns:** *[BaseTx](api_platformvm_basetx.basetx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[blockchainid](common_transactions.standardbasetx.md#protected-blockchainid)*

*Defined in [src/common/tx.ts:24](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L24)*

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[ins](common_transactions.standardbasetx.md#protected-ins)*

*Defined in [src/common/tx.ts:28](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L28)*

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[memo](common_transactions.standardbasetx.md#protected-memo)*

*Defined in [src/common/tx.ts:29](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L29)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[networkid](common_transactions.standardbasetx.md#protected-networkid)*

*Defined in [src/common/tx.ts:23](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L23)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numins](common_transactions.standardbasetx.md#protected-numins)*

*Defined in [src/common/tx.ts:27](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L27)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[numouts](common_transactions.standardbasetx.md#protected-numouts)*

*Defined in [src/common/tx.ts:25](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L25)*

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[outs](common_transactions.standardbasetx.md#protected-outs)*

*Defined in [src/common/tx.ts:26](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L26)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[clone](common_transactions.standardbasetx.md#abstract-clone)*

*Defined in [src/apis/platformvm/basetx.ts:102](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L102)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[create](common_transactions.standardbasetx.md#abstract-create)*

*Defined in [src/apis/platformvm/basetx.ts:108](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L108)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/platformvm/basetx.ts:42](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L42)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [BaseTx](api_platformvm_basetx.basetx.md), parses it, populates the class, and returns the length of the BaseTx in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [BaseTx](api_platformvm_basetx.basetx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [BaseTx](api_platformvm_basetx.basetx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)*

*Defined in [src/common/tx.ts:44](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L44)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getIns](common_transactions.standardbasetx.md#getins)*

*Defined in [src/common/tx.ts:49](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L49)*

Returns the array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getMemo](common_transactions.standardbasetx.md#getmemo)*

*Defined in [src/common/tx.ts:64](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L64)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getNetworkID](common_transactions.standardbasetx.md#getnetworkid)*

*Defined in [src/common/tx.ts:39](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L39)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[getOuts](common_transactions.standardbasetx.md#getouts)*

*Defined in [src/common/tx.ts:54](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L54)*

Returns the array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

###  getTotalOuts

▸ **getTotalOuts**(): *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[getTotalOuts](common_transactions.standardbasetx.md#abstract-gettotalouts)*

*Defined in [src/apis/platformvm/basetx.ts:73](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L73)*

**Returns:** *Array‹[TransferableOutput](api_platformvm_outputs.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[getTxType](common_transactions.standardbasetx.md#abstract-gettxtype)*

*Defined in [src/apis/platformvm/basetx.ts:29](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L29)*

Returns the id of the [BaseTx](api_platformvm_basetx.basetx.md)

**Returns:** *number*

___

###  select

▸ **select**(`id`: number, ...`args`: any[]): *this*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[select](common_transactions.standardbasetx.md#abstract-select)*

*Defined in [src/apis/platformvm/basetx.ts:112](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L112)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *this*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [KeyChain](api_platformvm_keychain.keychain.md)): *Array‹[Credential](common_signature.credential.md)›*

*Overrides [StandardBaseTx](common_transactions.standardbasetx.md).[sign](common_transactions.standardbasetx.md#abstract-sign)*

*Defined in [src/apis/platformvm/basetx.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/platformvm/basetx.ts#L85)*

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

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toBuffer](common_transactions.standardbasetx.md#tobuffer)*

*Defined in [src/common/tx.ts:69](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L69)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [StandardBaseTx](common_transactions.standardbasetx.md).[toString](common_transactions.standardbasetx.md#tostring)*

*Defined in [src/common/tx.ts:101](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L101)*

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
