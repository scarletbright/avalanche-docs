[avalanche](../README.md) › [AVMAPI-Transactions](../modules/avmapi_transactions.md) › [UnsignedTx](avmapi_transactions.unsignedtx.md)

# Class: UnsignedTx

Class representing an unsigned transaction.

## Hierarchy

* **UnsignedTx**

## Index

### Constructors

* [constructor](avmapi_transactions.unsignedtx.md#constructor)

### Properties

* [transaction](avmapi_transactions.unsignedtx.md#protected-transaction)

### Methods

* [fromBuffer](avmapi_transactions.unsignedtx.md#frombuffer)
* [getTransaction](avmapi_transactions.unsignedtx.md#gettransaction)
* [sign](avmapi_transactions.unsignedtx.md#sign)
* [toBuffer](avmapi_transactions.unsignedtx.md#tobuffer)

## Constructors

###  constructor

\+ **new UnsignedTx**(`transaction`: [BaseTx](avmapi_transactions.basetx.md)): *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

*Defined in [apis/avm/tx.ts:481](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L481)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`transaction` | [BaseTx](avmapi_transactions.basetx.md) | undefined |

**Returns:** *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

## Properties

### `Protected` transaction

• **transaction**: *[BaseTx](avmapi_transactions.basetx.md)*

*Defined in [apis/avm/tx.ts:449](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L449)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/tx.ts:455](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L455)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getTransaction

▸ **getTransaction**(): *[BaseTx](avmapi_transactions.basetx.md)*

*Defined in [apis/avm/tx.ts:451](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L451)*

**Returns:** *[BaseTx](avmapi_transactions.basetx.md)*

___

###  sign

▸ **sign**(`kc`: [AVMKeyChain](avmapi_keychain.avmkeychain.md)): *[Tx](avmapi_transactions.tx.md)*

*Defined in [apis/avm/tx.ts:476](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L476)*

Signs this [UnsignedTx](avmapi_transactions.unsignedtx.md) and returns signed [Tx](avmapi_transactions.tx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`kc` | [AVMKeyChain](avmapi_keychain.avmkeychain.md) | An [AVMKeyChain](avmapi_keychain.avmkeychain.md) used in signing  |

**Returns:** *[Tx](avmapi_transactions.tx.md)*

A signed [Tx](avmapi_transactions.tx.md)

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:462](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/tx.ts#L462)*

**Returns:** *Buffer*
