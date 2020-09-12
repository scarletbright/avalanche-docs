[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [OutputOwners](common_output.outputowners.md)

# Class: OutputOwners

Defines the most basic values for output ownership. Mostly inherited from, but can be used in population of NFT Owner data.

## Hierarchy

* **OutputOwners**

  ↳ [Output](common_output.output.md)

## Index

### Constructors

* [constructor](common_output.outputowners.md#constructor)

### Properties

* [addresses](common_output.outputowners.md#protected-addresses)
* [locktime](common_output.outputowners.md#protected-locktime)
* [numaddrs](common_output.outputowners.md#protected-numaddrs)
* [threshold](common_output.outputowners.md#protected-threshold)

### Methods

* [fromBuffer](common_output.outputowners.md#frombuffer)
* [getAddress](common_output.outputowners.md#getaddress)
* [getAddressIdx](common_output.outputowners.md#getaddressidx)
* [getAddresses](common_output.outputowners.md#getaddresses)
* [getLocktime](common_output.outputowners.md#getlocktime)
* [getSpenders](common_output.outputowners.md#getspenders)
* [getThreshold](common_output.outputowners.md#getthreshold)
* [meetsThreshold](common_output.outputowners.md#meetsthreshold)
* [toBuffer](common_output.outputowners.md#tobuffer)
* [toString](common_output.outputowners.md#tostring)
* [comparator](common_output.outputowners.md#static-comparator)

## Constructors

###  constructor

\+ **new OutputOwners**(`addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[OutputOwners](common_output.outputowners.md)*

*Defined in [src/common/output.ts:245](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L245)*

An [Output](common_output.output.md) class which contains addresses, locktimes, and thresholds.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing output owner's addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction  |

**Returns:** *[OutputOwners](common_output.outputowners.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Defined in [src/common/output.ts:88](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L88)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Defined in [src/common/output.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L85)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/output.ts:87](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L87)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Defined in [src/common/output.ts:86](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L86)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [src/common/output.ts:192](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L192)*

Returns a base-58 string representing the [Output](common_output.output.md).

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Defined in [src/common/output.ts:135](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L135)*

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

*Defined in [src/common/output.ts:118](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L118)*

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

*Defined in [src/common/output.ts:103](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L103)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [src/common/output.ts:98](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L98)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [src/common/output.ts:164](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L164)*

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

*Defined in [src/common/output.ts:93](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L93)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [src/common/output.ts:145](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L145)*

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

*Defined in [src/common/output.ts:213](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L213)*

Returns the buffer representing the [Output](common_output.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [src/common/output.ts:229](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L229)*

Returns a base-58 string representing the [Output](common_output.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [src/common/output.ts:233](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L233)*

**Returns:** *function*

▸ (`a`: [Output](common_output.output.md), `b`: [Output](common_output.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](common_output.output.md) |
`b` | [Output](common_output.output.md) |
