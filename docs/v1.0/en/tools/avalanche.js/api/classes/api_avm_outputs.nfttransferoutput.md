[avalanche](../README.md) › [API-AVM-Outputs](../modules/api_avm_outputs.md) › [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)

# Class: NFTTransferOutput

An [Output](common_output.output.md) class which specifies an Output that carries an NFT and uses secp256k1 signature scheme.

## Hierarchy

  ↳ [NFTOutput](api_avm_outputs.nftoutput.md)

  ↳ **NFTTransferOutput**

## Index

### Constructors

* [constructor](api_avm_outputs.nfttransferoutput.md#constructor)

### Properties

* [addresses](api_avm_outputs.nfttransferoutput.md#protected-addresses)
* [groupID](api_avm_outputs.nfttransferoutput.md#protected-groupid)
* [locktime](api_avm_outputs.nfttransferoutput.md#protected-locktime)
* [numaddrs](api_avm_outputs.nfttransferoutput.md#protected-numaddrs)
* [payload](api_avm_outputs.nfttransferoutput.md#protected-payload)
* [sizePayload](api_avm_outputs.nfttransferoutput.md#protected-sizepayload)
* [threshold](api_avm_outputs.nfttransferoutput.md#protected-threshold)

### Methods

* [clone](api_avm_outputs.nfttransferoutput.md#clone)
* [create](api_avm_outputs.nfttransferoutput.md#create)
* [fromBuffer](api_avm_outputs.nfttransferoutput.md#frombuffer)
* [getAddress](api_avm_outputs.nfttransferoutput.md#getaddress)
* [getAddressIdx](api_avm_outputs.nfttransferoutput.md#getaddressidx)
* [getAddresses](api_avm_outputs.nfttransferoutput.md#getaddresses)
* [getGroupID](api_avm_outputs.nfttransferoutput.md#getgroupid)
* [getLocktime](api_avm_outputs.nfttransferoutput.md#getlocktime)
* [getOutputID](api_avm_outputs.nfttransferoutput.md#getoutputid)
* [getPayload](api_avm_outputs.nfttransferoutput.md#getpayload)
* [getPayloadBuffer](api_avm_outputs.nfttransferoutput.md#getpayloadbuffer)
* [getSpenders](api_avm_outputs.nfttransferoutput.md#getspenders)
* [getThreshold](api_avm_outputs.nfttransferoutput.md#getthreshold)
* [makeTransferable](api_avm_outputs.nfttransferoutput.md#maketransferable)
* [meetsThreshold](api_avm_outputs.nfttransferoutput.md#meetsthreshold)
* [select](api_avm_outputs.nfttransferoutput.md#select)
* [toBuffer](api_avm_outputs.nfttransferoutput.md#tobuffer)
* [toString](api_avm_outputs.nfttransferoutput.md#tostring)
* [comparator](api_avm_outputs.nfttransferoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOutput**(`groupID`: number, `payload`: Buffer, `addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)*

*Overrides [OutputOwners](common_output.outputowners.md).[constructor](common_output.outputowners.md#constructor)*

*Defined in [src/apis/avm/outputs.ts:251](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L251)*

An [Output](common_output.output.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`groupID` | number | undefined | A number representing the amount in the output |
`payload` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) of max length 1024 |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction   |

**Returns:** *[NFTTransferOutput](api_avm_outputs.nfttransferoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Inherited from [OutputOwners](common_output.outputowners.md).[addresses](common_output.outputowners.md#protected-addresses)*

*Defined in [src/common/output.ts:88](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L88)*

___

### `Protected` groupID

• **groupID**: *Buffer* = Buffer.alloc(4)

*Inherited from [BaseNFTOutput](common_output.basenftoutput.md).[groupID](common_output.basenftoutput.md#protected-groupid)*

*Defined in [src/common/output.ts:418](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L418)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Inherited from [OutputOwners](common_output.outputowners.md).[locktime](common_output.outputowners.md#protected-locktime)*

*Defined in [src/common/output.ts:85](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L85)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[numaddrs](common_output.outputowners.md#protected-numaddrs)*

*Defined in [src/common/output.ts:87](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L87)*

___

### `Protected` payload

• **payload**: *Buffer*

*Defined in [src/apis/avm/outputs.ts:197](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L197)*

___

### `Protected` sizePayload

• **sizePayload**: *Buffer* = Buffer.alloc(4)

*Defined in [src/apis/avm/outputs.ts:196](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L196)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Inherited from [OutputOwners](common_output.outputowners.md).[threshold](common_output.outputowners.md#protected-threshold)*

*Defined in [src/common/output.ts:86](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L86)*

## Methods

###  clone

▸ **clone**(): *this*

*Overrides [Output](common_output.output.md).[clone](common_output.output.md#abstract-clone)*

*Defined in [src/apis/avm/outputs.ts:247](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L247)*

**Returns:** *this*

___

###  create

▸ **create**(...`args`: any[]): *this*

*Overrides [Output](common_output.output.md).[create](common_output.output.md#abstract-create)*

*Defined in [src/apis/avm/outputs.ts:243](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L243)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Overrides [OutputOwners](common_output.outputowners.md).[fromBuffer](common_output.outputowners.md#frombuffer)*

*Defined in [src/apis/avm/outputs.ts:221](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L221)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`utxobuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddress](common_output.outputowners.md#getaddress)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddressIdx](common_output.outputowners.md#getaddressidx)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getAddresses](common_output.outputowners.md#getaddresses)*

*Defined in [src/common/output.ts:103](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L103)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getGroupID

▸ **getGroupID**(): *number*

*Inherited from [BaseNFTOutput](common_output.basenftoutput.md).[getGroupID](common_output.basenftoutput.md#getgroupid)*

*Defined in [src/common/output.ts:423](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L423)*

Returns the groupID as a number.

**Returns:** *number*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [OutputOwners](common_output.outputowners.md).[getLocktime](common_output.outputowners.md#getlocktime)*

*Defined in [src/common/output.ts:98](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L98)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Overrides [Output](common_output.output.md).[getOutputID](common_output.output.md#abstract-getoutputid)*

*Defined in [src/apis/avm/outputs.ts:202](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L202)*

Returns the outputID for this output

**Returns:** *number*

___

###  getPayload

▸ **getPayload**(): *Buffer*

*Defined in [src/apis/avm/outputs.ts:209](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L209)*

Returns the payload as a [Buffer](https://github.com/feross/buffer) with content only.

**Returns:** *Buffer*

___

###  getPayloadBuffer

▸ **getPayloadBuffer**(): *Buffer*

*Defined in [src/apis/avm/outputs.ts:215](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L215)*

Returns the payload as a [Buffer](https://github.com/feross/buffer) with length of payload prepended.

**Returns:** *Buffer*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [OutputOwners](common_output.outputowners.md).[getSpenders](common_output.outputowners.md#getspenders)*

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

*Inherited from [OutputOwners](common_output.outputowners.md).[getThreshold](common_output.outputowners.md#getthreshold)*

*Defined in [src/common/output.ts:93](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L93)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

*Inherited from [NFTOutput](api_avm_outputs.nftoutput.md).[makeTransferable](api_avm_outputs.nftoutput.md#maketransferable)*

*Overrides [Output](common_output.output.md).[makeTransferable](common_output.output.md#abstract-maketransferable)*

*Defined in [src/apis/avm/outputs.ts:68](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L68)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](api_avm_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [OutputOwners](common_output.outputowners.md).[meetsThreshold](common_output.outputowners.md#meetsthreshold)*

*Defined in [src/common/output.ts:145](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L145)*

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

*Inherited from [NFTOutput](api_avm_outputs.nftoutput.md).[select](api_avm_outputs.nftoutput.md#select)*

*Overrides [Output](common_output.output.md).[select](common_output.output.md#abstract-select)*

*Defined in [src/apis/avm/outputs.ts:72](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L72)*

**Parameters:**

Name | Type |
------ | ------ |
`id` | number |
`...args` | any[] |

**Returns:** *[Output](common_output.output.md)*

___

###  toBuffer

▸ **toBuffer**(): *Buffer*

*Overrides [OutputOwners](common_output.outputowners.md).[toBuffer](common_output.outputowners.md#tobuffer)*

*Defined in [src/apis/avm/outputs.ts:235](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/apis/avm/outputs.ts#L235)*

Returns the buffer representing the [NFTTransferOutput](api_avm_outputs.nfttransferoutput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [OutputOwners](common_output.outputowners.md).[toString](common_output.outputowners.md#tostring)*

*Defined in [src/common/output.ts:229](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L229)*

Returns a base-58 string representing the [Output](common_output.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [OutputOwners](common_output.outputowners.md).[comparator](common_output.outputowners.md#static-comparator)*

*Defined in [src/common/output.ts:233](https://github.com/ava-labs/avalanche.js/blob/a2feb77/src/common/output.ts#L233)*

**Returns:** *function*

▸ (`a`: [Output](common_output.output.md), `b`: [Output](common_output.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](common_output.output.md) |
`b` | [Output](common_output.output.md) |
