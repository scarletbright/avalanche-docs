[avalanche](../README.md) › [AVMAPI-Outputs](../modules/avmapi_outputs.md) › [SecpOutput](avmapi_outputs.secpoutput.md)

# Class: SecpOutput

An [Output](avmapi_outputs.output.md) class which specifies an Output that carries an ammount for an assetID and uses secp256k1 signature scheme.

## Hierarchy

  ↳ [AmountOutput](avmapi_outputs.amountoutput.md)

  ↳ **SecpOutput**

## Index

### Constructors

* [constructor](avmapi_outputs.secpoutput.md#constructor)

### Properties

* [addresses](avmapi_outputs.secpoutput.md#protected-addresses)
* [amount](avmapi_outputs.secpoutput.md#protected-amount)
* [amountValue](avmapi_outputs.secpoutput.md#protected-amountvalue)
* [locktime](avmapi_outputs.secpoutput.md#protected-locktime)
* [numaddrs](avmapi_outputs.secpoutput.md#protected-numaddrs)
* [threshold](avmapi_outputs.secpoutput.md#protected-threshold)

### Methods

* [fromBuffer](avmapi_outputs.secpoutput.md#frombuffer)
* [getAddress](avmapi_outputs.secpoutput.md#getaddress)
* [getAddressIdx](avmapi_outputs.secpoutput.md#getaddressidx)
* [getAddresses](avmapi_outputs.secpoutput.md#getaddresses)
* [getAmount](avmapi_outputs.secpoutput.md#getamount)
* [getLocktime](avmapi_outputs.secpoutput.md#getlocktime)
* [getOutputID](avmapi_outputs.secpoutput.md#getoutputid)
* [getSpenders](avmapi_outputs.secpoutput.md#getspenders)
* [getThreshold](avmapi_outputs.secpoutput.md#getthreshold)
* [makeTransferable](avmapi_outputs.secpoutput.md#maketransferable)
* [meetsThreshold](avmapi_outputs.secpoutput.md#meetsthreshold)
* [toBuffer](avmapi_outputs.secpoutput.md#tobuffer)
* [toString](avmapi_outputs.secpoutput.md#tostring)
* [comparator](avmapi_outputs.secpoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new SecpOutput**(`amount`: BN, `locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[SecpOutput](avmapi_outputs.secpoutput.md)*

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[constructor](avmapi_outputs.amountoutput.md#constructor)*

*Overrides [Output](avmapi_outputs.output.md).[constructor](avmapi_outputs.output.md#constructor)*

*Defined in [src/apis/avm/outputs.ts:318](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L318)*

An [AmountOutput](avmapi_outputs.amountoutput.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the output |
`locktime` | BN | undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number | undefined | A number representing the the threshold number of signers required to sign the transaction |
`addresses` | Array‹Buffer› | undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses  |

**Returns:** *[SecpOutput](avmapi_outputs.secpoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](avmapi_types.address.md)›* = []

*Inherited from [Output](avmapi_outputs.output.md).[addresses](avmapi_outputs.output.md#protected-addresses)*

*Defined in [src/apis/avm/outputs.ts:37](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L37)*

___

### `Protected` amount

• **amount**: *Buffer* = Buffer.alloc(8)

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[amount](avmapi_outputs.amountoutput.md#protected-amount)*

*Defined in [src/apis/avm/outputs.ts:290](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L290)*

___

### `Protected` amountValue

• **amountValue**: *BN* = new BN(0)

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[amountValue](avmapi_outputs.amountoutput.md#protected-amountvalue)*

*Defined in [src/apis/avm/outputs.ts:292](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L292)*

___

### `Protected` locktime

• **locktime**: *Buffer* = Buffer.alloc(8)

*Inherited from [Output](avmapi_outputs.output.md).[locktime](avmapi_outputs.output.md#protected-locktime)*

*Defined in [src/apis/avm/outputs.ts:31](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L31)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* = Buffer.alloc(4)

*Inherited from [Output](avmapi_outputs.output.md).[numaddrs](avmapi_outputs.output.md#protected-numaddrs)*

*Defined in [src/apis/avm/outputs.ts:35](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L35)*

___

### `Protected` threshold

• **threshold**: *Buffer* = Buffer.alloc(4)

*Inherited from [Output](avmapi_outputs.output.md).[threshold](avmapi_outputs.output.md#protected-threshold)*

*Defined in [src/apis/avm/outputs.ts:33](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L33)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`outbuff`: Buffer, `offset`: number): *number*

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[fromBuffer](avmapi_outputs.amountoutput.md#frombuffer)*

*Overrides [Output](avmapi_outputs.output.md).[fromBuffer](avmapi_outputs.output.md#frombuffer)*

*Defined in [src/apis/avm/outputs.ts:302](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L302)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [AmountOutput](avmapi_outputs.amountoutput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`outbuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [Output](avmapi_outputs.output.md).[getAddress](avmapi_outputs.output.md#getaddress)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getAddressIdx](avmapi_outputs.output.md#getaddressidx)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getAddresses](avmapi_outputs.output.md#getaddresses)*

*Defined in [src/apis/avm/outputs.ts:57](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L57)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getAmount

▸ **getAmount**(): *BN*

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[getAmount](avmapi_outputs.amountoutput.md#getamount)*

*Defined in [src/apis/avm/outputs.ts:297](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L297)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [Output](avmapi_outputs.output.md).[getLocktime](avmapi_outputs.output.md#getlocktime)*

*Defined in [src/apis/avm/outputs.ts:52](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L52)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

###  getOutputID

▸ **getOutputID**(): *number*

*Overrides [Output](avmapi_outputs.output.md).[getOutputID](avmapi_outputs.output.md#abstract-getoutputid)*

*Defined in [src/apis/avm/outputs.ts:344](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L344)*

Returns the outputID for this output

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [Output](avmapi_outputs.output.md).[getSpenders](avmapi_outputs.output.md#getspenders)*

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

*Inherited from [Output](avmapi_outputs.output.md).[getThreshold](avmapi_outputs.output.md#getthreshold)*

*Defined in [src/apis/avm/outputs.ts:47](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L47)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

*Inherited from [Output](avmapi_outputs.output.md).[makeTransferable](avmapi_outputs.output.md#maketransferable)*

*Defined in [src/apis/avm/outputs.ts:192](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L192)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](avmapi_outputs.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [Output](avmapi_outputs.output.md).[meetsThreshold](avmapi_outputs.output.md#meetsthreshold)*

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

*Inherited from [AmountOutput](avmapi_outputs.amountoutput.md).[toBuffer](avmapi_outputs.amountoutput.md#tobuffer)*

*Overrides [Output](avmapi_outputs.output.md).[toBuffer](avmapi_outputs.output.md#tobuffer)*

*Defined in [src/apis/avm/outputs.ts:312](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L312)*

Returns the buffer representing the [AmountInput](avmapi_inputs.amountinput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Output](avmapi_outputs.output.md).[toString](avmapi_outputs.output.md#tostring)*

*Defined in [src/apis/avm/outputs.ts:184](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L184)*

Returns a base-58 string representing the [Output](avmapi_outputs.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Output](avmapi_outputs.output.md).[comparator](avmapi_outputs.output.md#static-comparator)*

*Defined in [src/apis/avm/outputs.ts:196](https://github.com/ava-labs/avalanche.js/blob/eabcc2f/src/apis/avm/outputs.ts#L196)*

**Returns:** *function*

▸ (`a`: [Output](avmapi_outputs.output.md), `b`: [Output](avmapi_outputs.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](avmapi_outputs.output.md) |
`b` | [Output](avmapi_outputs.output.md) |
