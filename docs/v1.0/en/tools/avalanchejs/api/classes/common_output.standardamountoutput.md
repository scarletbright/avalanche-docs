[avalanche](../README.md) › [Common-Output](../modules/common_output.md) › [StandardAmountOutput](common_output.standardamountoutput.md)

# Class: StandardAmountOutput

An [Output](common_output.output.md) class which specifies a token amount .

## Hierarchy

  ↳ [Output](common_output.output.md)

  ↳ **StandardAmountOutput**

  ↳ [AmountOutput](api_avm_outputs.amountoutput.md)

  ↳ [AmountOutput](api_platformvm_outputs.amountoutput.md)

## Index

### Constructors

* [constructor](common_output.standardamountoutput.md#constructor)

### Properties

* [addresses](common_output.standardamountoutput.md#protected-addresses)
* [amount](common_output.standardamountoutput.md#protected-amount)
* [amountValue](common_output.standardamountoutput.md#protected-amountvalue)
* [locktime](common_output.standardamountoutput.md#protected-locktime)
* [numaddrs](common_output.standardamountoutput.md#protected-numaddrs)
* [threshold](common_output.standardamountoutput.md#protected-threshold)

### Methods

* [clone](common_output.standardamountoutput.md#abstract-clone)
* [create](common_output.standardamountoutput.md#abstract-create)
* [fromBuffer](common_output.standardamountoutput.md#frombuffer)
* [getAddress](common_output.standardamountoutput.md#getaddress)
* [getAddressIdx](common_output.standardamountoutput.md#getaddressidx)
* [getAddresses](common_output.standardamountoutput.md#getaddresses)
* [getAmount](common_output.standardamountoutput.md#getamount)
* [getLocktime](common_output.standardamountoutput.md#getlocktime)
* [getOutputID](common_output.standardamountoutput.md#abstract-getoutputid)
* [getSpenders](common_output.standardamountoutput.md#getspenders)
* [getThreshold](common_output.standardamountoutput.md#getthreshold)
* [makeTransferable](common_output.standardamountoutput.md#abstract-maketransferable)
* [meetsThreshold](common_output.standardamountoutput.md#meetsthreshold)
* [select](common_output.standardamountoutput.md#abstract-select)
* [toBuffer](common_output.standardamountoutput.md#tobuffer)
* [toString](common_output.standardamountoutput.md#tostring)
* [comparator](common_output.standardamountoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new StandardAmountOutput**(`amount`: BN, `addresses`: Array‹Buffer›, `locktime`: BN, `threshold`: number): *[StandardAmountOutput](common_output.standardamountoutput.md)*

*Overrides [OutputOwners](common_output.outputowners.md).[constructor](common_output.outputowners.md#constructor)*

*Defined in [src/common/output.ts:394](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L394)*

A [[BaseAmountOutput]] class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the output |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction   |

**Returns:** *[StandardAmountOutput](common_output.standardamountoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](common_output.address.md)›* = []

*Inherited from [OutputOwners](common_output.outputowners.md).[addresses](common_output.outputowners.md#protected-addresses)*

*Defined in [src/common/output.ts:88](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L88)*

___

### `Protected` amount

• **amount**: *Buffer* = Buffer.alloc(8)

*Defined in [src/common/output.ts:366](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L366)*

___

### `Protected` amountValue

• **amountValue**: *BN* = new BN(0)

*Defined in [src/common/output.ts:368](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L368)*

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

### `Abstract` clone

▸ **clone**(): *this*

*Inherited from [Output](common_output.output.md).[clone](common_output.output.md#abstract-clone)*

*Defined in [src/common/output.ts:280](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L280)*

**Returns:** *this*

___

### `Abstract` create

▸ **create**(...`args`: any[]): *this*

*Inherited from [Output](common_output.output.md).[create](common_output.output.md#abstract-create)*

*Defined in [src/common/output.ts:282](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L282)*

**Parameters:**

Name | Type |
------ | ------ |
`...args` | any[] |

**Returns:** *this*

___

###  fromBuffer

▸ **fromBuffer**(`outbuff`: Buffer, `offset`: number): *number*

*Overrides [OutputOwners](common_output.outputowners.md).[fromBuffer](common_output.outputowners.md#frombuffer)*

*Defined in [src/common/output.ts:378](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L378)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [StandardAmountOutput](common_output.standardamountoutput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`outbuff` | Buffer | - |
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

###  getAmount

▸ **getAmount**(): *BN*

*Defined in [src/common/output.ts:373](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L373)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [OutputOwners](common_output.outputowners.md).[getLocktime](common_output.outputowners.md#getlocktime)*

*Defined in [src/common/output.ts:98](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L98)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Inherited from [Output](common_output.output.md).[getOutputID](common_output.output.md#abstract-getoutputid)*

*Defined in [src/common/output.ts:278](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L278)*

Returns the outputID for the output which tells parsers what type it is

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

### `Abstract` makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

*Inherited from [Output](common_output.output.md).[makeTransferable](common_output.output.md#abstract-maketransferable)*

*Defined in [src/common/output.ts:292](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L292)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  Must be implemented to use the appropriate TransferableOutput for the VM.  |

**Returns:** *[StandardTransferableOutput](common_output.standardtransferableoutput.md)*

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

### `Abstract` select

▸ **select**(`id`: number, ...`args`: any[]): *[Output](common_output.output.md)*

*Inherited from [Output](common_output.output.md).[select](common_output.output.md#abstract-select)*

*Defined in [src/common/output.ts:284](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L284)*

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

*Defined in [src/common/output.ts:388](https://github.com/ava-labs/avalanchejs/blob/a2feb77/src/common/output.ts#L388)*

Returns the buffer representing the [StandardAmountOutput](common_output.standardamountoutput.md) instance.

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
