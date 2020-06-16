[slopes - v1.7.5](../README.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [UnsignedTx](_apis_avm_tx_.unsignedtx.md)

# Class: UnsignedTx

Class representing an unsigned transaction.

## Hierarchy

* **UnsignedTx**

## Index

### Constructors

* [constructor](_apis_avm_tx_.unsignedtx.md#constructor)

### Properties

* [transaction](_apis_avm_tx_.unsignedtx.md#protected-transaction)

### Methods

* [fromBuffer](_apis_avm_tx_.unsignedtx.md#frombuffer)
* [getTransaction](_apis_avm_tx_.unsignedtx.md#gettransaction)
* [sign](_apis_avm_tx_.unsignedtx.md#sign)
* [toBuffer](_apis_avm_tx_.unsignedtx.md#tobuffer)

## Constructors

###  constructor

\+ **new UnsignedTx**(`transaction`: [BaseTx](_apis_avm_tx_.basetx.md)): *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

*Defined in [apis/avm/tx.ts:480](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L480)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`transaction` | [BaseTx](_apis_avm_tx_.basetx.md) |  undefined |

**Returns:** *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)*

## Properties

### `Protected` transaction

• **transaction**: *[BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:448](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L448)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/tx.ts:454](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L454)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getTransaction

▸ **getTransaction**(): *[BaseTx](_apis_avm_tx_.basetx.md)*

*Defined in [apis/avm/tx.ts:450](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L450)*

**Returns:** *[BaseTx](_apis_avm_tx_.basetx.md)*

___

###  sign

▸ **sign**(`kc`: [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md)): *[Tx](_apis_avm_tx_.tx.md)*

*Defined in [apis/avm/tx.ts:475](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L475)*

Signs this [UnsignedTx](_apis_avm_tx_.unsignedtx.md) and returns signed [Tx](_apis_avm_tx_.tx.md)

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`kc` | [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md) | An [AVMKeyChain](_apis_avm_keychain_.avmkeychain.md) used in signing  |

**Returns:** *[Tx](_apis_avm_tx_.tx.md)*

A signed [Tx](_apis_avm_tx_.tx.md)

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:461](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/tx.ts#L461)*

**Returns:** *Buffer*
