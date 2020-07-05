[avalanche](../README.md) › [AVMAPI-Transactions](../modules/avmapi_transactions.md) › [CreateAssetTx](avmapi_transactions.createassettx.md)

# Class: CreateAssetTx

## Hierarchy

* [BaseTx](avmapi_transactions.basetx.md)

  ↳ **CreateAssetTx**

## Index

### Constructors

* [constructor](avmapi_transactions.createassettx.md#constructor)

### Properties

* [blockchainid](avmapi_transactions.createassettx.md#protected-blockchainid)
* [denomination](avmapi_transactions.createassettx.md#protected-denomination)
* [initialstate](avmapi_transactions.createassettx.md#protected-initialstate)
* [ins](avmapi_transactions.createassettx.md#protected-ins)
* [name](avmapi_transactions.createassettx.md#protected-name)
* [networkid](avmapi_transactions.createassettx.md#protected-networkid)
* [numins](avmapi_transactions.createassettx.md#protected-numins)
* [numouts](avmapi_transactions.createassettx.md#protected-numouts)
* [outs](avmapi_transactions.createassettx.md#protected-outs)
* [symbol](avmapi_transactions.createassettx.md#protected-symbol)

### Methods

* [fromBuffer](avmapi_transactions.createassettx.md#frombuffer)
* [getBlockchainID](avmapi_transactions.createassettx.md#getblockchainid)
* [getDenomination](avmapi_transactions.createassettx.md#getdenomination)
* [getDenominationBuffer](avmapi_transactions.createassettx.md#getdenominationbuffer)
* [getInitialStates](avmapi_transactions.createassettx.md#getinitialstates)
* [getIns](avmapi_transactions.createassettx.md#getins)
* [getName](avmapi_transactions.createassettx.md#getname)
* [getNetworkID](avmapi_transactions.createassettx.md#getnetworkid)
* [getOuts](avmapi_transactions.createassettx.md#getouts)
* [getSymbol](avmapi_transactions.createassettx.md#getsymbol)
* [getTxType](avmapi_transactions.createassettx.md#gettxtype)
* [sign](avmapi_transactions.createassettx.md#sign)
* [toBuffer](avmapi_transactions.createassettx.md#tobuffer)
* [toString](avmapi_transactions.createassettx.md#tostring)

## Constructors

###  constructor

\+ **new CreateAssetTx**(`networkid`: number, `blockchainid`: Buffer, `outs`: Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›, `ins`: Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›, `name`: string, `symbol`: string, `denomination`: number, `initialstate`: [InitialStates](avmapi_types.initialstates.md)): *[CreateAssetTx](avmapi_transactions.createassettx.md)*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[constructor](avmapi_transactions.basetx.md#constructor)*

*Defined in [src/apis/avm/tx.ts:272](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L272)*

Class representing an unsigned Create Asset transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`networkid` | number | 3 | Optional networkid, default 3 |
`blockchainid` | Buffer | Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`outs` | Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)› | undefined | Optional array of the [TransferableOutput](avmapi_outputs.transferableoutput.md)s |
`ins` | Array‹[TransferableInput](avmapi_inputs.transferableinput.md)› | undefined | Optional array of the [TransferableInput](avmapi_inputs.transferableinput.md)s |
`name` | string | undefined | String for the descriptive name of the asset |
`symbol` | string | undefined | String for the ticker symbol of the asset |
`denomination` | number | undefined | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA |
`initialstate` | [InitialStates](avmapi_types.initialstates.md) | undefined | Optional [InitialStates](avmapi_types.initialstates.md) that represent the intial state of a created asset  |

**Returns:** *[CreateAssetTx](avmapi_transactions.createassettx.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* = Buffer.alloc(32)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[blockchainid](avmapi_transactions.basetx.md#protected-blockchainid)*

*Defined in [src/apis/avm/tx.ts:28](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L28)*

___

### `Protected` denomination

• **denomination**: *Buffer* = Buffer.alloc(1)

*Defined in [src/apis/avm/tx.ts:184](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L184)*

___

### `Protected` initialstate

• **initialstate**: *[InitialStates](avmapi_types.initialstates.md)* = new InitialStates()

*Defined in [src/apis/avm/tx.ts:186](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L186)*

___

### `Protected` ins

• **ins**: *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[ins](avmapi_transactions.basetx.md#protected-ins)*

*Defined in [src/apis/avm/tx.ts:36](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L36)*

___

### `Protected` name

• **name**: *string* = ""

*Defined in [src/apis/avm/tx.ts:180](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L180)*

___

### `Protected` networkid

• **networkid**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[networkid](avmapi_transactions.basetx.md#protected-networkid)*

*Defined in [src/apis/avm/tx.ts:26](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L26)*

___

### `Protected` numins

• **numins**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[numins](avmapi_transactions.basetx.md#protected-numins)*

*Defined in [src/apis/avm/tx.ts:34](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L34)*

___

### `Protected` numouts

• **numouts**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[numouts](avmapi_transactions.basetx.md#protected-numouts)*

*Defined in [src/apis/avm/tx.ts:30](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L30)*

___

### `Protected` outs

• **outs**: *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[outs](avmapi_transactions.basetx.md#protected-outs)*

*Defined in [src/apis/avm/tx.ts:32](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L32)*

___

### `Protected` symbol

• **symbol**: *string* = ""

*Defined in [src/apis/avm/tx.ts:182](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L182)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[fromBuffer](avmapi_transactions.basetx.md#frombuffer)*

*Defined in [src/apis/avm/tx.ts:229](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L229)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [CreateAssetTx](avmapi_transactions.createassettx.md), parses it, populates the class, and returns the length of the [CreateAssetTx](avmapi_transactions.createassettx.md) in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [CreateAssetTx](avmapi_transactions.createassettx.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [CreateAssetTx](avmapi_transactions.createassettx.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getBlockchainID](avmapi_transactions.basetx.md#getblockchainid)*

*Defined in [src/apis/avm/tx.ts:53](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L53)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getDenomination

▸ **getDenomination**(): *number*

*Defined in [src/apis/avm/tx.ts:213](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L213)*

Returns the numeric representation of the denomination

**Returns:** *number*

___

###  getDenominationBuffer

▸ **getDenominationBuffer**(): *Buffer*

*Defined in [src/apis/avm/tx.ts:218](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L218)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the denomination

**Returns:** *Buffer*

___

###  getInitialStates

▸ **getInitialStates**(): *[InitialStates](avmapi_types.initialstates.md)*

*Defined in [src/apis/avm/tx.ts:198](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L198)*

Returns the array of array of [Output](avmapi_outputs.output.md)s for the initial state

**Returns:** *[InitialStates](avmapi_types.initialstates.md)*

___

###  getIns

▸ **getIns**(): *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getIns](avmapi_transactions.basetx.md#getins)*

*Defined in [src/apis/avm/tx.ts:58](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L58)*

Returns the array of [TransferableInput](avmapi_inputs.transferableinput.md)s

**Returns:** *Array‹[TransferableInput](avmapi_inputs.transferableinput.md)›*

___

###  getName

▸ **getName**(): *string*

*Defined in [src/apis/avm/tx.ts:203](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L203)*

Returns the string representation of the name

**Returns:** *string*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getNetworkID](avmapi_transactions.basetx.md#getnetworkid)*

*Defined in [src/apis/avm/tx.ts:48](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L48)*

Returns the NetworkID as a number

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[getOuts](avmapi_transactions.basetx.md#getouts)*

*Defined in [src/apis/avm/tx.ts:63](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L63)*

Returns the array of [TransferableOutput](avmapi_outputs.transferableoutput.md)s

**Returns:** *Array‹[TransferableOutput](avmapi_outputs.transferableoutput.md)›*

___

###  getSymbol

▸ **getSymbol**(): *string*

*Defined in [src/apis/avm/tx.ts:208](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L208)*

Returns the string representation of the symbol

**Returns:** *string*

___

###  getTxType

▸ **getTxType**(): *number*

*Overrides [BaseTx](avmapi_transactions.basetx.md).[getTxType](avmapi_transactions.basetx.md#gettxtype)*

*Defined in [src/apis/avm/tx.ts:191](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L191)*

Returns the id of the [CreateAssetTx](avmapi_transactions.createassettx.md)

**Returns:** *number*

___

###  sign

▸ **sign**(`msg`: Buffer, `kc`: [AVMKeyChain](avmapi_keychain.avmkeychain.md)): *Array‹[Credential](avmapi_credentials.credential.md)›*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[sign](avmapi_transactions.basetx.md#sign)*

*Defined in [src/apis/avm/tx.ts:142](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L142)*

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

*Defined in [src/apis/avm/tx.ts:255](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L255)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [CreateAssetTx](avmapi_transactions.createassettx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [BaseTx](avmapi_transactions.basetx.md).[toString](avmapi_transactions.basetx.md#tostring)*

*Defined in [src/apis/avm/tx.ts:130](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L130)*

Returns a base-58 representation of the [BaseTx](avmapi_transactions.basetx.md).

**Returns:** *string*
