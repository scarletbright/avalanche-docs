[avalanche](../README.md) › [AVMAPI-Transactions](../modules/avmapi_transactions.md) › [OperationTx](avmapi_transactions.operationtx.md)

# Class: OperationTx

Class representing an unsigned Operation transaction.

## Hierarchy

* [BaseTx](avmapi_transactions.basetx.md)

  ↳ **OperationTx**

## Index

### Constructors

* [constructor](avmapi_transactions.operationtx.md#constructor)

### Properties

* [blockchainid](avmapi_transactions.operationtx.md#protected-blockchainid)
* [ins](avmapi_transactions.operationtx.md#protected-ins)
* [networkid](avmapi_transactions.operationtx.md#protected-networkid)
* [numOps](avmapi_transactions.operationtx.md#protected-numops)
* [numins](avmapi_transactions.operationtx.md#protected-numins)
* [numouts](avmapi_transactions.operationtx.md#protected-numouts)
* [ops](avmapi_transactions.operationtx.md#protected-ops)
* [outs](avmapi_transactions.operationtx.md#protected-outs)

### Methods

* [fromBuffer](avmapi_transactions.operationtx.md#frombuffer)
* [getBlockchainID](avmapi_transactions.operationtx.md#getblockchainid)
* [getIns](avmapi_transactions.operationtx.md#getins)
* [getNetworkID](avmapi_transactions.operationtx.md#getnetworkid)
* [getOperations](avmapi_transactions.operationtx.md#getoperations)
* [getOuts](avmapi_transactions.operationtx.md#getouts)
* [getTxType](avmapi_transactions.operationtx.md#gettxtype)
* [sign](avmapi_transactions.operationtx.md#sign)
* [toBuffer](avmapi_transactions.operationtx.md#tobuffer)
* [toString](avmapi_transactions.operationtx.md#tostring)

## Constructors

###  constructor

\+ **new OperationTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›, `ops`: Array‹[TransferableOperation](avmapi_operations.transferableoperation.md)›): *[OperationTx](avmapi_transactions.operationtx.md)*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[constructor](avmapi_transactions.basetx.md#constructor)*

*Defined in [apis/avm/tx.ts:417](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L417)*

Class representing an unsigned Operation transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](avmapi_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](avmapi_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](avmapi_inputs.transferableinput.md)s |
`ops` | Array‹[TransferableOperation](avmapi_operations.transferableoperation.md)› | undefined | Array of [Operation](avmapi_operations.operation.md)s used in the transaction  |

**Returns:** *[OperationTx](avmapi_transactions.operationtx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[blockchainid](avmapi_transactions.basetx.md#protected-blockchainid)*

*Defined in [apis/avm/tx.ts:47](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L47)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[ins](avmapi_transactions.basetx.md#protected-ins)*

*Defined in [apis/avm/tx.ts:51](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L51)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[networkid](avmapi_transactions.basetx.md#protected-networkid)*

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L46)*

___

### `Protected` numOps

• **numOps**: *Buffer* = Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:343](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L343)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[numins](avmapi_transactions.basetx.md#protected-numins)*

*Defined in [apis/avm/tx.ts:50](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L50)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[numouts](avmapi_transactions.basetx.md#protected-numouts)*

*Defined in [apis/avm/tx.ts:48](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L48)*

___

### `Protected` ops

• **ops**: *Array‹[TransferableOperation](avmapi_operations.transferableoperation.md)›* = []

*Defined in [apis/avm/tx.ts:344](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L344)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[outs](avmapi_transactions.basetx.md#protected-outs)*

*Defined in [apis/avm/tx.ts:49](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L49)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[fromBuffer](avmapi_transactions.basetx.md#frombuffer)*

*Defined in [apis/avm/tx.ts:362](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L362)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [OperationTx](avmapi_transactions.operationtx.md), parses it, populates the class, and returns the length of the [OperationTx](avmapi_transactions.operationtx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [OperationTx](avmapi_transactions.operationtx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [OperationTx](avmapi_transactions.operationtx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getBlockchainID](avmapi_transactions.basetx.md#getblockchainid)*

*Defined in [apis/avm/tx.ts:70](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L70)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getIns](avmapi_transactions.basetx.md#getins)*

*Defined in [apis/avm/tx.ts:77](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L77)*

Returns the array of [TransferableInput](avmapi_inputs.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getNetworkID](avmapi_transactions.basetx.md#getnetworkid)*

*Defined in [apis/avm/tx.ts:63](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L63)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOperations

▸ **getOperations**(): *Array‹[TransferableOperation](avmapi_operations.transferableoperation.md)›*

*Defined in [apis/avm/tx.ts:390](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L390)*

Returns an array of [Operation](avmapi_operations.operation.md)s in this transaction.

**Returns:** *Array‹[TransferableOperation](avmapi_operations.transferableoperation.md)›*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getOuts](avmapi_transactions.basetx.md#getouts)*

*Defined in [apis/avm/tx.ts:84](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L84)*

Returns the array of [TransferableOutput](avmapi_outputs.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[getTxType](avmapi_transactions.basetx.md#gettxtype)*

*Defined in [apis/avm/tx.ts:349](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L349)*

Returns the id of the [OperationTx](avmapi_transactions.operationtx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](avmapi_keychain.avmkeychain.md)): *Array‹[Credential](avmapi_credentials.credential.md)›*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[sign](avmapi_transactions.basetx.md#sign)*

*Defined in [apis/avm/tx.ts:402](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L402)*

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

*Overrides [BaseTx](avmapi_transactions.basetx.md).[toBuffer](avmapi_transactions.basetx.md#tobuffer)*

*Defined in [apis/avm/tx.ts:378](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L378)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [OperationTx](avmapi_transactions.operationtx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[toString](avmapi_transactions.basetx.md#tostring)*

*Defined in [apis/avm/tx.ts:153](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/tx.ts#L153)*

Returns a base-58 representation of the [BaseTx](avmapi_transactions.basetx.md).

**Returns:** *string*
