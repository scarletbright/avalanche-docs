[slopes - v1.7.1](../README.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)

# Class: NFTTransferOutput

An [Output](_apis_avm_outputs_.output.md) class which specifies an Output that carries an NFT and uses secp256k1 signature scheme.

## Hierarchy

  ↳ [NFTOutBase](_apis_avm_outputs_.nftoutbase.md)

  ↳ **NFTTransferOutput**

## Index

### Constructors

* [constructor](_apis_avm_outputs_.nfttransferoutput.md#constructor)

### Properties

* [addresses](_apis_avm_outputs_.nfttransferoutput.md#protected-addresses)
* [groupID](_apis_avm_outputs_.nfttransferoutput.md#protected-groupid)
* [locktime](_apis_avm_outputs_.nfttransferoutput.md#protected-locktime)
* [numaddrs](_apis_avm_outputs_.nfttransferoutput.md#protected-numaddrs)
* [payload](_apis_avm_outputs_.nfttransferoutput.md#protected-payload)
* [sizePayload](_apis_avm_outputs_.nfttransferoutput.md#protected-sizepayload)
* [threshold](_apis_avm_outputs_.nfttransferoutput.md#protected-threshold)

### Methods

* [fromBuffer](_apis_avm_outputs_.nfttransferoutput.md#frombuffer)
* [getAddress](_apis_avm_outputs_.nfttransferoutput.md#getaddress)
* [getAddressIdx](_apis_avm_outputs_.nfttransferoutput.md#getaddressidx)
* [getAddresses](_apis_avm_outputs_.nfttransferoutput.md#getaddresses)
* [getGroupID](_apis_avm_outputs_.nfttransferoutput.md#getgroupid)
* [getLocktime](_apis_avm_outputs_.nfttransferoutput.md#getlocktime)
* [getOutputID](_apis_avm_outputs_.nfttransferoutput.md#getoutputid)
* [getPayload](_apis_avm_outputs_.nfttransferoutput.md#getpayload)
* [getSpenders](_apis_avm_outputs_.nfttransferoutput.md#getspenders)
* [getThreshold](_apis_avm_outputs_.nfttransferoutput.md#getthreshold)
* [makeTransferable](_apis_avm_outputs_.nfttransferoutput.md#maketransferable)
* [meetsThreshold](_apis_avm_outputs_.nfttransferoutput.md#meetsthreshold)
* [toBuffer](_apis_avm_outputs_.nfttransferoutput.md#tobuffer)
* [toString](_apis_avm_outputs_.nfttransferoutput.md#tostring)
* [comparator](_apis_avm_outputs_.nfttransferoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new NFTTransferOutput**(`groupID`: number, `payload`: Buffer, `locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)*

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[constructor](_apis_avm_outputs_.nftoutbase.md#constructor)*

*Overrides [Output](_apis_avm_outputs_.output.md).[constructor](_apis_avm_outputs_.output.md#constructor)*

*Defined in [apis/avm/outputs.ts:403](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L403)*

An [Output](_apis_avm_outputs_.output.md) class which contains an NFT on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`groupID` | number |  undefined | A number representing the amount in the output |
`payload` | Buffer |  undefined | A [Buffer](https://github.com/feross/buffer) of max length 1024 |
`locktime` | BN |  undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number |  undefined | A number representing the the threshold number of signers required to sign the transaction  |
`addresses` | Array‹Buffer› |  undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses |

**Returns:** *[NFTTransferOutput](_apis_avm_outputs_.nfttransferoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](_apis_avm_types_.address.md)›* =  []

*Inherited from [Output](_apis_avm_outputs_.output.md).[addresses](_apis_avm_outputs_.output.md#protected-addresses)*

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L33)*

___

### `Protected` groupID

• **groupID**: *Buffer* =  Buffer.alloc(4)

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[groupID](_apis_avm_outputs_.nftoutbase.md#protected-groupid)*

*Defined in [apis/avm/outputs.ts:362](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L362)*

___

### `Protected` locktime

• **locktime**: *Buffer* =  Buffer.alloc(8)

*Inherited from [Output](_apis_avm_outputs_.output.md).[locktime](_apis_avm_outputs_.output.md#protected-locktime)*

*Defined in [apis/avm/outputs.ts:30](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L30)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Output](_apis_avm_outputs_.output.md).[numaddrs](_apis_avm_outputs_.output.md#protected-numaddrs)*

*Defined in [apis/avm/outputs.ts:32](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L32)*

___

### `Protected` payload

• **payload**: *Buffer*

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[payload](_apis_avm_outputs_.nftoutbase.md#protected-payload)*

*Defined in [apis/avm/outputs.ts:364](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L364)*

___

### `Protected` sizePayload

• **sizePayload**: *Buffer* =  Buffer.alloc(4)

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[sizePayload](_apis_avm_outputs_.nftoutbase.md#protected-sizepayload)*

*Defined in [apis/avm/outputs.ts:363](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L363)*

___

### `Protected` threshold

• **threshold**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Output](_apis_avm_outputs_.output.md).[threshold](_apis_avm_outputs_.output.md#protected-threshold)*

*Defined in [apis/avm/outputs.ts:31](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L31)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`utxobuff`: Buffer, `offset`: number): *number*

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[fromBuffer](_apis_avm_outputs_.nftoutbase.md#frombuffer)*

*Overrides [Output](_apis_avm_outputs_.output.md).[fromBuffer](_apis_avm_outputs_.output.md#frombuffer)*

*Defined in [apis/avm/outputs.ts:383](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L383)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [NFTOutBase](_apis_avm_outputs_.nftoutbase.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`utxobuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:89](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L89)*

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

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:72](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L72)*

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

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:57](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L57)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getGroupID

▸ **getGroupID**(): *number*

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md)*

*Defined in [apis/avm/outputs.ts:369](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L369)*

Returns the groupID as a number.

**Returns:** *number*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:50](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L50)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Overrides [Output](_apis_avm_outputs_.output.md).[getOutputID](_apis_avm_outputs_.output.md#abstract-getoutputid)*

*Defined in [apis/avm/outputs.ts:431](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L431)*

Returns the outputID for this output

**Returns:** *number*

___

###  getPayload

▸ **getPayload**(): *Buffer*

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md)*

*Defined in [apis/avm/outputs.ts:376](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L376)*

Returns the payload as a [Buffer](https://github.com/feross/buffer)

**Returns:** *Buffer*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:118](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L118)*

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

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:43](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L43)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

*Inherited from [Output](_apis_avm_outputs_.output.md).[makeTransferable](_apis_avm_outputs_.output.md#maketransferable)*

*Defined in [apis/avm/outputs.ts:192](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L192)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:99](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L99)*

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

*Inherited from [NFTOutBase](_apis_avm_outputs_.nftoutbase.md).[toBuffer](_apis_avm_outputs_.nftoutbase.md#tobuffer)*

*Overrides [Output](_apis_avm_outputs_.output.md).[toBuffer](_apis_avm_outputs_.output.md#tobuffer)*

*Defined in [apis/avm/outputs.ts:397](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L397)*

Returns the buffer representing the [NFTOutBase](_apis_avm_outputs_.nftoutbase.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Output](_apis_avm_outputs_.output.md).[toString](_apis_avm_outputs_.output.md#tostring)*

*Defined in [apis/avm/outputs.ts:184](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L184)*

Returns a base-58 string representing the [Output](_apis_avm_outputs_.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:196](https://github.com/ava-labs/slopes/blob/0d1acbd/src/apis/avm/outputs.ts#L196)*

**Returns:** *function*

▸ (`a`: [Output](_apis_avm_outputs_.output.md), `b`: [Output](_apis_avm_outputs_.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](_apis_avm_outputs_.output.md) |
`b` | [Output](_apis_avm_outputs_.output.md) |
