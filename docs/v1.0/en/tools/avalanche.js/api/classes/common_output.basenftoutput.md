[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [BaseNFTOutput](common_output.basenftoutput.md)

# Class: BaseNFTOutput

An [Output](common_output.output.md) class which specifies an NFT.

## Hierarchy

  ↳ [Output](common_output.output.md)

  ↳ **BaseNFTOutput**

  ↳ [NFTOutput](api_avm_outputs.nftoutput.md)

## Index

### Constructors

* [constructor](common_output.basenftoutput.md#constructor)

### Properties

* [addresses](common_output.basenftoutput.md#protected-addresses)
* [groupID](common_output.basenftoutput.md#protected-groupid)
* [locktime](common_output.basenftoutput.md#protected-locktime)
* [numaddrs](common_output.basenftoutput.md#protected-numaddrs)
* [threshold](common_output.basenftoutput.md#protected-threshold)

### Methods

* [fromBuffer](common_output.basenftoutput.md#frombuffer)
* [getAddress](common_output.basenftoutput.md#getaddress)
* [getAddressIdx](common_output.basenftoutput.md#getaddressidx)
* [getAddresses](common_output.basenftoutput.md#getaddresses)
* [getGroupID](common_output.basenftoutput.md#getgroupid)
* [getLocktime](common_output.basenftoutput.md#getlocktime)
* [getOutputID](common_output.basenftoutput.md#abstract-getoutputid)
* [getSpenders](common_output.basenftoutput.md#getspenders)
* [getThreshold](common_output.basenftoutput.md#getthreshold)
* [makeTransferable](common_output.basenftoutput.md#abstract-maketransferable)
* [meetsThreshold](common_output.basenftoutput.md#meetsthreshold)
* [toBuffer](common_output.basenftoutput.md#tobuffer)
* [toString](common_output.basenftoutput.md#tostring)
* [comparator](common_output.basenftoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new BaseNFTOutput**(`addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[BaseNFTOutput](common_output.basenftoutput.md)*

*Inherited from [OutputOwners](common_output.outputowners.md).[constructor](common_output.outputowners.md#constructor)*

Defined in src/common/output.ts:232

An [Output](common_output.output.md) class which contains addresses, locktimes, and thresholds.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing output owner's addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction  |

**Returns:** *[BaseNFTOutput](common_output.basenftoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Inherited from [OutputOwners](common_output.outputowners.md).[addresses](common_output.outputowners.md#protected-addresses)*

Defined in src/common/output.ts:75

___

### `Protected` groupID

• **groupID**: *Buffer* = Buffer.alloc(4)

Defined in src/common/output.ts:375

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Inherited from [OutputOwners](common_output.outputowners.md).[locktime](common_output.outputowners.md#protected-locktime)*

Defined in src/common/output.ts:72

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[numaddrs](common_output.outputowners.md#protected-numaddrs)*

Defined in src/common/output.ts:74

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[threshold](common_output.outputowners.md#protected-threshold)*

Defined in src/common/output.ts:73

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Inherited from [OutputOwners](common_output.outputowners.md).[fromBuffer](common_output.outputowners.md#frombuffer)*

Defined in src/common/output.ts:179

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

Defined in src/common/output.ts:122

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

Defined in src/common/output.ts:105

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

Defined in src/common/output.ts:90

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getGroupID

▸ **getGroupID**(): *number*

Defined in src/common/output.ts:380

Returns the groupID as a number.

**Returns:** *number*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [OutputOwners](common_output.outputowners.md).[getLocktime](common_output.outputowners.md#getlocktime)*

Defined in src/common/output.ts:85

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Inherited from [Output](common_output.output.md).[getOutputID](common_output.output.md#abstract-getoutputid)*

Defined in src/common/output.ts:265

Returns the outputID for the output which tells parsers what type it is

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [OutputOwners](common_output.outputowners.md).[getSpenders](common_output.outputowners.md#getspenders)*

Defined in src/common/output.ts:151

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

Defined in src/common/output.ts:80

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

### `Abstract` makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

*Inherited from [Output](common_output.output.md).[makeTransferable](common_output.output.md#abstract-maketransferable)*

Defined in src/common/output.ts:273

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  Must be implemented to use the appropriate TransferableOutput for the VM.  |

**Returns:** *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [OutputOwners](common_output.outputowners.md).[meetsThreshold](common_output.outputowners.md#meetsthreshold)*

Defined in src/common/output.ts:132

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

*Inherited from [OutputOwners](common_output.outputowners.md).[toBuffer](common_output.outputowners.md#tobuffer)*

Defined in src/common/output.ts:200

Returns the buffer representing the [Output](common_output.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [OutputOwners](common_output.outputowners.md).[toString](common_output.outputowners.md#tostring)*

Defined in src/common/output.ts:216

Returns a base-58 string representing the [Output](common_output.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [OutputOwners](common_output.outputowners.md).[comparator](common_output.outputowners.md#static-comparator)*

Defined in src/common/output.ts:220

**Returns:** *function*

▸ (`a`: [Output](common_output.output.md), `b`: [Output](common_output.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](common_output.output.md) |
`b` | [Output](common_output.output.md) |
