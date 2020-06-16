[slopes - v1.7.5](../README.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [Output](_apis_avm_outputs_.output.md)

# Class: Output

## Hierarchy

* **Output**

  ↳ [AmountOutput](_apis_avm_outputs_.amountoutput.md)

  ↳ [NFTOutBase](_apis_avm_outputs_.nftoutbase.md)

## Index

### Constructors

* [constructor](_apis_avm_outputs_.output.md#constructor)

### Properties

* [addresses](_apis_avm_outputs_.output.md#protected-addresses)
* [locktime](_apis_avm_outputs_.output.md#protected-locktime)
* [numaddrs](_apis_avm_outputs_.output.md#protected-numaddrs)
* [threshold](_apis_avm_outputs_.output.md#protected-threshold)

### Methods

* [fromBuffer](_apis_avm_outputs_.output.md#frombuffer)
* [getAddress](_apis_avm_outputs_.output.md#getaddress)
* [getAddressIdx](_apis_avm_outputs_.output.md#getaddressidx)
* [getAddresses](_apis_avm_outputs_.output.md#getaddresses)
* [getLocktime](_apis_avm_outputs_.output.md#getlocktime)
* [getOutputID](_apis_avm_outputs_.output.md#abstract-getoutputid)
* [getSpenders](_apis_avm_outputs_.output.md#getspenders)
* [getThreshold](_apis_avm_outputs_.output.md#getthreshold)
* [makeTransferable](_apis_avm_outputs_.output.md#maketransferable)
* [meetsThreshold](_apis_avm_outputs_.output.md#meetsthreshold)
* [toBuffer](_apis_avm_outputs_.output.md#tobuffer)
* [toString](_apis_avm_outputs_.output.md#tostring)
* [comparator](_apis_avm_outputs_.output.md#static-comparator)

## Constructors

###  constructor

\+ **new Output**(`locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:210](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L210)*

An [Output](_apis_avm_outputs_.output.md) class which contains locktimes, thresholds, and addresses.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`locktime` | BN |  undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number |  undefined | A number representing the the threshold number of signers required to sign the transaction |
`addresses` | Array‹Buffer› |  undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses  |

**Returns:** *[Output](_apis_avm_outputs_.output.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](_apis_avm_types_.address.md)›* =  []

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L33)*

___

### `Protected` locktime

• **locktime**: *Buffer* =  Buffer.alloc(8)

*Defined in [apis/avm/outputs.ts:30](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L30)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:32](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L32)*

___

### `Protected` threshold

• **threshold**: *Buffer* =  Buffer.alloc(4)

*Defined in [apis/avm/outputs.ts:31](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L31)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`bytes`: Buffer, `offset`: number): *number*

*Defined in [apis/avm/outputs.ts:147](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L147)*

Returns a base-58 string representing the [Output](_apis_avm_outputs_.output.md).

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`bytes` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Defined in [apis/avm/outputs.ts:89](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L89)*

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

*Defined in [apis/avm/outputs.ts:72](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L72)*

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

*Defined in [apis/avm/outputs.ts:57](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L57)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Defined in [apis/avm/outputs.ts:50](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L50)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Defined in [apis/avm/outputs.ts:38](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L38)*

Returns the outputID for the output which tells parsers what type it is

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Defined in [apis/avm/outputs.ts:118](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L118)*

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

*Defined in [apis/avm/outputs.ts:43](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L43)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

*Defined in [apis/avm/outputs.ts:192](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L192)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Defined in [apis/avm/outputs.ts:99](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L99)*

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

*Defined in [apis/avm/outputs.ts:168](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L168)*

Returns the buffer representing the [Output](_apis_avm_outputs_.output.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Defined in [apis/avm/outputs.ts:184](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L184)*

Returns a base-58 string representing the [Output](_apis_avm_outputs_.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Defined in [apis/avm/outputs.ts:196](https://github.com/ava-labs/slopes/blob/be20cee/src/apis/avm/outputs.ts#L196)*

**Returns:** *function*

▸ (`a`: [Output](_apis_avm_outputs_.output.md), `b`: [Output](_apis_avm_outputs_.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](_apis_avm_outputs_.output.md) |
`b` | [Output](_apis_avm_outputs_.output.md) |
