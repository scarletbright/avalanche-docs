[slopes - v1.7.3](../README.md) › ["apis/avm/outputs"](../modules/_apis_avm_outputs_.md) › [AmountOutput](_apis_avm_outputs_.amountoutput.md)

# Class: AmountOutput

An [Output](_apis_avm_outputs_.output.md) class which specifies a token amount .

## Hierarchy

* [Output](_apis_avm_outputs_.output.md)

  ↳ **AmountOutput**

  ↳ [SecpOutput](_apis_avm_outputs_.secpoutput.md)

## Index

### Constructors

* [constructor](_apis_avm_outputs_.amountoutput.md#constructor)

### Properties

* [addresses](_apis_avm_outputs_.amountoutput.md#protected-addresses)
* [amount](_apis_avm_outputs_.amountoutput.md#protected-amount)
* [amountValue](_apis_avm_outputs_.amountoutput.md#protected-amountvalue)
* [locktime](_apis_avm_outputs_.amountoutput.md#protected-locktime)
* [numaddrs](_apis_avm_outputs_.amountoutput.md#protected-numaddrs)
* [threshold](_apis_avm_outputs_.amountoutput.md#protected-threshold)

### Methods

* [fromBuffer](_apis_avm_outputs_.amountoutput.md#frombuffer)
* [getAddress](_apis_avm_outputs_.amountoutput.md#getaddress)
* [getAddressIdx](_apis_avm_outputs_.amountoutput.md#getaddressidx)
* [getAddresses](_apis_avm_outputs_.amountoutput.md#getaddresses)
* [getAmount](_apis_avm_outputs_.amountoutput.md#getamount)
* [getLocktime](_apis_avm_outputs_.amountoutput.md#getlocktime)
* [getOutputID](_apis_avm_outputs_.amountoutput.md#abstract-getoutputid)
* [getSpenders](_apis_avm_outputs_.amountoutput.md#getspenders)
* [getThreshold](_apis_avm_outputs_.amountoutput.md#getthreshold)
* [makeTransferable](_apis_avm_outputs_.amountoutput.md#maketransferable)
* [meetsThreshold](_apis_avm_outputs_.amountoutput.md#meetsthreshold)
* [toBuffer](_apis_avm_outputs_.amountoutput.md#tobuffer)
* [toString](_apis_avm_outputs_.amountoutput.md#tostring)
* [comparator](_apis_avm_outputs_.amountoutput.md#static-comparator)

## Constructors

###  constructor

\+ **new AmountOutput**(`amount`: BN, `locktime`: BN, `threshold`: number, `addresses`: Array‹Buffer›): *[AmountOutput](_apis_avm_outputs_.amountoutput.md)*

*Overrides [Output](_apis_avm_outputs_.output.md).[constructor](_apis_avm_outputs_.output.md#constructor)*

*Defined in [apis/avm/outputs.ts:326](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L326)*

An [AmountOutput](_apis_avm_outputs_.amountoutput.md) class which issues a payment on an assetID.

**Parameters:**

Name | Type | Default | Description |
------ | ------ | ------ | ------ |
`amount` | BN |  undefined | A [BN](https://github.com/indutny/bn.js/) representing the amount in the output |
`locktime` | BN |  undefined | A [BN](https://github.com/indutny/bn.js/) representing the locktime |
`threshold` | number |  undefined | A number representing the the threshold number of signers required to sign the transaction |
`addresses` | Array‹Buffer› |  undefined | An array of [Buffer](https://github.com/feross/buffer)s representing addresses  |

**Returns:** *[AmountOutput](_apis_avm_outputs_.amountoutput.md)*

## Properties

### `Protected` addresses

• **addresses**: *Array‹[Address](_apis_avm_types_.address.md)›* =  []

*Inherited from [Output](_apis_avm_outputs_.output.md).[addresses](_apis_avm_outputs_.output.md#protected-addresses)*

*Defined in [apis/avm/outputs.ts:33](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L33)*

___

### `Protected` amount

• **amount**: *Buffer* =  Buffer.alloc(8)

*Defined in [apis/avm/outputs.ts:297](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L297)*

___

### `Protected` amountValue

• **amountValue**: *BN* =  new BN(0)

*Defined in [apis/avm/outputs.ts:298](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L298)*

___

### `Protected` locktime

• **locktime**: *Buffer* =  Buffer.alloc(8)

*Inherited from [Output](_apis_avm_outputs_.output.md).[locktime](_apis_avm_outputs_.output.md#protected-locktime)*

*Defined in [apis/avm/outputs.ts:30](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L30)*

___

### `Protected` numaddrs

• **numaddrs**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Output](_apis_avm_outputs_.output.md).[numaddrs](_apis_avm_outputs_.output.md#protected-numaddrs)*

*Defined in [apis/avm/outputs.ts:32](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L32)*

___

### `Protected` threshold

• **threshold**: *Buffer* =  Buffer.alloc(4)

*Inherited from [Output](_apis_avm_outputs_.output.md).[threshold](_apis_avm_outputs_.output.md#protected-threshold)*

*Defined in [apis/avm/outputs.ts:31](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L31)*

## Methods

###  fromBuffer

▸ **fromBuffer**(`outbuff`: Buffer, `offset`: number): *number*

*Overrides [Output](_apis_avm_outputs_.output.md).[fromBuffer](_apis_avm_outputs_.output.md#frombuffer)*

*Defined in [apis/avm/outputs.ts:310](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L310)*

Popuates the instance from a [Buffer](https://github.com/feross/buffer) representing the [AmountOutput](_apis_avm_outputs_.amountoutput.md) and returns the size of the output.

**Parameters:**

Name | Type | Default |
------ | ------ | ------ |
`outbuff` | Buffer | - |
`offset` | number | 0 |

**Returns:** *number*

___

###  getAddress

▸ **getAddress**(`idx`: number): *Buffer*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:89](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L89)*

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

*Defined in [apis/avm/outputs.ts:72](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L72)*

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

*Defined in [apis/avm/outputs.ts:57](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L57)*

Returns an array of [Buffer](https://github.com/feross/buffer)s for the addresses.

**Returns:** *Array‹Buffer›*

___

###  getAmount

▸ **getAmount**(): *BN*

*Defined in [apis/avm/outputs.ts:303](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L303)*

Returns the amount as a [BN](https://github.com/indutny/bn.js/).

**Returns:** *BN*

___

###  getLocktime

▸ **getLocktime**(): *BN*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:50](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L50)*

Returns the a [BN](https://github.com/indutny/bn.js/) repersenting the UNIX Timestamp when the lock is made available.

**Returns:** *BN*

___

### `Abstract` getOutputID

▸ **getOutputID**(): *number*

*Inherited from [Output](_apis_avm_outputs_.output.md).[getOutputID](_apis_avm_outputs_.output.md#abstract-getoutputid)*

*Defined in [apis/avm/outputs.ts:38](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L38)*

Returns the outputID for the output which tells parsers what type it is

**Returns:** *number*

___

###  getSpenders

▸ **getSpenders**(`addresses`: Array‹Buffer›, `asOf`: BN): *Array‹Buffer›*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:118](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L118)*

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

*Defined in [apis/avm/outputs.ts:43](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L43)*

Returns the threshold of signers required to spend this output.

**Returns:** *number*

___

###  makeTransferable

▸ **makeTransferable**(`assetID`: Buffer): *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

*Inherited from [Output](_apis_avm_outputs_.output.md).[makeTransferable](_apis_avm_outputs_.output.md#maketransferable)*

*Defined in [apis/avm/outputs.ts:192](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L192)*

**Parameters:**

Name | Type | Description |
------ | ------ | ------ |
`assetID` | Buffer | An assetID which is wrapped around the Buffer of the Output  |

**Returns:** *[TransferableOutput](_apis_avm_outputs_.transferableoutput.md)*

___

###  meetsThreshold

▸ **meetsThreshold**(`addresses`: Array‹Buffer›, `asOf`: BN): *boolean*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:99](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L99)*

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

*Overrides [Output](_apis_avm_outputs_.output.md).[toBuffer](_apis_avm_outputs_.output.md#tobuffer)*

*Defined in [apis/avm/outputs.ts:320](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L320)*

Returns the buffer representing the [AmountInput](_apis_avm_inputs_.amountinput.md) instance.

**Returns:** *Buffer*

___

###  toString

▸ **toString**(): *string*

*Inherited from [Output](_apis_avm_outputs_.output.md).[toString](_apis_avm_outputs_.output.md#tostring)*

*Defined in [apis/avm/outputs.ts:184](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L184)*

Returns a base-58 string representing the [Output](_apis_avm_outputs_.output.md).

**Returns:** *string*

___

### `Static` comparator

▸ **comparator**(): *function*

*Inherited from [Output](_apis_avm_outputs_.output.md)*

*Defined in [apis/avm/outputs.ts:196](https://github.com/ava-labs/slopes/blob/51a37ef/src/apis/avm/outputs.ts#L196)*

**Returns:** *function*

▸ (`a`: [Output](_apis_avm_outputs_.output.md), `b`: [Output](_apis_avm_outputs_.output.md)): *0 | 1 | -1*

**Parameters:**

Name | Type |
------ | ------ |
`a` | [Output](_apis_avm_outputs_.output.md) |
`b` | [Output](_apis_avm_outputs_.output.md) |
