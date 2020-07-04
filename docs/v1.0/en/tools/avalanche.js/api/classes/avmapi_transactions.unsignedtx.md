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

*Defined in [src/apis/avm/tx.ts:446](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L446)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`transaction` | [BaseTx](avmapi_transactions.basetx.md) | undefined |

**Returns:** *[UnsignedTx](avmapi_transactions.unsignedtx.md)*

## Properties

### `Protected` transaction

• **transaction**: *[BaseTx](avmapi_transactions.basetx.md)*

*Defined in [src/apis/avm/tx.ts:416](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L416)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/tx.ts:420](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L420)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getTransaction

▸ **getTransaction**(): *[BaseTx](avmapi_transactions.basetx.md)*

*Defined in [src/apis/avm/tx.ts:418](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L418)*

**Returns:** *[BaseTx](avmapi_transactions.basetx.md)*

___

###  sign

▸ **sign**(`kc`: [AVMKeyChain](avmapi_keychain.avmkeychain.md)): *[Tx](avmapi_transactions.tx.md)*

*Defined in [src/apis/avm/tx.ts:441](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L441)*

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

*Defined in [src/apis/avm/tx.ts:427](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/tx.ts#L427)*

**Returns:** *Buffer*
