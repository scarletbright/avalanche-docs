[slopes - v1.4.3](../README.md) › [Globals](../globals.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [SecpOutput](_apis_avm_outputs_.secpoutput.md)

# Class: SecpOutput

## Hierarchy

  ↳ [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)

  ↳ **SecpOutput**

## Index

### Constructors

* [constructor](_apis_avm_outputs_.secpoutput.md#constructor)

### Properties

* [addresses](_apis_avm_outputs_.secpoutput.md#protected-addresses)
* [amount](_apis_avm_outputs_.secpoutput.md#protected-amount)
* [amountValue](_apis_avm_outputs_.secpoutput.md#protected-amountvalue)
* [assetid](_apis_avm_outputs_.secpoutput.md#protected-assetid)
* [locktime](_apis_avm_outputs_.secpoutput.md#protected-locktime)
* [numaddrs](_apis_avm_outputs_.secpoutput.md#protected-numaddrs)
* [outputid](_apis_avm_outputs_.secpoutput.md#protected-outputid)
* [outputidnum](_apis_avm_outputs_.secpoutput.md#protected-outputidnum)
* [threshold](_apis_avm_outputs_.secpoutput.md#protected-threshold)

### Methods

* [fromBuffer](_apis_avm_outputs_.secpoutput.md#frombuffer)
* [getAddress](_apis_avm_outputs_.secpoutput.md#getaddress)
* [getAddressIdx](_apis_avm_outputs_.secpoutput.md#getaddressidx)
* [getAddresses](_apis_avm_outputs_.secpoutput.md#getaddresses)
* [getAmount](_apis_avm_outputs_.secpoutput.md#getamount)
* [getAssetID](_apis_avm_outputs_.secpoutput.md#getassetid)
* [getLocktime](_apis_avm_outputs_.secpoutput.md#getlocktime)
* [getOutputID](_apis_avm_outputs_.secpoutput.md#getoutputid)
* [getSpenders](_apis_avm_outputs_.secpoutput.md#getspenders)
* [getThreshold](_apis_avm_outputs_.secpoutput.md#getthreshold)
* [meetsThreshold](_apis_avm_outputs_.secpoutput.md#meetsthreshold)
* [toBuffer](_apis_avm_outputs_.secpoutput.md#tobuffer)
* [toString](_apis_avm_outputs_.secpoutput.md#tostring)
* [comparator](_apis_avm_outputs_.secpoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpOutput**(`assetid?`: Buffer, `amount?`: BN, `addresses?`: Array‹Buffer›, `locktime?`: BN, `threshold?`: number): *[SecpOutput](_apis_avm_outputs_.secpoutput.md)*

*Overrides [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[constructor](_apis_avm_outputs_.secpoutbase.md#constructor)*

*Defined in [apis/avm/outputs.ts:299](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L299)*

**Parameters:**

Name | Type |
------ | ------ |
`assetid?` | Buffer |
`amount?` | BN |
`addresses?` | Array‹Buffer› |
`locktime?` | BN |
`threshold?` | number |

**Returns:** *[SecpOutput](_apis_avm_outputs_.secpoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](_apis_avm_types_.address.md)›* =  []

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[addresses](_apis_avm_outputs_.secpoutbase.md#protected-addresses)*

*Defined in [apis/avm/outputs.ts:73](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L73)*

___

### `Protected` amount

• **amount**: *Buffer* =  Buffer.alloc(8)

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[amount](_apis_avm_outputs_.secpoutbase.md#protected-amount)*

*Defined in [apis/avm/outputs.ts:74](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L74)*

___

### `Protected` amountValue

• **amountValue**: *BN* =  new BN(0)

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[amountValue](_apis_avm_outputs_.secpoutbase.md#protected-amountvalue)*

*Defined in [apis/avm/outputs.ts:75](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L75)*

___

### `Protected` assetid

• **assetid**: *Buffer* =  Buffer.alloc(32)

*Defined in [apis/avm/outputs.ts:280](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L280)*

___

### `Protected` locktime

• **locktime**: *Buffer* =  Buffer.alloc(8)

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[locktime](_apis_avm_outputs_.secpoutbase.md#protected-locktime)*

*Defined in [apis/avm/outputs.ts:70](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L70)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* =  Buffer.alloc(4)

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[numaddrs](_apis_avm_outputs_.secpoutbase.md#protected-numaddrs)*

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

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[threshold](_apis_avm_outputs_.secpoutbase.md#protected-threshold)*

*Defined in [apis/avm/outputs.ts:71](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L71)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`outbuff`: Buffer, `offset`: number): *number*

*Overrides [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[fromBuffer](_apis_avm_outputs_.secpoutbase.md#frombuffer)*

*Defined in [apis/avm/outputs.ts:282](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L282)*

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`outbuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

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

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

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

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

*Defined in [apis/avm/outputs.ts:101](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L101)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getAmount

▸ **getAmount**(): *BN*

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

*Defined in [apis/avm/outputs.ts:80](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L80)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getAssetID

▸ **getAssetID**(): *Buffer*

*Defined in [apis/avm/outputs.ts:297](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L297)*

Returns the assetID as a [Buffer](https://github.com/feross/buffer).

**Returns:** *Buffer*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

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

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

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

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

*Defined in [apis/avm/outputs.ts:87](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L87)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md)*

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

*Overrides [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[toBuffer](_apis_avm_outputs_.secpoutbase.md#tobuffer)*

*Defined in [apis/avm/outputs.ts:289](https://github.com/ava-labs/slopes/blob/709e172/src/apis/avm/outputs.ts#L289)*

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [SecpOutBase](_apis_avm_outputs_.secpoutbase.md).[toString](_apis_avm_outputs_.secpoutbase.md#tostring)*

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
