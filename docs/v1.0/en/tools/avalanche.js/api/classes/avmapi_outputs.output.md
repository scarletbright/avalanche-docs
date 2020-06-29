[avalanche](../README.md) › [AVMAPI-Outputs](../modules/avmapi_outputs.md) › [Output](avmapi_outputs.output.md)

# Class: Output

## Hierarchy

* **Output**

  ↳ [AmountOutput](avmapi_outputs.amountoutput.md)

  ↳ [NFTOutBase](avmapi_outputs.nftoutbase.md)

## Index

### Constructors

* [constructor](avmapi_outputs.output.md#constructor)

### Properties

* [addresses](avmapi_outputs.output.md#protected-addresses)
* [locktime](avmapi_outputs.output.md#protected-locktime)
* [numaddrs](avmapi_outputs.output.md#protected-numaddrs)
* [threshold](avmapi_outputs.output.md#protected-threshold)

### Methods

* [fromBuffer](avmapi_outputs.output.md#frombuffer)
* [getAddress](avmapi_outputs.output.md#getaddress)
* [getAddressIdx](avmapi_outputs.output.md#getaddressidx)
* [getAddresses](avmapi_outputs.output.md#getaddresses)
* [getLocktime](avmapi_outputs.output.md#getlocktime)
* [getOutputID](avmapi_outputs.output.md#abstract-getoutputid)
* [getSpenders](avmapi_outputs.output.md#getspenders)
* [getThreshold](avmapi_outputs.output.md#getthreshold)
* [makeTransferable](avmapi_outputs.output.md#maketransferable)
* [meetsThreshold](avmapi_outputs.output.md#meetsthreshold)
* [toBuffer](avmapi_outputs.output.md#tobuffer)
* [toString](avmapi_outputs.output.md#tostring)
* [comparator](avmapi_outputs.output.md#static-comparator)

## Constructors

###  constructor

\+ **new Output**(`locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[Output](avmapi_outputs.output.md)*

*Defined in [apis/avm/outputs.ts:211](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L211)*

An [Output](avmapi_outputs.output.md) class which contains locktimes, thresholds, and addresses.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses  |

**Returns:** *[Output](avmapi_outputs.output.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](avmapi_types.address.md)›* = []

*Defined in [apis/avm/outputs.ts:34](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L34)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Defined in [apis/avm/outputs.ts:31](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L31)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L33)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:32](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L32)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/outputs.ts:148](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L148)*

Returns a base-58 string representing the [Output](avmapi_outputs.output.md).

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Defined in [apis/avm/outputs.ts:90](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L90)*

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

*Defined in [apis/avm/outputs.ts:73](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L73)*

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

*Defined in [apis/avm/outputs.ts:58](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L58)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [apis/avm/outputs.ts:51](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L51)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Defined in [apis/avm/outputs.ts:39](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L39)*

Returns the outputID for the output which tells parsers what type it is

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [apis/avm/outputs.ts:119](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L119)*

Given an array of addresses and an optional timestamp, select an array of address [Buffer](https://github.com/feross/buffer)s of qualified spenders for the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN | undefined |

**Returns:** *Array‹Buffer›*

___

###  getThreshold

▸ **getThreshold**(): *number*

*Defined in [apis/avm/outputs.ts:44](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L44)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

*Defined in [apis/avm/outputs.ts:193](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L193)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [apis/avm/outputs.ts:100](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L100)*

Given an array of address [Buffer](https://github.com/feross/buffer)s and an optional timestamp, returns true if the addresses meet the threshold required to spend the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN | undefined |

**Returns:** *boolean*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Defined in [apis/avm/outputs.ts:169](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L169)*

Returns the buffer representing the [Output](avmapi_outputs.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/outputs.ts:185](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L185)*

Returns a base-58 string representing the [Output](avmapi_outputs.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/outputs.ts:197](https://github.com/ava-labs/avalanche.js/blob/4d26b45/src/apis/avm/outputs.ts#L197)*

**Returns:** *function*

▸ (`a`: [Output](avmapi_outputs.output.md), `b`: [Output](avmapi_outputs.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](avmapi_outputs.output.md) |
`b` | [Output](avmapi_outputs.output.md) |
