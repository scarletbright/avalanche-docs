[avalanche](../README.md) › [Common-Transactions](../modules/common_transactions.md) › [StandardTx](common_transactions.standardtx.md)

# Class: StandardTx ‹**KPClass, KCClass, SUBTx**›

Class representing a signed transaction.

## Type parameters

▪ **KPClass**: *[StandardKeyPair](common_keychain.standardkeypair.md)*

▪ **KCClass**: *[StandardKeyChain](common_keychain.standardkeychain.md)‹KPClass›*

▪ **SUBTx**: *[StandardUnsignedTx](common_transactions.standardunsignedtx.md)‹KPClass, KCClass, [StandardBaseTx](common_transactions.standardbasetx.md)‹KPClass, KCClass››*

## Hierarchy

* **StandardTx**

  ↳ [Tx](api_avm_transactions.tx.md)

  ↳ [Tx](api_platformvm_transactions.tx.md)

## Index

### Constructors

* [constructor](common_transactions.standardtx.md#constructor)

### Properties

* [credentials](common_transactions.standardtx.md#protected-credentials)
* [unsignedTx](common_transactions.standardtx.md#protected-unsignedtx)

### Methods

* [fromBuffer](common_transactions.standardtx.md#abstract-frombuffer)
* [fromString](common_transactions.standardtx.md#fromstring)
* [getUnsignedTx](common_transactions.standardtx.md#getunsignedtx)
* [toBuffer](common_transactions.standardtx.md#tobuffer)
* [toString](common_transactions.standardtx.md#tostring)

## Constructors

###  constructor

\+ **new StandardTx**(`unsignedTx`: SUBTx, `credentials`: Array‹[Credential](common_signature.credential.md)›): *[StandardTx](common_transactions.standardtx.md)*

*Defined in [src/common/tx.ts:322](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L322)*

Class representing a signed transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`unsignedTx` | SUBTx | undefined | Optional [StandardUnsignedTx](common_transactions.standardunsignedtx.md) |
`credentials` | Array‹[Credential](common_signature.credential.md)› | undefined | - |

**Returns:** *[StandardTx](common_transactions.standardtx.md)*

## Properties

### `Protected` credentials

• **credentials**: *Array‹[Credential](common_signature.credential.md)›* = []

*Defined in [src/common/tx.ts:266](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L266)*

___

### `Protected` unsignedTx

• **unsignedTx**: *SUBTx* = undefined

*Defined in [src/common/tx.ts:265](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L265)*

## Methods

### `Abstract` fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset?`: number): *number*

*Defined in [src/common/tx.ts:275](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L275)*

**Parameters:**

Name | Type |
------ | ------ |
`bytes` | Buffer |
`offset?` | number |

**Returns:** *number*

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [src/common/tx.ts:310](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L310)*

Takes a base-58 string containing an [StandardTx](common_transactions.standardtx.md), parses it, populates the class, and returns the length of the Tx in bytes.

**`remarks`** 
unlike most fromStrings, it expects the string to be serialized in cb58 format

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`serialized` | string | A base-58 string containing a raw [StandardTx](common_transactions.standardtx.md)  |

**Returns:** *number*

The length of the raw [StandardTx](common_transactions.standardtx.md)

___

###  getUnsignedTx

▸ **getUnsignedTx**(): *SUBTx*

*Defined in [src/common/tx.ts:271](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L271)*

Returns the [StandardUnsignedTx](common_transactions.standardunsignedtx.md)

**Returns:** *SUBTx*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [src/common/tx.ts:280](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L280)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [StandardTx](common_transactions.standardtx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/common/tx.ts:320](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/tx.ts#L320)*

Returns a cb58 representation of the [StandardTx](common_transactions.standardtx.md).

**`remarks`** 
unlike most toStrings, this returns in cb58 serialization format

**Returns:** *string*
