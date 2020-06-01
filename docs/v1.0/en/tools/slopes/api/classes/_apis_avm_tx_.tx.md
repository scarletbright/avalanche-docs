[slopes - v1.7.1](../README.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [Tx](_apis_avm_tx_.tx.md)

# Class: Tx

Class representing a signed transaction.

## Hierarchy

* **Tx**

## Index

### Constructors

* [constructor](_apis_avm_tx_.tx.md#constructor)

### Properties

* [credentials](_apis_avm_tx_.tx.md#protected-credentials)
* [unsignedTx](_apis_avm_tx_.tx.md#protected-unsignedtx)

### Methods

* [fromBuffer](_apis_avm_tx_.tx.md#frombuffer)
* [fromString](_apis_avm_tx_.tx.md#fromstring)
* [toBuffer](_apis_avm_tx_.tx.md#tobuffer)
* [toString](_apis_avm_tx_.tx.md#tostring)

## Constructors

###  constructor

\+ **new Tx**(`unsignedTx`: [UnsignedTx](_apis_avm_tx_.unsignedtx.md), `credentials`: Array‹[Credential](_apis_avm_credentials_.credential.md)›): *[Tx](_apis_avm_tx_.tx.md)*

*Defined in [apis/avm/tx.ts:563](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L563)*

Class representing a signed transaction.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`unsignedTx` | [UnsignedTx](_apis_avm_tx_.unsignedtx.md) |  undefined | Optional [UnsignedTx](_apis_avm_tx_.unsignedtx.md) |
`credentials` | Array‹[Credential](_apis_avm_credentials_.credential.md)› |  undefined | - |

**Returns:** *[Tx](_apis_avm_tx_.tx.md)*

## Properties

### `Protected` credentials

• **credentials**: *Array‹[Credential](_apis_avm_credentials_.credential.md)›* =  []

*Defined in [apis/avm/tx.ts:492](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L492)*

___

### `Protected` unsignedTx

• **unsignedTx**: *[UnsignedTx](_apis_avm_tx_.unsignedtx.md)* =  new UnsignedTx()

*Defined in [apis/avm/tx.ts:491](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L491)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/tx.ts:502](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L502)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [Tx](_apis_avm_tx_.tx.md), parses it, populates the class, and returns the length of the Tx in bytes.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`bytes` | Buffer | - | A [Buffer](https://github.com/feross/buffer) containing a raw [Tx](_apis_avm_tx_.tx.md) |
`offset` | number | 0 | A number representing the starting point of the bytes to begin parsing  |

**Returns:** *number*

The length of the raw [Tx](_apis_avm_tx_.tx.md)

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [apis/avm/tx.ts:551](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L551)*

Takes a base-58 string containing an [Tx](_apis_avm_tx_.tx.md), parses it, populates the class, and returns the length of the Tx in bytes.

**`remarks`** 
unlike most fromStrings, it expects the string to be serialized in AVA format

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`serialized` | string | A base-58 string containing a raw [Tx](_apis_avm_tx_.tx.md)  |

**Returns:** *number*

The length of the raw [Tx](_apis_avm_tx_.tx.md)

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/tx.ts:521](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L521)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [Tx](_apis_avm_tx_.tx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/tx.ts:561](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/tx.ts#L561)*

Returns a base-58 AVA-serialized representation of the [Tx](_apis_avm_tx_.tx.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
