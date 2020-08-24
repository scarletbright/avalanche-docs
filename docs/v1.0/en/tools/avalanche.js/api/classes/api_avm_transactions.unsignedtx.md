[avalanche](../README.md) › [API-AVM-Transactions](../modules/api_avm_transactions.md) › [UnsignedTx](api_avm_transactions.unsignedtx.md)

# Class: UnsignedTx

## Hierarchy

* [StandardUnsignedTx](common_transactions.standardunsignedtx.md)‹[AVMKeyPair](api_avm_keychain.avmkeypair.md), [AVMKeyChain](api_avm_keychain.avmkeychain.md), [BaseTx](api_avm_basetx.basetx.md)›

  ↳ **UnsignedTx**

## Index

### Constructors

* [constructor](api_avm_transactions.unsignedtx.md#constructor)

### Properties

* [codecid](api_avm_transactions.unsignedtx.md#protected-codecid)
* [transaction](api_avm_transactions.unsignedtx.md#protected-transaction)

### Methods

* [fromBuffer](api_avm_transactions.unsignedtx.md#frombuffer)
* [getBurn](api_avm_transactions.unsignedtx.md#getburn)
* [getCodecID](api_avm_transactions.unsignedtx.md#getcodecid)
* [getCodecIDBuffer](api_avm_transactions.unsignedtx.md#getcodecidbuffer)
* [getInputTotal](api_avm_transactions.unsignedtx.md#getinputtotal)
* [getOutputTotal](api_avm_transactions.unsignedtx.md#getoutputtotal)
* [getTransaction](api_avm_transactions.unsignedtx.md#gettransaction)
* [sign](api_avm_transactions.unsignedtx.md#sign)
* [toBuffer](api_avm_transactions.unsignedtx.md#tobuffer)

## Constructors

###  constructor

\+ **new UnsignedTx**(`transaction`: [BaseTx](api_avm_basetx.basetx.md), `codecid`: number): *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[constructor](common_transactions.standardunsignedtx.md#constructor)*

Defined in src/common/tx.ts:238

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`transaction` | [BaseTx](api_avm_basetx.basetx.md) | undefined |
`codecid` | number | 0 |

**Returns:** *[UnsignedTx](api_avm_transactions.unsignedtx.md)*

## Properties

### `Protected` codecid

• **codecid**: *number* = 0

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[codecid](common_transactions.standardunsignedtx.md#protected-codecid)*

Defined in src/common/tx.ts:149

___

### `Protected` transaction

• **transaction**: *[BaseTx](api_avm_basetx.basetx.md)*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[transaction](common_transactions.standardunsignedtx.md#protected-transaction)*

Defined in src/common/tx.ts:150

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Overrides [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[fromBuffer](common_transactions.standardunsignedtx.md#abstract-frombuffer)*

Defined in src/apis/avm/tx.ts:26

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getBurn

▸ **getBurn**(`assetID`: Buffer): *BN*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getBurn](common_transactions.standardunsignedtx.md#getburn)*

Defined in src/common/tx.ts:208

Returns the number of burned tokens as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getCodecID

▸ **getCodecID**(): *number*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getCodecID](common_transactions.standardunsignedtx.md#getcodecid)*

Defined in src/common/tx.ts:155

Returns the CodecID as a number

**Returns:** *number*

___

###  getCodecIDBuffer

▸ **getCodecIDBuffer**(): *Buffer*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getCodecIDBuffer](common_transactions.standardunsignedtx.md#getcodecidbuffer)*

Defined in src/common/tx.ts:160

Returns the [Buffer](https://github.com/feross/buffer) representation of the CodecID

**Returns:** *Buffer*

___

###  getInputTotal

▸ **getInputTotal**(`assetID`: Buffer): *BN*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getInputTotal](common_transactions.standardunsignedtx.md#getinputtotal)*

Defined in src/common/tx.ts:169

Returns the inputTotal as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getOutputTotal

▸ **getOutputTotal**(`assetID`: Buffer): *BN*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getOutputTotal](common_transactions.standardunsignedtx.md#getoutputtotal)*

Defined in src/common/tx.ts:189

Returns the outputTotal as a BN

**Parameters:**

Name | Type |
------ | ------ |
`assetID` | Buffer |

**Returns:** *BN*

___

###  getTransaction

▸ **getTransaction**(): *[BaseTx](api_avm_basetx.basetx.md)*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[getTransaction](common_transactions.standardunsignedtx.md#gettransaction)*

Defined in src/common/tx.ts:215

Returns the Transaction

**Returns:** *[BaseTx](api_avm_basetx.basetx.md)*

___

###  sign

▸ **sign**(`kc`: [AVMKeyChain](api_avm_keychain.avmkeychain.md)): *[StandardTx](common_transactions.standardtx.md)‹[AVMKeyPair](api_avm_keychain.avmkeypair.md), [AVMKeyChain](api_avm_keychain.avmkeychain.md), [UnsignedTx](api_avm_transactions.unsignedtx.md)›*

*Overrides [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[sign](common_transactions.standardunsignedtx.md#abstract-sign)*

Defined in src/apis/avm/tx.ts:42

Signs this [UnsignedTx](api_avm_transactions.unsignedtx.md) and returns signed [StandardTx](common_transactions.standardtx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`kc` | [AVMKeyChain](api_avm_keychain.avmkeychain.md) | An [KeyChain](common_keychain.keychain.md) used in signing  |

**Returns:** *[StandardTx](common_transactions.standardtx.md)‹[AVMKeyPair](api_avm_keychain.avmkeypair.md), [AVMKeyChain](api_avm_keychain.avmkeychain.md), [UnsignedTx](api_avm_transactions.unsignedtx.md)›*

A signed [StandardTx](common_transactions.standardtx.md)

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [StandardUnsignedTx](common_transactions.standardunsignedtx.md).[toBuffer](common_transactions.standardunsignedtx.md#tobuffer)*

Defined in src/common/tx.ts:219

**Returns:** *Buffer*
