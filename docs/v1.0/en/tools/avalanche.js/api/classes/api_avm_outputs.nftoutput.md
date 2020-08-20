[avalanche](../README.md) › [API-AVM-Outputs](../modules/api_avm_outputs.md) › [NFTOutput](api_avm_outputs.nftoutput.md)

# Class: NFTOutput

## Hierarchy

  ↳ [BaseNFTOutput](common_output.basenftoutput.md)

  ↳ **NFTOutput**

  ↳ [NFTMintOutput](api_avm_outputs.nftmintoutput.md)

  ↳ [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)

## Index

### Constructors

* [constructor](api_avm_outputs.nftoutput.md#constructor)

### Properties

* [addresses](api_avm_outputs.nftoutput.md#protected-addresses)
* [groupID](api_avm_outputs.nftoutput.md#protected-groupid)
* [locktime](api_avm_outputs.nftoutput.md#protected-locktime)
* [numaddrs](api_avm_outputs.nftoutput.md#protected-numaddrs)
* [threshold](api_avm_outputs.nftoutput.md#protected-threshold)

### Methods

* [fromBuffer](api_avm_outputs.nftoutput.md#frombuffer)
* [getAddress](api_avm_outputs.nftoutput.md#getaddress)
* [getAddressIdx](api_avm_outputs.nftoutput.md#getaddressidx)
* [getAddresses](api_avm_outputs.nftoutput.md#getaddresses)
* [getGroupID](api_avm_outputs.nftoutput.md#getgroupid)
* [getLocktime](api_avm_outputs.nftoutput.md#getlocktime)
* [getOutputID](api_avm_outputs.nftoutput.md#abstract-getoutputid)
* [getSpenders](api_avm_outputs.nftoutput.md#getspenders)
* [getThreshold](api_avm_outputs.nftoutput.md#getthreshold)
* [makeTransferable](api_avm_outputs.nftoutput.md#maketransferable)
* [meetsThreshold](api_avm_outputs.nftoutput.md#meetsthreshold)
* [toBuffer](api_avm_outputs.nftoutput.md#tobuffer)
* [toString](api_avm_outputs.nftoutput.md#tostring)
* [comparator](api_avm_outputs.nftoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTOutput**(`addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[NFTOutput](api_avm_outputs.nftoutput.md)*

*Inherited from [OutputOwners](common_output.outputowners.md).[constructor](common_output.outputowners.md#constructor)*

Defined in src/common/output.ts:232

An [Output](common_output.output.md) class which contains addresses, locktimes, and thresholds.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing output owner's addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction  |

**Returns:** *[NFTOutput](api_avm_outputs.nftoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Inherited from [OutputOwners](common_output.outputowners.md).[addresses](common_output.outputowners.md#protected-addresses)*

Defined in src/common/output.ts:75

___

### `Protected` groupID

• **groupID**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseNFTOutput](common_output.basenftoutput.md).[groupID](common_output.basenftoutput.md#protected-groupid)*

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

*Inherited from [BaseNFTOutput](common_output.basenftoutput.md).[getGroupID](common_output.basenftoutput.md#getgroupid)*

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

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

*Overrides [Output](common_output.output.md).[makeTransferable](common_output.output.md#abstract-maketransferable)*

Defined in src/apis/avm/outputs.ts:60

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

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
