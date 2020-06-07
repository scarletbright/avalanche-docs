[slopes - v1.7.3](../README.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [CreateAssetTx](_apis_avm_tx_.createassettx.md)

# Class: CreateAssetTx

## Hierarchy

* [BaseTx](_apis_avm_tx_.basetx.md)

  ↳ **CreateAssetTx**

## Index

### Constructors

* [constructor](_apis_avm_tx_.createassettx.md#constructor)

### Properties

* [blockchainid](_apis_avm_tx_.createassettx.md#protected-blockchainid)
* [denomination](_apis_avm_tx_.createassettx.md#protected-denomination)
* [initialstate](_apis_avm_tx_.createassettx.md#protected-initialstate)
* [ins](_apis_avm_tx_.createassettx.md#protected-ins)
* [name](_apis_avm_tx_.createassettx.md#protected-name)
* [networkid](_apis_avm_tx_.createassettx.md#protected-networkid)
* [numins](_apis_avm_tx_.createassettx.md#protected-numins)
* [numouts](_apis_avm_tx_.createassettx.md#protected-numouts)
* [outs](_apis_avm_tx_.createassettx.md#protected-outs)
* [symbol](_apis_avm_tx_.createassettx.md#protected-symbol)

### Methods

* [fromBuffer](_apis_avm_tx_.createassettx.md#frombuffer)
* [getBlockchainID](_apis_avm_tx_.createassettx.md#getblockchainid)
* [getDenomination](_apis_avm_tx_.createassettx.md#getdenomination)
* [getDenominationBuffer](_apis_avm_tx_.createassettx.md#getdenominationbuffer)
* [getInitialStates](_apis_avm_tx_.createassettx.md#getinitialstates)
* [getIns](_apis_avm_tx_.createassettx.md#getins)
* [getName](_apis_avm_tx_.createassettx.md#getname)
* [getNetworkID](_apis_avm_tx_.createassettx.md#getnetworkid)
* [getOuts](_apis_avm_tx_.createassettx.md#getouts)
* [getSymbol](_apis_avm_tx_.createassettx.md#getsymbol)
* [getTxType](_apis_avm_tx_.createassettx.md#gettxtype)
* [sign](_apis_avm_tx_.createassettx.md#sign)
* [toBuffer](_apis_avm_tx_.createassettx.md#tobuffer)
* [toString](_apis_avm_tx_.createassettx.md#tostring)

## Constructors

###  constructor

\+ **new CreateAssetTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›, `ins`: Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›, `name`: string, `symbol`: string, `denomination`: number, `initialstate`: [InitialStates](_apis_avm_types_.initialstates.md)): *[CreateAssetTx](_apis_avm_tx_.createassettx.md)*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[constructor](_apis_avm_tx_.basetx.md#constructor)*

*Defined in [apis/avm/tx.ts:305](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L305)*

Class representing an unsigned Create Asset transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer |  Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)› |  undefined | Optional array of the [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)› |  undefined | Optional array of the [TransferableInput](_apis_avm_inputs_.transferableinput.md)s |
`name` | string |  undefined | String for the descriptive name of the asset |
`symbol` | string |  undefined | String for the ticker symbol of the asset |
`denomination` | number |  undefined | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA |
`initialstate` | [InitialStates](_apis_avm_types_.initialstates.md) |  undefined | Optional [InitialStates](_apis_avm_types_.initialstates.md) that represent the intial state of a created asset  |

**Returns:** *[CreateAssetTx](_apis_avm_tx_.createassettx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[blockchainid](_apis_avm_tx_.basetx.md#protected-blockchainid)*

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L46)*

___

### `Protected` denomination

• **denomination**: *Buffer* =  Buffer.alloc(1)

*Defined in [apis/avm/tx.ts:204](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L204)*

___

### `Protected` initialstate

• **initialstate**: *[InitialStates](_apis_avm_types_.initialstates.md)* =  new InitialStates()

*Defined in [apis/avm/tx.ts:205](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L205)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[ins](_apis_avm_tx_.basetx.md#protected-ins)*

*Defined in [apis/avm/tx.ts:50](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L50)*

___

### `Protected` name

• **name**: *string* = ""

*Defined in [apis/avm/tx.ts:202](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L202)*

___

### `Protected` networkid

• **networkid**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[networkid](_apis_avm_tx_.basetx.md#protected-networkid)*

*Defined in [apis/avm/tx.ts:45](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L45)*

___

### `Protected` numins

• **numins**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[numins](_apis_avm_tx_.basetx.md#protected-numins)*

*Defined in [apis/avm/tx.ts:49](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L49)*

___

### `Protected` numouts

• **numouts**: *Buffer* =  Buffer.alloc(4)

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[numouts](_apis_avm_tx_.basetx.md#protected-numouts)*

*Defined in [apis/avm/tx.ts:47](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L47)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[outs](_apis_avm_tx_.basetx.md#protected-outs)*

*Defined in [apis/avm/tx.ts:48](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L48)*

___

### `Protected` symbol

• **symbol**: *string* = ""

*Defined in [apis/avm/tx.ts:203](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L203)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[fromBuffer](_apis_avm_tx_.basetx.md#frombuffer)*

*Defined in [apis/avm/tx.ts:262](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L262)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [CreateAssetTx](_apis_avm_tx_.createassettx.md), parses it, populates the class, and returns the length of the [CreateAssetTx](_apis_avm_tx_.createassettx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [CreateAssetTx](_apis_avm_tx_.createassettx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [CreateAssetTx](_apis_avm_tx_.createassettx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:69](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L69)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getDenomination

▸ **getDenomination**(): *number*

*Defined in [apis/avm/tx.ts:241](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L241)*

Returns the numeric representation of the denomination

**Returns:** *number*

___

###  getDenominationBuffer

▸ **getDenominationBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:249](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L249)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the denomination

**Returns:** *Buffer*

___

###  getInitialStates

▸ **getInitialStates**(): *[InitialStates](_apis_avm_types_.initialstates.md)*

*Defined in [apis/avm/tx.ts:217](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L217)*

Returns the array of array of [Output](_apis_avm_outputs_.output.md)s for the initial state

**Returns:** *[InitialStates](_apis_avm_types_.initialstates.md)*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:76](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L76)*

Returns the array of [TransferableInput](_apis_avm_inputs_.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](_apis_avm_inputs_.transferableinput.md)›*

___

###  getName

▸ **getName**(): *string*

*Defined in [apis/avm/tx.ts:224](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L224)*

Returns the string representation of the name

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:62](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L62)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:83](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L83)*

Returns the array of [TransferableOutput](_apis_avm_outputs_.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)›*

___

###  getSymbol

▸ **getSymbol**(): *string*

*Defined in [apis/avm/tx.ts:232](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L232)*

Returns the string representation of the symbol

**Returns:** *string*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](_apis_avm_tx_.basetx.md).[getTxType](_apis_avm_tx_.basetx.md#gettxtype)*

*Defined in [apis/avm/tx.ts:210](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L210)*

Returns the id of the [CreateAssetTx](_apis_avm_tx_.createassettx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)): *Array‹[Credential](_apis_avm_credentials_.credential.md)›*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[sign](_apis_avm_tx_.basetx.md#sign)*

*Defined in [apis/avm/tx.ts:164](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L164)*

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

*Defined in [apis/avm/tx.ts:288](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L288)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [CreateAssetTx](_apis_avm_tx_.createassettx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [BaseTx](_apis_avm_tx_.basetx.md).[toString](_apis_avm_tx_.basetx.md#tostring)*

*Defined in [apis/avm/tx.ts:152](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/tx.ts#L152)*

Returns a base-58 representation of the [BaseTx](_apis_avm_tx_.basetx.md).

**Returns:** *string*
