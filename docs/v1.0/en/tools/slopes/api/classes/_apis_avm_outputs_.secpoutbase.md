[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)

# Class: SecpOutBase

An [Output](_apis_avm_outputs_.output.md) class which specifies a secp256k1 .

## Hierarchy

* [Output](_apis_avm_outputs_.output.md)

  ↳ **SecpOutBase**

  ↳ [SecpOutput](_apis_avm_outputs_.secpoutput.md)

## Index

### Constructors

* [constructor](_apis_avm_outputs_.secpoutbase.md#constructor)

### Properties

* [addresses](_apis_avm_outputs_.secpoutbase.md#protected-addresses)
* [amount](_apis_avm_outputs_.secpoutbase.md#protected-amount)
* [amountValue](_apis_avm_outputs_.secpoutbase.md#protected-amountvalue)
* [locktime](_apis_avm_outputs_.secpoutbase.md#protected-locktime)
* [numaddrs](_apis_avm_outputs_.secpoutbase.md#protected-numaddrs)
* [outputid](_apis_avm_outputs_.secpoutbase.md#protected-outputid)
* [outputidnum](_apis_avm_outputs_.secpoutbase.md#protected-outputidnum)
* [threshold](_apis_avm_outputs_.secpoutbase.md#protected-threshold)

### Methods

* [fromBuffer](_apis_avm_outputs_.secpoutbase.md#frombuffer)
* [getAddress](_apis_avm_outputs_.secpoutbase.md#getaddress)
* [getAddressIdx](_apis_avm_outputs_.secpoutbase.md#getaddressidx)
* [getAddresses](_apis_avm_outputs_.secpoutbase.md#getaddresses)
* [getAmount](_apis_avm_outputs_.secpoutbase.md#getamount)
* [getLocktime](_apis_avm_outputs_.secpoutbase.md#getlocktime)
* [getOutputID](_apis_avm_outputs_.secpoutbase.md#getoutputid)
* [getSpenders](_apis_avm_outputs_.secpoutbase.md#getspenders)
* [getThreshold](_apis_avm_outputs_.secpoutbase.md#getthreshold)
* [meetsThreshold](_apis_avm_outputs_.secpoutbase.md#meetsthreshold)
* [toBuffer](_apis_avm_outputs_.secpoutbase.md#tobuffer)
* [toString](_apis_avm_outputs_.secpoutbase.md#tostring)
* [comparator](_apis_avm_outputs_.secpoutbase.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpOutBase**(`amount?`: BN, `addresses?`: Array‹Buffer›, `locktime?`: BN, `threshold?`: number): *[SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

*Overrides [Output](_apis_avm_outputs_.output.md).[constructor](_apis_avm_outputs_.output.md#constructor)*

*Defined in [apis/avm/outputs.ts:245](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L245)*

An [Output](_apis_avm_outputs_.output.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`amount?` | BN | A [BN](https://github.com/indutny/bn.js/) representing the amount in the output |
`addresses?` | Array‹Buffer› | An array of [Buffer](https://github.com/feross/buffer)s representing addresses |
`locktime?` | BN | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold?` | number | A number representing the the threshold number of signers required to sign the transaction  |

**Returns:** *[SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](_apis_avm_types_.address.md)›* =  []

*Defined in [apis/avm/outputs.ts:73](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L73)*

___

### `Protected` amount

• **amount**: *Buffer* =  Buffer.alloc(8)

*Defined in [apis/avm/outputs.ts:74](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L74)*

___

### `Protected` amountValue

• **amountValue**: *BN* =  new BN(0)

*Defined in [apis/avm/outputs.ts:75](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L75)*

___

### `Protected` locktime

• **locktime**: *Buffer* =  Buffer.alloc(8)

*Defined in [apis/avm/outputs.ts:70](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L70)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:72](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L72)*

___

### `Protected` outputid

• **outputid**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Output](_apis_avm_outputs_.output.md).[outputid](_apis_avm_outputs_.output.md#protected-outputid)*

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L33)*

___

### `Protected` outputidnum

• **outputidnum**: *number*

*Inherited from [Output](_apis_avm_outputs_.output.md).[outputidnum](_apis_avm_outputs_.output.md#protected-outputidnum)*

*Defined in [apis/avm/outputs.ts:34](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L34)*

___

### `Protected` threshold

• **threshold**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:71](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L71)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Overrides [Output](_apis_avm_outputs_.output.md).[fromBuffer](_apis_avm_outputs_.output.md#frombuffer)*

*Defined in [apis/avm/outputs.ts:143](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L143)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [SecpOutBase](_apis_avm_outputs_.secpoutbase.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`utxobuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Defined in [apis/avm/outputs.ts:133](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L133)*

Returns the address from the index provided.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`idx` | number | The index of the address.  |

**Returns:** *Buffer*

Returns the string representing the address.

___

###  getAddressIdx

▸ **getAddressIdx**(`address`: Buffer): *number*

*Defined in [apis/avm/outputs.ts:116](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L116)*

Returns the index of the address.

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`address` | Buffer | A [Buffer](https://github.com/feross/buffer) of the address to look up to return its index.  |

**Returns:** *number*

The index of the address.

___

###  getAddresses

▸ **getAddresses**(): *Array‹Buffer›*

*Defined in [apis/avm/outputs.ts:101](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L101)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getAmount

▸ **getAmount**(): *BN*

*Defined in [apis/avm/outputs.ts:80](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L80)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [apis/avm/outputs.ts:94](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L94)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:36](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L36)*

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [apis/avm/outputs.ts:202](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L202)*

Given an array of addresses and an optional timestamp, select an array of address [Buffer](https://github.com/feross/buffer)s of qualified spenders for the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN |  undefined |

**Returns:** *Array‹Buffer›*

___

###  getThreshold

▸ **getThreshold**(): *number*

*Defined in [apis/avm/outputs.ts:87](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L87)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [apis/avm/outputs.ts:231](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L231)*

Given an array of address [Buffer](https://github.com/feross/buffer)s and an optional timestamp, returns true if the addresses meet the threshold required to spend the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN |  undefined |

**Returns:** *boolean*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [Output](_apis_avm_outputs_.output.md).[toBuffer](_apis_avm_outputs_.output.md#tobuffer)*

*Defined in [apis/avm/outputs.ts:171](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L171)*

Returns the buffer representing the [SecpOutBase](_apis_avm_outputs_.secpoutbase.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Overrides [Output](_apis_avm_outputs_.output.md).[toString](_apis_avm_outputs_.output.md#tostring)*

*Defined in [apis/avm/outputs.ts:195](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L195)*

Returns a base-58 string representing the [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:54](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L54)*

**Returns:** *function*

▸ (`a`: [Output](_apis_avm_outputs_.output.md), `b`: [Output](_apis_avm_outputs_.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](_apis_avm_outputs_.output.md) |
`b` | [Output](_apis_avm_outputs_.output.md) |
