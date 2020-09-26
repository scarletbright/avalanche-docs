[avalanche](../README.md) › [API-AVM-Outputs](../modules/api_avm_outputs.md) › [SECPMintOutput](api_avm_outputs.secpmintoutput.md)

# Class: SECPMintOutput

An [Output](common_output.output.md) class which specifies an Output that carries an ammount for an assetID and uses secp256k1 signature scheme.

## Hierarchy

  ↳ [Output](common_output.output.md)

  ↳ **SECPMintOutput**

## Index

### Constructors

* [constructor](api_avm_outputs.secpmintoutput.md#constructor)

### Properties

* [addresses](api_avm_outputs.secpmintoutput.md#protected-addresses)
* [locktime](api_avm_outputs.secpmintoutput.md#protected-locktime)
* [numaddrs](api_avm_outputs.secpmintoutput.md#protected-numaddrs)
* [threshold](api_avm_outputs.secpmintoutput.md#protected-threshold)

### Methods

* [clone](api_avm_outputs.secpmintoutput.md#clone)
* [create](api_avm_outputs.secpmintoutput.md#create)
* [fromBuffer](api_avm_outputs.secpmintoutput.md#frombuffer)
* [getAddress](api_avm_outputs.secpmintoutput.md#getaddress)
* [getAddressIdx](api_avm_outputs.secpmintoutput.md#getaddressidx)
* [getAddresses](api_avm_outputs.secpmintoutput.md#getaddresses)
* [getLocktime](api_avm_outputs.secpmintoutput.md#getlocktime)
* [getOutputID](api_avm_outputs.secpmintoutput.md#getoutputid)
* [getSpenders](api_avm_outputs.secpmintoutput.md#getspenders)
* [getThreshold](api_avm_outputs.secpmintoutput.md#getthreshold)
* [makeTransferable](api_avm_outputs.secpmintoutput.md#maketransferable)
* [meetsThreshold](api_avm_outputs.secpmintoutput.md#meetsthreshold)
* [select](api_avm_outputs.secpmintoutput.md#select)
* [toBuffer](api_avm_outputs.secpmintoutput.md#tobuffer)
* [toString](api_avm_outputs.secpmintoutput.md#tostring)
* [comparator](api_avm_outputs.secpmintoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new SECPMintOutput**(`addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[SECPMintOutput](api_avm_outputs.secpmintoutput.md)*

*Inherited from [OutputOwners](common_output.outputowners.md).[constructor](common_output.outputowners.md#constructor)*

*Defined in [src/common/output.ts:245](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L245)*

An [Output](common_output.output.md) class which contains addresses, locktimes, and thresholds.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing output owner's addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction  |

**Returns:** *[SECPMintOutput](api_avm_outputs.secpmintoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Inherited from [OutputOwners](common_output.outputowners.md).[addresses](common_output.outputowners.md#protected-addresses)*

*Defined in [src/common/output.ts:88](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L88)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Inherited from [OutputOwners](common_output.outputowners.md).[locktime](common_output.outputowners.md#protected-locktime)*

*Defined in [src/common/output.ts:85](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L85)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[numaddrs](common_output.outputowners.md#protected-numaddrs)*

*Defined in [src/common/output.ts:87](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L87)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[threshold](common_output.outputowners.md#protected-threshold)*

*Defined in [src/common/output.ts:86](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L86)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [Output](common_output.output.md).[clone](common_output.output.md#abstract-clone)*

*Defined in [src/apis/avm/outputs.ts:124](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L124)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [Output](common_output.output.md).[create](common_output.output.md#abstract-create)*

*Defined in [src/apis/avm/outputs.ts:120](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L120)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Inherited from [OutputOwners](common_output.outputowners.md).[fromBuffer](common_output.outputowners.md#frombuffer)*

*Defined in [src/common/output.ts:192](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L192)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddress](common_output.outputowners.md#getaddress)*

*Defined in [src/common/output.ts:135](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L135)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddressIdx](common_output.outputowners.md#getaddressidx)*

*Defined in [src/common/output.ts:118](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L118)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddresses](common_output.outputowners.md#getaddresses)*

*Defined in [src/common/output.ts:103](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L103)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [OutputOwners](common_output.outputowners.md).[getLocktime](common_output.outputowners.md#getlocktime)*

*Defined in [src/common/output.ts:98](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L98)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Overrides [Output](common_output.output.md).[getOutputID](common_output.output.md#abstract-getoutputid)*

*Defined in [src/apis/avm/outputs.ts:108](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L108)*

Returns the outputID for this output

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [OutputOwners](common_output.outputowners.md).[getSpenders](common_output.outputowners.md#getspenders)*

*Defined in [src/common/output.ts:164](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L164)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getThreshold](common_output.outputowners.md#getthreshold)*

*Defined in [src/common/output.ts:93](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L93)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

*Overrides [Output](common_output.output.md).[makeTransferable](common_output.output.md#abstract-maketransferable)*

*Defined in [src/apis/avm/outputs.ts:116](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L116)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [OutputOwners](common_output.outputowners.md).[meetsThreshold](common_output.outputowners.md#meetsthreshold)*

*Defined in [src/common/output.ts:145](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L145)*

Given an array of address [Buffer](https://github.com/feross/buffer)s and an optional timestamp, returns true if the addresses meet the threshold required to spend the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`addresses` | Array‹Buffer› | - |
`asOf` | BN | undefined |

**Returns:** *boolean*

___

###  select

▸ **select**(`id`: number, ...`args`: any[]): *[Output](common_output.output.md)*

*Overrides [Output](common_output.output.md).[select](common_output.output.md#abstract-select)*

*Defined in [src/apis/avm/outputs.ts:130](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/apis/avm/outputs.ts#L130)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Inherited from [OutputOwners](common_output.outputowners.md).[toBuffer](common_output.outputowners.md#tobuffer)*

*Defined in [src/common/output.ts:213](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L213)*

Returns the buffer representing the [Output](common_output.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [OutputOwners](common_output.outputowners.md).[toString](common_output.outputowners.md#tostring)*

*Defined in [src/common/output.ts:229](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L229)*

Returns a base-58 string representing the [Output](common_output.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [OutputOwners](common_output.outputowners.md).[comparator](common_output.outputowners.md#static-comparator)*

*Defined in [src/common/output.ts:233](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L233)*

**Returns:** *function*

▸ (`a`: [Output](common_output.output.md), `b`: [Output](common_output.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](common_output.output.md) |
`b` | [Output](common_output.output.md) |
