[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [TxCreateAsset](_apis_avm_tx_.txcreateasset.md)

# Class: TxCreateAsset

## Hierarchy

* [TxUnsigned](_apis_avm_tx_.txunsigned.md)

  ↳ **TxCreateAsset**

## Index

### Constructors

* [constructor](_apis_avm_tx_.txcreateasset.md#constructor)

### Properties

* [blockchainid](_apis_avm_tx_.txcreateasset.md#protected-blockchainid)
* [denomination](_apis_avm_tx_.txcreateasset.md#protected-denomination)
* [initialstate](_apis_avm_tx_.txcreateasset.md#protected-initialstate)
* [ins](_apis_avm_tx_.txcreateasset.md#protected-ins)
* [name](_apis_avm_tx_.txcreateasset.md#protected-name)
* [namebuff](_apis_avm_tx_.txcreateasset.md#protected-namebuff)
* [networkid](_apis_avm_tx_.txcreateasset.md#protected-networkid)
* [numins](_apis_avm_tx_.txcreateasset.md#protected-numins)
* [numouts](_apis_avm_tx_.txcreateasset.md#protected-numouts)
* [outs](_apis_avm_tx_.txcreateasset.md#protected-outs)
* [symbol](_apis_avm_tx_.txcreateasset.md#protected-symbol)
* [symbolbuff](_apis_avm_tx_.txcreateasset.md#protected-symbolbuff)
* [txtype](_apis_avm_tx_.txcreateasset.md#protected-txtype)

### Methods

* [fromBuffer](_apis_avm_tx_.txcreateasset.md#frombuffer)
* [getBlockchainID](_apis_avm_tx_.txcreateasset.md#getblockchainid)
* [getDenomination](_apis_avm_tx_.txcreateasset.md#getdenomination)
* [getDenominationBuffer](_apis_avm_tx_.txcreateasset.md#getdenominationbuffer)
* [getInitialStates](_apis_avm_tx_.txcreateasset.md#getinitialstates)
* [getIns](_apis_avm_tx_.txcreateasset.md#getins)
* [getName](_apis_avm_tx_.txcreateasset.md#getname)
* [getNameBuffer](_apis_avm_tx_.txcreateasset.md#getnamebuffer)
* [getNetworkID](_apis_avm_tx_.txcreateasset.md#getnetworkid)
* [getOuts](_apis_avm_tx_.txcreateasset.md#getouts)
* [getSymbol](_apis_avm_tx_.txcreateasset.md#getsymbol)
* [getSymbolBuffer](_apis_avm_tx_.txcreateasset.md#getsymbolbuffer)
* [getTxType](_apis_avm_tx_.txcreateasset.md#gettxtype)
* [toBuffer](_apis_avm_tx_.txcreateasset.md#tobuffer)
* [toString](_apis_avm_tx_.txcreateasset.md#tostring)

## Constructors

###  constructor

\+ **new TxCreateAsset**(`name`: string, `symbol`: string, `denomination`: number, `initialstate`: [InitialStates](_apis_avm_types_.initialstates.md), `ins`: Array‹[Input](_apis_avm_inputs_.input.md)›, `outs`: Array‹[Output](_apis_avm_outputs_.output.md)›, `networkid`: number, `blockchainid`: Buffer, `txtype`: number): *[TxCreateAsset](_apis_avm_tx_.txcreateasset.md)*

*Overrides [TxUnsigned](_apis_avm_tx_.txunsigned.md).[constructor](_apis_avm_tx_.txunsigned.md#constructor)*

*Defined in [apis/avm/tx.ts:273](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L273)*

Class representing an unsigned Create Asset transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`name` | string |  undefined | String for the descriptive name of the asset |
`symbol` | string |  undefined | String for the ticker symbol of the asset |
`denomination` | number |  undefined | Optional number for the denomination which is 10^D. D must be >= 0 and <= 32. Ex: $1 AVA = 10^9 $nAVA |
`initialstate` | [InitialStates](_apis_avm_types_.initialstates.md) |  undefined | Optional [InitialStates](_apis_avm_types_.initialstates.md) that represent the intial state of a created asset |
`ins` | Array‹[Input](_apis_avm_inputs_.input.md)› |  undefined | Optional array of the [Input](_apis_avm_inputs_.input.md)s |
`outs` | Array‹[Output](_apis_avm_outputs_.output.md)› |  undefined | Optional array of the [Output](_apis_avm_outputs_.output.md)s |
`networkid` | number | 2 | Optional networkid, default 2 |
`blockchainid` | Buffer |  Buffer.alloc(32, 16) | Optional blockchainid, default Buffer.alloc(32, 16) |
`txtype` | number |  AVMConstants.CREATEASSETTX | Optional txtype, default 1  |

**Returns:** *[TxCreateAsset](_apis_avm_tx_.txcreateasset.md)*

## Properties

### `Protected` blockchainid

• **blockchainid**: *Buffer* =  Buffer.alloc(32)

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[blockchainid](_apis_avm_tx_.txunsigned.md#protected-blockchainid)*

*Defined in [apis/avm/tx.ts:42](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L42)*

___

### `Protected` denomination

• **denomination**: *Buffer* =  Buffer.alloc(1)

*Defined in [apis/avm/tx.ts:189](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L189)*

___

### `Protected` initialstate

• **initialstate**: *[InitialStates](_apis_avm_types_.initialstates.md)* =  new InitialStates()

*Defined in [apis/avm/tx.ts:190](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L190)*

___

### `Protected` ins

• **ins**: *Array‹[Input](_apis_avm_inputs_.input.md)›*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[ins](_apis_avm_tx_.txunsigned.md#protected-ins)*

*Defined in [apis/avm/tx.ts:46](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L46)*

___

### `Protected` name

• **name**: *string* = ""

*Defined in [apis/avm/tx.ts:185](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L185)*

___

### `Protected` namebuff

• **namebuff**: *Buffer* =  Buffer.alloc(2)

*Defined in [apis/avm/tx.ts:186](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L186)*

___

### `Protected` networkid

• **networkid**: *Buffer* =  Buffer.alloc(4)

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[networkid](_apis_avm_tx_.txunsigned.md#protected-networkid)*

*Defined in [apis/avm/tx.ts:41](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L41)*

___

### `Protected` numins

• **numins**: *Buffer* =  Buffer.alloc(4)

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[numins](_apis_avm_tx_.txunsigned.md#protected-numins)*

*Defined in [apis/avm/tx.ts:45](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L45)*

___

### `Protected` numouts

• **numouts**: *Buffer* =  Buffer.alloc(4)

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[numouts](_apis_avm_tx_.txunsigned.md#protected-numouts)*

*Defined in [apis/avm/tx.ts:43](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L43)*

___

### `Protected` outs

• **outs**: *Array‹[Output](_apis_avm_outputs_.output.md)›*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[outs](_apis_avm_tx_.txunsigned.md#protected-outs)*

*Defined in [apis/avm/tx.ts:44](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L44)*

___

### `Protected` symbol

• **symbol**: *string* = ""

*Defined in [apis/avm/tx.ts:187](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L187)*

___

### `Protected` symbolbuff

• **symbolbuff**: *Buffer* =  Buffer.alloc(2)

*Defined in [apis/avm/tx.ts:188](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L188)*

___

### `Protected` txtype

• **txtype**: *Buffer* =  Buffer.alloc(4)

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[txtype](_apis_avm_tx_.txunsigned.md#protected-txtype)*

*Defined in [apis/avm/tx.ts:40](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L40)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [TxUnsigned](_apis_avm_tx_.txunsigned.md).[fromBuffer](_apis_avm_tx_.txunsigned.md#frombuffer)*

*Defined in [apis/avm/tx.ts:251](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L251)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [TxCreateAsset](_apis_avm_tx_.txcreateasset.md), parses it, populates the class, and returns the length of the TxUnsigned in bytes.

**`remarks`** assume not-checksummed

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [TxCreateAsset](_apis_avm_tx_.txcreateasset.md)  |
`offset` | number | 0 | - |

**Returns:** *number*

The length of the raw [TxCreateAsset](_apis_avm_tx_.txcreateasset.md)

___

###  getBlockchainID

▸ **getBlockchainID**(): *Buffer*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:65](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L65)*

Returns the Buffer representation of the BlockchainID

**Returns:** *Buffer*

___

###  getDenomination

▸ **getDenomination**(): *number*

*Defined in [apis/avm/tx.ts:230](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L230)*

Returns the numeric representation of the denomination

**Returns:** *number*

___

###  getDenominationBuffer

▸ **getDenominationBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:238](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L238)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the denomination

**Returns:** *Buffer*

___

###  getInitialStates

▸ **getInitialStates**(): *[InitialStates](_apis_avm_types_.initialstates.md)*

*Defined in [apis/avm/tx.ts:195](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L195)*

Returns the array of array of [Output](_apis_avm_outputs_.output.md)s for the initial state

**Returns:** *[InitialStates](_apis_avm_types_.initialstates.md)*

___

###  getIns

▸ **getIns**(): *Array‹[Input](_apis_avm_inputs_.input.md)›*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:72](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L72)*

Returns the array of [Input](_apis_avm_inputs_.input.md)s

**Returns:** *Array‹[Input](_apis_avm_inputs_.input.md)›*

___

###  getName

▸ **getName**(): *string*

*Defined in [apis/avm/tx.ts:202](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L202)*

Returns the string representation of the name

**Returns:** *string*

___

###  getNameBuffer

▸ **getNameBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:209](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L209)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the name

**Returns:** *Buffer*

___

###  getNetworkID

▸ **getNetworkID**(): *number*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:58](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L58)*

Returns the number representation of the NetworkID

**Returns:** *number*

___

###  getOuts

▸ **getOuts**(): *Array‹[Output](_apis_avm_outputs_.output.md)›*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:79](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L79)*

Returns the array of [Output](_apis_avm_outputs_.output.md)s

**Returns:** *Array‹[Output](_apis_avm_outputs_.output.md)›*

___

###  getSymbol

▸ **getSymbol**(): *string*

*Defined in [apis/avm/tx.ts:216](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L216)*

Returns the string representation of the symbol

**Returns:** *string*

___

###  getSymbolBuffer

▸ **getSymbolBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:223](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L223)*

Returns the [Buffer](https://github.com/feross/buffer) representation of the symbol

**Returns:** *Buffer*

___

###  getTxType

▸ **getTxType**(): *number*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md)*

*Defined in [apis/avm/tx.ts:51](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L51)*

Returns the number representation of the txtype

**Returns:** *number*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [TxUnsigned](_apis_avm_tx_.txunsigned.md).[toBuffer](_apis_avm_tx_.txunsigned.md#tobuffer)*

*Defined in [apis/avm/tx.ts:270](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L270)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [TxUnsigned](_apis_avm_tx_.txunsigned.md).[toString](_apis_avm_tx_.txunsigned.md#tostring)*

*Defined in [apis/avm/tx.ts:158](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L158)*

Returns a base-58 representation of the [TxUnsigned](_apis_avm_tx_.txunsigned.md).

**Returns:** *string*
