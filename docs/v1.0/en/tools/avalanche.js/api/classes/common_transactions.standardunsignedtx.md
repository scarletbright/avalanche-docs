[avalanche](../README.md) › [Common-Transactions](../modules/common_transactions.md) › [StandardUnsignedTx](common_transactions.standardunsignedtx.md)

# Class: StandardUnsignedTx ‹**KPClass, KCClass, SBTx**›

Class representing an unsigned transaction.

## Type parameters

▪ **KPClass**: *[KeyPair](common_keychain.keypair.md)*

▪ **KCClass**: *[KeyChain](common_keychain.keychain.md)‹KPClass›*

▪ **SBTx**: *[StandardBaseTx](common_transactions.standardbasetx.md)‹KPClass, KCClass›*

## Hierarchy

* **StandardUnsignedTx**

  ↳ [UnsignedTx](api_avm_transactions.unsignedtx.md)

  ↳ [UnsignedTx](api_platformvm_transactions.unsignedtx.md)

## Index

### Constructors

* [constructor](common_transactions.standardunsignedtx.md#constructor)

### Properties

* [codecid](common_transactions.standardunsignedtx.md#protected-codecid)
* [transaction](common_transactions.standardunsignedtx.md#protected-transaction)

### Methods

* [fromBuffer](common_transactions.standardunsignedtx.md#abstract-frombuffer)
* [getBurn](common_transactions.standardunsignedtx.md#getburn)
* [getCodecID](common_transactions.standardunsignedtx.md#getcodecid)
* [getCodecIDBuffer](common_transactions.standardunsignedtx.md#getcodecidbuffer)
* [getInputTotal](common_transactions.standardunsignedtx.md#getinputtotal)
* [getOutputTotal](common_transactions.standardunsignedtx.md#getoutputtotal)
* [getTransaction](common_transactions.standardunsignedtx.md#gettransaction)
* [sign](common_transactions.standardunsignedtx.md#abstract-sign)
* [toBuffer](common_transactions.standardunsignedtx.md#tobuffer)

## Constructors

###  constructor

\+ **new StandardUnsignedTx**(`transaction`: SBTx, `codecid`: number): *[StandardUnsignedTx](common_transactions.standardunsignedtx.md)*

Defined in src/common/tx.ts:237

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`transaction` | SBTx | undefined |
`codecid` | number | 0 |

**Returns:** *[StandardUnsignedTx](common_transactions.standardunsignedtx.md)*

## Properties

### `Protected` codecid

• **codecid**: *number* = 0

Defined in src/common/tx.ts:148

___

### `Protected` transaction

• **transaction**: *SBTx*

Defined in src/common/tx.ts:149

## Methods

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

Defined in src/common/tx.ts:216

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset?` | number |

**Returns:** *number*

___

###  getBurn

▸ **getBurn**(`assetID`: Buffer): *BN*

Defined in src/common/tx.ts:207

Returns the number of burned tokens as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getCodecID

▸ **getCodecID**(): *number*

Defined in src/common/tx.ts:154

Returns the CodecID as a number

**Returns:** *number*

___

###  getCodecIDBuffer

▸ **getCodecIDBuffer**(): *Buffer*

Defined in src/common/tx.ts:159

Returns the [Buffer](https://github.com/feross/buffer) representation of the CodecID

**Returns:** *Buffer*

___

###  getInputTotal

▸ **getInputTotal**(`assetID`: Buffer): *BN*

Defined in src/common/tx.ts:168

Returns the inputTotal as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getOutputTotal

▸ **getOutputTotal**(`assetID`: Buffer): *BN*

Defined in src/common/tx.ts:188

Returns the outputTotal as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getTransaction

▸ **getTransaction**(): *SBTx*

Defined in src/common/tx.ts:214

Returns the Transaction

**Returns:** *SBTx*

___

### `Abstract` sign

▸ **sign**(`kc`: KCClass): *[StandardTx](common_transactions.standardtx.md)‹KPClass, KCClass, [StandardUnsignedTx](common_transactions.standardunsignedtx.md)‹KPClass, KCClass, SBTx››*

Defined in src/common/tx.ts:233

Signs this [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns signed [StandardTx](common_transactions.standardtx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`kc` | KCClass | An [KeyChain](common_keychain.keychain.md) used in signing  |

**Returns:** *[StandardTx](common_transactions.standardtx.md)‹KPClass, KCClass, [StandardUnsignedTx](common_transactions.standardunsignedtx.md)‹KPClass, KCClass, SBTx››*

A signed [StandardTx](common_transactions.standardtx.md)

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

Defined in src/common/tx.ts:218

**Returns:** *Buffer*
