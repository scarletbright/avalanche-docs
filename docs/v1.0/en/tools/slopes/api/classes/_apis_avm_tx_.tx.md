[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/tx"](../modules/_apis_avm_tx_.md) › [Tx](_apis_avm_tx_.tx.md)

# Class: Tx

Class representing a signed transaction.

## Hierarchy

* **Tx**

## Index

### Constructors

* [constructor](_apis_avm_tx_.tx.md#constructor)

### Properties

* [signatures](_apis_avm_tx_.tx.md#protected-signatures)
* [tx](_apis_avm_tx_.tx.md#protected-tx)

### Methods

* [fromBuffer](_apis_avm_tx_.tx.md#frombuffer)
* [fromString](_apis_avm_tx_.tx.md#fromstring)
* [toBuffer](_apis_avm_tx_.tx.md#tobuffer)
* [toString](_apis_avm_tx_.tx.md#tostring)

## Constructors

###  constructor

\+ **new Tx**(`tx?`: [TxUnsigned](_apis_avm_tx_.txunsigned.md), `signatures?`: Array‹Array‹[Signature](_apis_avm_types_.signature.md)››): *[Tx](_apis_avm_tx_.tx.md)*

*Defined in [apis/avm/tx.ts:399](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L399)*

Class representing a signed transaction.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`tx?` | [TxUnsigned](_apis_avm_tx_.txunsigned.md) | Optional [Tx](_apis_avm_tx_.tx.md) |
`signatures?` | Array‹Array‹[Signature](_apis_avm_types_.signature.md)›› | Optional array of [Signature](_apis_avm_types_.signature.md)s  |

**Returns:** *[Tx](_apis_avm_tx_.tx.md)*

## Properties

### `Protected` signatures

• **signatures**: *Array‹Array‹[Signature](_apis_avm_types_.signature.md)››* =  []

*Defined in [apis/avm/tx.ts:306](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L306)*

___

### `Protected` tx

• **tx**: *[TxUnsigned](_apis_avm_tx_.txunsigned.md)* =  new TxUnsigned()

*Defined in [apis/avm/tx.ts:305](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L305)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer): *number*

*Defined in [apis/avm/tx.ts:315](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L315)*

Takes a [Buffer](https://github.com/feross/buffer) containing an [Tx](_apis_avm_tx_.tx.md), parses it, populates the class, and returns the length of the Tx in bytes.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`bytes` | Buffer | A [Buffer](https://github.com/feross/buffer) containing a raw [Tx](_apis_avm_tx_.tx.md)  |

**Returns:** *number*

The length of the raw [Tx](_apis_avm_tx_.tx.md)

___

###  fromString

▸ **fromString**(`serialized`: string): *number*

*Defined in [apis/avm/tx.ts:351](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L351)*

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

*Defined in [apis/avm/tx.ts:358](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L358)*

Returns a [Buffer](https://github.com/feross/buffer) representation of the [Tx](_apis_avm_tx_.tx.md).

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/tx.ts:397](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/tx.ts#L397)*

Returns a base-58 AVA-serialized representation of the [Tx](_apis_avm_tx_.tx.md).

**`remarks`** 
unlike most toStrings, this returns in AVA serialization format

**Returns:** *string*
