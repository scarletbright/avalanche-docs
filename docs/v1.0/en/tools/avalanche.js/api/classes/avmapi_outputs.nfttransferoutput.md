[avalanche](../README.md) › [AVMAPI-Outputs](../modules/avmapi_outputs.md) › [NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)

# Class: NFTTransferOutput

An [Output](avmapi_outputs.output.md) class which specifies an Output that carries an NFT and uses secp256k1 signature scheme.

## Hierarchy

  ↳ [NFTOutBase](avmapi_outputs.nftoutbase.md)

  ↳ **NFTTransferOutput**

## Index

### Constructors

* [constructor](avmapi_outputs.nfttransferoutput.md#constructor)

### Properties

* [addresses](avmapi_outputs.nfttransferoutput.md#protected-addresses)
* [groupID](avmapi_outputs.nfttransferoutput.md#protected-groupid)
* [locktime](avmapi_outputs.nfttransferoutput.md#protected-locktime)
* [numaddrs](avmapi_outputs.nfttransferoutput.md#protected-numaddrs)
* [payload](avmapi_outputs.nfttransferoutput.md#protected-payload)
* [sizePayload](avmapi_outputs.nfttransferoutput.md#protected-sizepayload)
* [threshold](avmapi_outputs.nfttransferoutput.md#protected-threshold)

### Methods

* [fromBuffer](avmapi_outputs.nfttransferoutput.md#frombuffer)
* [getAddress](avmapi_outputs.nfttransferoutput.md#getaddress)
* [getAddressIdx](avmapi_outputs.nfttransferoutput.md#getaddressidx)
* [getAddresses](avmapi_outputs.nfttransferoutput.md#getaddresses)
* [getGroupID](avmapi_outputs.nfttransferoutput.md#getgroupid)
* [getLocktime](avmapi_outputs.nfttransferoutput.md#getlocktime)
* [getOutputID](avmapi_outputs.nfttransferoutput.md#getoutputid)
* [getPayload](avmapi_outputs.nfttransferoutput.md#getpayload)
* [getSpenders](avmapi_outputs.nfttransferoutput.md#getspenders)
* [getThreshold](avmapi_outputs.nfttransferoutput.md#getthreshold)
* [makeTransferable](avmapi_outputs.nfttransferoutput.md#maketransferable)
* [meetsThreshold](avmapi_outputs.nfttransferoutput.md#meetsthreshold)
* [toBuffer](avmapi_outputs.nfttransferoutput.md#tobuffer)
* [toString](avmapi_outputs.nfttransferoutput.md#tostring)
* [comparator](avmapi_outputs.nfttransferoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOutput**(`groupID`: number, `payload`: Buffer, `locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)*

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[constructor](avmapi_outputs.nftoutbase.md#constructor)*

*Overrides [Output](avmapi_outputs.output.md).[constructor](avmapi_outputs.output.md#constructor)*

*Defined in [apis/avm/outputs.ts:404](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L404)*

An [Output](avmapi_outputs.output.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`groupID` | number | undefined | A number representing the amount in the output |
`payload` | Buffer | undefined | A [Buffer](https://github.com/feross/buffer) of max length 1024 |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction  |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses |

**Returns:** *[NFTTransferOutput](avmapi_outputs.nfttransferoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](avmapi_types.address.md)›* = []

*Inherited from [Output](avmapi_outputs.output.md).[addresses](avmapi_outputs.output.md#protected-addresses)*

*Defined in [apis/avm/outputs.ts:34](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L34)*

___

### `Protected` groupID

• **groupID**: *Buffer* = Buffer.alloc(4)

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[groupID](avmapi_outputs.nftoutbase.md#protected-groupid)*

*Defined in [apis/avm/outputs.ts:363](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L363)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Inherited from [Output](avmapi_outputs.output.md).[locktime](avmapi_outputs.output.md#protected-locktime)*

*Defined in [apis/avm/outputs.ts:31](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L31)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Inherited from [Output](avmapi_outputs.output.md).[numaddrs](avmapi_outputs.output.md#protected-numaddrs)*

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L33)*

___

### `Protected` payload

• **payload**: *Buffer*

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[payload](avmapi_outputs.nftoutbase.md#protected-payload)*

*Defined in [apis/avm/outputs.ts:365](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L365)*

___

### `Protected` sizePayload

• **sizePayload**: *Buffer* = Buffer.alloc(4)

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[sizePayload](avmapi_outputs.nftoutbase.md#protected-sizepayload)*

*Defined in [apis/avm/outputs.ts:364](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L364)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Inherited from [Output](avmapi_outputs.output.md).[threshold](avmapi_outputs.output.md#protected-threshold)*

*Defined in [apis/avm/outputs.ts:32](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L32)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[fromBuffer](avmapi_outputs.nftoutbase.md#frombuffer)*

*Overrides [Output](avmapi_outputs.output.md).[fromBuffer](avmapi_outputs.output.md#frombuffer)*

*Defined in [apis/avm/outputs.ts:384](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L384)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTOutBase](avmapi_outputs.nftoutbase.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`utxobuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [Output](avmapi_outputs.output.md).[getAddress](avmapi_outputs.output.md#getaddress)*

*Defined in [apis/avm/outputs.ts:90](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L90)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getAddressIdx](avmapi_outputs.output.md#getaddressidx)*

*Defined in [apis/avm/outputs.ts:73](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L73)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getAddresses](avmapi_outputs.output.md#getaddresses)*

*Defined in [apis/avm/outputs.ts:58](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L58)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getGroupID

▸ **getGroupID**(): *number*

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[getGroupID](avmapi_outputs.nftoutbase.md#getgroupid)*

*Defined in [apis/avm/outputs.ts:370](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L370)*

Returns the groupID as a number.

**Returns:** *number*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [Output](avmapi_outputs.output.md).[getLocktime](avmapi_outputs.output.md#getlocktime)*

*Defined in [apis/avm/outputs.ts:51](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L51)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Overrides [Output](avmapi_outputs.output.md).[getOutputID](avmapi_outputs.output.md#abstract-getoutputid)*

*Defined in [apis/avm/outputs.ts:432](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L432)*

Returns the outputID for this output

**Returns:** *number*

___

###  getPayload

▸ **getPayload**(): *Buffer*

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[getPayload](avmapi_outputs.nftoutbase.md#getpayload)*

*Defined in [apis/avm/outputs.ts:377](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L377)*

Returns the payload as a [Buffer](https://github.com/feross/buffer)

**Returns:** *Buffer*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [Output](avmapi_outputs.output.md).[getSpenders](avmapi_outputs.output.md#getspenders)*

*Defined in [apis/avm/outputs.ts:119](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L119)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getThreshold](avmapi_outputs.output.md#getthreshold)*

*Defined in [apis/avm/outputs.ts:44](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L44)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

*Inherited from [Output](avmapi_outputs.output.md).[makeTransferable](avmapi_outputs.output.md#maketransferable)*

*Defined in [apis/avm/outputs.ts:193](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L193)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [Output](avmapi_outputs.output.md).[meetsThreshold](avmapi_outputs.output.md#meetsthreshold)*

*Defined in [apis/avm/outputs.ts:100](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L100)*

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

*Inherited from [NFTOutBase](avmapi_outputs.nftoutbase.md).[toBuffer](avmapi_outputs.nftoutbase.md#tobuffer)*

*Overrides [Output](avmapi_outputs.output.md).[toBuffer](avmapi_outputs.output.md#tobuffer)*

*Defined in [apis/avm/outputs.ts:398](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L398)*

Returns the buffer representing the [NFTOutBase](avmapi_outputs.nftoutbase.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Output](avmapi_outputs.output.md).[toString](avmapi_outputs.output.md#tostring)*

*Defined in [apis/avm/outputs.ts:185](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L185)*

Returns a base-58 string representing the [Output](avmapi_outputs.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Output](avmapi_outputs.output.md).[comparator](avmapi_outputs.output.md#static-comparator)*

*Defined in [apis/avm/outputs.ts:197](https://github.com/ava-labs/avalanche.js/blob/3888064/src/apis/avm/outputs.ts#L197)*

**Returns:** *function*

▸ (`a`: [Output](avmapi_outputs.output.md), `b`: [Output](avmapi_outputs.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](avmapi_outputs.output.md) |
`b` | [Output](avmapi_outputs.output.md) |
