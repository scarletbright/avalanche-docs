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

*Defined in [src/apis/avm/outputs.ts:208](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L208)*

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

*Defined in [src/apis/avm/outputs.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L37)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Defined in [src/apis/avm/outputs.ts:31](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L31)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/outputs.ts:35](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L35)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/outputs.ts:33](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L33)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/apis/avm/outputs.ts:147](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L147)*

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

*Defined in [src/apis/avm/outputs.ts:89](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L89)*

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

*Defined in [src/apis/avm/outputs.ts:72](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L72)*

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

*Defined in [src/apis/avm/outputs.ts:57](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L57)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [src/apis/avm/outputs.ts:52](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L52)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Defined in [src/apis/avm/outputs.ts:42](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L42)*

Returns the outputID for the output which tells parsers what type it is

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [src/apis/avm/outputs.ts:118](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L118)*

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

*Defined in [src/apis/avm/outputs.ts:47](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L47)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

*Defined in [src/apis/avm/outputs.ts:192](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L192)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [src/apis/avm/outputs.ts:99](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L99)*

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

*Defined in [src/apis/avm/outputs.ts:168](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L168)*

Returns the buffer representing the [Output](avmapi_outputs.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/apis/avm/outputs.ts:184](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L184)*

Returns a base-58 string representing the [Output](avmapi_outputs.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/apis/avm/outputs.ts:196](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L196)*

**Returns:** *function*

▸ (`a`: [Output](avmapi_outputs.output.md), `b`: [Output](avmapi_outputs.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](avmapi_outputs.output.md) |
`b` | [Output](avmapi_outputs.output.md) |
