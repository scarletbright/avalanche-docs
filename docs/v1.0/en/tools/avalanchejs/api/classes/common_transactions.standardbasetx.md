[avalanche](../README.md) › [Common-Transactions](../modules/common_transactions.md) › [StandardBaseTx](common_transactions.standardbasetx.md)

# Class: StandardBaseTx ‹**KPClass, KCClass**›

Class representing a base for all transactions.

## Type parameters

▪ **KPClass**: *[StandardKeyPair](common_keychain.standardkeypair.md)*

▪ **KCClass**: *[StandardKeyChain](common_keychain.standardkeychain.md)‹KPClass›*

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

* [clone](common_transactions.standardbasetx.md#abstract-clone)
* [create](common_transactions.standardbasetx.md#abstract-create)
* [getBlockchainID](common_transactions.standardbasetx.md#getblockchainid)
* [getIns](common_transactions.standardbasetx.md#getins)
* [getMemo](common_transactions.standardbasetx.md#getmemo)
* [getNetworkID](common_transactions.standardbasetx.md#getnetworkid)
* [getOuts](common_transactions.standardbasetx.md#getouts)
* [getTotalOuts](common_transactions.standardbasetx.md#abstract-gettotalouts)
* [select](common_transactions.standardbasetx.md#abstract-select)
* [sign](common_transactions.standardbasetx.md#abstract-sign)
* [toBuffer](common_transactions.standardbasetx.md#tobuffer)
* [toString](common_transactions.standardbasetx.md#tostring)

## Constructors

###  constructor

\+ **new StandardBaseTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›, `ins`: Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›, `memo`: Buffer): *[StandardBaseTx](common_transactions.standardbasetx.md)*

*Defined in [src/common/tx.ts:119](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L119)*

Class representing a StandardBaseTx which is the foundation for all transactions.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | DefaultNetworkID | Optional networkid, [DefaultNetworkID](../modules/utils_constants.md#const-defaultnetworkid) |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)› | undefined | Optional array of the [TransferableOutput](api_avm_outputs.transferableoutput.md)s |
`ins` | Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)› | undefined | Optional array of the [TransferableInput](api_avm_inputs.transferableinput.md)s |
`memo` | Buffer | undefined | Optional [Buffer](https://github.com/feross/buffer) for the memo field  |

**Returns:** *[StandardBaseTx](common_transactions.standardbasetx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Defined in [src/common/tx.ts:24](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L24)*

___

### `Abstract` getTxType

• **getTxType**: *function*

*Defined in [src/common/tx.ts:34](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L34)*

Returns the id of the [StandardBaseTx](common_transactions.standardbasetx.md)

#### Type declaration:

▸ (): *number*

___

### `Protected` ins

• **ins**: *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Defined in [src/common/tx.ts:28](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L28)*

___

### `Protected` memo

• **memo**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/tx.ts:29](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L29)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/tx.ts:23](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L23)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/tx.ts:27](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L27)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/tx.ts:25](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L25)*

___

### `Protected` outs

• **outs**: *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Defined in [src/common/tx.ts:26](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L26)*

## Methods

### `Abstract` clone

▸ **clone**(): *this*

*Defined in [src/common/tx.ts:115](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L115)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Defined in [src/common/tx.ts:117](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L117)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Defined in [src/common/tx.ts:44](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L44)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

*Defined in [src/common/tx.ts:49](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L49)*

Returns the array of [StandardTransferableInput](common_inputs.standardtransferableinput.md)s

**Returns:** *Array‹[StandardTransferableInput](common_inputs.standardtransferableinput.md)›*

___

###  getMemo

▸ **getMemo**(): *Buffer*

*Defined in [src/common/tx.ts:64](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L64)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the memo

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Defined in [src/common/tx.ts:39](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L39)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Defined in [src/common/tx.ts:54](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L54)*

Returns the array of [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

### `Abstract` getTotalOuts

▸ **getTotalOuts**(): *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

*Defined in [src/common/tx.ts:59](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L59)*

Returns the array of combined total [StandardTransferableOutput](common_output.standardtransferableoutput.md)s

**Returns:** *Array‹[StandardTransferableOutput](common_output.standardtransferableoutput.md)›*

___

### `Abstract` select

▸ **select**(`id`: number, ...`args`: any[]): *this*

*Defined in [src/common/tx.ts:119](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L119)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *this*

___

### `Abstract` sign

▸ **sign**(`msg`: Buffer, `kc`: [StandardKeyChain](common_keychain.standardkeychain.md)‹KPClass›): *Array‹[Credential](common_signature.credential.md)›*

*Defined in [src/common/tx.ts:113](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L113)*

Takes the bytes of an [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns an array of [Credential](common_signature.credential.md)s

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`msg` | Buffer | A Buffer for the [UnsignedTx](api_avm_transactions.unsignedtx.md) |
`kc` | [StandardKeyChain](common_keychain.standardkeychain.md)‹KPClass› | An [KeyChain](api_avm_keychain.keychain.md) used in signing  |

**Returns:** *Array‹[Credential](common_signature.credential.md)›*

An array of [Credential](common_signature.credential.md)s

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/tx.ts:69](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L69)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/common/tx.ts:101](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/tx.ts#L101)*

Returns a base-58 representation of the [StandardBaseTx](common_transactions.standardbasetx.md).

**Returns:** *string*
