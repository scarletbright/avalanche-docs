[slopes - v1.7.2](../README.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [OperationTx](_apis_avm_tx_.operationtx.md)

# Class: OperationTx

Class representing an unsigned Operation transaction.

## Hierarchy

* [BaseTx](_apis_avm_tx_.basetx.md)

  ↳ **OperationTx**

## Index

### Constructors

* [constructor](_apis_avm_tx_.operationtx.md#constructor)

### Properties

* [blockchainid](_apis_avm_tx_.operationtx.md#protected-blockchainid)
* [ins](_apis_avm_tx_.operationtx.md#protected-ins)
* [networkid](_apis_avm_tx_.operationtx.md#protected-networkid)
* [numOps](_apis_avm_tx_.operationtx.md#protected-numops)
* [numins](_apis_avm_tx_.operationtx.md#protected-numins)
* [numouts](_apis_avm_tx_.operationtx.md#protected-numouts)
* [ops](_apis_avm_tx_.operationtx.md#protected-ops)
* [outs](_apis_avm_tx_.operationtx.md#protected-outs)

### Methods

* [fromBuffer](_apis_avm_tx_.operationtx.md#frombuffer)
* [getBlockchainID](_apis_avm_tx_.operationtx.md#getblockchainid)
* [getIns](_apis_avm_tx_.operationtx.md#getins)
* [getNetworkID](_apis_avm_tx_.operationtx.md#getnetworkid)
* [getOperations](_apis_avm_tx_.operationtx.md#getoperations)
* [getOuts](_apis_avm_tx_.operationtx.md#getouts)
* [getTxType](_apis_avm_tx_.operationtx.md#gettxtype)
* [sign](_apis_avm_tx_.operationtx.md#sign)
* [toBuffer](_apis_avm_tx_.operationtx.md#tobuffer)
* [toString](_apis_avm_tx_.operationtx.md#tostring)

## Constructors

###  constructor

\+ **new OperationTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›, `ins`: Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›, `ops`: Array‹[TransferableOperation](_apis_avm_ops_.transferableoperation.md)›): *[OperationTx](_apis_avm_tx_.operationtx.md)*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[constructor](_apis_avm_tx_.basetx.md#constructor)*

*Defined in [apis/avm/tx.ts:416](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L416)*

Class representing an unsigned Operation transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 2 | Optional networkid, default 2 |
`blockchainid` | Buffer |  Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)› |  undefined | Optional array of the [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)› |  undefined | Optional array of the [TransferableInput](_apis_avm_inputs_.transferableinput.md)s |
`ops` | Array‹[TransferableOperation](_apis_avm_ops_.transferableoperation.md)› |  undefined | Array of [Operation](_apis_avm_ops_.operation.md)s used in the transaction  |

**Returns:** *[OperationTx](_apis_avm_tx_.operationtx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[blockchainid](_apis_avm_tx_.basetx.md#protected-blockchainid)*

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L46)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[ins](_apis_avm_tx_.basetx.md#protected-ins)*

*Defined in [apis/avm/tx.ts:50](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L50)*

___

### `Protected` networkid

• **networkid**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[networkid](_apis_avm_tx_.basetx.md#protected-networkid)*

*Defined in [apis/avm/tx.ts:45](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L45)*

___

### `Protected` numOps

• **numOps**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/tx.ts:342](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L342)*

___

### `Protected` numins

• **numins**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[numins](_apis_avm_tx_.basetx.md#protected-numins)*

*Defined in [apis/avm/tx.ts:49](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L49)*

___

### `Protected` numouts

• **numouts**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[numouts](_apis_avm_tx_.basetx.md#protected-numouts)*

*Defined in [apis/avm/tx.ts:47](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L47)*

___

### `Protected` ops

• **ops**: *Array‹[TransferableOperation](_apis_avm_ops_.transferableoperation.md)›* =  []

*Defined in [apis/avm/tx.ts:343](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L343)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[outs](_apis_avm_tx_.basetx.md#protected-outs)*

*Defined in [apis/avm/tx.ts:48](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L48)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[fromBuffer](_apis_avm_tx_.basetx.md#frombuffer)*

*Defined in [apis/avm/tx.ts:361](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L361)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [OperationTx](_apis_avm_tx_.operationtx.md), parses it, populates the class, and returns the length of the [OperationTx](_apis_avm_tx_.operationtx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [OperationTx](_apis_avm_tx_.operationtx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [OperationTx](_apis_avm_tx_.operationtx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:69](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L69)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:76](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L76)*

Returns the array of [TransferableInput](_apis_avm_inputs_.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:62](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L62)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOperations

▸ **getOperations**(): *Array‹[TransferableOperation](_apis_avm_ops_.transferableoperation.md)›*

*Defined in [apis/avm/tx.ts:389](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L389)*

Returns an array of [Operation](_apis_avm_ops_.operation.md)s in this transaction.

**Returns:** *Array‹[TransferableOperation](_apis_avm_ops_.transferableoperation.md)›*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:83](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L83)*

Returns the array of [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[getTxType](_apis_avm_tx_.basetx.md#gettxtype)*

*Defined in [apis/avm/tx.ts:348](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L348)*

Returns the id of the [OperationTx](_apis_avm_tx_.operationtx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)): *Array‹[Credential](_apis_avm_credentials_.credential.md)›*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[sign](_apis_avm_tx_.basetx.md#sign)*

*Defined in [apis/avm/tx.ts:401](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L401)*

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

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[toBuffer](_apis_avm_tx_.basetx.md#tobuffer)*

*Defined in [apis/avm/tx.ts:377](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L377)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [OperationTx](_apis_avm_tx_.operationtx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[toString](_apis_avm_tx_.basetx.md#tostring)*

*Defined in [apis/avm/tx.ts:152](https://github.com/ava-labs/slopes/blob/ba50532/src/apis/avm/tx.ts#L152)*

Returns a base-58 representation of the [BaseTx](_apis_avm_tx_.basetx.md).

**Returns:** *string*
